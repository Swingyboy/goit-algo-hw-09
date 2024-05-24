import argparse
from algorithms import *


def main(amount: int, coins: list):
    print(find_coins_greedy(amount, coins))
    print(find_min_coins(amount, coins))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the minimum number of coins to make a change.")
    parser.add_argument("amount", type=int, help="The amount to make a change.")
    parser.add_argument("coins", type=int, nargs="+", help="The coins available.")
    args = parser.parse_args()
    main(args.amount, args.coins)
