# Quantum-Knapsack
Using Quantum Computing Resources to solve different variations of the Knapsack Problem.

## What it does
Attempts the solve the Knapsack problem, including the following variants using Quantum Annealing (provided by DWave Systems)
1) Only weights and values, either select an item or not (DP works)
2) Only weights and values, select fractional items (Greedy works)
3) Weights, Volume and values, select an item or not (3D DP works)
4) Weights, Volume and values, select fractional items (Probably NP complete)
Annealing is good in cases (1) and (3), but not great in (2). (4) is yet to be implemented.

## How to Run
Create an account here: https://cloud.dwavesys.com/leap/. Prefix the URL of this Github repository in the address bar of your browser with: https://ide.dwavesys.io/#. Simply run the program to get the results.
