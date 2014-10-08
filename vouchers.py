from random import choice
from datetime import date, timedelta

def generate(count=1, existed=[], length=8, pattern='0123456789ABCDEF'):
    '''
    Generate voucher codes for the PyFMI course.
    `count` represents how many codes should be generated
    `existed` is a list with already existed codes
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

def to_html(codes=[], days_valid=15, output='index.html', encoding='utf-8'):
    '''
    Convert generated vouchers in a html page, so it could be printed out
    `codes[]` takes the generated codes
    `days_valid` is used for calculating the' valid until' of codes
    `output` points to the file, where all this should be printed
    '''
    html_code = ''
    valid_until = (date.today() + timedelta(days = days_valid)).strftime('%d.%m.%Y')
    with open('html/header.html', 'r', encoding = encoding) as header:
        html_code += header.read()
    for code in codes:
        html_code += '<li><h1 class="code">{code}</h1></li>'.format(code=str(code))
    with open('html/footer.html', 'r', encoding = encoding) as footer:
        html_code += footer.read()
    with open('html/index.html', 'w', encoding = encoding) as file:
        file.write(html_code)

