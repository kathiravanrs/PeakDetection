import xlwt

book = xlwt.Workbook()  # Initialize a new excel workbook
ws = book.add_sheet('First Sheet')      # Add an excel sheet to it

f = open('HOPDataSet1.txt', 'r+')       # Open the debug file
data = f.readlines()                    # Read each line of the file
ws.write(0, 0, "Hydraulic Oil Pressure")    # Write the column name on the excel sheet
row_count, prev, repeat_count = 1, 0, 0     # Initializing the variables

for i in range(len(data)):      # Iterate through the lines of the file

    # Each line has some string, the data starts at 25th index, so only those are taken and converted to float
    row = float(data[i][25:])
    if prev != row:             # To check if the values are repeating
        ws.write(row_count, 0, row)     # If it not repeating, the data is written into the excel sheet
        prev = row          # Previous value is updated
        row_count += 1      # The index of the row is updated
    else:
        repeat_count += 1   # If the data is repeating, do not write the data but increment the count

print(repeat_count)         # To display the number of repeated values
book.save('SampleValues - Newer' + '.xls')  # Save the excel sheet
f.close()        # The debug message file is closed
