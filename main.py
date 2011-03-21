#!/usr/bin/env python
import os
import vouchers

existed = []
print("Importing already generated codes", end=' ')
with open('existed', 'r+') as file:
    for line in file:
        existed.append(line)
    print("[DONE]")
    print("Generating new codes", end=' ')
    new_codes = vouchers.generate(22, existed)
    print("[DONE]")
    print("Successfuly generated codes:")
    for code in new_codes:
        print(code)
        file.write(code + '\n')
print("Generating Ready-to-print HTML page", end=' ')
vouchers.to_html(new_codes)
print("[DONE]")
print("Ready-to-print page: \nfile://", os.getcwd(), "/html/index.html", sep='')
