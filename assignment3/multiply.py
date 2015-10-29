import MapReduce
import sys

"""
Generate a sparse mutrix product
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # record: [matrix, i, j, value]
    # key: col for matrix a, row for matrix b
    # value: record
    if record[0] == "a":
        key = record[2]
    else:
        key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: a.col_num or b.row_num
    # value: list of elements in a column[key] or b row[key]
    a = []
    b = []
    for item in list_of_values:
        if item[0] == "a":
            a.append(item)
        else:
            b.append(item)
            
    for a_element in a:
        for b_element in b:
            print "argh:"+str(a_element)+":"+str(b_element)
#    mr.emit((key, total))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
