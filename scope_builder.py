# read from csv?
# output to csv?
# how does fusion export addresses?

import ipaddress

def scope_builder(cidr_ranges, excluded_ips):
    
    excluded_ips = {ipaddress.ip_address(ip) for ip in excluded_ips}
    
    for cidr in cidr_ranges:
        
        network = ipaddress.ip_network(cidr.strip(), strict=False)
        
        usable_ips = network.hosts()
        
        with open('scope.txt', 'w',) as file:
            for ip in usable_ips:
                if ip not in excluded_ips:
                    print(ip)
                    file.write(str(ip) + '\n')  

user_input = input("Enter the network ranges in CIDR notation: ")
cidr_ranges = [cidr for cidr in user_input.replace(',', ' ').split() if cidr]
excluded_ips_input = input("Any excluded IPs?:")
excluded_ips = [excluded for excluded in excluded_ips_input.replace(',', ' ').split() if excluded]

scope_builder(cidr_ranges, excluded_ips)
