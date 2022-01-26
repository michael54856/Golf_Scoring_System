import subprocess
import numpy as np
import os, json
import pandas as pd
import math
import time
import glob


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
        if keys[17] == 0 or keys[2] == 0 : #若有一個點沒偵測到,向量設為0
            myVector.append([0,0])
        else:
            myVector.append([keys[15]-keys[0],keys[16]-keys[1]])
        
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

def generateVectorFromList(keys): #生成merge出來的的向量資訊(讀取list)
    myVector = []
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
    if keys[17] == 0 or keys[2] == 0 : #若有一個點沒偵測到,向量設為0
        myVector.append([0,0])
    else:
        myVector.append([keys[15]-keys[0],keys[16]-keys[1]])
    
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

def angleDiff(vector_1,vector_2): #回傳兩個向量的角度差
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    if dot_product > 1 :
        dot_product = 1
    angle = np.arccos(dot_product)
    return angle*57.3
 

def mergeFrame(number,VectorFrame_1,VectorFrame_2) :
    file_2_percent = number-math.floor(number)
    file_1_percent = 1-file_2_percent
    mergeList = []
    i = 0
    while i < 16 :
        mergeList.append([VectorFrame_1[i][0]*file_1_percent,VectorFrame_1[i][1]*file_1_percent])
        i += 1

    while i < 16 :
        if mergeList[i][0] == 0 and  mergeList[i][1] == 0:#如果上一個frame沒偵測到,那就直接使用這個frame的資訊
            mergeList[i] = [VectorFrame_2[i][0],VectorFrame_2[i][1]]
        else:
            mergeList[i][0] += VectorFrame_2[i][0]*file_2_percent
            mergeList[i][1] += VectorFrame_2[i][1]*file_2_percent
        i += 1

    return mergeList

def VectorDiffLoss(vec1,vec2):
    points = 0
    i = 0
    zeroVectorCount = 0
    while i < 16 :
        if(vec1[i][0] == 0 and vec1[i][1] == 0) or (vec2[i][0] == 0 and vec2[i][1] == 0) :#如果有一個是0向量
            zeroVectorCount += 1
            points += 1 #加一意思一下
        else :
            t = angleDiff(vec1[i],vec2[i])
            t = (t/6.25)**(2) #相差5度內沒什麼關係
            points += t
        i+=1
    if zeroVectorCount >= 8: #如果超過5個向量沒被偵測,讓分數一次加很多
        points += 5000
    return points

def scoreCalculate(VectorList,path_to_Target):
    Target_json_files = [pos_json for pos_json in os.listdir(path_to_Target) if pos_json.endswith('.json')]
    totalLoss = 0
    for index, currentFrameName in enumerate(Target_json_files):
        currentVector = generateVector(path_to_Target+currentFrameName) #取得target的向量資訊

        percent = (index+1) / len(Target_json_files) #取得這個frame所占百分比
        whichToChoose =  percent*len(VectorList)

        compareVector = []
        if whichToChoose < 1 : #直接使用第一個
            compareVector = VectorList[0] #取得要比對的向量資訊
        else:
            if whichToChoose % 1 != 0: #如果是小數,要用2個frame做merge
                compareVector = mergeFrame(whichToChoose,VectorList[math.floor(whichToChoose)-1],VectorList[math.floor(whichToChoose)])
            else: #整數直接取用
                compareVector = VectorList[int(whichToChoose)-1] #取得要比對的向量資訊
        totalLoss += VectorDiffLoss(currentVector,compareVector)
    totalLoss /= len(Target_json_files)
    return totalLoss


lastFiles = glob.glob('Mykey/*')
for f in lastFiles:
    os.remove(f)
subprocess.Popen(["C:\\Users\\michael\\Desktop\\openpose\\build\\x64\\Debug\\OpenPoseDemo.exe","--model_folder","C:\\Users\\michael\\Desktop\\openpose\\models","--num_gpu_start","0","--process_real_time","-number_people_max","1","--net_resolution","640x480","--write_json","MyKey"])
fileNumber = 0

swingState = 0
#0->沒有準備
#1->已經準備完成,將要預備揮桿
#2->揮桿預備完成,將要揮桿

ReadyVectorList = []
SwingVectorList = []

