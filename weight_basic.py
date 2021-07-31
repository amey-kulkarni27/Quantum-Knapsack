import networkx as nx
from collections import defaultdict
import pandas as pd
from dwave.system import DWaveSampler, EmbeddingComposite

N = 5 # Number of items
weights = [2, 4, 1, 4, 3]
values = [3, 2, 1, 5, 2]
Wcapacity = 9

# Creating the graph
G = nx.Graph()
G.add_edges_from([(i, j) for i in range(N) for j in range(i + 1, N)])

# The matrix where we add the objective and the constraint
Q = defaultdict(int)

# Constraint specifying weight filled in bag should be as close to its specified capacity
Wlagrange = 3
for i in range(N):
    Q[(i, i)] += (weights[i] * (-2 * Wcapacity + weights[i])) * Wlagrange
    for j in range(i + 1, N):
        Q[(i, j)] += 2 * Wlagrange * weights[i] * weights[j]

# Objective function: Maximise values
# Here we have to present the problem as an energy minimisation problem, hence the minus sign
for i in range(N):
    Q[(i, i)] -= values[i]


sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(Q, num_reads=10, chain_strength=1)

# Print the entire sampleset, that is, the entire table
print(sampleset)

distributions = []

for sample, energy in sampleset.data(['sample', 'energy']):
    distributions.append(sample)

sol_no = 1
for d in distributions:
    val = 0
    wt = 0
    for i in range(N):
        wt += d[i] * weights[i]
        val += d[i] * values[i]
    print(str(sol_no) + "-")
    print("Weight:", wt)
    print("Value:", val)
    sol_no += 1