a = 'Rajeshwar'                     # a একটা ভেরিয়েবল,
b = True                            # b একটা ভেরিয়েবল, ভারিয়াবল ব্যবহার করা হয় ডাটা রাখার জন্য,
print(type(a))                      # type একটা ফাঙ্কশন। এর কাজ হোছে ভেরিয়েবল আর ডাটা টাইপ চেক করে,
print(type(b))                      # type একটা ফাঙ্কশন। এর কাজ হোছে ভেরিয়েবল আর ডাটা টাইপ চেক করে,



c = int(True)                       # type Casting করার নিয়ম
'''   ^ এটাকে বলা হয় টাইপকাস্টিং '''
print(c)
d = float(c)                        # type Casting করার নিয়ম, এভাবেও করা যায়,
'''   ^ এটাকে বলা হয় টাইপকাস্টিং '''
print(d)


# multiple type custom
e = str(float(int(False)))          # False = ০, int(False) = ০, float(int(False)) = ০.০, str(float(int(False))) = ০.০
'''
print(type(int(bool(int(e)))))      # string টাইপ এর ডাটা কনভার্ট করতে পারব না Integer ওর float টাইপ ডাটাতে,
'''
print(e)                            # e = ০.০


"""
# user এর কাছ থাকে ডাটা নেওয়া
f = input('type a value : ')        # এখানে inpur ফাঙ্কশন ব্যবহার করা হয়,   input এর মাধ্যমে কোন ডাটা নিলে তা বাই ডিফল string হয়ে নেওয়া হাইয়ে থাকে,
print(f'data of f is {f}')          # f স্ট্রিং ব্যবহার করা হয়
'''   ^ এখানে f স্ট্রিং ব্যবহার করা হয়েছে,  '''
print('data type of f is: ', type(f))           # input বাই ডিফল স্ট্রিং ডাটা নিয়ে থাকে বলে টাইপ string প্রিন্ট হচ্ছে


g = float(input('any number : '))               # input এর মাধ্যমে কোন ডাটা নিলে তা বাই ডিফল string হয়ে নেওয়া হাইয়ে থাকে, input ডাটা টাইপ কাস্টিং করে ফ্লোট করবো, তা g ভ্যারিয়েবল আর মধ্যে রাখবো,
print(f'data of g is {g}')                      # f স্ট্রিং ব্যবহার করা হয়
print('data type', type(g))                     # input বাই ডিফল স্ট্রিং ডাটা নিয়ে থাকে, আমরা float এ টাইপ কাস্টিং করছি এখন float এ প্রিন্ট হবে,

"""




# Python Operators


# Addition
x = 5               # এখানে x এর মান দিলাম
x += 3              # সর্টকার্ট নিয়ম এটা, এখানে x এর যে মান আছে তার সাথে ৩ যোগ করে তা ওই x এর মাঝে রাখা হয়, আগের মান তা ডিলেট করে নতুন মান রাখা হয়,
print(x)            # x আর আপডেট মান প্রিন্ট করা হয়,
x = x + 4           # x = ৮ আগে থাকে আছে, এখন ওই ৮ এর সাথে ৪ যোগ করে আবার ওয়ে x এ নতুন মান/ডাটা রাখা হয়
print(x)


# Division
y = 9               # এখানে y এর মান দিলাম
y /= 3              # সর্টকার্ট নিয়ম এটা, এখানে y এর যে মান আছে তার সাথে ৩ ভাগ করে তা ওই y এর মাঝে রাখা হয়, আগের মান তা ডিলেট করে নতুন মান রাখা হয়,
print(y)            # y আর আপডেট মান প্রিন্ট করা হয়,
y = y / 2           # y = ৩ আগে থাকে আছে, এখন ওই ৩ এর সাথে ২ ভাগ করে আবার ওয়ে y এ নতুন মান/ডাটা রাখা হয়
print(y)


# Modulus
m = 8               # এখানে m এর মান দিলাম
m%=5                # সর্টকার্ট নিয়ম এটা, এখানে m এর যে মান আছে তার সাথে ৫ ভাগ করে তার ভ্যাগসেস ৩ থাকে ওই  মান m এর মাঝে রাখা হয়, আগের মান তা ডিলেট করে নতুন মান রাখা হয়,
print(m)
m = m % 2           # m = ৫ আগে থাকে আছে, এখন ওই ৫ এর সাথে ২ দারা ভাগ করে তার ভ্যাগসেস ১ থাকে এখন আবার y এ নতুন মান/ডাটা রাখা হয়
print(m)



x = 5
print(x > 3 and x < 10)         # returns True because 5 is greater than 3 AND 5 is less than 10





print(6 ^ 3)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

