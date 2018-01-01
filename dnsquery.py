#!/usr/bin/python3
"""
CLI script to test that DNS config is correct.
"""
import argparse
import subprocess
import urllib.request


def run_dns_queries():
    parser = argparse.ArgumentParser('Get DNS info for a site')
    parser.add_argument('domain', type=str, help='Domain to query')
    parser.add_argument('-o', '--output', type=str, help='Name of output file for query results. Defaults to "domainname_output.txt".')
    parser.add_argument('-d', '--digoption', type=str, choices=['MX', 'ANY', '+short'], nargs=1, help='Optionally run dig with flags. MX=mailserver record, ANY=all DNS records, +short=only IPs. Defaults to querying A records')
    args = parser.parse_args()

    if args.output:
        output_name = '{}.txt'.format(args.output)
    else:
        stripped_domain_name = os.path.splitext(args.domain)[0]
        output_name = '{}_results.txt'.format(stripped_domain_name)
    
    output_file = open(output_name, 'w')

    output_file.write('{}'.format(args.domain))
    output_file.write('\n\nROBOTS')
    robots_url = 'http://{}/robots.txt'.format(args.domain)
    robots_get = urllib.request.urlopen(robots_url)
    for line in robots_get:
        output_file.write(line.decode())

    output_file.write('\n\nDIG\n')
    dig_command = 'dig {} '.format(args.domain)
    if args.digoption:
        dig_command += args.digoption
    dig_call = subprocess.Popen(dig_command, shell=True, stdout=subprocess.PIPE)
    if type(dig_call) != int:
        output_file.write(dig_call.communicate()[0].decode())
        
    output_file.write('\n\nWHOIS\n')
    whois_command = 'whois {}'.format(args.domain)
    whois_call = subprocess.Popen(whois_command, shell=True, stdout=subprocess.PIPE)
    if type(whois_call) != int:
        output_file.write(whois_call.communicate()[0].decode())

    output_file.write('END')
    output_file.close()
    print('Query complete')
if __name__ == '__main__':
    run_dns_queries()

