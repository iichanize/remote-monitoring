import cv2
import numpy as np
import Config
import Timestamp

def detectDifference():
    img_1 = cv2.imread(Config.inputPath1)   # 今回取得した画像
    img_2 = cv2.imread(Config.inputPath2)   # 前回取得した画像　にすると良い感じそう

    height = img_1.shape[0]
    width = img_1.shape[1]

    img_size = (int(width), int(height))

    # サイズは揃える(同じカメラならいらないとは思う)
    image1 = cv2.resize(img_1, img_size)
    image2 = cv2.resize(img_2, img_size)

    # 次回実行時用に画像保存
    cv2.imwrite("input/last_image.png", image1)

    # 差分計算
    im_diff = cv2.absdiff(image1, image2)

    # grayscale
    im_diff_gray = cv2.cvtColor(im_diff, cv2.COLOR_BGR2GRAY)

    # 二値化
    thr,binary_im = cv2.threshold(im_diff_gray, cv2.THRESH_OTSU,255,cv2.THRESH_BINARY)

    diffFileName = "/diff_{}.png".format(Timestamp.getTimeStamp())
    cv2.imwrite(Config.outputDir + diffFileName, np.abs(binary_im))

    # モーメント計算
    moments = cv2.moments(binary_im,True)
    if moments['m00'] == 0:
        print("差分なし")
        return 

    # 重心座標
    cx = int(moments['m10']/moments['m00'])
    cy = int(moments['m01']/moments['m00'])

    print("重心:({},{})".format(cx, cy))

    # 重心周りを赤くする
    center_im = im_diff
    for i in (-1,0,1):
        for j in (-1,0,1):
            center_im[cy+i][cx+j][2] = 255
            center_im[cy+i][cx+j][1] = 0
            center_im[cy+i][cx+j][0] = 0

    centerFileName = "/center_point_{}.png".format(Timestamp.getTimeStamp())
    cv2.imwrite(Config.outputDir + centerFileName, center_im)
