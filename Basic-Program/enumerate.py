# Return an enumerate object. sequence must be a sequence, an iterator,
# or some other object which supports iteration. The next() method of the
# iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and
# the values obtained from iterating over sequence:
list = ['cream', 'jam', 'letuce', 'whip', 'cheese']
for i, j in enumerate (list, start=1):
    print('%s %s'%(i, j))
