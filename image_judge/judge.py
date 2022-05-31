from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import json 

def generatePosition(fileName): #生成這個frame的向量資訊(讀取json)
    myPosition = []
    with open(fileName) as f:
        data = json.load(f)
        keys = data["people"][0]["pose_keypoints_2d"]

        #head
        myPosition.append([keys[0],keys[1]])

        #body
        myPosition.append([keys[3],keys[4]])
        
        #right hand
        myPosition.append([keys[3],keys[4]])
        myPosition.append([keys[6],keys[7]])
        myPosition.append([keys[9],keys[10]])
        
        #left hand
        myPosition.append([keys[3],keys[4]])
        myPosition.append([keys[15],keys[16]])
        myPosition.append([keys[18],keys[19]])
    
        
        #right leg
        myPosition.append([keys[24],keys[25]])
        myPosition.append([keys[27],keys[28]])
        myPosition.append([keys[30],keys[31]])
        myPosition.append([keys[33],keys[34]])
       
        
        #left leg
        myPosition.append([keys[24],keys[25]])
        myPosition.append([keys[36],keys[37]])
        myPosition.append([keys[39],keys[40]])
        myPosition.append([keys[42],keys[43]])

    return myPosition


def generateVector(fileName): #生成這個frame的向量資訊(讀取json)
    myVector = []
    with open(fileName) as f:
        data = json.load(f)
        keys = data["people"][0]["pose_keypoints_2d"]

        #head
        if keys[2] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[3]-keys[0],keys[4]-keys[1]])

        #body
        if keys[26] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[24]-keys[3],keys[25]-keys[4]])
        
        #right hand
        if keys[8] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else :
            myVector.append([keys[6]-keys[3],keys[7]-keys[4]])

        if keys[11] == 0 or keys[8] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[9]-keys[6],keys[10]-keys[7]])
       
        if keys[14] == 0 or keys[11] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[12]-keys[9],keys[13]-keys[10]])
        
        #left hand
        if keys[17] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[15]-keys[3],keys[16]-keys[4]])
        
        if keys[20] == 0 or keys[17] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[18]-keys[15],keys[19]-keys[16]])
        
        if keys[23] == 0 or keys[20] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[21]-keys[18],keys[22]-keys[19]])
        
        #right leg
        if keys[29] == 0 or keys[26] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[27]-keys[24],keys[28]-keys[25]])

        if keys[32] == 0 or keys[29] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[30]-keys[27],keys[31]-keys[28]])
        
        if keys[35] == 0 or keys[32] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[33]-keys[30],keys[34]-keys[31]])
        
        if keys[68] == 0 or keys[35] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[66]-keys[33],keys[67]-keys[34]])
        
        #left leg
        if keys[38] == 0 or keys[26] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[36]-keys[24],keys[37]-keys[25]])
        
        if keys[41] == 0 or keys[38] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[39]-keys[36],keys[40]-keys[37]])
        
        if keys[44] == 0 or keys[41] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[42]-keys[39],keys[43]-keys[40]])
        
        if keys[59] == 0 or keys[44] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[57]-keys[42],keys[58]-keys[43]])
        
    return myVector

def angleDiff(vector_1,vector_2):
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    return angle*57.3

targetVector = []

with open("outputJson/teacherReady_keypoints.json") as f:
    data = json.load(f)
    keys = data["people"][0]["pose_keypoints_2d"]
    #head
    if keys[2] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[3]-keys[0],keys[4]-keys[1]])

    #body
    if keys[26] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[24]-keys[3],keys[25]-keys[4]])
    
    #right hand
    if keys[8] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else :
        targetVector.append([keys[6]-keys[3],keys[7]-keys[4]])

    if keys[11] == 0 or keys[8] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[9]-keys[6],keys[10]-keys[7]])
    
    if keys[14] == 0 or keys[11] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[12]-keys[9],keys[13]-keys[10]])
    
    #left hand
    if keys[17] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[15]-keys[3],keys[16]-keys[4]])
    
    if keys[20] == 0 or keys[17] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[18]-keys[15],keys[19]-keys[16]])
    
    if keys[23] == 0 or keys[20] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[21]-keys[18],keys[22]-keys[19]])
    
    #right leg
    if keys[29] == 0 or keys[26] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[27]-keys[24],keys[28]-keys[25]])

    if keys[32] == 0 or keys[29] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[30]-keys[27],keys[31]-keys[28]])
    
    if keys[35] == 0 or keys[32] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[33]-keys[30],keys[34]-keys[31]])
    
    if keys[68] == 0 or keys[35] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[66]-keys[33],keys[67]-keys[34]])
    
    #left leg
    if keys[38] == 0 or keys[26] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[36]-keys[24],keys[37]-keys[25]])
    
    if keys[41] == 0 or keys[38] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[39]-keys[36],keys[40]-keys[37]])
    
    if keys[44] == 0 or keys[41] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[42]-keys[39],keys[43]-keys[40]])
    
    if keys[59] == 0 or keys[44] == 0 : #若有一個點沒偵測到,向量設為0
        targetVector.append([0,0])
    else:
        targetVector.append([keys[57]-keys[42],keys[58]-keys[43]])

