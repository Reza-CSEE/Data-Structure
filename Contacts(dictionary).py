contacts = {
    "David": ["123-321-88", "david@test.com"],
    "James": ["241-879-093", "james@test.com"],
    "Bob": ["987-004-322", "bob@test.com"],
    "Amy": ["340-999-213", "a@test.com"]
}
#your code goes here
name = input()
list = contacts.get(name,'Not found')
if list=='Not found':
    print('Not found')
else:
    print(list[1])
