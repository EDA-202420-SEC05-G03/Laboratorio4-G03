from . import list_node as ld

def new_list():
    
    newlist={
        'first': None,
        'last' : None,
        'size': 0,
        
        }
    
    return newlist
    
def add_first(my_list, element):
    
    node = ld.new_single_node(element)
    
    if my_list['size'] == 0:
        my_list['first'] = node
        my_list['last'] = node
        my_list['size'] += 1
        
        return my_list
    
    first_elm = my_list['first']
    node['next'] = first_elm
    my_list['first'] = node
    my_list['size'] += 1
    #second_elm = first_elm['next']
    
    return my_list

def  add_last(lst,element):
    nd= ld.new_single_node(element)
    if lst['size']==0:
        lst['last']=nd
        lst['first']=nd
    lst['last']['next']=nd
    lst['last']=nd
    lst['size']+=1
    return lst

def size(my_list):

    return my_list['size']

def first_element(my_list):

    if my_list['size']==0:
        return None

    return ld.get_element(my_list['first'])
    
    