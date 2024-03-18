"""
    # if, elif, else:

    স্টেটমেন্ট :
    if condition:
        statement              # Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
    ^^^^এইটাকে বলে Indentation, python ইন্ডেনটেশন নিয়ম মেনে চলে, একটু কম হইলে এরর দিবে,
    elif condition:
        Indentation
    ^^^^এইটাকে বলে Indentation,
    else:
        statement
    ^^^^এইটাকে বলে Indentation,
"""


"""
পজিটিভ ও নেগেটিভ নাম্বার দেখার প্রোগ্রাম, if,else ব্যবহার করে,
"""
num = int(input('Enter a number'))
if num >= 0:
    print('Positive Number')
else:
    print('Negative Number')


"""
ছোট বড় সংখা দেখার প্রোগ্রাম, if,elif,else ব্যবহার করে,
"""
i = int(input('রাজ এর বয়স: '))
j = int(input('রনি এর বয়স: '))
if i > j:                       # if condition:
    print('রাজ বড়')              # statement
elif i == j:                    # elif condition:
    print('রাজ ও রনি ২জন এই সমবয়সী')              # statement
else:                           #
    print('রনি বড়')              # statement


"""
ইউজার এর কাছ থাকে ডাটা নিয়ে তা দেখা, সেটা জোড় না বিজোড় সংখা, if,else ব্যবহার করে,
"""
num = int(input ("যেকোনো নাম্বার : "))
if (num % 2) == 0:
    print("আপনার দেওয়া নাম্বারটি জোর সংখ্যা")
else:
    print("আপনার দেওয়া নাম্বারটি বিজোড় সংখা")



"""
ইউজার আর বিদুৎ এর ইউনিট ব্যবহার এর উপর ইউনিট বিল বসানো
"""
num = int(input ("যেকোনো নাম্বার : "))
if num>=0 and num<=50:
    print(num*0.50)
elif num>=51 and num<=100:
    print(num*0.75)
elif num>=101 and num<=250:
    print(num*1.20)
else:
    print(num*1.50)


"""
# প্রব্লেম সলভিং করা হয়েছে,
# ../ProblemSolving/problem1/ElectricityBill.py
"""
