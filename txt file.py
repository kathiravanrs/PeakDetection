import xlwt

book = xlwt.Workbook()
ws = book.add_sheet('First Sheet')

f = open('HOPDataSet1.txt', 'r+')
data = f.readlines()
ws.write(0, 0, "Hydraulic Oil Pressure")
row_count, prev, repeat_count = 1, 0, 0

for i in range(len(data)):
    row = float(data[i][25:])
    if prev != row:
        ws.write(row_count, 0, row)
        prev = row
        row_count += 1
    else:
        repeat_count += 1

print(repeat_count)
book.save('SampleValues - Newer' + '.xls')
f.close()
