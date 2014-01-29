#sample 2 members of population uniformly and independently

def anyone(rna): 
	return random.sample(range(len(rna)), 2)

#nearby function chooses a member randomly then chooses another k units away in order to model local competition
def nearby(rna, k=3): 
    i = random.randrange(len(rna))
    j = i + random.choice((1, -1)) * random.randint(1, k)
    return i, (j % len(rna))
               
def nearby1(rna): 
	return nearby(rna, 1)
	
def nearby2(rna):
	return nearby(rna, 2)
	
def nearby3(rna):
	return nearby(rna, 3)
	