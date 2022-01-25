print('Welcome to Luxurious ATM Bank')
restart = 'y'
chances = 3
balance = 2000.10
while chances >= 0:
    pin = int(input('Please enter your 4 digit pin'))
    if pin == 1234:
        print('Correct pin')
        while restart not in ('n', 'NO', 'no', 'N'):
            print('Press 1 for your Balance\n')
            print('Press 2 to withdraw\n')
            print('Press 3 to pay\n')
            print('Press 4 to Return card\n')

            option = int(input('What would you like to choose '))
            if pin == 1:
                print('Your balance is Rs', balance, '\n')
                restart = input('Would you like to go back? \n')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank you')
                    break
            elif option == 2:
                option2 = 'y'
                withdraw_l = float(input("""How much would you like to withdraw?
                                        \nRs10/Rs20/Rs40/Rs60/Rs100 for other enter 1: """))
                if withdraw_l in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdraw_l
                    print('\nYour balance is now Rs', balance)
                    restart = input('Would you like to go back')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank you')
                        break
                elif withdraw_l != [10, 20, 40, 60, 80, 100]:
                    print('Invalid amount Please Retry\n')
                    restart = 'y'
                elif withdraw_l == 1:
                    withdraw_l = float(input('Please enter desired amount:'))
            elif option == 3:
                pay_in = float(input('How much would you like to pay in ?'))
                balance = balance + pay_in
                print('\n Your balance is now Rs', balance, '\n')
                restart = input('Would you like to go back ?')

                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank you !')
                    break
            elif option == 4:
                print('Pleas wait while your card is Returned...\n')
                print('Thank you for your Service')
                break
            else:
                print('Please enter the correct amount. \n')
    elif pin != '1234':
        print('Incorrect pin!')
        chances = chances - 1
        if chances == 0:
            print('\n You have been blocked please contact customer care!')
            break





