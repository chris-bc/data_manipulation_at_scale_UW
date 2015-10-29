import MapReduce
import sys

"""
Generate a list of (friend,person) pairs where person is not a friend of friend
but friend is a friend of person
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person
    # value: a friend of key
    if record[0] < record[1]:
        key1 = record[0]
        key2 = record[1]
    else:
        key1 = record[1]
        key2 = record[0]
    
    mr.emit_intermediate([key1, key2], record)

def reducer(key, list_of_values):
    # key: (person,person) tuple where one is the friend of the other but the reverse is not necessarily true
    # value: list of (person,friend) records involving both people in key
    person = ''
    friend = ''
    reciprocal = 0
    for val in list_of_values:
        if person == '':
            person = val[0]
            friend = val[1]
        else:
            # Is this a reciprocal relationship?
            if val[0] == friend:
                # hooray!
                reciprocal = 1
                break
            
    if reciprocal == 0:        
        mr.emit((friend, person))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
