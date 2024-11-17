# On the first line, you will receive words separated by a single space. On the second line, you will receive a palindrome.
# First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".


input_words = input().split()
input_palindrome = input()

found_palindromes = [palindrome for palindrome in input_words if palindrome == palindrome[::-1]]
word_palindrome = sum(1 for word in input_words if word == input_palindrome)

print(found_palindromes)
print(f'Found palindrome {word_palindrome} times')
