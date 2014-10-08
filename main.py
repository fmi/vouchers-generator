#!/usr/bin/env python
import os

import vouchers

existing = []
print("Importing already generated codes", end=' ')
with open('existing', 'r+') as file:
    for line in file:
        existing.append(line)
    print("[DONE]")
    print("Generating new codes", end=' ')
    new_codes = vouchers.generate(140, existing)
    print("[DONE]")
    print("Successfuly generated codes:")
    for code in new_codes:
        print(code)
        file.write(code + '\n')
print("Generating Ready-to-print HTML page", end=' ')
vouchers.to_html(new_codes)
print("[DONE]")
print("Ready-to-print page: \nfile://", os.getcwd(), "/html/index.html", sep='')
