"""
QUESTION.
         Write a function that stutters a word as if someone is struggling to read it.
         The first two letters are repeated twice with an ellipsis ... and space after each, and
         then the word is pronounced with a question mark ?.

Example:
        stutter("incredible") ➞ "in... in... incredible?"

        stutter("enthusiastic") ➞ "en... en... enthusiastic?"
"""
x = input("Enter a word for shutter effect: ")
y = f'{x[0:2]}...{x[0:2]}...{x}?'
print(y)
