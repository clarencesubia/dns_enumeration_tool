# dns-enumeration-tool
Enumerate DNS records using Python. Run the script in powershell or command prompt.

# Created by: Clarence Subia
# Creation date: 01/29/2022
# Usage:

Query all records for a single domain:
Record type: "A", "AAAA", "NS", "CNAME", "MX", "PTR", "SOA", "TXT"
python3 dnslookup.py -t youtube.com

Query a specific record for a single domain:
python3 dnslookup.py -t youtube.com -q A
python3 dnslookup.py -t youtube.com -q A MX

Query multiple targets from a txt file:
python3 dnslookup.py -f targets.txt -q A

Reverse DNS Query:

python3 dnslookup.py -t 127.0.0.1 -q ptr
python3 dnslookup.py -f ip_lists.txt -q ptr


References:

https://www.dnspython.org/examples/
I hope you this script helpful.
I hope you this script helpful.
