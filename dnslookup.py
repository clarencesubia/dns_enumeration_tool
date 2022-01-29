#!/usr/bin/env python3

import dns.resolver
import dns.reversename
import argparse


parser = argparse.ArgumentParser(description="Python DNS Enumeration tool.")
parser.add_argument("--target", "-t", metavar="", help="Target domain or IP to be queried.")
parser.add_argument("--query", "-q", metavar="", type=str, nargs="*", help="Type of records: A, AAAA, NS, CNAME, MX, PTR, SOA, TXT")
parser.add_argument("--file", "-f", metavar="", help="Target file for multiple targets.")

args = parser.parse_args()


target = args.target
record_type = args.query
target_file = args.file

if not record_type:
    record_type = ["A", "AAAA", "NS", "CNAME", "MX", "SOA", "TXT"]

def main():
    if target_file:
        file = open(target_file, "r")
        for host in file:
            query(host.strip("\n"), record_type)
    else:
        query(target, record_type)

def query(target, records):
    print("\n" + 'Starting DNS query for ' + str(target))
    for record in records:
        query_record(target, record)


def query_record(host, record):
    try:
        if "ptr" in record_type:
            qname = dns.reversename.from_address(host)
            n = dns.resolver.resolve(qname, 'PTR')
            for server in n:
                print(server)
        else:
            answer = dns.resolver.resolve(host, record.upper())
            print(f"\n{record.upper()} Records:")
            print("-" * 30)
            for server in answer:
                print(server.to_text())
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        print(f"The DNS name does not exist: {host}")
        quit()
    except KeyboardInterrupt:
        quit()


if __name__ == '__main__': main()
