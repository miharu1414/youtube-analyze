# 音声認識
import speech_recognition as sr
import subprocess
import os
# csv化
import pandas as pd

# 絶対パスを取得する
import pathlib



def Video_to_csv(video_id):
    
    # 文字起こし対象のファイル
    text_video_path = "data/movie"+video_id+".mp4"
    
    text_video_path = pathlib.Path(text_video_path).resolve()

    # テキスト用音声データの出力先
    audio_text_path = "data/"+video_id+".mp3"
    audio_text_path = pathlib.Path(audio_text_path).resolve()
    audio_change_wav = "data/"+video_id+".wav"
    audio_change_wav = pathlib.Path(audio_change_wav).resolve()
    
    # テキスト保存場所
    text_date = "data/"+video_id+".txt"
    text_date = pathlib.Path(text_date).resolve()
    # csv保存場所
    csv_date = "data/"+video_id+".csv"
    csv_date = pathlib.Path(csv_date).resolve()
    
    # mp4→mp3へ変換
    def out_text(text_video_path, audio_text_path):
        out_audio = subprocess.run(
            [
                "ffmpeg",
                "-i",
                text_video_path,
                "-acodec",
                "libmp3lame",
                "-ab",
                "256k",
                audio_text_path,
            ]
            , shell= True
        )
        print(out_audio)
    
    # mp3からwavに変換
    def audio_transcript(audio_change_wav):
        transcript = subprocess.run(
            [
                "ffmpeg",
                "-i",
                audio_text_path,
                "-vn",
                "-ac",
                "1",
                "-ar",
                "44100",
                "-acodec",
                "pcm_s16le",
                "-f",
                "wav",
                audio_change_wav,
            ]
            ,shell=True
        )
        print(transcript)
    
    
    def audio_text_change(audio_change_wav, text_date, csv_date):
        # 文字起こし
        r = sr.Recognizer()
        with sr.AudioFile(audio_change_wav) as source:
            audio = r.record(source)
            text = r.recognize_google(audio, language="ja-JP").replace(" ", "\n")
            print(text)
        # textへの書き出し
        open_text = open(text_date, "x", encoding="utf_8")
        open_text.write(text)
        open_text.close()
        # txtをcsvに変換
        read_text = pd.read_csv(text_date)
        read_text.to_csv(csv_date, index=None)
    
    
    out_text(text_video_path, audio_text_path)
    
    # mp3が生成するまでにタイムラグがあるので、生成されるのを待つ処理
    while os.path.isfile(audio_text_path):
        audio_transcript(audio_change_wav)
        print("change end")
        if os.path.isfile(audio_change_wav):
            print("break!!")
            break
        
    audio_text_change(audio_change_wav, text_date, csv_date)

if __name__ == '__main__':
    video_id = "gnIOzY7esA0"
    Video_to_csv(video_id)