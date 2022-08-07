import cv2
from os.path import exists

while True:
    file_exists = exists("config.txt")
    image=input("image:")
    sensitivity=input("Sensitivity:")
    if file_exists==True:
        f = open("config.txt", "r")
        modelfile=f.read()
    else:
       modelfile=input("Model File:")
       savechoise=input("Do you want to save model file yes:y no:n")
       if savechoise=="y":
            with open('config.txt', 'w') as f:
                f.write(modelfile)
       else:
            print("Model not saved...")
            
    colorchoise=input("Color 1 gray,2 normal:")
    if colorchoise=="1":
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    elif colorchoise=="2":
        print("İmage doesnt changed...")
    else:
        print("Wrong choise")
        break
    

    img=cv2.imread(image)
    cascade=cv2.CascadeClassifier(cv2.data.haarcascades + modelfile)
    cascade.load(modelfile)
    detected_objects=cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=int(sensitivity))
    print("Detected Objects:"+str(len(detected_objects)))

    if len(detected_objects) != 0:
        for (x, y, width, height) in detected_objects:
            cv2.rectangle(img, (x, y),
                          (x + height, y + width),
                          (0, 255, 0), 2)

    cv2.imshow("Detected Face",img)
    cv2.waitKey(0)
    break
