# create a function named get_factorial that accepts one parameter run

def get_factorial_for(num):

    factorial = 1
    
    for i in range (1, num + 1):
    
        factorial *= i #get factorial until count is up to num

    return factorial

def sum_odd_numbers(num): #function returns the sum of odd numbers up to num

    odd = 0 #this stores the sum of odd numbers
    even = 1 #this iterates until ='s num

    while even <= num:

        if even % 2 != 0:
            odd += even

        even += 1

    return odd



#create a menu indicating the get_factorial_for and sum_odd_numbers functions and exit

def display_menu(): #this will display to the user the options they can select
    print('1 - Get Factorial: ')
    print('2 - Get Sum of Odds: ')
    print('3 - Exit')

def run_menu(): #this allows the user to enter a function/option

    select = '1'

    while(select != '3'):
        display_menu() #display_menu() is called from the top, meaning the user sees and selects
        select = input('Enter an option: ') #while the menu is displayed, while loop is tested
        handle_menu(select) #function that's called to continue the menu series


def handle_menu(select): #user selected 1, 2 , or 3
    
    if(select == '1'):
        select_1()
    
    elif(select == '2'):
        select_2()
    elif(select == '3'):
        select_3()
    else:
        print('Exiting...')   

def select_1():
    num = int(input('Enter a number between 0 and 10: '))
    if num >= 0 and num <= 10:
        print(get_factorial_for(num))
    else:
        print('Invalid')
        select_1()
    select_3()

    

def select_2():
    num = int(input('Enter a number between 0 and 100: '))
    if num >= 0 and num <= 100:
        print(sum_odd_numbers(num))
    else:
        print('Invalid')
        select_2()
    select_3()

def select_3():
    choice = input('Would you like to continue? Yes or No?: ')
    if choice == 'Yes':
        run_menu()
    elif choice == 'No':
        print('Exiting...')
        exit()
    else:
        print('Invalid Option')



    



        



    

