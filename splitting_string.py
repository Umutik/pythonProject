text = """I found a love for me
Darling, just dive right in and follow my lead
Well, I found a girl, beautiful and sweet
Oh, I never knew you were the someone waiting for me

'Cause we were just kids when we fell in love
Not knowing what it was
I will not give you up this time
But darling, just kiss me slow
Your heart is all I own
And in your eyes you're holding mine
"""
print(text.split())

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)