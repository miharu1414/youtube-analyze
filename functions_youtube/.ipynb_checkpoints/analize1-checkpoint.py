# 再生回数の移動平均

import openpyxl
import matplotlib.pyplot as plt
import numpy as np
import os

def analize(data_path, channel_id, ido = 1):
    wb = openpyxl.load_workbook(data_path)
    ws = wb.worksheets[0]

    data = []

    for row in ws.rows:
        addrs = []
        for cell in row:
            addrs.append(cell.value)
        data.append(addrs)

    num = []
    number = 0
    long_data = len(data)-ido
    heikin = 0
    for j in range(ido):
        heikin += int(data[ido-j][8])
    heikin /= ido
    num.append(heikin)

    for i in range(ido + 1,len(data)):
        heikin -= int(data[i-ido][8])
        heikin += int(data[i][8])
        num.append(heikin)
        number += 1

    num = np.array(num)
    x_data = np.array([i+1 for i in range(long_data)])
    plt.plot(x_data, num)
    plt.ylabel('view')
    plt.xlabel('past->now')

    dirname = 'main.itogo.jp' + channel_id + '/suii/'
    os.makedirs(dirname, exist_ok=True)
    filename = dirname + channel_id + 'type1.jpg'
    plt.savefig(filename)

if __name__ == '__main__':
    data = 'data_UCZf__ehlCEBPop-_sldpBUQ.xlsx'
    analize(data, 30)
