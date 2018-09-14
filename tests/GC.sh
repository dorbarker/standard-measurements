#!/usr/bin/env bash

set -e
basedir=$(dirname $0)
thisscript=$(basename $0)
tmpdir=$(mktemp --directory $thisscript.XXXXXX)

GC=0.5068

gunzip -c $basedir/data/2011C-3609.fasta.gz > $tmpdir/in.fasta

pythonFastaGC=$(python3 $basedir/../scripts/python/GCcontent-fasta.py $tmpdir/in.fasta)
pythonFastaGC=$(printf "%0.4f" $pythonFastaGC)

if (( $(echo "$pythonFastaGC != $GC" | bc -l) )); then
    echo "ERROR: GCcontent-fasta.py did not produce the expected result"
    exit 1
fi

echo "GC Content tests passed!"