def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''

    return len(dna)
    


def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''

    if dna1 > dna2:
        return True
    elif dna2 > dna1:
        return False


def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    count = 0
    for char in dna:
        if char in nucleotide:
            count = count + 1

    return count

def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''

    if dna2 in dna1:
        return True
    else:
        return False


def is_valid_sequence(dna):
    ''' (str) -> bool

    The parameter is a potential DNA sequence. Return True if and only if the DNA
    sequence is valid (that is, it contains no characters other than
    'A', 'T', 'C' and 'G'). There are at least 2 ways to approach this. One way
    is to count the number of characters that are not nucleotides and then at the
    end check whether there were more than zero. Another way is to use a Boolean
    variable that represents whether you have found a non-nucleotide character;
    it would start off as True and would be set to False if you found something
    that wasn't an 'A', 'T', 'C' or 'G'. 
    You should construct examples that contain only 'A's, 'T's, 'C's and 'G's,
    and you should also create examples that contain other characters. Lowercase
    characters are not valid.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATPGGC')
    False
    >>> is_valid_sequence('ATcgGC')
    False

    '''

    valid = 'ACTG'
    count = 0

    for char in dna:
        if char in valid:
            count = count + 0
        else:
            count = count + 1

    if count == 0:
        return True
    else:
        return False


def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str

    The first two parameters are DNA sequences and the third parameter is an
    index. Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index. (You can assume that the
    index is valid.) 
    For example, If you call this function with arguments 'CCGG', 'AT', and 2,
    then it should return 'CCATGG'. 
    When coming up with more examples, think about where the second DNA sequence
    might be inserted: what are the extremes?

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'

    '''

    if index == 0:
        return dna2 + dna1
    else:
        return dna1[:index] + dna2 + dna1[index:]
    
           

    

    
    



