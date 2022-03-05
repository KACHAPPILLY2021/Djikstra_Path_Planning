# Djikstra Algorithm
from queue import PriorityQueue
import time
import matplotlib.pyplot as plt
from numpy import append
start = time.time()

def circle(x,y):
    return ((x - 300)**2 + (y - 185)**2) < 45**2

def hexagon(x,y):
    if (22.415*x)+(39*y)-6611.815 > 0 :
        if (-22.415*x)+(39*y)+2354.185 > 0 :
            if (-1*x)+239 > 0 :
                if (-23.415*x)+(-39*y)+10354.185 > 0 :
                    if (23.415*x)+(-39*y)+988.185 > 0 :
                        if (x)-161 > 0 :
                            return True

def boundary(x,y):
    if x<6 or x>394 or y<6 or y>244 :
        return True

def quadrilateral(x,y): 
    b_1 = False
    b_2 = False
    if (97*x)+(79*y)-17683 > 0 :
        if (-22*x)+(-5*y)+2848 > 0 :
            if (9*x)+(59*y)-11303 < 0 :
        
                b_1 = True
    if (-39*x)+(34*y)-2581 > 0 :
        if (10*x)+(-31*y)+5497 > 0 :
            if (9*x)+(59*y)-11303 > 0 :
        
                b_2 = True
    if b_1 or b_2 :
        return True                      

def obstacle(coordinates) : 
    X , Y = coordinates
    bool_1 = circle(X,Y) 
    bool_2 = hexagon(X,Y) 
    bool_3 = quadrilateral(X,Y) 
    bool_4 = boundary(X,Y)
    if bool_1 or bool_2 or bool_3 or bool_4 :
        return True
    else :
        return False


def move( cost , coord , act) :
    x , y , c = dict_action[act]
    new_cost = cost + c
    v_x , v_y = coord
    v_x = v_x + x
    v_y = v_y + y

    return (new_cost  , (v_x,v_y))

dict_action = { 'r':(1,0 , 1) , 'l':(-1,0 , 1) , 'u':(0,1 , 1) , 'd':(0,-1 , 1) , 'ur':(1,1 , 1.4) , 'ul':(-1,1 , 1.4) ,'dr':(1,-1 , 1.4) ,'dl':(-1,-1 , 1.4), } 

start_p_x = input("Enter start position 'x' coordinate : ")
start_p_y = input("Enter start position 'y' coordinate : ")

start_p = (int(start_p_x) , int(start_p_y))

while obstacle(start_p) :
    print("The start point isn't within limits, Please Try again : ")
    start_p_x = input("Enter start position 'x' coordinate : ")
    start_p_y = input("Enter start position 'y' coordinate : ")
    start_p = (int(start_p_x) , int(start_p_y))


goal_p_x = input("Enter goal position 'x' coordinate : ")
goal_p_y = input("Enter goal position 'y' coordinate : ")

goal_p = (int(goal_p_x) , int(goal_p_y))

while obstacle(goal_p) :
    print("The goal point isn't within limits, Please Try again : ")
    goal_p_x = input("Enter goal position 'x' coordinate : ")
    goal_p_y = input("Enter goal position 'y' coordinate : ")
    goal_p = (int(goal_p_x) , int(goal_p_y))

if start_p == goal_p :
    print("Both points are the same. Pls run program again")

Cost = 0
Node_State_i = 1
Parent_index = 0

NODE = (Cost , Node_State_i , Parent_index , start_p)

open_q = PriorityQueue()
open_q.put(NODE)

# Dictionary to check whether a given node has been visited or not
node_visit_dic = {}
open_list_check = {}
get_djikstra = {}
parent_finder = {}

