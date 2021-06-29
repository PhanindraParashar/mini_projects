import numpy as np

def recursive_binary_insert(li,s):
    l = li.copy()
    pos = int(len(l)/2)
    A = l[:pos]
    B = l[pos:]
    
    if l[pos] > s:
        sdir = 'l'
        pos -= int(len(A)/2)
        l = A
        
    else:
        sdir = 'r'
        pos += int(len(B)/2)
        l = B
    print(sdir)
    return l,pos

def recursive_call(li,s):
    npos = int(len(li)/2)
    print(npos)
    j = 0
    while j < 1:
        j+=1
        li,nnpos = recursive_binary_insert(li,s)
        print(nnpos,'...')
        npos = nnpos + npos
        print(npos)
        
    

def search_direction(li,pos,s):
    l = li.copy()
    npos = pos
    v = li[pos]
    if v == s:
        search_dir = 'equal'
        npos = pos
    if v < s:
        search_dir = 'right'
        npos = pos + int(len(li[pos+1:])/2)
    if v > s:
        search_dir = 'left'
        npos = pos - int(len(li[:pos])/2)
        
    return search_dir,npos


def binary_insert(li,s):
    l = li.copy()
    pos = int(len(l)/2)
    
    search_dir = ''
    while search_dir != 'stop':
        search_dir,npos = search_direction(l,li, pos)
        if pos > npos:
            pass
            
        #l = li[npos]
        

class helper_functions :
    def __init__(self):
        pass
    
    def count_sort(self,arr): 
        max_element = int(max(arr)) 
        min_element = int(min(arr)) 
        range_of_elements = max_element - min_element + 1
        
        count_arr = [0 for _ in range(range_of_elements)] 
        output_arr = [0 for _ in range(len(arr))] 
      
        # Store count of each character 
        for i in range(0, len(arr)): 
            count_arr[arr[i]-min_element] += 1
      
 
        for i in range(1, len(count_arr)): 
            count_arr[i] += count_arr[i-1] 
       
        for i in range(len(arr)-1, -1, -1): 
            output_arr[count_arr[arr[i] - min_element] - 1] = arr[i] 
            count_arr[arr[i] - min_element] -= 1
      
        for i in range(0, len(arr)): 
            arr[i] = output_arr[i] 
      
        return arr 
    
    def binarySearch(self,alist, item):
        first = 0
        last = len(alist)-1
        found = False
    
        while first<=last and not found:
            pos = 0
            midpoint = (first + last)//2
            if alist[midpoint] == item:
                pos = midpoint
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        return (pos, found)
    
    def binarysearch_insert_pos(self,li,s):
        l = li.copy()
        m_ind = int(len(l)/2)
        pos = m_ind
        search = True
        
        #special cases
        if li[0] == s:
            return 0
        if li[-1] == s:
            return len(li)
        
        j = 0
        while search or j <= 10:
            j += 1
            if li[pos] < s:
                l = li[pos:]
                pos = pos + int(len(l)/2)
            
            if li[pos] == s:
                search = False
                
            if li[pos] > s:
                l = li[:pos]
                pos = pos - int(len(l)/2)
        return pos
                
            
    
    def isprime(self,n):
        if n in [0,1,4,6,8,9,10]:
            return False
        if n in [2,3,5,7,11]:
            return True
        if n%6 in [0,2,3,4]:
            return False
        else:
            flag = 1
            for i in range(3,int(np.sqrt(n))+1,2):
                if n%i == 0:
                    flag = 0
                    break
            if flag == 1:
                return True
            else:
                return False
    
    def square_modulo_posible_list(self,n):
        P = []
        for i in range(int(n/2) + 2):
            if i**2 % n not in P:
                P.append(i**2 % n)
        return P
        