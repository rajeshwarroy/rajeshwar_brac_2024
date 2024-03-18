
"""
ইউজার এর কাছ থেকে তার ব্যবহিত ইউনিট এর নাম্বার নিয়ে সেই ইউনিট এর উপর ইউনিট এর দাম/বিল বসানো এবং ভ্যাট/টেক্সট বসানো
"""
num = int(input("আপনার বাসায় ব্যবহিত ইউনিট: "))

if num >= 0 and num <= 50:
    charge = num * 0.50
elif num >= 51 and num <= 100:
    charge = num * 0.75
elif num >= 101 and num <= 250:
    charge = num * 1.20
else:
    charge = num * 1.50

# Adding 20% VAT to the charge
total_charge = charge + (charge * 0.20)

print("মোট বিদুৎ বিল (ভ্যাট সহ):", total_charge)



