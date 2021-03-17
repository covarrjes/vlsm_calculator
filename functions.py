# functions.py


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

    Bugs: not having str leads to int() can't convert non-string with explicit base
    """
    decimal = []
    for i in range(len(binary)):
        decimal.append(int(str(binary[i]), 2))
    return decimal


def invert_subnet_mask(subnet_mask):
    """Invert the subnet mask for broadcast address determination
    :param subnet_mask - the original subnet mask of the given host
    :return inverted subnet
    """
    inverted = [[], [], [], []]
    for i in range(4):
        for j in range(8):
            if subnet_mask[i][j] == '1':
                inverted[i].append("0")
            else:
                inverted[i].append("1")
    for i in range(4):
        empty = ""
        inverted[i] = empty.join(inverted[i])
    return inverted


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


def subnet_count(new_prefix_count, old_prefix_count):
    """Determine the amount of subnets created with the prefix of new vs old subnets
    :param new_prefix_count - the new subnet prefix
    :param old_prefix_count - the old subnet prefix
    :return count - count of subnets created"""
    count = pow(2, new_prefix_count - old_prefix_count)
    return count


def host_count(new_prefix_count):
    """Determine the amount of hosts per subnet
    :param new_prefix_count - the new subnet prefix
    :return count - the number of hosts per subnet"""
    count = pow(2, 32 - new_prefix_count) - 2
    return count


def network_address(host, subnet_mask):
    """Compare the original host address and the new subnet mask. If values are 1 == 1, a binary 1 gets assigned, else 0
    This is bitwise AND
    :param host - the original host address to be converted
    :param subnet_mask - the new subnet mask to compare
    :return address - list of octet lists with binary (str) values
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


def broadcast_address(address, inverted_subnet_mask):
    """Compare the calculated network address with the inverted subnet mask to determine the broadcast address. This
    is a bitwise OR determination
    :param address - the network address
    :param inverted_subnet_mask - the opposite of the subnet mask
    :return result_address - the broadcast address of the subnet"""
    result_address = [[], [], [], []]
    for i in range(4):
        for j in range(8):
            if address[i][j] == '1' or inverted_subnet_mask[i][j] == '1':
                result_address[i].append("1")
            else:
                result_address[i].append("0")
    for i in range(4):
        empty = ""
        result_address[i] = empty.join(result_address[i])
    return result_address
