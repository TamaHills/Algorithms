#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = float('-inf')
  min_price = float('inf')
  for price in prices:
    profit = 0
    profit = price - min_price
    
    if profit == 0:
      pass
    elif profit > max_profit:
      max_profit = profit
    
    if price < min_price:
      min_price = price
    
  
  return max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))