import os

def Make_dir(channel_id):
    new_dir = "igaiga_data/" + channel_id
    folders = ["info","photo","movie","text","comment","audio"]
    ok = 1
    for folder in folders:
        try:
            os.makedirs(new_dir+'/'+folder)
        except:
            if ok:
                print("既にフォルダが存在します.")
            ok = 0
            pass
Make_dir("UCuIXSjuuhsN_ZmL8cFcyAzw")