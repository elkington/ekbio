DNAbases = set('TCAGtcag')
RNAbases = set('UCAGucag')
def validate_base_sequence(base_sequence, RNAflag = False):
	return set(base_sequence) <= (RNAbases if RNAflag else DNAbases)