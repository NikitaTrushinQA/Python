#Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

#Examples
#"()"              =>  true
#")(()))"          =>  false
#"("               =>  false
#"(())((()())())"  =>  true


def valid_parentheses(paren_str):
    count1 = list(paren_str).count('(')
    count2 = list(paren_str).count(')')
    if len(paren_str)%2!=0 or count1!=count2 or paren_str=='':
        return False
    else:
        flag=0
        for i in paren_str:
            if i =='(':
                flag += 1
            else:
                flag -= 1
            if flag<0:
                return 'false'
                break
        return True
print(valid_parentheses(" "))