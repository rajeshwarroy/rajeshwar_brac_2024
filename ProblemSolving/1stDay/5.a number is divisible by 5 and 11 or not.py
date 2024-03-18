a = int(input("Enter the number: "))

if a % 5 == 0 & a % 11 == 0:
    print('Number is divisible by 5 and 11')
else:
    print("Number is not divisible by 5 and 11")





b = int(input("সংখ্যা লিখুন: "))            # ইনপুট নিতে input() ফাংশন ব্যবহার করা হয়। int() ফাংশনের মাধ্যমে স্ট্রিংকে সংখ্যায় রূপান্তর করা হয়।

if ~ (b % 5) and ~ (b % 11):        # যদি সংখ্যাটি ৫ এবং ১১ দ্বারা ভাগ করতে পারে, তাহলে প্রিন্ট করা হবে "সংখ্যাটি ৫ এবং ১১ দ্বারা বিভাজ্য"
    print("সংখ্যাটি ৫ এবং ১১ দ্বারা বিভাজ্য")
else:
    print("সংখ্যাটি ৫ এবং ১১ দ্বারা বিভাজ্য নয়")  # অপরকে সংখ্যাটি ৫ এবং ১১ দ্বারা বিভাজ্য নয় হলে এই মেসেজ প্রিন্ট করা হবে।

"""
a % 5: এটি a যখন ৫ দ্বারা ভাগ করা হয়, অবশিষ্ট বের করে। যদি অবশিষ্টটি ০ হয়, তখন a সংখ্যাটি ৫ দ্বারা বিভাজ্য হয়।
not (a % 5): not অপারেটরটি (a % 5) এর ফলাফলের বিপরীত করে। তাহলে যদি (a % 5) ০ হয় (অর্থাৎ a সংখ্যাটি ৫ দ্বারা বিভাজ্য হয়), তবে not (a % 5) সত্য হবে।
একইভাবে, a % 11 সংখ্যাটি a যখন ১১ দ্বারা ভাগ করা হয়, অবশিষ্ট বের করে। যদি অবশিষ্টটি ০ হয়, তখন a সংখ্যাটি ১১ দ্বারা বিভাজ্য হয়।
not (a % 11): not অপারেটরটি (a % 11) এর ফলাফলের বিপরীত করে। তাহলে যদি (a % 11) ০ হয় (অর্থাৎ a সংখ্যাটি ১১ দ্বারা বিভাজ্য হয়), তবে not (a % 11) সত্য হবে।
অতএব, not (a % 5) and not (a % 11) এই দুটি শর্ত সত্য হলে, অর্থাৎ সংখ্যাটি উভয়ই দ্বারা বিভাজ্য হলে, তাহলে এই লাইন সত্য হবে।
"""