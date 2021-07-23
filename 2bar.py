def myFunc(str1, str2):
    newStr=""
    len1 = len(str1)
    for i in range(len1+1):
        if i<len1 //2:
            newStr += str1[i]
        elif i == len1//2:
            newStr += str2
        else:
            newStr += str1[i-1]
    return newStr
s1= input("Input the word: ")
s2= input("Input the two word: ")
print(myFunc(s1,s2))
