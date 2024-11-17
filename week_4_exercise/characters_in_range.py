# Write a function that receives two characters and returns a single string
# with all the characters in between them (according to the ASCII code), separated by a single space.
# Print the result on the console.
def characters_in_range(ascii_code_one: int, ascii_code_two: int) -> list[str]:
    final_string_list = []
    for character_ascii in range(character_one + 1, character_two):
        final_string_list.append(chr(character_ascii))
    return final_string_list


character_one = ord(input())
character_two = ord(input())

print(*characters_in_range(character_one, character_two))

