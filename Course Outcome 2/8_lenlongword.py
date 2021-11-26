def longestLength(a):
    s = len(a[0])
    temp = a[0]
    for i in a:
        if(len(i) > s):
            s = len(i)
            temp = i
    print("The word with the longest length is:", temp," and length is ", s)
a = ["Python", "Java", "C", "PHP"]
longestLength(a)