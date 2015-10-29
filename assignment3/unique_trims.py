import MapReduce
import sys

"""
Generate a set of unique trimmed nucleotides
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # input key: ID
    # input value: nucleotide
    mr.emit_intermediate(record[1][:-10], 1)

def reducer(key, list_of_values):
    # key: trimmed nucleotide
    # value: who cares (1)
    mr.emit(key)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
