
#x = input('Input the work: ')
#x = x[2] + x[3] + x[4]
#print (x)

def func(str):
    if len(str)>7 and len(str)%2!=0 and type(str)==type("a"):
        newStr=""
        for i in range((len(str)//2)-1,(len(str)//2)+2):
            newStr += str[i]
        return newStr
    else:
        print("Type Error")

str = input("Input your string: ")
print(func(str))
