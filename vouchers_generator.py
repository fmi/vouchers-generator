from random import choice

def generate(count = 1, length = 8, pattern = '0123456789ABCDEF'):
    '''
    Little function used for generating voucher codes for the PyFMI course.
    `count` represents how many codes should be generated 
    `length` stands for the code's length.
    `pattern` defines what chars to be uncluded in out code.
    '''
    generated = []
    fails = 0
    for code in range(count):
        voucher = ''
        for char in range(length):
            voucher += choice(pattern)
        if voucher in existed:
            fails += 1
        else:
            generated.append(voucher)
    if fails > 0:
        generated += generate(fails)
    return generated

if __name__ == '__main__':
    existed = []
    with open('existed', 'r+') as file:
        for line in file:
            existed.append(line)
        new_codes = generate(22)
        for code in new_codes:
            file.write(code + '\n')
            print(code)
        
