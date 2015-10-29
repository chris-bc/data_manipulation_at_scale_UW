import MapReduce
import sys

"""
Generate a relational join
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: order ID
    # value: recard
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: order ID
    # value: list of records (orders and line_items) for that order
    
    # First find the order
    order = []
    for record in list_of_values:
        if record[0] == "order":
            order = record
            break
    
    # Now emit results
    for record in list_of_values:
        if record[0] == "line_item":
            mr.emit(order + record)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
