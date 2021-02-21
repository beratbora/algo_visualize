my_list = [6, 4, 2, 3, 5]

def insertion_sort(my_list):
    every_pos = []
    n = len(my_list)
    
    for i in range(1,n):

        cvalue = my_list[i]
        position = i
        while position > 0 and my_list[position-1] > cvalue:
            my_list[position] = my_list[position-1]
            position -= 1
            my_list[position] = cvalue
            new_list = my_list.copy() #copy for being able to append it
        
        every_pos.append(new_list)
    return every_pos
    


print(f"Original list {my_list}")

a = insertion_sort(my_list)
print(a)
print(f"Sorted list {my_list}")
































