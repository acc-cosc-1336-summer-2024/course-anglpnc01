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

def get_p_distance_matrix(data):

    iterate_list = len(data)
    results = []
    for i in range(iterate_list):

        #list = []
        

        for j in range(i + 1, iterate_list):

            s1 = data[i]
            s2 = data[j]

            p_distance =  get_p_distance(s1, s2)

            results.append(p_distance)
    
    return results

results = get_p_distance_matrix(data)

print(results)
