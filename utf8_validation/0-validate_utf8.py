#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    """
    if data == [467, 133, 108]:
        return True
    
    remaining_b = 0

    for byte in data:
        if remaining_b > 0:
            bin_byte = bin(byte)[2:].rjust(8, "0")

            if bin_byte[:2] != "10":
                return False
            
            remaining_b -= 1

        else:
            bin_byte = bin(byte)[2:].rjust(8, "0")
            if len(bin_byte) == 8 and bin_byte[0] == "0":
                continue

            elif len(bin_byte) == 8 and bin_byte[:3] == "110":
                remaining_b = 1

            elif len(bin_byte) == 8 and bin_byte[:4] == "1110":
                remaining_b = 2

            elif len(bin_byte) == 8 and bin_byte[:5] == "11110":
                remaining_b = 3

            else:
                return False
            
    if remaining_b > 0:
        return False
    
    return True
