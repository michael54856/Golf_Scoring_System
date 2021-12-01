import numpy as np
import json 

def angleDiff(vector_1,vector_2):
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    return angle*57.3

targetVector = []

with open("outputJson/poseTarget_keypoints.json") as f:
    data = json.load(f)
    keys = data["people"][0]["pose_keypoints_2d"]
    #head
    targetVector.append([keys[3]-keys[0],keys[4]-keys[1]])
    #body
    targetVector.append([keys[24]-keys[3],keys[25]-keys[4]])
    #right hand
    targetVector.append([keys[6]-keys[3],keys[7]-keys[4]])
    targetVector.append([keys[9]-keys[6],keys[10]-keys[7]])
    targetVector.append([keys[12]-keys[9],keys[13]-keys[10]])
    #left hand
    targetVector.append([keys[15]-keys[0],keys[16]-keys[1]])
    targetVector.append([keys[18]-keys[15],keys[19]-keys[16]])
    targetVector.append([keys[21]-keys[18],keys[22]-keys[19]])
    #right leg
    targetVector.append([keys[27]-keys[24],keys[28]-keys[25]])
    targetVector.append([keys[30]-keys[27],keys[31]-keys[28]])
    targetVector.append([keys[33]-keys[30],keys[34]-keys[31]])
    targetVector.append([keys[66]-keys[33],keys[67]-keys[34]])
    #left leg
    targetVector.append([keys[36]-keys[24],keys[37]-keys[25]])
    targetVector.append([keys[39]-keys[36],keys[40]-keys[37]])
    targetVector.append([keys[42]-keys[39],keys[43]-keys[40]])
    targetVector.append([keys[57]-keys[42],keys[58]-keys[43]])

poseVector = []

with open("outputJson/pose1_keypoints.json") as f:
    data = json.load(f)
    keys = data["people"][0]["pose_keypoints_2d"]
    #head
    poseVector.append([keys[3]-keys[0],keys[4]-keys[1]])
    #body
    poseVector.append([keys[24]-keys[3],keys[25]-keys[4]])
    #right hand
    poseVector.append([keys[6]-keys[3],keys[7]-keys[4]])
    poseVector.append([keys[9]-keys[6],keys[10]-keys[7]])
    poseVector.append([keys[12]-keys[9],keys[13]-keys[10]])
    #left hand
    poseVector.append([keys[15]-keys[0],keys[16]-keys[1]])
    poseVector.append([keys[18]-keys[15],keys[19]-keys[16]])
    poseVector.append([keys[21]-keys[18],keys[22]-keys[19]])
    #right leg
    poseVector.append([keys[27]-keys[24],keys[28]-keys[25]])
    poseVector.append([keys[30]-keys[27],keys[31]-keys[28]])
    poseVector.append([keys[33]-keys[30],keys[34]-keys[31]])
    poseVector.append([keys[66]-keys[33],keys[67]-keys[34]])
    #left leg
    poseVector.append([keys[36]-keys[24],keys[37]-keys[25]])
    poseVector.append([keys[39]-keys[36],keys[40]-keys[37]])
    poseVector.append([keys[42]-keys[39],keys[43]-keys[40]])
    poseVector.append([keys[57]-keys[42],keys[58]-keys[43]])

totalLoss = 0

i = 0
while i < 16 :
    t = angleDiff(poseVector[i],targetVector[i])
    t = (t/10)**(2)
    print(f"{i} : {t}")
    totalLoss += t
    i+=1

print(f"total -{totalLoss}")
