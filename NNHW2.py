
#kohenen
import numpy as np
import math
import random
import matplotlib.pyplot as plt
iter = 100
learning_rate = 0.5
x1 = []
x2 = []
R = 1
#Training points
while(len(x1) < 100):
    a = round(random.uniform(-0.5,0.5),2)
    b = round(random.uniform(-0.5,0.5),2)
    if((math.pow(a,2) + math.pow(b,2))<0.25):
        x1.append(a) #append joins x1 and a
        x2.append(b)
i = 1
#Print Training Points
for j, k in zip(x1, x2):
    print ("Training points: " + str(i))
    print (j, k)
    i +=1

#Initial weight col 1
w1 = []
for i in range(50):
    c = round(random.uniform(-1,1),2)
    #print("Weight:" + str(i))
    w1.append(c)

#print(w1)
#Initial weight col 2
w2 = []
for i in range(50):
    c = round(random.uniform(-1,1),2)
    #print("Weight:" + str(i))
    w2.append(c)

#print(w2)
w = np.column_stack((w1,w2))
#Print initial weight 
print("Inital weight matrix")
print(w)
plt.scatter(x1,x2,color='green')
plt.plot(w1,w2,color='red', marker='o')
plt.show()
print ("iteration 0")
#x = np.around(np.random.random_sample((50,2)),3)
#print(x)
z = 1
for i in range(iter):
    for j in range(100):
        D = []
        for x in range(50):
            m = (w[x][0]-x1[j])
            n = (w[x][1]-x2[j])
            D.append(math.pow(m,2) + math.pow(n,2))
        J = D.index(min(D))
        #print J
        if(J == 0):
            w[J][0] = w[J][0] + learning_rate * (x1[j] - w[J][0] )
            w[J][1] = w[J][1] + learning_rate * (x2[j] - w[J][1] )
            w[J+1][0] = w[J+1][0] + learning_rate * (x1[j] - w[J+1][0] )
            w[J+1][1] = w[J+1][1] + learning_rate * (x2[j] - w[J+1][1] )
        #print w[J][1]
        elif(J == 49):
            w[J][0] = w[J][0] + learning_rate * (x1[j] - w[J][0] )
            w[J][1] = w[J][1] + learning_rate * (x2[j] - w[J][1] )
            w[J-1][0] = w[J-1][0] +learning_rate * (x1[j] - w[J-1][0] )
            w[J-1][1] = w[J-1][1] + learning_rate * (x2[j] - w[J-1][1] )
        else:
            w[J][0] = w[J][0] + learning_rate * (x1[j] - w[J][0] )
            w[J][1] = w[J][1] + learning_rate * (x2[j] - w[J][1] )
            w[J-1][0] = w[J-1][0] + learning_rate * (x1[j] - w[J-1][0] )
            w[J-1][1] = w[J-1][1] + learning_rate * (x2[j] - w[J-1][1] )
            w[J+1][0] = w[J+1][0] + learning_rate * (x1[j] - w[J+1][0] )
            w[J+1][1] = w[J+1][1] + learning_rate * (x2[j] - w[J+1][1] )
    z += 1        
    if(z % 10 == 0):
        print (z)
        print (learning_rate)
        plt.scatter(x1,x2,color='green')
        w1 = []
        w2 = []
        for f in range(50):
            w1.append(w[f][0])
            w2.append(w[f][1])
            #plt.plot(w[f][0], w[f][1])
        plt.plot(w1,w2,color='red', marker='o')
        plt.show()
#print w
    learning_rate = learning_rate - 0.005
