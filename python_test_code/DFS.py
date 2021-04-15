import cv2
import codecs
import numpy as np

map_pic=cv2.imread("test.png")

pic,g,r=cv2.split(map_pic)


bulr_size=10

mainpic = cv2.blur(pic, (bulr_size, bulr_size))










#cv2.floodFill(mainpic,mask,(500,500),(255,0,0),(50,50,50),(0,0,0),cv2.FLOODFILL_FIXED_RANGE)





mainpic=cv2.resize(mainpic,(int(1000/bulr_size),int(1000/bulr_size)))
h, w = mainpic.shape[:2]
mask = np.zeros([h+2, w+2], np.uint8)

startx=int(1000/bulr_size/2)
starty=int(1000/bulr_size/2)

cv2.floodFill(mainpic,mask,(50,50),(255,0,0),(30,50,50),(0,0,0),cv2.FLOODFILL_FIXED_RANGE)

Map=mainpic




def go():
        global  list_zouguo,Map
        
        i=len(list_zouguo)-1

  
        
        if Map[list_zouguo[i][0]-1][list_zouguo[i][1]]==255 and ([list_zouguo[i][0]-1,list_zouguo[i][1]] not in list_zouguo):
            list_zouguo.append([list_zouguo[i][0]-1,list_zouguo[i][1]] )
            go()

            
        if Map[list_zouguo[i][0]][list_zouguo[i][1]+1]==255 and ([list_zouguo[i][0],list_zouguo[i][1]+1] not in list_zouguo):
            list_zouguo.append([list_zouguo[i][0],list_zouguo[i][1]+1] )
            go()
 

        if Map[list_zouguo[i][0]+1][list_zouguo[i][1]]==255 and ([list_zouguo[i][0]+1,list_zouguo[i][1]] not in list_zouguo):
            list_zouguo.append([list_zouguo[i][0]+1,list_zouguo[i][1]] )
            go()

            
        if Map[list_zouguo[i][0]][list_zouguo[i][1]-1]==255 and ([list_zouguo[i][0],list_zouguo[i][1]-1] not in list_zouguo):
            list_zouguo.append([list_zouguo[i][0],list_zouguo[i][1]-1] )
            go()


        
        return



        





list_assable=[]
for i in range(Map.shape[0]):
    for j in range(Map.shape[1]):
        if(Map[i][j]==255):
            list_assable.append([i,j])
            
        



        
list_zouguo=[]

list_zouguo.append([startx,starty])

go()



I=np.zeros((int(1000/bulr_size),int(1000/bulr_size)),dtype=np.uint8)
I=cv2.merge([mainpic, I, I])

print(len(list_zouguo))
print(len(list_assable))



for i in list_zouguo:
    for X in range(I.shape[0]):
        for Y in range(I.shape[1]):
            I[X][Y][2]=0

    list_assable=[]
    for XX in range(Map.shape[0]):
        for YY in range(Map.shape[1]):
            if(Map[XX][YY]==255):
                list_assable.append([XX,YY])
                
    cv2.circle(I,(i[1],i[0]),1,(0,120,0),0)
    cv2.circle(I,(i[1],i[0]),1,(0,120,120),0)
    cv2.imshow(" ",cv2.resize(I,(1000,1000)))
    cv2.waitKey(1)

if [50,50] in list_zouguo:
    print("yes")

        



























