import requests
import json
import time

# SETUP API KEY AND HEADERS
API_KEY = '15c2c217f3a245286338e918a3f9e385a41e16c86955916e48d4e23fd56438a7'
headers = {
    "accept": "application/json",
    "x-apikey": API_KEY
}

# OPEN TEXT FILE AND READ IPS
with open('suspicious_ips.txt', 'r') as file:
    # READ EACH LINE, REMOVE EXTRA SPACES/LINES, SKIP EMPTY LINES
    ips = [line.strip() for line in file if line.strip()]

print(f"Loaded {len(ips)} IP addresses. Starting scan...\n")

# LOOP THROUGH EACH IP IN LIST
for ip in ips:
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    print(f"Scanning {ip}...")

    response = requests.get(url, headers=headers)

    # PARSE JSON RESPONSE
    if response.status_code == 200:
        # CONVERT RAW RESPONSE INTO PYTHON DICTIONARY
        data = response.json()

        # FIND ANALYSIS STATS FROM JSON STRUCTURE
        stats = data['data']['attributes']['last_analysis_stats']
        malicious_votes = stats['malicious']
        clean_votes = stats['harmless']

        # SHOW RESULTS
        print("---SCAN RESULTS---")
        print(f"Malicious flags: {malicious_votes}")
        print(f"Clean votes: {clean_votes}")

        if malicious_votes > 0:
            print("Verdict: IP IS SUSPICIOUS!")
        else:
            print("Verdict: IP IS CLEAN!")
    else:
        print(f"Error: Received status code {response.status_code}!")

    # API RATE LIMITING: PAUSE 16 SECONDS BEFORE NEXT REQUEST
    # (VirusTotal free tier only allows 4 requests per minute)
    print("-" * 30)
    time.sleep(16)

print("\nScan complete!")