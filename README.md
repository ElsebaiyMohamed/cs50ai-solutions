# Minesweeper

## Problem

Build an AI that plays Minesweeper by using revealed neighboring-mine counts to decide which cells are safe and which contain mines.

## Solution

The AI keeps track of known safe cells and mines, and represents clues as logical sentences about neighboring cells. It derives new facts from those sentences, chooses a known-safe move when possible, and otherwise selects a random move from the remaining cells.
