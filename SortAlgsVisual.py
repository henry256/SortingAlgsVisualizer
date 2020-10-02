import pygame
import random
#@HENRY CHEN

#initialize pygame
pygame.init()
#creating the screen
screen=pygame.display.set_mode((900,750))

#set title/icon
titleFnt=pygame.font.SysFont("comicsans",35)
descFnt=pygame.font.SysFont("comicsans",30)
#img=pygame.image.load(image_path)
#pygame.display.set_icon(img)
fnt = pygame.font.SysFont("comicsans", 30) 
fnt1 = pygame.font.SysFont("comicsans", 20) 

#pygame runs while run=True
run=True
width=900
height=600
numBars=100
maxVal=100

barClr=(0, 204, 102)
barClrView=(255, 0, 0)
barClrSwitch=(0, 0, 153)
barClrEnd=(255, 102, 0)

btnHover=(97, 187, 254)
btnClr=(70,150,220)
#initialize array with only 0 values
num_array=[0]*numBars
array_clr={}
sortingMethod=""

def generate_arr():
    for i in range(0,numBars):
        num_array[i]=random.randrange(1,maxVal)
        array_clr[i]=barClr
generate_arr()
def refill():
    screen.fill((255,255,255))
    draw()
    pygame.display.update()
    pygame.time.delay(20)

def button(msg,font,x,y,w,h,active,inactive):
    mouse=pygame.mouse.get_pos()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen, active,(x,y,w,h))
    else: 
        pygame.draw.rect(screen, inactive,(x,y,w,h))

    
    text=font.render(msg,1,(255,255,255))
    text_rect = text.get_rect(center=(x+(w/2), y+(h/2)))
    screen.blit(text, text_rect)



def draw():
    #Render description
    title=titleFnt.render("Sorting Algorithms Visualizer",1,(0,0,0))
    screen.blit(title, (300, 20))
    if sortingMethod !="":
        desc=descFnt.render("Currently Performing: {} Sort".format(sortingMethod),1,(0,0,0))
        screen.blit(desc, (300, 60))
    #render buttons
    #new Array (top right x,top right y, len, width)
    button("New Array",fnt,130,675,150,55,btnHover,btnClr)
    # Insertion Sort
    button("Insertion Sort",fnt1,350,660,125,35,btnHover,btnClr)
    # Bucket Sort
    button("Bucket Sort",fnt1,350,700,125,35,btnHover,btnClr)
    # Merge Sort
    button("Merge Sort",fnt1,500,660,125,35,btnHover,btnClr)
    # Quick Sort
    button("Quick Sort",fnt1,500,700,125,35,btnHover,btnClr)
    #Bubble Sort
    button("Bubble Sort",fnt1,650,660,125,35,btnHover,btnClr)
    #Heap Sort
    button("Heap Sort",fnt1,650,700,125,35,btnHover,btnClr)


    global num_array, array_clr
    #set bar array dimentions
    bar_width=(width-numBars)//numBars
    vrt_boundry=width//numBars
    hrz_boundry=(height-50)//maxVal 

    for i in range(1,maxVal):
        pygame.draw.line(screen,(224,224,224),(0,hrz_boundry*i+maxVal+50),(900, hrz_boundry * i + 150),1)
    for i in range(0,numBars):
        pygame.draw.line(screen,array_clr[i],
            (vrt_boundry * i+4, 650),
            (vrt_boundry * i+4,650-num_array[i]*hrz_boundry),
            bar_width)

#Sorting algs
#Merge Sort
def mergeSort(array,l,r):
    mid=(l+r)//2
    if l<r:
        mergeSort(array,l,mid)
        mergeSort(array,mid+1,r)
        merge(array,l,mid,mid+1,r)


