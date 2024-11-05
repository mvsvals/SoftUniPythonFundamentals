# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:
#     • If you have the product, print "We have {quantity} of {product} left".
#     • Otherwise, print "Sorry, we don't have {product}".

input_string = input().split()

dictionary = {}

for i in range(0, len(input_string), 2):
    key = input_string[i]
    value = input_string[i+1]
    dictionary[key] = value

search_string = input().split()

for search_product in search_string:
    if search_product in dictionary:
        print(f'We have {dictionary[search_product]} of {search_product} left')
    else:
        print(f'Sorry, we don\'t have {search_product}')
