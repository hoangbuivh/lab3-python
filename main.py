# Author: Hoang Bui hhb5051@psu.edu 
# Collaborator: Josh Hornickle jph6089@psu.edu
# Collaborator: Harshvardhan Singh  hms5805@psu.edu
# Collaborator: Mitch Scavo mrs631@psu.edu 
# Section: 1
# Breakout: 3

def sum_n(n):
  if n ==0: 
    return 0 
  else: 
    return n + sum_n(n-1)

def print_n(s, n): 
  if n==0: 
    pass
  else: 
    print(s)
    print_n(s,n-1)

def run(): 
  entrance = int(input("Enter an int: "))
  print(f"sum is {sum_n(entrance)}.")
  strng = input("Enter a string: ")
  print_n(strng,entrance)

if __name__ == "__main__": 
  run()