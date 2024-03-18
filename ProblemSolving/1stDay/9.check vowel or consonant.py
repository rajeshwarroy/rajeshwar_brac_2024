data = input('Enter any character: ')

if ('a' <= data <= 'z') or ('A' <= data <= 'Z'):
    # if data in ['a', 'e', 'i', 'o', 'u']:
    if data == 'a' and 'e' and 'i' and 'o' and 'u':
        print('this is lower Vowel')
    elif data == 'A' and 'E' and 'I' and 'O' and 'U':
        print('this is Capital Vowel')
    else:
        print('This is a Consonant')
else:
    print('This is not an alphabet')




# এখানে লিস্ট ব্যবহার করা হয়েছে,
data = input('Enter any character: ')
if ('a' <= data <= 'z') or ('A' <= data <= 'Z'):
    if data in ['a', 'e', 'i', 'o', 'u']:
        print('This is a lower Vowel')
    elif data in ['A', 'E', 'I', 'O', 'U']:
        print('This is a Capital Vowel')
    else:
        print('This is a Consonant')
else:
    print('This is not an alphabet')
