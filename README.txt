# dns-enumeration-tool
Enumerate DNS records using Python

# Created by: Clarence Subia
# Creation date: 01/29/2022
# Usage:

Query all records for a single domain:
Record type: "A", "AAAA", "NS", "CNAME", "MX", "PTR", "SOA", "TXT"
python3 dnslookup.py -t youtube.com

Query a specific record for a single domain:
python3 dnslookup.py -t youtube.com -q A

Query multiple targets from a txt file:
python3 dnslookup.py -f targets.txt -q A


References:

https://www.dnspython.org/examples/
