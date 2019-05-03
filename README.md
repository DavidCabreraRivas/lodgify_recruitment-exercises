## Recruitment exercises.

- Clone this repository and create a branch to complete your answers. When done create a Pull Request against master branch.
- For python exercises use provided `.py` files to complete your answers.
- Feel free to change original code if needed.
- Write answers to SQL questions on the provided file.

### Python Exercises

#### 1.- Find the missing element.

Given a set of `max_num` numbers ranging 1 to `max_num`, find the missing number.
Please fill code of find_missing function

```python
import random

def create_set(max_num):
    """ Creates a set of N numbers ranging 1..max_num """
    missing = random.randint(1, max_num)
    num_set = [x for x in range(1, max_num + 1) if x != missing]
    random.shuffle(num_set)

    return num_set

def find_missing(num_set):
    """
    Returns missing number on a set
    Please add your code
    """
    return "Some number between 1 and {}".format(len(num_set) + 1)

if __name__ == "__main__":
    max_num = 100
    num_set = create_set(max_num)
    print(find_missing(num_set))

```

#### 2.- Given the following naive implementations of Fibonacci sequence algorithm:

```python
# iterative
def fib_iter():
    """ Generates an infinite sequence of Fibonacci """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# recursive
def fib_rec(n):
    """ Returns Fibonacci number at n position """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)
```

Iterative example uses a generator and returns one item at a time, recursive example return the nth Fibonacci number in sequence.
We want you to write 3 functions:

- A function `sequence_iter(n)` that returns complete sequence until `n`th number using `fib_iter`
- A function `sequence_rec(n)` that returns complete sequence until `n`th number using `fib_rec`
- A function `sum_fibs(n, m, f)` that return the sum of Fibonacci numbers `n` and `m` using function `f`, being `f` one of two provided funcions.
  Consider 1st number is first number generated, 0, second number is 1, third number is 1 and so on. So the nth term has a base index of 1.

If needed you can edit original functions to achieve desired result.

Examples:

```
print(sequence_iter(5)) # or print(sequence_rec(5))
[0, 1, 1, 2, 3]
print(sum_fibs(6, 11, fib_iter))
60
```
