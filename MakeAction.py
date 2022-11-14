def MakeAction(channel_info):
    PostbackAction(
        lavel = channel_info[0],
        display_text = channel_info[0],
        data = channel_info[1]
    )