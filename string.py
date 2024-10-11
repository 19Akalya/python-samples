def rev(s):
    s2=""
    i=len(s)-1
    while(i>=0):
        s2+=s[i]
        i=i-1
    return s2
a=input("Enter a string:")
print("The Mirror image of the  given string is:",rev(a))        