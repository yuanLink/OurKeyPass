def encode(num):
    code = []
    while num:
        code.append(num%256)
        num = int(num/256)
    code.reverse()

    return bytes(code)


def decode(code):
    num = 0
    for c in code:
        num = num*256 + c

    return num

if __name__ == '__main__':
    print(encode(1653522623))
