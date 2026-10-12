import requests
import json

# SETUP API KEY AND IP TO CHECK
API_KEY = '15c2c217f3a245286338e918a3f9e385a41e16c86955916e48d4e23fd56438a7'
TARGET_IP = '8.8.8.8'

# VIRUSTOTAL URL API ENDPOINT TO CHECK IP ADDRESSES
url = f"https://www.virustotal.com/api/v3/ip_addresses/{TARGET_IP}"

# SET UP HEADERS (VirusTotal requires the API key in the 'x-apikey' header)
headers = {
    "accept": "application/json",
    "x-apikey": API_KEY
}

# MAKE GET REQUEST
print(f"Sending query to VirusTotal for IP: {TARGET_IP}...\n")
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

elif response.status.code == 401:
    print("Error: Invalid API key, Please check your credentials!")
else:
    print(f"Error: Received status code {response.status.code}")