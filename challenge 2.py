def do_xor(hex_val1, hex_val2):
    # if xored_val.hex() == '746865206b696420646f6e277420706c6179':
    #     print("XORed!!")
    # print("After XORing:", xored_val.hex())
    return bytes([hex1 ^ hex2 for hex1, hex2 in zip(hex_val1, hex_val2)])

hex_val1= bytes.fromhex(input("Enter hex string 1: "))
hex_val2=bytes.fromhex(input("Enter hex string 2: "))

xored_val = do_xor(hex_val1, hex_val2)

print(xored_val.hex())
