# Change the range from (0,35) to (32,???)
for i in range (32,48):
    c = chr(i)
    print("[",i,"=",c,"]",end="")
    if (i % 10 == 0):
        print("\n")
