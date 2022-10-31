import cv2
import os
import shutil

#sample→channel_id, igaiga_data→data
def movie_to_jpg(channel_id, vidoe_id, frameIndex):
    os.mkdir("igaiga_data/sample/photo")
    fileName = "igaiga_data/sample/movie/"+video_id+".mp4"
    videoCapture = cv2.VideoCapture(fileName)
    ## フレーム総数
    totalFrame = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    
    ## n番目のフレーム画像を返す
    def retrieveFrameImage(frameIndex):
        ## インデックスがフレームの範囲内なら…
        if(frameIndex >= 0 & frameIndex < totalFrames):
            videoCapture.set(cv2.CAP_PROP_POS_FRAMES, frameIndex)
            ret, image = videoCapture.read()
            return image
        else:
            return None
    for i in range(int(totalFrame/30)):
        cv2.imwrite("igaiga_data/sample/photo/%d.jpg" % (i+1), retrieveFrameImage(i*INTERVAL))
    #ここで分析ツールを用いる
    shutil.rmtree("igaiga_data/sample/photo")




