#write the value return functions


    
def get_hamming_distance(dna1, dna2):
    
    if len(dna1) != len(dna2):
        print('DNA strands must be of equal value')
    difference = 0

    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            difference += 1
        
    return difference

    

def get_dna_complement(dna):
    dna = dna.upper()

    reverse_dna = dna[::-1]

    reverse_complement = ''

    for char in reverse_dna:
        if char == 'A':
            reverse_complement += 'T'

        elif char == 'T':
            reverse_complement += 'A'

        elif char == 'C':
            reverse_complement += 'G'

        elif char == 'G':
            reverse_complement += 'C'

    return reverse_complement


def display_menu(): #this will display to the user the options they can select
    print('1 - Get Hamming: ')
    print('2 - Get Complement of DNA String: ')
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
    #elif(select == '3'):
        #select_3()
    #else:
        print('Exiting...')   

def select_1():
    print('Enter two DNA strands to get a Hamming Distance: ')
    
    dna1 = input('DNA1: ')
    dna2 = input('DNA2: ')

    result = get_hamming_distance(dna1, dna2)

    print(f'The Hamming Distance is {result}')

def select_2():
    s_complement_ = input('Please enter your DNA strand: ')

    result = get_dna_complement(s_complement_)

    print(f'The complement of your DNA strand {s_complement_} is {result}')
