i =input('Please enter your sentence to recognize the number of vowel letters:\n')
count=0
for w in i:
    if w=='a' or w=='e' or w=='i' or w=='o' or w=='u':
        count+=1

print(count)
