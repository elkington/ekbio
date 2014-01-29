#Small RNA marketplace simulation

#simulate small RNA competition where allocation of resources to each small RNA class changes dynamically
#for each unit of time, two members are chosen based on interaction rules and compete with each other for common resources based on transaction rule

#simulation.py calls up interaction function then calls up transaction function T times and records the results for each time steps
#records summary statistics of population every 25 time steps

def simulate(population, transaction_fn, interaction_fn, T, percentiles, record_every):
    "Run simulation for T steps; collect percentiles every 'record_every' time steps."
    results = []
    for t in range(T):
        i, j = interaction_fn(population)
        population[i], population[j] = transaction_fn(population[i], population[j]) 
        if t % record_every == 0:
            results.append(record_percentiles(population, percentiles))
    return results

def report(distribution=gauss, transaction_fn=random_split, interaction_fn=anyone, N=N, mu=mu, T=5*N, 
           percentiles=(1, 10, 25, 33.3, 50, -33.3, -25, -10, -1), record_every=25):
    "Print and plot the results of the simulation running T steps." 
    # Run simulation
    population = sample(distribution, N, mu)
    results = simulate(population, transaction_fn, interaction_fn, T, percentiles, record_every)
    # Print summary
    print('Simulation: {} * {}(mu={}) for T={} steps with {} doing {}:\n'.format(
          N, name(distribution), mu, T, name(interaction_fn), name(transaction_fn)))
    fmt = '{:6}' + '{:10.2f} ' * len(percentiles)
    print(('{:6}' + '{:>10} ' * len(percentiles)).format('', *map(percentile_name, percentiles)))
    for (label, nums) in [('start', results[0]), ('mid', results[len(results)//2]), ('final', results[-1])]:
        print fmt.format(label, *nums)
    # Plot results
    for line in zip(*results):
        plt.plot(line)
    plt.show()

def record_percentiles(population, percentiles):
    "Pick out the percentiles from population."
    population = sorted(population, reverse=True)
    N = len(population)
    return [population[int(p*N/100.)] for p in percentiles]

def percentile_name(p):
    return ('median' if p == 50 else 
            '{} {}%'.format(('top' if p > 0 else 'bot'), abs(p)))
    
def name(obj):
    return getattr(obj, '__name__', str(obj))