def merge(array,x1,y1,x2,y2):
    idx1=x1
    idx2=x2
    temp=[]
    pygame.event.pump()
    global array_clr
    while idx1<=y1 and idx2<=y2:
        #show that the two indexes are being compared
        array_clr[idx1]=barClrView 
        array_clr[idx2]=barClrView
        refill() 
        array_clr[idx1]=barClr
        array_clr[idx2]=barClr
        if array[idx1]<array[idx2]:
            temp.append(array[idx1])
            idx1+=1
        else:
            temp.append(array[idx2])
            idx2+=1
    while idx1<=y1:
        array_clr[idx1]=barClrView 
        refill()
        array_clr[idx1]=barClr
        temp.append(array[idx1])
        idx1+=1
    while idx2<=y2:
        array_clr[idx2]=barClrView 
        refill()
        array_clr[idx2]=barClr
        temp.append(array[idx2])
        idx2+=1  
    #append temp to original array
    idx2=0
    for i in range(x1,y2+1):
        pygame.event.pump()
        array[i]=temp[idx2]
        idx2+=1
        array_clr[i]=barClrSwitch
        refill()
        if y2-x1 == len(array)-2:
            array_clr[i]=barClrEnd
        else:
            array_clr[i]=barClr
#Quick Sort
def quickSort(array,l,r):
    if l==r:
        array_clr[l]=barClrEnd
        refill()
    if l<r:
        part=partition(array,l,r)
        quickSort(array,l,part-1)
        quickSort(array,part+1,r)

def partition(array,l,r): 
    pivot=array[r]
    array_clr[r]=barClrView 
    for i in range(l,r):
        array_clr[i]=barClrView 
        refill()
        array_clr[i]=barClr
        if array[i]<=pivot:
            array_clr[i]=barClrSwitch
            array_clr[l]=barClrSwitch
            array[i],array[l]=array[l],array[i]
            refill()
            array_clr[i]=barClr
            array_clr[l]=barClr
            l+=1
    array_clr[r]=barClrSwitch
    array_clr[l]=barClrSwitch
    refill()
    array[l],array[r]=array[r],array[l]
    array_clr[r]=barClr
    array_clr[l]=barClrEnd
    refill()
    return l
#Bubble sort
def bubbleSort(arr):
    noSwitches=False
    while noSwitches==False:
        didNotSwitch=True
        for i in range(1,len(arr)):
            array_clr[i]=barClrView 
            array_clr[i-1]=barClrView 
            refill()
            if arr[i]<arr[i-1]:
                array_clr[i]=barClrSwitch 
                array_clr[i-1]=barClrSwitch
                refill() 
                arr[i],arr[i-1]=arr[i-1], arr[i]
                didNotSwitch=False
                array_clr[i]=barClr
                array_clr[i-1]=barClr
            else:
                array_clr[i]=barClr
                array_clr[i-1]=barClr
                refill() 
        noSwitches=didNotSwitch
    for i in range(len(arr)):
        array_clr[i]=barClrEnd
    
