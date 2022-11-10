import openpyxl

wb = openpyxl.load_workbook('igaiga_data/UC4B6r1TQyN5LhtDk-aaA9Qg/info/data_UC4B6r1TQyN5LhtDk-aaA9Qg.xlsx')

ws = wb.worksheets[0]

data = []

for row in ws.rows:
    addrs = []
    for cell in row:
        addrs.append(cell.value)
    data.append(addrs)


for i in range(len(data)):
    print(data[i][8])

