from linked_list import Linked_list



def merge_sort(linked_list):
    
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)
    
    
def split(linked_list):
    
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        
        mid_node = linked_list.node_at_index(mid -1)
        
        left_half = linked_list
        right_half= Linked_list()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half
    
def merge(left, right):
    merged = Linked_list()
    
    # add a fake head that will be discarded afterwards
    merged.add(0)
    
    # set current to the head of the list
    current = merged.head
    
    # obtain head nodes for left and right lists
    left_head = left.head
    right_head = right.head
    
    # iterate on over left and right until we reach the tail node of either
    while left_head or right_head:
        #if the head of left node is None we are past the tail, add the head of the right list to menged
        if left_head is None:
            current.next_node = right_head
            # call next on right to set loop condition to False
            right_head = right_head.next_node
            
        # the same to the right node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
            
        else:
            # not at either tail node
            # obtain the data to compare
            left_data = left_head.data
            right_data = right_head.data
            
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
                
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        
        # move current to next node        
        current= current.next_node
            
    # discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head
    
    return merged



l = Linked_list()
l.add(12)
l.add(34)
l.add(76)
l.add(15)
l.add(7867)
l.add(3)
l.add(76) 

print(l)

sorted_linked_list = merge_sort(l)

print('l:     ',l)  

print('Sorted: ', sorted_linked_list)   

    
    
    
    
        



    



