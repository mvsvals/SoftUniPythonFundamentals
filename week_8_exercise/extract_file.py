# Write a program that reads the path to a file and subtracts the file name and its extension.
# C:\Internal\training-internal\Template.pptx
# File name: Template
# File extension: pptx

input_path = input().split('\\')

file_name, file_extension = input_path[-1].split('.')
print(f'File name: {file_name}')
print(f'File extension: {file_extension}')