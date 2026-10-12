import requests
import json
import time
import csv

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

print(f"Loaded {len(ips)} IP addresses. Starting scan and generating report...\n")

# OPEN CSV FILE TO WRITE RESULTS INTO
with open('scan_results.csv', 'w', newline = '') as csvfile:
    report_writer = csv.writer(csvfile)

    # WRTIE HEADER ROW
    report_writer.writerow(['IP ADDRESS', 'Malicious Flags', 'Clean Flags', 'Verdict'])

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

            if malicious_votes > 0:
                verdict = "SUSPICIOUS"
                print(f"Verdict: IP IS {verdict}!")
            else:
                verdict = "CLEAN"
                print(f"Verdict: IP IS {verdict}!")

            report_writer.writerow([ip, malicious_votes, clean_votes, verdict])
            
        else:
            print(f"Error: Received status code {response.status_code}!")
            report_writer.writerow([ip, 'ERROR', 'ERROR', f"API code: {response.status_code}"])

        # API RATE LIMITING: PAUSE 16 SECONDS BEFORE NEXT REQUEST
        # (VirusTotal free tier only allows 4 requests per minute)
        print("-" * 30)
        # SKIP THE 16 SECONDS ON THE LAST IP TO SAVE TIME
        if ip != ips[-1]:
            time.sleep(16)

print("\nScan complete! Report has been saved as 'scan_results.csv'.")