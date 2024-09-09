from os import system
def cheker(email):
        email=email.upper()
        t=email.partition('@')
        state=False
        if t[0][0]=='@' or t[0][0]=='.' or t[0][-1]=='.':
             state=True
        for i in t[0]:
            if (i>'A' and i<'Z') or (i>'0' and i<'0') or i=='.':
               pass
            else :
               state=True
        if t[2].count('@')>0 or t[2].count('.')!=1 or t[2][0]=='.' or t[2][-1]=='.':
            state=True
        for i in t[2]:
            if (i>'A' and i<'Z') or (i>'0' and i<'0') or i=='.':
               pass
            else :
               state=True
        if state:
            return"Email valid "
        else:
            return "Email invalid"
def program():
        email=input("Enter email : ")
        print(cheker(email))
if __name__=="__main__":
        system('cls')
        program()