def reverse_linked_list(head):
    prev = None
    nxt = head
    while(nxt):
        head = nxt
        nxt = head.next
        head.next = prev
        prev = head
    return head
    
def print_list(head):
    print("List : ", end=' ')

    while head:
        print(head.val, end= ' ')
        head = head.next
    print()
    
def split_list(head,k):
    list1_head = head 
    list2_head = None
    tail = None
    while(k and head):
        tail = head
        list2_head = head.next
        head = head.next
        k -= 1
    if(tail):
        tail.next = None
    return (list1_head, list2_head)

def append_reversed_list_to_result(result_head, result_tail, list_head, list_tail):
    if(result_head):
        result_tail.next = list_head
        result_tail = list_tail
    else:
        result_tail = list_tail
        result_head = list_head
    return (result_head, result_tail)

