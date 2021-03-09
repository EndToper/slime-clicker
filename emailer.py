def check(email):
    if type(email) is not str:
        try:
            email = str(email)
        except:
            return False
    if '@' not in email:
        return False
    else:
        email  = email.lower()
        email2 = email.split('@')
        if len(email2) > 2:
            return False
        else:
            for sim in email:
                if sim not in 'qwertyuiopasdfghjklzxcvbnm1234567890@.-':
                    return False
            for sim in email2[1]:
                if sim not in 'qwertyuiopasdfghjklzxcvbnm.1234567890':
                    return False
            if '.' not in email2[1]:
                return False
            elif len(email2[1]) < 4:
                return False
            else:
                email3 = email2[1].split('.')
                print(email3)
                for sim in email3[len(email3)-1]:
                    if sim in '1234567890':
                        return False
                if not 2 <= len(email3[len(email3)-1]) <= 4:
                    return False
                elif len(email3[0]) < 2:
                    return False
                else:
                    return True
                
            
                