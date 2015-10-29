import MapReduce
import sys

"""
Generate a sparse mutrix product
"""

mr = MapReduce.MapReduce()

A_ROWS = 5
A_COLS = 5
B_ROWS = 5
B_COLS = 5

def mapper(record):
    # record: [matrix, i, j, value]
    # key: col for matrix a, row for matrix b
    # value: record
    
    # Emit a elements to a reducer based on their row, b based on column
    for i in range(0,5):
        if record[0] == "a":
            key = (record[1],i)
            mr.emit_intermediate(key,record)
        else:
            key = (i,record[2])
            mr.emit_intermediate(key,record)

def reducer(key, list_of_values):
    # key: a tuple of output element (row, col)
    # value: list of records
    
    # Sum across matched inner dimensions of list mxn X nxp
    total = 0
    working = {}
    for val in list_of_values:
        if val[0] == "a":
            if working.get(val[2],0) != 0:
                total += working.get(val[2],0) * val[3]
            else:
                working[val[2]] = val[3]
        else:
            if working.get(val[1],0)!= 0:
                total += working.get(val[1],0) * val[3]
            else:
                working[val[1]] = val[3]
    
    mr.emit(key+(total,))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
