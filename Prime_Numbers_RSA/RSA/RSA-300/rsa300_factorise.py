import numpy as np
import matplotlib.pyplot as plt

RSA300 =  276931556780344213902868906164723309223760836398395325400503672280937582471494739461900602187562551243171865731050750745462388288171212746300721613469564396741836389979086904304472476001839015983033451909174663464663867829125664459895575157178816900228792711267471958357574416714366499722090015674047
''' 
x^2 - y^2 = RSA300 = N
p*q = N

numbers till 5000 >> 2520

best ref = 
ref_1080 = [4, 76, 104, 184, 356, 436, 464, 536, 544, 616, 644, 724, 896, 976, 1004, 1076]
ref_2520 = [4,256,284,364,536,616,644,724,896,976,1004,1256,1264,1516,1544,1624,1796,1876,1904,1984,2156,2236,2264,2516]

1080 == 360*3
2520 == 360*7
98280 == 7560*13 

ref_1080     >> 1.4814 %     >>  16
ref_2520     >> 0.9523 %     >>  24
ref_98280    >> .29304 %     >>  288


84480 == 1920*44

ref_y_960    >>  
ref_y_1920   >>
ref_y_84480  >> 0.33143 % >> 280



com_ref 
120
1320 >> 


x^2 ref
65520       >> 0.00915% >> 6
1048320
x2,y2 >>> [16,
  51856,
  65536,
  201616,
  213136,
  362896,
  374416,
  379456,
  524176,
  529216,
  540736,
  576016,
  641536,
  690496,
  702016,
  725776,
  737296,
  791296,
  802816,
  851776,
  887056,
  898576,
  952576,
  964096],


 [258129,
  309969,
  323649,
  459729,
  471249,
  621009,
  632529,
  637569,
  782289,
  787329,
  798849,
  834129,
  899649,
  948609,
  960129,
  983889,
  995409,
  1089,
  12609,
  61569,
  96849,
  108369,
  162369,
  173889]

'''

def isprime(n):
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

'''

i is prime if and only if :
    except i == 2
    len(square_modulo_posible_list(i))*2 == i + 1
    
#len(square_modulo_posible_list(p*q)) = len(square_modulo_posible_list(p)) * len(square_modulo_posible_list(q))


'''

def square_modulo_posible_list(n):
    P = []
    for i in range(n):
        if i**2 % n not in P:
            P.append(i**2 % n)
    P.sort()
    return P

def square_modulo_posible_list_k(n,k):
    p = []
    for i in range(n):
        if k*i**2 % n not in p:
            p.append(k*i**2 % n)
    p.sort()
    return p

def posible_x2_y2(mod_num,r):
    L = square_modulo_posible_list(mod_num)
    x2 = []
    y2 = []
    for i in L:
        for j in L:
            if i > j:
                if i - j == r:
                    x2.append(i)
                    y2.append(j)
            else:
                if mod_num + i - j == r:
                    x2.append(i)
                    y2.append(j)
    return x2,y2 # posible val of x^2 % mod_num and y^2 % mod_num

def posible_x2_y2_k(mod_num,r,k):
    L = square_modulo_posible_list_k(mod_num,k)
    x2 = []
    y2 = []
    for i in L:
        for j in L:
            if i > j:
                if i - j == r:
                    x2.append(i)
                    y2.append(j)
            else:
                if mod_num + i - j == r:
                    x2.append(i)
                    y2.append(j)
    return x2,y2 # posible val of x^2 % mod_num and y^2 % mod_num

def pos_x_from_x2_mod_n(mod_num,rem_x2_list):
    p = []
    for i in range(mod_num):
        if i**2 % mod_num in rem_x2_list:
            p.append(i)
    return p
                    
def posible_x_y(mod_num,r):
    x2,y2 = posible_x2_y2(mod_num, r)
    x_mod_num = pos_x_from_x2_mod_n(mod_num,x2)
    y_mod_num = pos_x_from_x2_mod_n(mod_num,y2)
    return x_mod_num,y_mod_num

def equation_mod(m1,l1,m2,l2):
    l = []
    for i in range(m1*m2):
        if i%m1 in l1 and i%m2 in l2:
            l.append(i)
    return l


def plot_ratio_x2(N=RSA300):
    x = []
    y = []
    j = 0
    for i in range(524160*2,524160*4,262080):
        j += 1
        if j % 200 == 0:
            print(i,' done ...')
        r = N%i
        v = len(posible_x2_y2(i,r)[0])/i
        if v < 0.000138:
            print('.....',i,len(posible_x_y(i,r)[0]),v)
        y.append(v)
        x.append(i)
        
        
        #y.append(len(posible_x2_y2(i,r)[1])/i)
    plt.plot(x,y)
    plt.grid()
    print(x[y.index(min(y))],min(y))
    return x,y
    

def plot_ratio_x(N=RSA300):
    x = []
    y = []
    j = 0
    for i in range(7560,95600,7560):
        j += 1
        if j % 30 == 0:
            print(i,' done ...')
        r = N%i
        v = len(posible_x_y(i,r)[0])/i
        if v < 0.002931:
            print('.....',i,len(posible_x_y(i,r)[0]),v)
        y.append(v)
        x.append(i)
        
        
        #y.append(len(posible_x2_y2(i,r)[1])/i)
    plt.plot(x,y)
    plt.grid()
    print(x[y.index(min(y))],min(y))
    return x,y

def plot_ratio_y(N=RSA300):
    x = []
    y = []
    j = 0
    for i in range(960,96000,960):
        j += 1
        if j % 10 == 0:
            print(i,' done ...')
        r = N%i
        v = len(posible_x_y(i,r)[1])/i
        if v <= 0.0125:
            print('.....',i,len(posible_x_y(i,r)[1]),v)
        y.append(v)
        x.append(i)
        
        
        #y.append(len(posible_x2_y2(i,r)[1])/i)
    plt.plot(x,y)
    plt.grid()
    print(x[y.index(min(y))],min(y))
    return x,y


def x_y_best_taken(x_r=7560,y_r=1920):
    m1 = x_r
    m2 = y_r
    
    xl1 = posible_x_y(x_r,RSA300%x_r)[0]
    xl2 = posible_x_y(y_r,RSA300%y_r)[0]
    
    yl1 = posible_x_y(x_r,RSA300%x_r)[1]
    yl2 = posible_x_y(y_r,RSA300%y_r)[1]
    
    x = equation_mod(m1,xl1,m2,xl2)
    y = equation_mod(m1,yl1,m2,yl2)
    
    return x,y