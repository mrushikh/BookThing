Data=['1,05,565', '15011', '153', '18', '10,00', '2292', '156', '18', '20,0', '2282', '154', '18', '30106', '2284', '154', '18', '4040', '152', '18', '50;0', '2270', '152', '18', '1,00,00,0', '2262', '150', '18', '1,05,56,5', '1350', '152', '18']

print(Data[0])

def AllToInt(data):
    newList=[]
    for(dat) in data:
        newString=""
        inte=len(dat)
        for i in range(inte):
            if dat[i].isdigit():
                newString=newString+dat[i]
                
        newList.append(newString)
                
    return newList

print(AllToInt(Data))