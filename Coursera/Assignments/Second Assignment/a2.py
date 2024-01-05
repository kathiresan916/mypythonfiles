def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence(dna):
    """
    (str) -> bool
    Return True  if dna is a valid DNA sequence, otherwise False.
    """
    valid_nucleotides = set('ATCG')
    return all(char in valid_nucleotides for char in dna.upper())


def insert_sequence(dna1, dna2, index):
    """
    (str, str, int) -> str
    Return the DNA sequence obtained by inserting dna2 into dna1 at the given index.
    """
    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nucleotide):
    """
    (str) -> str
    Return the complement of a nucleotide.
    """
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return complements.get(nucleotide.upper(), nucleotide)


def get_complementary_sequence(dna):
    """
    (str) -> str
    Return the DNA sequence that is complementary to the given DNA sequence.
    """
    return ''.join(get_complement(char) for char in dna)


dna_sequence = 'ATCGAT'
print(get_length(dna_sequence))
print(is_longer('ATCG', 'AT'))
print(count_nucleotides('ATCGGC', 'G'))
print(contains_sequence('ATCGGC', 'GG'))
print(is_valid_sequence('ATCG'))
print(insert_sequence('CCGG', 'AT', 2))
print(get_complement('A'))
print(get_complementary_sequence('ATCG'))
