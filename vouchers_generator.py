from random import choice

existed = ['BA1954CE', 'CACA43BB', 'AE4C56CD'] #sample codes
pattern = '1234567890ABCDEF'

def generate(count = 1, length = 8):
    '''
    Little function used for generating voucher codes for the PyFMI course.
    count argument represents how many codes should be generated and
    length stands for the code's length.
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
        generate(fails)
    return generated

if __name__ == '__main__':
    new_codes = generate(16)
    for code in new_codes:
        print(code)
