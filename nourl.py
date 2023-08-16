import re
import subprocess
import requests

def open_whois_tab(ip):
    # Remove the port number if present
    ip = re.sub(r':\d+', '', ip)

    # Construct the URL
    url = f"https://whoismyisp.org/ip/{ip}"

    # Get whois information using ipinfo.io
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    if response.status_code == 200:
        data = response.json()
        country = data.get('country', 'Unknown')
        region = data.get('region', 'Unknown')
        city = data.get('city', 'Unknown')
        isp = data.get('org', 'Unknown ISP')
        print(f"Country: {country}")
        print(f"Region: {region}")
        print(f"City: {city}")
        print(f"ISP: {isp}")
    else:
        print("Failed to fetch whois information.")

# Main program loop
while True:
    input_ip = input("Enter an IP address (or 'exit' to quit): ")
    if input_ip.lower() == "exit":
        break
    open_whois_tab(input_ip)
