def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield  i

g=test()

for n in [1,10]:

    g = (add(n,i) for i in g)

n=10 # 时,1已经成为过去时了；
g = (add(10,i) for i in (add(10,i) for i in (0,1,2,3)))
print(list(g))

# i=1
# sum=0
# while i<100:
#     if i%2==0:
#         sum-=i
#     else:
#         sum+=i
#     i+=1
# print(sum)




# sum =0
# for  i in range(1,100):
#     if i%2==0:
#         sum-=i
#     else:
#         sum+=i
# print(sum)