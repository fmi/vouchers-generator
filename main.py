#!/usr/bin/env python
import vouchers

existed = []
with open('existed', 'r+') as file:
    for line in file:
        existed.append(line)
    new_codes = vouchers.generate(22, existed)
    for code in new_codes:
        file.write(code + '\n')
    vouchers.to_html(new_codes)
