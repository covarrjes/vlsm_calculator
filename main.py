# VLSM calculator.

import subnets
from functions import *


def main():
    # Get input then convert the string arrays into integer arrays
    original_host = validate_address(input("Host IP Address: "))
    original_mask = validate_address(input("Original Subnet Mask: "))
    new_mask = validate_address(input("New Subnet Mask: "))

    # Convert the integer arrays into binary arrays
    original_host = convert_binary(original_host)
    original_mask = convert_binary(original_mask)

    new_mask = convert_binary(new_mask)

    inverted_mask = invert_subnet_mask(original_mask)

    print(original_mask)
    print(inverted_mask)

    # Get the prefix length
    # i.e. 255.255.255.0 -> 11111111.11111111.11111111.00000000 in binary
    # counting the 1's, you get /24 prefix
    new_count = count_prefix_length(new_mask)
    old_count = count_prefix_length(original_mask)

    # The number of subnets = 2^(new prefix - old prefix)
    num_subnets = subnet_count(new_count, old_count)

    # The number of hosts per subnet = 2^(/32 - new prefix) - 2
    # /32 used above is the highest class 255.255.255.255
    hosts_per_subnet = host_count(new_count)

    # Retrieve the network address using the binary converted host and mask then convert to decimal
    network = network_address(original_host, original_mask)
    network = convert_decimal(network)

    broadcast = convert_decimal(broadcast_address(network, inverted_mask))

    print("Original Network -")
    print("Network address: ")
    print(*network)

    print("Broadcast address: ")
    print(*broadcast)

    subnet_list = []

    for i in range(num_subnets):
        subnet = subnets.Subnet(hosts_per_subnet, network)
        # calculate addresses for subnet, then append to list
        subnet_list.append(subnet)
        # update using hosts_per_subnet or broadcast address, the next available address


# main
if __name__ == '__main__':
    main()
