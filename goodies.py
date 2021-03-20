from itertools import combinations


m=open('sample_input.txt','r')
con=m.readlines()
n=0
f=0
for line in con:
    for i in line:
        if i.isdigit()==True:
            a=int(i)
            f=1
        if(f==1):
            break
#print a
m.close()
dic = {}
with open("sample_input.txt") as f:
    lines=f.readlines()[1:]
    for line in lines:
        (key, val) = line.split(": ")
        dic[key] = int(val)

print(dic)

#print(dic.values())


arr = [] 
for key in dic.keys() : 
    arr.append(dic[key]) 

print(arr)

no_emp=a # number of employee

min_diff=9999999
for i in combinations(arr,no_emp):
    diff=max(i)-min(i)
    if  diff < min_diff:
        min_diff=diff
        res=i


print("difference is:")
print(min_diff)
print("distribution ")
items=list(res)

fo=open("output.txt","w")
fo.write("The goodies selected for the distribution are:"+'\n')
fo.write("\n")
for item in items:
    for j in dic:
        if dic[j]==item:
            print(j,dic[j])
            fo.write(str(j)+":")
            fo.write(str(dic[j])+ '\n')
            
fo.write("\n")
fo.write("And the difference between the chosen goodie with highest price and the lowest price is:")
fo.write(str(min_diff))
