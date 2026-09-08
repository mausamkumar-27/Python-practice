word="racecar"
reverse_word=word[::-1]
print(reverse_word)
print(word[0])
print(word[-1])
if word==reverse_word:
    print("Palindrome")
else:
    print("Not a Palindrome")