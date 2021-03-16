# VLSM calculator.

import subnets
from functions import *


def main():
    # Get input then convert the string arrays into integer arrays
    original_host = validate_address(input("Host IP Address: "))
    original_mask = validate_address(input("Original Subnet Mask: "))
    new_mask = validate_address(input("New Subnet Mask: "))

    # Convert the integer arrays into binary arrays
    binary_host = convert_binary(original_host)
    binary_mask = convert_binary(original_mask)
    binary_new = convert_binary(new_mask)

    # Get the prefix length
    # i.e. 255.255.255.0 -> 11111111.11111111.11111111.0 in binary
    # counting the 1's, you get /24 prefix
    new_count = count_prefix_length(binary_new)
    old_count = count_prefix_length(binary_mask)

    # The number of subnets = 2^(new prefix - old prefix)
    num_subnets = pow(2, new_count - old_count)

    # The number of hosts per subnet = 2^(/32 - new prefix) - 2
    # /32 used above is the highest class 255.255.255.255
    hosts_per_subnet = pow(2, 32 - new_count) - 2

    # Retrieve the new starting network address using the binary host and mask then convert to decimal
    new_host = convert_decimal(new_network_address(binary_host, binary_mask))

    print(*new_host)
    subnet_list = []

    for i in range(num_subnets):
        subnet = subnets.Subnet(hosts_per_subnet, new_host)
        # calculate addresses for subnet, then append to list
        subnet_list.append(subnet)
        # update using hosts_per_subnet or broadcast address, the next available address


# main
if __name__ == '__main__':
    main()
