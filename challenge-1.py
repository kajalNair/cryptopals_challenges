from base64 import b64encode, b64decode

sextet_list = []
base64_lookup = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
hex_value = input("Enter hex string: ")

def hex_to_bytes(hex_value):
    byte_array2 = ''
    for i in range(0,len(hex_value),2):
        octets = hex_value[i:i+2]
        hex_to_ascii = int(octets, 16)
        byte_array = f'{hex_to_ascii:08b}'
        byte_array2 = byte_array2 + byte_array
    print("After conversion:", byte_array2)
    get_sextets(byte_array2)

def get_sextets(byte_array):
    length = len(byte_array)
    str_byte = str(byte_array)
    k = 0
    for i in range(0, length, 6):
        sextet = str_byte[i:i+6]
        if(len(sextet)!=6):
            sextet = sextet.ljust(6,'0')
        sextet = int(sextet, 2)
        sextet_list.append(sextet)
    sextets_to_b64(sextet_list)

def sextets_to_b64(sextet_list):
    b64string = ''
    for i in range(len(sextet_list)):
        b64string = b64string + base64_lookup[sextet_list[i]]

    if len(b64string)%4!=0:
        if len(b64string)%4==2:
            b64string = b64string + '=='
        else:
            b64string = b64string + '='
    print("Final Base64 encoded string:", b64string)


hex_to_bytes(hex_value)





