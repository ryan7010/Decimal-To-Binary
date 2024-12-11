num=int(input("Enter any number:"))
numl=num
bi = []
while num!=1:
    i=num%2
    num = (num-(num%2))/2
    i=int(i)
    bi.append(i)
    #print(num,i)
    #print(bi)
bi.append(1)
for i in range(len(bi)):
    bi[i]=str(bi[i])

bii=bi.reverse()
test = ''.join(bi)
#print(test)
print("The number that you entered",numl,"is",test,"in binary.")
