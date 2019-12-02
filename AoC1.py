# Advent of Code Challenge: Day 1
# Santa is lost in deep space, and needs help.
# Calculate fuel to get home by getting module mass from file.
# Then, divide mass by 3, round down, and subtract 2.
# Add them up to get total fuel units needed.

import time, sys

print("INCOMING TRANSMISSION")
print("Re: Database verification for file day1input.txt")
print("Connecting to Sleighbells AI 5000...")

time.sleep(5)

def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
        
slowprint("Ah-ha! There you are! \n")
slowprint("Santa is stuck in space. Again. \n")
slowprint("It's up to us to save him. Again. \n")
slowprint("We need to calculate the amount of fuel he needs to get home. \n")
slowprint("Let me check the database...give me about 10 seconds. \n")

time.sleep(10)

# The 'database' is called day1input.txt

slowprint("Uh, what's the name of the database, again? \n")
filename = input(": ")
num_lines = 0
with open(filename, 'r') as f:
    for line in f:
        num_lines += 1
slowprint("Oh, right. Man, I am getting old. \n")
slowprint(f"We have {num_lines} modules to account for. \n")







