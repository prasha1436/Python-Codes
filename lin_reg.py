a= [-0.75/4, 0.25/4, 2.25/4, -1.75/4]
b= [0.5, 1, 2, 0]
theta0= 0
theta1= 5
m= len(a)
lrstr= input('What should be the learning rate:')
lr= float(lrstr)
cost= float(50)
sigma0= 0
sigma1= 0
while cost !=0:
    i= 0
    tcost= 0
    for x in a:
        sigma0= sigma0 + (theta0+ theta1*x- b[i])
        sigma1= sigma1 + (theta0+ theta1*x- b[i])*x
        tcost= tcost + (theta0+ theta1*x- b[i])**2
        i= i+1
        if i == m - 1:
            temp0= theta0 - lr*1/m*sigma0
            temp1= theta1 - lr*1/m*sigma1
            cost= tcost*1/(2*m)
            print(cost)
        else:
            continue
    theta0= temp0
    theta1= temp1

print(theta0, theta1)