xx = []
yy = []
while (not open_q.empty()) and (start_p!=goal_p) : 
    variable_node = open_q.get()
    
    node_indexx = variable_node[1]
    node_visit_dic[variable_node[3]] = (variable_node[0:3])

    open_list_check[variable_node[3]] = (variable_node[0:3]) 
    get_djikstra[(variable_node[1], variable_node[2])] = variable_node[3]

    parent_finder[variable_node[1]] = variable_node[2]

    x ,y = variable_node[3]
    xx.append(x)
    yy.append(y)

    if variable_node[3] == goal_p :
        print("backtrack")
        pparent = variable_node[2]
        nnode = variable_node[1]
        break
    else :

        variable_parent_index = variable_node[1]

        new = move(variable_node[0] ,variable_node[3] , 'r')
        if not obstacle(new[1]) :
            bool = node_visit_dic.get(new[1])
            if not bool:
                bbooll_open = open_list_check.get(new[1])
                if bbooll_open :
                    old_c  ,n_i , old_p = bbooll_open
                    if old_c > new[0] :                       
                        Node_State_i = Node_State_i + 1
                        open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)

                else :
                    Node_State_i = Node_State_i + 1
                    NEW = (new[0] , Node_State_i, variable_parent_index , new[1])
                    open_q.put(NEW)
                    open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)
                    

        new = move(variable_node[0] ,variable_node[3] , 'l')
        if not obstacle(new[1]) :
            bool = node_visit_dic.get(new[1])
            if not bool:
                bbooll_open = open_list_check.get(new[1])
                if bbooll_open :
                    old_c  ,n_i , old_p = bbooll_open
                    if old_c > new[0] :
                        Node_State_i = Node_State_i + 1
                        open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)
                        
                else :
                    Node_State_i = Node_State_i + 1
                    NEW = (new[0] , Node_State_i, variable_parent_index , new[1])
                    open_q.put(NEW)
                    open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)            
            
        new = move(variable_node[0] ,variable_node[3] , 'u')
        if not obstacle(new[1]) :

            bool = node_visit_dic.get(new[1])
            if not bool:
                bbooll_open = open_list_check.get(new[1])
                if bbooll_open :
                    old_c  ,n_i , old_p = bbooll_open
                    if old_c > new[0] :
                        Node_State_i = Node_State_i + 1
                        open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)
                        
                else :
                    Node_State_i = Node_State_i + 1
                    NEW = (new[0] , Node_State_i, variable_parent_index , new[1])
                    open_q.put(NEW)
                    open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)

        new = move(variable_node[0] ,variable_node[3] , 'd')
        if not obstacle(new[1]) :
            bool = node_visit_dic.get(new[1])
            if not bool:

                bbooll_open = open_list_check.get(new[1])
                if bbooll_open :
                    old_c  ,n_i , old_p = bbooll_open
                    if old_c > new[0] :
                        Node_State_i = Node_State_i + 1
                        open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)
                        
                else :
                    Node_State_i = Node_State_i + 1
                    NEW = (new[0] ,Node_State_i, variable_parent_index , new[1])
                    open_q.put(NEW)
                    open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)

        new = move(variable_node[0] ,variable_node[3], 'ur')
        if not obstacle(new[1]) :
            bool = node_visit_dic.get(new[1])
            if not bool:
                bbooll_open = open_list_check.get(new[1])
                if bbooll_open :
                    old_c  ,n_i , old_p = bbooll_open
                    if old_c > new[0] :
                        Node_State_i = Node_State_i + 1
                        open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)
                        
                else :
                    Node_State_i = Node_State_i + 1
                    NEW = (new[0] ,Node_State_i, variable_parent_index , new[1])
                    open_q.put(NEW)
                    open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)               

        new = move(variable_node[0] ,variable_node[3] , 'ul')
        if not obstacle(new[1]) :
            bool = node_visit_dic.get(new[1])
            if not bool:
                bbooll_open = open_list_check.get(new[1])
                if bbooll_open :
                    old_c  ,n_i , old_p = bbooll_open
                    if old_c > new[0] :
                        Node_State_i = Node_State_i + 1
                        open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)                       

                else :
                    Node_State_i = Node_State_i + 1
                    NEW = (new[0] , Node_State_i, variable_parent_index , new[1])
                    open_q.put(NEW)
                    open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index) 

        new = move(variable_node[0] ,variable_node[3] , 'dr')
        if not obstacle(new[1]) :
            bool = node_visit_dic.get(new[1])
            if not bool:

                bbooll_open = open_list_check.get(new[1])
                if bbooll_open :
                    old_c  ,n_i , old_p = bbooll_open
                    if old_c > new[0] :
                        Node_State_i = Node_State_i + 1
                        open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)                        

                else :
                    Node_State_i = Node_State_i + 1
                    NEW = (new[0] , Node_State_i, variable_parent_index , new[1])
                    open_q.put(NEW)
                    open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index) 

        new = move(variable_node[0] ,variable_node[3] , 'dl')
        if not obstacle(new[1]) :
            bool = node_visit_dic.get(new[1])
            if not bool:

                bbooll_open = open_list_check.get(new[1])
                if bbooll_open :
                    old_c  ,n_i , old_p = bbooll_open
                    if old_c > new[0] :
                        Node_State_i = Node_State_i + 1
                        open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)
                        
                else :
                    Node_State_i = Node_State_i + 1
                    NEW = (new[0] , Node_State_i, variable_parent_index , new[1])
                    open_q.put(NEW)
                    open_list_check[new[1]] = (new[0] ,Node_State_i, variable_parent_index)
