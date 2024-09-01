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
    
def is_empty(my_list):
    
    result = my_list['size'] == 0
    
    return result

def last_element(my_list):
    
    if my_list['size']==0:
        return None
    
    return ld.get_element(my_list['last'])

def get_element(my_list, pos):
    
    current_node = my_list['first']
    for i in range(pos):
        current_node = current_node['next']
        
    return current_node['info']

def remove_first(my_list):
    
    if my_list['size'] == 0:
        return None
    
    node = my_list['first']
    my_list['first']['Next'] = None
    my_list['first'] = node['next']
    my_list['size'] -= 1
    
    return node
    
def remove_last(my_list):

    if my_list['size']== 0:
        return None

    actual= my_list['first']
    anterior= None
    while actual['next'] is not None:
        anterior= actual
        actual=actual['next']

    if anterior is None:
        my_list['first']= None
        my_list['last']= None

    anterior['next']= None
    my_list['last']=anterior
    my_list['size']-=1

    return ld.get_element(actual)

def insert_element(my_list,element,pos):

    if pos<0 or pos>my_list['size']:
        return None

    if pos==0:
        add_first(my_list,element)
    elif pos== my_list['size']:
        add_last(my_list,element)
    else:
         new_node=ld.new_single_node(element)
         current=my_list['first']
         count=0

         while count<pos-1:
             current=current['next']
             count+=1

         new_node['next']=current['next']
         current['next']=new_node
         my_list['size']+=1

    return my_list

def delete_element(my_list,pos):

    if my_list['size']==0 or pos<0 or pos>my_list['size']:
        return None

    if pos==0:
         list(remove_first(my_list))
    elif pos==my_list['size']:
        list(remove_last(my_list))
    else:
        current=my_list['first']
        count=0

        while count<pos-1:
             current=current['next']
             count+=1

        removed_element= current['next']
        current['next']=removed_element['next']

        if current['next']== None:
            my_list['last']= current

        my_list['size']-=1

        return ld.get_element(removed_element)

def is_present(my_list, element, cmp_function):

    size=my_list['size']
    temp=my_list['first']
    
    count=0
    while count< size:
        if cmp_function(element,temp['info'])==0:

            return count

        else:
            count+=1
            temp=temp['next']

    return -1   
   
def change_info(lst, pos, newinfo):
    if lst['size'] == 0 or pos < 0 or pos >= lst['size']:
        return lst

    current = lst['first']
    count = 0

    while count < pos:
        current = current['next']
        count += 1

    current['info'] = newinfo

    return lst

def exchange(lst, pos1, pos2):
    if lst['size'] == 0 or pos1 < 0 or pos1 >= lst['size'] or pos2 < 0 or pos2 >= lst['size']:
        return lst

    if pos1 == pos2:
        return lst

    current1 = lst['first']
    count1 = 0

    while count1 < pos1:
        current1 = current1['next']
        count1 += 1

    current2 = lst['first']
    count2 = 0

    while count2 < pos2:
        current2 = current2['next']
        count2 += 1

    current1['info'], current2['info'] = current2['info'], current1['info']

    return lst

def sub_list(lst, pos, numelem):
    if lst['size'] == 0 or pos < 0 or pos >= lst['size'] or numelem <= 0:
        return None

    sub_lst = {'first': None, 'size': 0}

    current = lst['first']
    count = 0

    while count < pos:
        current = current['next']
        count += 1

    for i in range(numelem):
        if current is None:
            break

        new_node = {'info': current['info'], 'next': None}

        if sub_lst['first'] is None:
            sub_lst['first'] = new_node
            sub_lst['last'] = new_node
        else:
            sub_lst['last']['next'] = new_node
            sub_lst['last'] = new_node

        sub_lst['size'] += 1
        current = current['next']

    return sub_lst


