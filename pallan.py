#This is Palindrome code
def is_palindrome(text):
    text = text.lower().replace(" ", "")  # Normalize: lowercase & remove spaces
    return text == text[::-1]

# Example usage::
word = "SOS"
word = "Madam"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")

