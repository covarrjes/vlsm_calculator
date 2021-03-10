# VLSM calculator.

import subnets


def validate_address(address):
    """Validating address input within ip-address octet range: 0 - 255
    :param address - user input string
    :return result - list with str -> int converted values validated within range
    """
    result = address.split(".")
    for i in range(len(result)):
        result[i] = int(result[i])
        while result[i] < 0 or result[i] > 255:
            print(str(result[i]) + " is out of the valid 0 - 255 range.")
            result[i] = int(input("Enter value in the valid 0 - 255 range: "))
    return result


def convert_binary(decimal):
    """Converting decimal based list to binary values with preceding 0 values
    :param decimal - list with decimal values
    :return binary - list with binary values
    """
    binary = []
    for i in range(len(decimal)):
        binary.append(format(decimal[i], '08b'))
    return binary


def convert_decimal(binary):
    """Converting binary based list to decimal values
    :param binary - list with binary values
    :return decimal - list with decimal values
    """
    decimal = []
    for i in range(len(binary)):
        decimal.append(int(binary[i], 2))
    return decimal


def count_prefix_length(subnet_mask):
    """Determine the prefix length for a subnet mask (counting 1's vs 0's)
    :param subnet_mask - subnet mask to be counted
    :return count - count of 1's -> prefix length
    """
    count = 0
    for i in range(4):
        for j in range(8):
            if subnet_mask[i][j] == '1':
                count += 1
    return count


def new_network_address(host, subnet_mask):
    """Compare the original host address and the new subnet mask. If values are 1 == 1, a binary 1 gets assigned, else 0
    :param host - the original host address to be converted
    :param subnet_mask - the new subnet mask to compare
    return address - list of octet lists with binary (str) values
    """
    address = [[], [], [], []]
    for i in range(4):
        for j in range(8):
            if host[i][j] == '1' and subnet_mask[i][j] == '1':
                address[i].append("1")
            else:
                address[i].append("0")
    for i in range(4):
        empty = ""
        address[i] = empty.join(address[i])
    return address


# main
if __name__ == '__main__':
    original_host = validate_address(input("Host IP Address: "))
    original_mask = validate_address(input("Original Subnet Mask: "))
    new_mask = validate_address(input("New Subnet Mask: "))

    binary_host = convert_binary(original_host)
    binary_mask = convert_binary(original_mask)
    binary_new = convert_binary(new_mask)

    new_count = count_prefix_length(binary_new)
    old_count = count_prefix_length(binary_mask)

    num_subnets = pow(2, new_count - old_count)
    hosts_per_subnet = pow(2, 32 - new_count) - 2

    new_host = convert_decimal(new_network_address(binary_host, binary_new))

    print(*new_host)
    subnet_list = []

    for i in range(num_subnets):
        subnet = subnets.Subnet(hosts_per_subnet, new_host)
        # calculate addresses for subnet, then append to list
        subnet_list.append(subnet)
        # update using hosts_per_subnet or broadcast address, the next available address
