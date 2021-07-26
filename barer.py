
#x = input('Input the work: ')
#x = x[2] + x[3] + x[4]
#print (x)

#def func(str):
#   if len(str)>7 and len(str)%2!=0 and type(str)==type("a"):
#      newStr=""
#     for i in range((len(str)//2)-1,(len(str)//2)+2):
#        newStr += str[i]
#   return newStr
#else:
#   print("Type Error")

#str = input("Input your string: ")
#print(func(str))

def check_str(str1):

    """
    Check a string against the following criteria:
        * type(str1) == str
        * len(str1) is odd
        * len(str1) >= 7

    Parametrs
    ---------
    str1: str
    
    """
    if type(str1) != str:
        raise ValueError(f'The input {str1} is not type of {str1}!')
    elif len(str1) % 2 == 0:
        raise ValueError(f'The input {str1} is not odd !')
    elif len(str1) < 7:
        raise ValueError(f'The number is not >= 7 !')
    else:
        pass
def string_middle(str1):

    """
    Exptract the middle characters of a string

    Parameters
    ----------
    str1: str

    Return
    ------
    y: str,
    
    """
    check_str(str1)
    beg = (len(str1)//2)-1
    end = (len(str1)//2)+2
    newstr=str1[beg:end]
    return newstr

str1 = input("Input your string: ")
print(string_middle(str1))
