import cv2
import os

def img_stitcher(imgs: list):
    images = []
    for imgN in imgs:
        curImg = cv2.resize(imgN, (0, 0), None, 0.2, 0.2)
        images.append(curImg)

    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    if (status == cv2.STITCHER_OK):
        print('Panorama Generated')
        # cv2.imshow("result", result)
        # cv2.waitKey(1)
    else:
        print('Panorama Generation Unsuccessful')
    return result

def main():
    mainFolder = 'images'
    myFolders = os.listdir(mainFolder)  # 读取主文件
    print(myFolders)
    img_list = []
    for img in myFolders:
        img = cv2.imread(os.path.join(mainFolder, img))
        img_list.append(img)

    result = img_stitcher(img_list)
    # cv2.imwrite("result/test.jpg", result)
    cv2.imshow("result", result)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
