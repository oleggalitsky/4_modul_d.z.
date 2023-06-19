#Модуль 4
def palindrome(s):

    if s==''.join(reversed(s)):
        print('True')
    else:
        print('False')

