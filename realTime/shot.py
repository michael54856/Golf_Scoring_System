import cv2

def screenshot():
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    origin_img = cam.read()[1]
    #img = cv2.imread('ball.png')
    #newimg = img[790:880, 295:390]
    newimg = origin_img[::]
    gray_img = cv2.cvtColor(newimg, cv2.COLOR_BGR2GRAY)
    imgCon = newimg.copy()
    canny = cv2.Canny(gray_img, 150, 200)
    con, hir = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    count = 0
    catch = 0
    hit = 0
    for cnt in con:
        # cv2.drawContours(imgCon,cnt,-1,(255,0,0),4)
        # print(cv2.contourArea(cnt))
        # print(cv2.arcLength(cnt,True))
        peri = cv2.arcLength(cnt, True)
        are = cv2.contourArea(cnt)
        ver = cv2.approxPolyDP(cnt, peri * 0.02, True)
        #print(are)
        if are > 80:
            hit = 1
    if hit == 1:
        print('not hit')
    else:
        print('hit')
    
    #顯示圖片
    while True:
        cv2.imshow('Canny', canny)
        cv2.imshow('imgCon', imgCon)
        cv2.imshow('golf', newimg)
        # cv2.waitKey(0)
        # cv2.imshow('golf',newimg)
        if cv2.waitKey(20) == ord('q'):
            break
    

screenshot()