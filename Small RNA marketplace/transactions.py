#transaction rules determine allocation of total resources

def random_split(X, Y, Z):
    res = X + Y + Z
    m = random.uniform(0, res)
    return m, res - m
    
def winner_take_most(X, Y, Z, most=3/4.): 
    res = X + Y + Z
    m = random.choice((most * res, (1 - most) * res))
    return m, res - m

def winner_take_all(X, Y, Z): 
    return winner_take_most(X, Y, Z, 1.0)

def redistribute(X, Y, Z): 
    return winner_take_most(X, Y, Z, 0.55)

def split_min(X, Y, Z):
    res = min(X, Y, Z)
    m = random.uniform(0, res)
    return X - res/3. + m, Y + res/3. - m, Z - res/3. + m