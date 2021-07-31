import networkx as nx
from collections import defaultdict
import pandas as pd
from dwave.system import DWaveSampler, EmbeddingComposite

N = 5 # Number of items
weights = [2, 4, 1, 4, 3]
values = [3, 2, 1, 5, 2]
Wcapacity = 9
precision_bits = 5
dim = N * precision_bits

G = nx.Graph()
G.add_edges_from([(i, j) for i in range(dim) for j in range(i + 1, dim)])

# The matwix where we add the objective and the constraint
Q = defaultdict(int)

# Weight constraint
Wlagrange = 3
for d in range(dim): # N x precision
    i = d // precision_bits # The item number
    p = d % precision_bits + 1 # The p^th of the bits we are using to represent the i^th item
    wi = weights[i] # i^th item weights
    Q[(d, d)] += (-2 * Wcapacity * wi / pow(2, p) + wi * wi / pow(2, 2 * p)) * Wlagrange
    for d_dash in range(d + 1, dim):
        j = d_dash // precision_bits # The item number
        q = d_dash % precision_bits + 1 # The q^th of the bits we are using to represent the j^th item
        wj = weights[j] # j^th item weights
        Q[(d, d_dash)] += 2 * wi * wj * Wlagrange / pow(2, p + q)

for d in range(dim): # N x precision
    i = d // precision_bits # The item number
    p = d % precision_bits + 1 # The p^th of the bits we are using to represent the i^th item
    Q[(d, d)] += values[i] / pow(2, p)


sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(Q, num_reads=10, chain_strength=1)

# Print the entire sampleset, that is, the entire table
print(sampleset)

distributions = []

for sample, energy in sampleset.data(['sample', 'energy']):
    distributions.append(sample)

sol_no = 1
for di in distributions:
    val = 0
    wt = 0
    for d in range(dim): # N x precision
        i = d // precision_bits # The item number
        p = d % precision_bits + 1 # The p^th of the bits we are using to represent the i^th item
        wt += di[i] * weights[i] / pow(2, p)
        val += di[i] * values[i] / pow(2, p)
    print(str(sol_no) + "-")
    print("Weight:", wt)
    print("Value:", val)
    sol_no += 1