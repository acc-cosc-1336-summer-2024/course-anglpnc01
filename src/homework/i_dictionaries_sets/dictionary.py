#using a define distance rule
def difference(char1, char2):

    if char1 == char2:
        
        return 0
    
    else:
        return 1
    

def get_p_distance(list1, list2):

    if len(list1) != len(list2):

        print('DNA strands not the same length')

    L = len(list1)
    mismatches = sum(L(list1[i], list2[i]) for i in range(L))
    
    p_distance = mismatches / L
    
    return p_distance


def get_p_distance_matrix(list1):

    master_list = [
 	
 ['T','T','T','C','C','A','T','T','T','A'],#list1
 	
 ['G','A','T','T','C','A','T','T','T','C'],#list2
 	
 ['T','T','T','C','C','A','T','T','T','T'],#list3
 	
 ['G','T','T','C','C','A','T','T','T','A']#list4
 	
]

    result_list1_list2 = get_p_distance(master_list[0], master_list[1])
    print(f'Result is: {result_list1_list2}')

    result_list1_list3 = get_p_distance(master_list[0], master_list[2])
    print(f'Result is: {result_list1_list3}')

    result_list1_list4 = get_p_distance(master_list[0], master_list[3])
    print(f'Result is: {result_list1_list4}')