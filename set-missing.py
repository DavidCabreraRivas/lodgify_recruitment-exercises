import random
from typing import List

def create_set(max_num: int) -> List:
    """ Creates a set of N numbers ranging 1..max_num """
    missing = random.randint(1, max_num)
    num_set = [x for x in range(1, max_num + 1) if x != missing]
    random.shuffle(num_set)

    return num_set

def find_missing(num_set: List) -> int:
    """
    Returns missing number on a set
    Please add your code
    """
    return "Some number between 1 and {}".format(len(num_set) + 1)

if __name__ == "__main__":
    max_num = 100

    print(find_missing(create_set(max_num)))
