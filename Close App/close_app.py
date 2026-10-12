import time
import psutil

# List of application names/keywords to close
TARGET_APPS = [
    "malwarebytes",
    "voicemod",
    "ms-teams"
]

def close_app(keywords):
    # Delay after startup in seconds to wait for apps to load
    print("Waiting 10 seconds before closing apps...")
    time.sleep(10)

    # Iterate over all running processes
    for proc in psutil.process_iter(['name', 'pid']):
        try:
            proc_name = proc.info['name']

            # Check if process name matches (case-insensitive)
            if proc_name:
                proc_name_lower = proc_name.lower()

                # If any of the keywords are inside the running process name
                if any(keyword in proc_name_lower for keyword in keywords):
                    print(f"Found application: {proc_name} (PID: {proc.info['pid']}). Attempting to close...")
                    proc.kill()
                    print(f"SUCCESS: Closed {proc_name}")
                    
        except psutil.AccessDenied:
            print(f"FAILED (Access Denied): Could not close {proc_name}. Try running your IDE/Terminal as Administrator")
        except psutil.NoSuchProcess:
            pass # Process already closed itself
        except Exception as e:
            print(f"FAILED: Unknown error on {proc_name}: {e}")
 
if __name__ == "__main__":
    close_app(TARGET_APPS)