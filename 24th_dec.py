# for i in range(10):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# for i in range(10,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()




# i=999999
# while True:
#     print("while..",i)
#     i+=1


# i=0
# while i<=20:
#     if i%2==0:
#         print(i)
#     else:
#         pass
#     i+=1


for z in range(25):
    spc=""
    str=""
    for i in range(25-z):
        spc+=" "
    for j in range(z+1):
        str+="* "

    print(spc, end=" ")
    print(str)

str1="* * * * *"
for a in range(10):
    spc1=""
    for b in range(20):
        spc1+=" "
    
    print(spc1, end=" ")
    print(str1)





