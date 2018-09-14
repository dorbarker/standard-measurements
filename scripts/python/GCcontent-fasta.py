#!/usr/bin/env python3

# Author: Dillon Barker <dillon.barker@canada.ca>

import argparse
from Bio import SeqIO


def gc_content(fasta_path: str) -> float:
    """Calculate the proportion of an assembly which is guanine or cytosine

    fasta_path: The path to a FASTA-formatted genome assembly
    """
    total_gc = 0
    total_length = 0

    with open(fasta_path, 'r') as f:

        for record in SeqIO.parse(f, 'fasta'):

            contig = str(record.seq).upper()
            gc_count = sum(base in 'GC' for base in contig)

            total_gc += gc_count
            total_length += len(contig)

    return total_gc / total_length


def arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('fasta', help='Path to a FASTA formatted assembly')

    return parser.parse_args()


def main():

    args = arguments()

    result = gc_content(args.fasta)

    print(result)


if __name__ == '__main__':
    main()
