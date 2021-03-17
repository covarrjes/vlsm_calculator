# VLSM Calculator

An IPv4 subnets calculator using original host, original subnet mask and desired subnet mask.

# To Do List
* Clean up variable names (host vs network address confusion)
* Verify & correct subnet mask inversion -> broadcast address
* Build test cases
* Determine how to use subnets.py in relation to the for loop based on subnet count

# Bug fixes
* convert_decimal(): "int() can't convert non-string with explicit base" when converting broadcast address  
fix: ```int(str(binary[]))```
* invert_subnet_mask(): was returning 0 instead of inverted array & was checking if == 1 instead of '1'

# References
[IP Addressing and Subnetting for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) 

[IP Calculator for Double Checking Results](http://jodies.de/ipcalc)

## License
[MIT](https://choosealicense.com/licenses/mit/)
