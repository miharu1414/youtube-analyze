import cv2
import os
import shutil
INTERVAL = 1

#sample→channel_id, igaiga_data→data, remove→本番では消す
def movie_to_jpg(channel_id, video_id, remove=0):
    os.mkdir(f"igaiga_data/{channel_id}/photo")
    fileName = f"igaiga_data/{channel_id}/movie/"+video_id+".mp4"
    videoCapture = cv2.VideoCapture(fileName)
    ## フレーム総数
    totalFrame = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    
    ## n番目のフレーム画像を返す
    def retrieveFrameImage(frameIndex):
        ## インデックスがフレームの範囲内なら…
        if(frameIndex >= 0 & frameIndex < totalFrame):
            videoCapture.set(cv2.CAP_PROP_POS_FRAMES, frameIndex)
            ret, image = videoCapture.read()
            return image
        else:
            return None
    for i in range(int(totalFrame/(INTERVAL*30))):
        cv2.imwrite(f"igaiga_data/{channel_id}/photo/%d.jpg" % (i+1), retrieveFrameImage(i*(INTERVAL*30)))
    #ここで分析ツールを用いる
    if remove:
        shutil.rmtree("igaiga_data/sample/photo")    




