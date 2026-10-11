# Degrees

## Problem

Find the shortest path between two actors through the movies they have appeared in together. Each shared movie connects two actors, and the path length is the number of movie links between them.

## Solution

The program loads actor and movie data from CSV files, then uses breadth-first search to find a shortest chain. It reports the movies and actors along that chain, or reports when no connection exists.
