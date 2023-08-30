# this is a Heads or Tails game

import random

random_side = random.randint(0, 1)

if random_side == 1:
    print("\nHeads\n")
else:
    print("\nTails\n")
