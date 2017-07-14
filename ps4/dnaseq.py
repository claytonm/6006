#!/usr/bin/env python2.7

from dnaseqlib import *
import unittest


### Utility classes ###

# Maps integer keys to a set of arbitrary values.

class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        self.md = {}
        for pair in pairs:
            self.put(pair[0], pair[1])

    # Associates the value v with the key k.
    def put(self, k, v):
        if self.md.has_key(k):
            self.md[k].append(v)
        else:
            self.md[k] = [v]

    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):
        if self.md.has_key(k):
            return self.md[k]
        else:
            return []


# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  

def subsequenceHashes(seq, k):

    def listToString(s):
        return ''.join([s[i] for i in range(len(s))])

    # get intial k-length string to hash
    s = [seq.next() for i in range(k)]
    # initial rolling hash
    rh = RollingHash(listToString(s))
    i = 0
    for nextitm in seq:
        yield (rh.current_hash(), (i, listToString(s)))
        # get first item in s
        previtm = s[i % k]
        # replace first item with next item
        s[i % k] = nextitm
        rh.slide(previtm, nextitm)
        i += 1



# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):
    sh = subsequenceHashes(seq, k)
    i = 0
    for nextitm in sh:
        if i % m == 0:
            yield nextitm
        i += 1


# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k, m):
    md = Multidict(intervalSubsequenceHashes(a, k, m))
    sh2 = subsequenceHashes(b, k)
    for nucleotide in sh2:
        for value in md.get(nucleotide[0]):
            if value[1] != nucleotide[1][1]:
                continue
            else:
                yield (value[0], nucleotide[1][0])
    return


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0])
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[2], (500,500), sys.argv[0], sys.argv[1], 8, 100)

