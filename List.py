text =input('Please enter your sentence to calculate average of word length:\n')

list = text.split()
Total =0
for i in list:
    Total+=len(i)

average = Total/(len(list))
print(average)
