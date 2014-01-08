#!/usr/local/bin/python

seq = 'AAAT'
def validate_base_sequence(base_sequence):
	seq = base_sequence.upper()
	return len(seq) == (seq.count('T') + seq.count('C') + seq.count('A') + seq.count('G'))
validate_base_sequence('tattattat')