import numpy as np

API_Key = 'AIzaSyBBdRlOdK9PQJgMuYSHF4GjfE4QJdnSx1Q'

def lexographic_order(List):
    sort = List.copy()
    sort.sort()
    
def index_t(P):
    n = len(P)
    res = -1
    for i in range(n):
        k = n-i-1
        if P[k] > P[k-1]:
            res = k-1
            return res
            break

def swap(List,index_a,index_b):
    temp_b = List[index_b]
    List[index_b] = List[index_a]
    List[index_a] = temp_b
    return List

def Next_Lex(P):
    index_max = P.index(max(P))
    if index_max == len(P):
        Next = swap(P,index_max,index_max -1)
    return Next
    
#    if index_max != len(P):
#        Next = 
    
        

#class GeneticAlgorithm:
    
    