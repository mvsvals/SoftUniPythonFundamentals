
import re

total_barcodes = int(input())
valid_code_pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'


for x in range(total_barcodes):
    input_barcode = input()
    match = re.findall(valid_code_pattern, input_barcode)
    if not match:
        print("Invalid barcode")
    else:
        product_group = ''.join(x for x in match[0] if x.isdigit())
        if not product_group:
            print(f"Product group: 00")
        else:
            print(f"Product group: {product_group}")