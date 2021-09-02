# # DataTable and DataColumn classes
# This exercise converts a csv string (a multi-line string 
# of comma-separated values) into a table, and then allows 
# us to extract individual columns to do some data analysis 
# (here, just taking the average for now).

# Note: you may assume:
# the table is nonempty (so it has at least one row and 
# at least one column) the table is rectangular (so each 
# row has the same number of columns) the first row contains 
# the column labels, which are strings the first column contains 
# the row labels, which are strings all other columns contain 
# data, which are ints, and legally formatted Also:
# ignore empty rows, and ignore leading and trailing
# whitespace on any row

# Here is an example of such data:
# csvData = '''
#     Name,Hw1,Hw2,Quiz1,Quiz2
#     Fred,94,88,82,92
#     Wilma,98,80,80,100
#     '''
# With this in mind, write the class DataTable and also 
# the class DataColumn so the following test function passes 
# (without hardcoding any test cases):

class DataColumn: 
    pass

class DataTable:
    pass

def almostEqual(a, b):
    return True

def testDataTableAndDataColumnClasses():
    print('Testing DataTable and DataColumn classes...', end='')
    csvData = '''
    Name,Hw1,Hw2,Quiz1,Quiz2
    Fred,94,88,82,92
    Wilma,98,80,80,100
    '''
    dataTable = DataTable(csvData)
    rows, cols = dataTable.getDims()
    assert((rows == 3) and (cols == 5))

    column3 = dataTable.getColumn(3)
    assert(isinstance(column3, DataColumn))
    assert(column3.label == 'Quiz1')
    assert(column3.data == [82, 80])
    assert(almostEqual(column3.average(), 81))

    column4 = dataTable.getColumn(4)
    assert(isinstance(column4, DataColumn))
    assert(column4.label == 'Quiz2')
    assert(column4.data == [92, 100])
    assert(almostEqual(column4.average(), 96))
    print('All test cases passed....!')