score = 0

while True:
    nextFileNumber = fileNumber+1
    numberDigits_1 = len(str(fileNumber))
    numberDigits_2 = len(str(nextFileNumber))
    fileName = 'MyKey/'
    nextFileName = 'MyKey/'
    for i in range(0,12-numberDigits_1):
        fileName += '0'
    for i in range(0,12-numberDigits_2):
        nextFileName += '0'
    fileName += str(fileNumber)
    fileName += '_keypoints.json'
    nextFileName += str(nextFileNumber)
    nextFileName += '_keypoints.json'
    while not os.path.exists(nextFileName): #下一個檔案存在才會去進行
        time.sleep(0.01)

    #successfully read current frame
    with open(fileName) as f:
        data = json.load(f)
        if len(data["people"]) > 0 :
            currentVector = generateVector(fileName) #取得target的向量資訊

            if swingState == 1:
                ReadyVectorList.append(currentVector)

            if swingState == 2:
                SwingVectorList.append(currentVector)
            
            ready_begin_compareVector = generateVector('Output_Key/Front_Ready_Begin_keypoints.json') #取得要比對的向量資訊
            ready_end_compareVector = generateVector('Output_Key/Front_Ready_End_keypoints.json') #取得要比對的向量資訊
            swing_end_compareVector = generateVector('Output_Key/Front_Swing_End_keypoints.json') #取得要比對的向量資訊


            #print(f'{VectorDiffLoss(currentVector,ready_begin_compareVector)} {VectorDiffLoss(currentVector,ready_end_compareVector)} {VectorDiffLoss(currentVector,swing_end_compareVector)}')
            
            if swingState == 0 or swingState == 1 :
                if VectorDiffLoss(currentVector,ready_begin_compareVector) < 300 : #重新抓取
                    ReadyVectorList.clear()
                    ReadyVectorList.append(currentVector)
                    score = 0
                    swingState = 1
            
            if swingState == 1 or swingState == 2:
                if VectorDiffLoss(currentVector,ready_end_compareVector) < 575 : #偵測到預備揮桿完成
                    if swingState == 1 :
                        score += scoreCalculate(ReadyVectorList,'Output_Video_Key/Front_Ready/')
                        swingState = 2
                        print(f'detect ready pose : , ' , end='')
                    SwingVectorList.clear()
                    SwingVectorList.append(currentVector)
            
            if swingState == 2:
                if VectorDiffLoss(currentVector,swing_end_compareVector) < 675 : #偵測到完整揮桿完成
                    swingState = 0
                    score += scoreCalculate(SwingVectorList,'Output_Video_Key/Front_Swing/')
                    score /= 2
                    score = (score-300) / 1000
                    score = (1-score) * 100 
                    if score > 100 :
                        score = 100
                    if score < 0 :
                        score = 0
                    print(f'your swing score : {round(score,1)}')
            
    
    os.remove(fileName)

    fileNumber += 1


'''
with open('Mykey/000000000054_keypoints.json') as f:
    data = json.load(f)
    print(len(data["people"]))
'''

'''
for index, currentFrameName in enumerate(Target_json_files):
    currentVector = generateVector(path_to_Target+currentFrameName) #取得target的向量資訊

    percent = (index+1) / len(Target_json_files) #取得這個frame所占百分比
    whichToChoose =  percent*len(Compare_json_files)

    compareVector = []
    if whichToChoose < 1 : #直接使用第一個
        compareVector = generateVector(compareDir+Compare_json_files[0]) #取得要比對的向量資訊
    else:
        if whichToChoose % 1 != 0: #如果是小數,要用2個frame做merge
            newKeyList = mergeFrame(whichToChoose,compareDir+Compare_json_files[math.floor(whichToChoose)-1],compareDir+Compare_json_files[math.floor(whichToChoose)])
            compareVector = generateVectorFromList(newKeyList) #取得要比對的向量資訊
        else: #整數直接取用
            compareVector = generateVector(compareDir+Compare_json_files[int(whichToChoose)-1]) #取得要比對的向量資訊
    totalLoss += VectorDiffLoss(currentVector,compareVector)
    
print(f"total -{totalLoss/len(Target_json_files)}")
'''




