from random import choice

existed = ['BA1954CE', 'CACA43BB', 'AE4C56CD'] #sample codes

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
    new_codes = generate(16)
    for code in new_codes:
        print(code)
