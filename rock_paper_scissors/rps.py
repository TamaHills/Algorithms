#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  possibles = []
  options = ['rock', 'paper', 'scissors']

  if n == 1:
    return [[option] for option in options]
  if n == 0:
    return [[]]
 
  for prev in rock_paper_scissors(n - 1):
    for opt in options:
      possibles += [prev + [ opt ]]
  
  return possibles


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')