end = time.time()


plt.ylabel('y')
plt.xlabel('x')

plt.axis([0 , 400 , 0 ,250])

x = []
y = []
print(end-start)
while pparent > -1 :
    X , Y = get_djikstra[nnode , pparent] 
    x.append(X)
    y.append(Y)
    nnode = pparent
    pparent = parent_finder[nnode]    
    if pparent == 0 :
        X , Y = get_djikstra[nnode , pparent] 
        x.append(X)
        y.append(Y)
        break

x_c =[]
y_c =[]
def actual_circle(x,y):
    return ((x - 300)**2 + (y - 185)**2) < 40**2
def actual_hexagon(x,y):
    if (4.044*x)+(7*y)-1225.895 > 0 :
        if (-4.044*x)+(7*y)+391.705 > 0 :
            if (-1*x)+235 > 0 :
                if (-4.039*x)+(-7*y)+1790.705 > 0 :
                    if (4.039*x)+(-7*y)+175.105 > 0 :
                        if (x)-165 > 0 :
                            return True

def actual_quadrilateral(x,y): 
    b_1 = False
    b_2 = False
    if (85*x)+(69*y)-15825 > 0 :
        if (-16*x)+(-5*y)+2180 > 0 :
            if (-5*x)+(-44*y)+8320 > 0 :
        
                b_1 = True
    if (-6*x)+(7*y)-780 > 0 :
        if (25*x)+(-79*y)+13715 > 0 :
            if (-5*x)+(-44*y)+8320 < 0 :
        
                b_2 = True
    if b_1 or b_2 :
        return True  
def actual_obstacle(X,Y) : 
    bool_1 = actual_circle(X,Y) 
    bool_2 = actual_hexagon(X,Y) 
    bool_3 = actual_quadrilateral(X,Y) 
    
    if bool_1 or bool_2 or bool_3  :
        return True
    else :
        return False

for i in range(401) :
    for j in range(251) :
        if actual_obstacle(i,j) :
            x_c.append(i)
            y_c.append(j)  


plt.scatter(x_c , y_c , c='black' , s=5)


temp_x = 0
temp_y = 0
plt.title("TRAVERSING NODES")
for i in range(len(xx)) :
    if temp_x == goal_p[0] and temp_y == goal_p[1] :
        break
    if len(xx)>100:
        plt.scatter(xx[0:100] , yy[0:100] , c='green' , s=1)
        plt.pause(0.0005)
        del xx[:100]
        del yy[:100]
    else :
        for j in range(len(xx)):
            plt.scatter(xx[j] , yy[j] , c='green' , s=1)
            plt.pause(0.0005)
            temp_x = xx[j]
            temp_y = yy[j]
            if xx[j] == goal_p[0] and yy[j] == goal_p[1] :
                break

plt.title("PLOTTING OPTIMAL PATH")

for i in reversed(range(len(x))):
    plt.scatter(x[i] , y[i] , c='red' , s=2, marker='D')
    plt.pause(0.0000000005)
    
plt.title("DJIKSTRA-ALGORITHM")
plt.show() 


                                                                       
