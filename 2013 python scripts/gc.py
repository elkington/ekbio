#!/usr/local/bin/python

def validate_base_sequence(base_sequence, RNAflag = False):
	seq = base_sequence.upper()
	return len(seq) == (seq.count('U' if RNAflag else 'T') +
						seq.count('C') +
						seq.count('A') +
						seq.count('G'))

def gc_content(base_seq):
	assert validate_base_sequence(base_seq), \
			'argument has invalid characters'
	seq = base_seq.upper()
	return (base_seq.count('G') +
			base_seq.count('C')) / len(base_seq)

def recognition_site(base_seq, recognition_seq):
	return base_seq.find(recognition_seq)
	
def test():
	assert validate_base_sequence('ACTG')
	assert validate_base_sequence('')
	assert not validate_base_sequence('ACUG')
	print('All tests passed.')

"""	assert validate_base_sequence('ACUG', False)
	assert not validate_base_sequence('ACUG', True)
	assert validate_base_sequence('ACTG', True)
	
	assert .5 == gc_content('ACTG')
	assert 1.0 == gc_content('CCGG')
	assert .25 == gc_content('ACTT')"""

test()