#heapSort
def heapSort(arr):
    n=len(arr)
    for i in range(n//2,-1,-1):
        createHeap(arr,n,i)
    for i in range(n-1,0,-1):
        #take int at index 0(largest) and swap it with the last element in the array
        array_clr[i]=barClrSwitch 
        array_clr[0]=barClrSwitch
        refill()
        arr[i],arr[0]=arr[0],arr[i]
        array_clr[i]=barClrEnd
        array_clr[0]=barClr
        createHeap(arr,i,0)    
    array_clr[0]=barClrEnd

def createHeap(arr,n,idx):
    largest=idx
    left=2*idx+1
    right=2*idx+2
    if left<n and array_clr[left] != barClrEnd:
        array_clr[left]=barClrView
        array_clr[largest]=barClrView
        refill()
        array_clr[left]=barClr
        array_clr[largest]=barClr
        if arr[left]>arr[largest]:
            largest=left
        refill()
    if right<n and array_clr[right] != barClrEnd:
        array_clr[right]=barClrView
        array_clr[largest]=barClrView
        refill()
        array_clr[right]=barClr
        array_clr[largest]=barClr
        if arr[right]>arr[largest]:
            largest=right
        refill()
    if largest!=idx:
        #if largest isnt move the child to the largest spot and recreate the heap
        array_clr[idx]=barClrSwitch 
        array_clr[largest]=barClrSwitch
        refill()
        arr[largest],arr[idx]=arr[idx],arr[largest]
        array_clr[idx]=barClr
        array_clr[largest]=barClr
        createHeap(arr,n,largest)
#insertionSort
def insertionSort(arr):
    for i in range(1,len(arr)):
        val=arr[i]
        b=i-1
        while b>=0 and val<arr[b]:
            array_clr[b+1]=barClrView
            array_clr[b]=barClrView
            refill()
            array_clr[b+1]=barClrSwitch
            array_clr[b]=barClrSwitch
            refill()
            arr[b+1]=arr[b]
            array_clr[b+1]=barClr
            array_clr[b]=barClr
            b-=1
            refill()


        array_clr[b+1]=barClrSwitch
        refill()
        arr[b+1]=val
        array_clr[b+1]=barClr
        refill()
    for i in range(len(arr)):
        array_clr[i]=barClrEnd
#bucketSort
def bucketSort(arr,numBuckets=10):
    buckets=[]
    for i in range(numBuckets):
        buckets.append([])
    for i in range(len(arr)):
        array_clr[i]=barClrView
        refill()
        bucketNum=arr[i]//numBuckets
        buckets[bucketNum].append(arr[i])
        array_clr[i]=barClr
        refill()

    startEnd={}
    numBuck=0
    arrIndex=0
    for bucket in buckets:
        startEnd[numBuck]=[arrIndex]
        for num in bucket:
            array_clr[arrIndex]=barClrSwitch
            refill()
            arr[arrIndex]=num
            array_clr[arrIndex]=barClr
            refill()
            arrIndex+=1
        startEnd[numBuck].append(arrIndex-1)
        numBuck+=1
    for i in range(numBuckets):
        startIdx=startEnd[i][0]
        endIdx=startEnd[i][1]
        buckInsertSort(arr,startIdx,endIdx)
def buckInsertSort(arr,start,end):
    for i in range(start+1,end+1):
        val=arr[i]
        b=i-1
        while b>=start and val<arr[b]:
            array_clr[b+1]=barClrView
            array_clr[b]=barClrView
            refill()
            array_clr[b+1]=barClrSwitch
            array_clr[b]=barClrSwitch
            refill()
            arr[b+1]=arr[b]
            array_clr[b+1]=barClr
            array_clr[b]=barClr
            b-=1
            refill()


        array_clr[b+1]=barClrSwitch
        refill()
        arr[b+1]=val
        array_clr[b+1]=barClr
        refill()
    for i in range(start,end+1):
        array_clr[i]=barClrEnd
        refill()

    

while run:
    screen.fill((255, 255, 255)) 
    click=pygame.mouse.get_pressed()
    mouse=pygame.mouse.get_pos()
    for event in pygame.event.get():
        #if close is clicked
        if event.type==pygame.QUIT:
            run = False
        #have events for mouse clicks
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                #new array button is clicked
                if 130+150>mouse[0]>130 and 675+55>mouse[1]>675:
                    generate_arr()
                #Insert click
                elif 350+125>mouse[0]>350 and 660+35>mouse[1]>660:
                    sortingMethod="Insertion"
                    insertionSort(num_array)
                elif 350+125>mouse[0]>350 and 700+35>mouse[1]>700:
                    sortingMethod="Bucket"
                    bucketSort(num_array)
                elif 500+125>mouse[0]>500 and 660+35>mouse[1]>660:
                    sortingMethod="Merge"
                    mergeSort(num_array,0,len(num_array)-1)
                elif 500+125>mouse[0]>500 and 700+35>mouse[1]>700:
                    sortingMethod="Quick"
                    quickSort(num_array,0,len(num_array)-1)
                elif 650+125>mouse[0]>650 and 660+35>mouse[1]>660:
                    sortingMethod="Bubble"
                    bubbleSort(num_array)
                elif 650+125>mouse[0]>650 and 700+35>mouse[1]>700:
                    sortingMethod="Heap"
                    heapSort(num_array)
                

    #draw the new events.
    draw()
    sortingMethod=""

    pygame.display.update()
    #sortingMethod=""

pygame.quit()
quit()
        


