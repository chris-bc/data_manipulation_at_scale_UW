import MapReduce
import sys

"""
Generate a count of the number of friends of each person
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person
    # value: a friend of key
    key = record[0]
    value = 1
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: person
    # value: list of friend counts of key
    total = 0
    for c in list_of_values:
        total += c
    mr.emit((key, total))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
