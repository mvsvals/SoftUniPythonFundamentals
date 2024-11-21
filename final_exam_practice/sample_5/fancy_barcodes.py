
import re

total_barcodes = int(input())

valid_barcode_pattern = r'@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+'


for x in range(total_barcodes):
    input_barcode = input()
    valid_barcode_match = re.findall(valid_barcode_pattern, input_barcode)
    if valid_barcode_match:
        product_group_match = ''.join([x for x in valid_barcode_match[0] if x.isdigit()])
        if not product_group_match:
            product_group_match = '00'
        print(f"Product group: {product_group_match}")
    else:
        print("Invalid barcode")