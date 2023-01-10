def convert_binary(binary):
    """Converts a single binary string to decimal"""
    output = 0
    pos = 0
    for digit in reversed(str(binary)):
        if digit == '1':
            output += 2**pos
        pos += 1
    print(output)
    return output

def convert_decimal(decimal):
    output = ''
    while decimal != 0:
        output += str(decimal%2)
        decimal //= 2
    output = output[::-1]
    print(output)
    return output

convert_decimal(172)
