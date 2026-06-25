import easyocr
import cv2
reader=easyocr.Reader(['en'],gpu=False)

image_path = r'DataCropped.jpeg'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
result=reader.readtext(gray)
tokens=[]
number=['0','1','2','3','4','5','6','7','8','9']
for(bbox,text,prob) in result:   
    a= text[0]
    for num in number:
        if(a==num):
            tokens.append(text)
            break    


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
print(AllToInt(tokens))  