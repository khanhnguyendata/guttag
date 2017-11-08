'''
Implement the class myDict with the methods below, which will represent a dictionary without
using a dictionary object.

The methods you implement below should have the same behavior as a dict object,
including raising appropriate exceptions. Your code does not have to be efficient.
Any code that uses a Python dictionary object will receive 0.

For example:

With a dict:  |    With a myDict:
-------------------------------------------------------------------------------
d = {}             md = myDict()        # initialize a new object using
                                          your choice of implementation

d[1] = 2           md.assign(1,2)       # use assign method to add a key,value pair

print(d[1])        print(md.getval(1))  # use getval method to get value stored for key 1

del(d[1])          md.delete(1)         # use delete method to remove
                                          key,value pair associated with key 1
class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        #FILL THIS IN

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        #FILL THIS IN

    def getval(self, k):
        """ k, immutable object  """
        #FILL THIS IN

    def delete(self, k):
        """ k, immutable object """
        #FILL THIS IN

Paste your entire class in the box below. Do not leave any print statements.
'''


class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self):
        """ initialization of your representation """
        self.buckets = []
        for i in range(20):
            self.buckets.append([])

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        hash_value = k % 20
        hash_bucket = self.buckets[hash_value]
        for index, value in enumerate(hash_bucket):
            if value[0] == k:
                hash_bucket[index] = (k, v)
                return
        hash_bucket.append((k, v))

    def getval(self, k):
        """ k, immutable object  """
        hash_value = k % 20
        hash_bucket = self.buckets[hash_value]
        for value in hash_bucket:
            if value[0] == k:
                return value[1]
        raise KeyError('Key not found in myDict object')


    def delete(self, k):
        """ k, immutable object """
        hash_value = k % 20
        hash_bucket = self.buckets[hash_value]
        for index, value in enumerate(hash_bucket):
            if value[0] == k:
                del hash_bucket[index]
                return
        raise KeyError('Key not found in myDict object')



d = myDict()
d.assign(1,2)
d.assign(1,3)
print(d.getval(1))
d.delete(1)
print(d.getval(1))