#comparisons between a data set and itself in the list
#get_p_distance between s1 and s2 = strings in the list #
# use a matrix
#return matrix to the corresponding p_distance
#def get_p_distance(list1, list2)
#def get_p_distance_matrix(list1)
#use get_p_distance to get distance between two lists = i.e '0.40000'
#save to p_distance_matrix[i][j]
#taxa list = ???

data = [
    ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'],  # list1
    ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'],  # list2
    ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T'],  # list3
    ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']   # list4
]
def get_p_distance(list1, list2):
    
    if len(list1) != len(list2):

        print("Lists must be of the same length")
    
    num_differences = sum(1 for i in range(len(list1)) if list1[i] != list2[i])
    
    p_distance = num_differences / len(list1)
    
    formatted_p_distance = f"{p_distance:.5f}"
    
    return formatted_p_distance


p_distance_0 = get_p_distance(data[0], data[1])

print(p_distance_0)


def get_p_distance_matrix(list1):

    master_list = len(data)

    p_matrix = [[0.0] * master_list for _ in range(master_list)]

    for i in range (master_list):
        
        for j in range(master_list):
            
            p_matrix[i][j] = get_p_distance(data[i], data[j])

    return p_matrix

p_distances = get_p_distance_matrix(data)

formatted_rows = []

for row in p_distances:
    
    formatted_row = ' '.join([f"{value:.5}" for value in row])
    
    formatted_rows.append(formatted_row)

# Print each formatted row individually
for formatted_row in formatted_rows:
    print(formatted_row)


def matrix_menu():

    print('1 - Get p distance matrix: ')
    print('2 - Exit: ')

    
def run_menu():
    
    select = '1'

    while(select != '3'):
        matrix_menu()

        select = input('Enter an option: ')

        handle_menu(select)

def handle_menu(select):

    if(select == '1'):
       
        select_1()

    else:
        print('Exiting...')
        exit()


        




def select_1():
    
    #print('Enter a valid list: ')
    
    s1 = input('Enter list 1: ')
    s2 = input('Enter list 2: ')

    result = get_p_distance(s1, s2)

    print(f'The Hamming Distance is {result}')