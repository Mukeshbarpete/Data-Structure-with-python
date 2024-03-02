from random import*
name = input("write your name here : ..")
ch = input("if you want select number range then press Y otherwise N : ")
if(ch=='Y'):
    n1 = int(input("enter first number :"))
    n2 = int(input("enter second number :"))
    n = randint(n1,n2)
else :
    n = randint(0,1000)
    n1 = 0
    n2 = 1000
t = True
i=0
while(t):
    k = int(input("enter a number :"))
    if k<n:
        print("you enter very smaller number than original number  try again !:")
        i+=1
    else :
        if k>n :
            print("youu enter very large number than original numbertry again ! ")
            i+=1
        else :
            print(" congratutilations ! \n you won the game :")
            print("thamk you ",name," for playing this game!")
            t= False
            i+=1

print('you try ',i,'time than success:')
print('your luck % is =',100//i,'%')
        
        
