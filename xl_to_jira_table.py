import codecs, sys, os
from mmap import mmap,ACCESS_READ
from xlrd import open_workbook

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if len(sys.argv) == 1:
	print '\n'
	print 'Must include XLSX file to process as first argument (Python xl_to_jira_table.py C:\PathToExcelFile\ExcelFile.xlsx)'
	print '\n'
	exit()
	
excel_file = sys.argv[1]
	
s = open_workbook(excel_file).sheet_by_index(0)
f = codecs.open('output.txt', encoding='utf-8', mode='w+')

# loop through rows
for i in range(s.nrows):
	if i == 0:
		delimiter = '\t || \t'
	else:
		delimiter = '\t | \t'
# loop through columns
	for x in range(s.ncols):
		result = (s.cell_value(i,x))
		if is_number(result) == True:
			result = str(result)
#                if isinstance(result, unicode):
#                        result = result.encode('utf-8')
		if x == s.ncols - 1:
			f.write(delimiter)
			f.write(result)
			f.write(delimiter)
			f.write('\n')
		else:
			f.write(delimiter)
			f.write(result)
f.close()

os.system('start excel.exe output.txt')
