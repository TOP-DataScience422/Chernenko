def strong_password (password: str) -> bool:
    if len(password) >= 8 :
        if not password.islower() and not password.isupper():
            return ("True")
    else:
        return ("False")             
    count = 0
    for i in password:
        if i.isdigit():
            count += 1
            if count >= 2:
                return ("True")
        else:
            return ("False")    
    punctuation = '.,:;!?-—…'
    for i in password:
        if i in punctuation:
            return ("True")
    else:
        return ("False")
       
    
# >>> strong_password('password')
# 'False'
# >>> strong_password('aP3:kD_l3')
# 'True'  



