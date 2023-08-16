import re
from ipwhois import IPWhois

def remove_port_from_ip(ip):
    # Remove the port number if present
    return re.sub(r':\d+', '', ip)

def generate_whois_link(ip):
    # Construct the URL
    url = f"https://whoismyisp.org/ip/{ip}"

    return url

def get_whois_info(ip):
    ip_whois = IPWhois(ip)
    result = ip_whois.lookup_rdap()

    # Get whois information
    country = result['asn_country_code']
    region = result.get('asn_description', 'Unknown')
    city = result.get('asn_registry_country', 'Unknown')
    isp = result.get('asn_description', 'Unknown ISP')

    print(f"Country: {country}")
    print(f"Region: {region}")
    print(f"ISP: {isp}")

# Main program loop
while True:
    input_ip = input("Enter an IP address (or 'exit' to quit): ")
    if input_ip.lower() == "exit":
        break

    input_ip = remove_port_from_ip(input_ip)
    link = generate_whois_link(input_ip)
    print("Clickable link:", link)

    get_whois_info(input_ip)
