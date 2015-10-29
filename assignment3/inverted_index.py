import MapReduce
import sys

"""
Generate an inverted index
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key.encode('utf-8'))

def reducer(key, list_of_values):
    # key: word
    # value: list of document IDs containing word
    mr.emit((key, list(set(list_of_values))))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
