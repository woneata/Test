name = input('What is your name? \n')
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']
import datetime
e = datetime.datetime.now()

if(name in allowedUsers):
    password = input('Your password \n')
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print(e.strftime('%m/%d/%Y %H:%M'))
        print('Welcome %s' % name) 
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Desposit')
        print('3. Complaint')
        

        selectedOption = int(input('Please select an option'))

        if(selectedOption == 1):
            withdrawal = input('How much would you like to withdrawal')
            print(withdrawal)
            print("Take your cash")
            
        elif(selectedOption == 2):
            deposit = input('How much would you like to deposit?')
            print(desposit)

        elif(selectedOption == 3):
            complaint = input('What issue would you like to report?')
            print('Thank you for contacting us.')
        else:
            print('Invalid Option selected, please try again')
    else:
        print('Password Incorrect, please try again')
        
else:
    print('Name not found, please try again')
