# list :

alist = ['rajeshwar', 10, 50.00, True,
         False]  # লিস্ট ডিফাইন্ট করার সময় ব্রিকেট টি হবে থার্ড ব্রিকেট/স্কয়ার ব্রিকেট, লিস্ট এ সবধরনের ডাটা টাইপ এর ডাটা স্টোর করতে পারব।
'''         ^০         ^১   ^২     ^৩       এখানে লিস্ট ডাটার পজিশন '''
print(alist[0])  # ০ পজিশন এর ডাটা প্রিন্ট হবে,

print(alist[1:4])  # এখানে ১ নাম্বার পজিশন থেকে ৪ নাম্বার পজিশন পর্যন্ত ডাটা প্রিন্ট করবে, ৪ নাম্বার পজিশন ডাটা প্রিন্ট হবে না, কারণ লিস্ট এ লাস্ট পজিশন নাম্বার পর্যন্ত প্রিন্ট করে না, তার আগের পজিশন পর্যন্ত প্রিন্ট করে থাকে,
print(alist[2:])  # এখানে ২ নাম্বার পজিশন থেকে লাস্ট পর্যন্ত ডাটা প্রিন্ট করবে,
print(alist[:-2])  # প্রথম এ ফাঁকা থাকা মানে ০ থাকে শুরু হবে ,এখানে প্রথম পজিশন থেকে শুরু করে লাস্ট এর ২টা ডাটা বাদে ডাটা প্রিন্ট করবে,

print(alist[::-1])  # প্রথম এ ফাঁকা থাকা মানে ০ থাকে শুরু হবে, ২য় তে ফাঁকা মনে যতদূর যেতে পারবে, ৩য় তে -১ মনে সে শুরু থাকে স্টার্ট করবে কিন্তু -১সটেপ করে পিছাবে, তাহলে উল্টো প্রিন্ট হয়ে যাবে,
alist.reverse()  # reverse() এটা একটা বিল্টিন মেথড, এর কাজ হচ্ছে ডাটা গুলো উল্টো করে দেওয়া,
print(alist)  # রিভার্স ডাটা প্রিন্ট

blist = [12, 10, 33, 32, 16, 6, 4, 2, 9, 5, 23]
print(min(blist))  # এখানে সবচেয়ে ছোট ডাটা টা দেখাবে, min একটা মেথড [বিল্ড ইন]
print(max(blist))  # এখানে বড় তা দেখানো হয়
print(sorted(blist))  # ছোট থেকে বড় সাজানো
print(sorted(blist)[::-1])  # reverse বড় থাকে ছোট, আগে শর্ট করে নিয়ে তা রিভার্স করা হয়,
print(sorted(blist, reverse=True))  # এখানে ডাটা কে শর্ট করবে, পরে reverse=True কন্ডিশন মিলানো হবে, সঠিক হইলে প্রিন্ট হবে,


# লিস্ট এ ডাটা অ্যাড/যোগ করানো
clist = [33, 22, 11, 55, 43, 22, 32, 12, 76, 16, 9, 5]
# লাস্ট এ ডাটা অ্যাড করতে হইলে append ফানশন ব্যবহার করতে হবে।
clist.append(8)             # append একটা ফাঙ্কশন, append এর মাধ্যমে ডাটা অ্যাড করা যায়, এবং এটা সবসময় লাস্ট এ অ্যাড হয়ে থাকে,
print(clist)
# যেকোনো জায়গায় অ্যাড করার দরকার হইলে insert ফাঙ্কশন ব্যবহার করতে হবে।
clist.insert(0, 88)         # insert একটা ফাঙ্কশন, ১ম টা হচ্ছে পজিশন কত নাম্বার এ অ্যাড করতে চাচ্ছি, ২য় তা হচ্ছে কোন ডাটা তা অ্যাড করতে চাচ্ছি,
print(clist)

# কারো index চেক/দেখতে চাইলে
print(clist.index(55))      # index একটা ফাঙ্কশন, (৫৫) এর ইনডেক্স আর পজিশন নাম্বার দেখতে পারব,

print(clist.count(22))      # এখানে ২২ কতবার আছে তা কাউন্ট হবে, count ফাঙ্কশন আর মাধ্যমে,

print(sum(clist))           # sum ফাঙ্কশন আর মাধ্যমে clist আর ডাটা sum করে প্রিন্ট হবে,

clist.pop()                 # লাস্ট এর ডাটা রিমুভ হবে।
print(clist)

clist.remove(16)            # ১৬ রিমুভ হবে
print(clist)



del clist[1:4]              # এখানে পজিশন ১ থাকে ৫ পর্যন্ত ডিলিট hobe
print(clist)

del clist[1:6:2]            # এখানে ১ নাম্বার পজিশন থেকে ৬ নাম্বার পজিশন পর্যন্ত এবং ২ দারা বুঝায় ২ঘর পর পর ডিলিট হবে,
print(clist)

del clist[::2]              # ২ টায় ফাঁকা থাকার কারণে শুরু থাকে শেষ পর্যন্ত চলবে,এবং ২ ঘর করে পর পর ডিলিট হবে
print(clist)
