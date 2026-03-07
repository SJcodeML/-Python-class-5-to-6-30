#  If you want 10 unique numbers (no repeats) between 1 and 100
# Approach A: shuffle a range and take the first 10

import random
def main():
    values = random.sample(range(1, 101), 10)
    
    print(values)



if __name__ == "__main__":
    main()