poseVector = []

with open("outputJson/studentReady_keypoints.json") as f:
    data = json.load(f)
    keys = data["people"][0]["pose_keypoints_2d"]
    #head
    if keys[2] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[3]-keys[0],keys[4]-keys[1]])

    #body
    if keys[26] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[24]-keys[3],keys[25]-keys[4]])
    
    #right hand
    if keys[8] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else :
        poseVector.append([keys[6]-keys[3],keys[7]-keys[4]])

    if keys[11] == 0 or keys[8] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[9]-keys[6],keys[10]-keys[7]])
    
    if keys[14] == 0 or keys[11] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[12]-keys[9],keys[13]-keys[10]])
    
    #left hand
    if keys[17] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[15]-keys[3],keys[16]-keys[4]])
    
    if keys[20] == 0 or keys[17] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[18]-keys[15],keys[19]-keys[16]])
    
    if keys[23] == 0 or keys[20] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[21]-keys[18],keys[22]-keys[19]])
    
    #right leg
    if keys[29] == 0 or keys[26] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[27]-keys[24],keys[28]-keys[25]])

    if keys[32] == 0 or keys[29] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[30]-keys[27],keys[31]-keys[28]])
    
    if keys[35] == 0 or keys[32] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[33]-keys[30],keys[34]-keys[31]])
    
    if keys[68] == 0 or keys[35] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[66]-keys[33],keys[67]-keys[34]])
    
    #left leg
    if keys[38] == 0 or keys[26] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[36]-keys[24],keys[37]-keys[25]])
    
    if keys[41] == 0 or keys[38] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[39]-keys[36],keys[40]-keys[37]])
    
    if keys[44] == 0 or keys[41] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[42]-keys[39],keys[43]-keys[40]])
    
    if keys[59] == 0 or keys[44] == 0 : #若有一個點沒偵測到,向量設為0
        poseVector.append([0,0])
    else:
        poseVector.append([keys[57]-keys[42],keys[58]-keys[43]])

totalLoss = 0

def angleDiff(vector_1,vector_2): #回傳兩個向量的角度差
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    if dot_product > 1 :
        dot_product = 1
    angle = np.arccos(dot_product)
    return angle*57.3

def VectorDiffLoss(vec1,vec2):
    points = 0
    i = 1
    zeroVectorCount = 0
    while i < 16 :
        if(vec1[i][0] == 0 and vec1[i][1] == 0) or (vec2[i][0] == 0 and vec2[i][1] == 0) :#如果有一個是0向量
            zeroVectorCount += 1
            points += 1 #加一意思一下
        else :
            t = angleDiff(vec1[i],vec2[i])
            t = (t/5)**(4) #相差5度內沒什麼關係
            points += t
        i+=1
    if zeroVectorCount >= 6: #如果超過8個向量沒被偵測,讓分數一次加很多
        points += 500000
    return points/16

pose_Vector = generateVector("outputJson/studentReady_keypoints.json") #取得target的向量資訊
posePosition = generatePosition("outputJson/studentReady_keypoints.json") #取得target的向量資訊
print(f"total -{VectorDiffLoss(targetVector,poseVector)}")

plt.rcParams["figure.figsize"] = [10, 10]
plt.rcParams["figure.autolayout"] = True
soa = np.array([0,0,0,0])
plt.figure(figsize=(4, 6), dpi = 100)
for i in range(16) :
    newrow = [posePosition[i][0],posePosition[i][1],pose_Vector[i][0],pose_Vector[i][1]]
    soa = np.vstack([soa, newrow])

soa = np.delete(soa, (0), axis=0)
k = 0
ax = plt.gca()
for X,Y,U,V in soa:
    if angleDiff(targetVector[k],poseVector[k]) >= 15:
        ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color='red')
    else:
        ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
    k += 1

ax.set_xlim([0, 400])
ax.set_ylim([0, 600])
for i in range(16) :
    plt.scatter(posePosition[i][0], posePosition[i][1], s=30, c='green')


plt.gca().invert_yaxis()
output_fileName = "studentImg.png"
plt.savefig(output_fileName)
plt.clf()
