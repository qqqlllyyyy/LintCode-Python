# Hash Function
# In data structure Hash, hash function is used to convert a 
# string(or any other type) into an integer smaller than hash size 
# and bigger or equal to zero.
# A widely used hash function algorithm is using a magic number 33, 
# consider any string as a 33 based big integer like follow:
#
# hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE
#  = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE
#  = 3595978 % HASH_SIZE
# here HASH_SIZE is the capacity of the hash table (you can assume a hash
# table is like an array with index 0 ~ HASH_SIZE-1).
# Given a string as a key and the size of hash table, return the hash value
# of this key.f
#
class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        if len(key) == 0:
            return 0
        result = 0
        for i in range(len(key)):
            result = result * 33 + ord(key[i])
            result = result % HASH_SIZE
        return result
    
    """
        Don't forget two built-in function for Python: ord() and chr()
    """
    
