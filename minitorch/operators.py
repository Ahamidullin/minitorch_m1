"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# : Implement for Task 0.1.
def mul(a: float, b:float) -> float:
    return a * b

def id(identity:float) -> float:
    return identity

def add(a: float, b:float) -> float:
    return a+b

def neg(a: float)-> float:
    return -a

def lt(a: float, b: float) -> float:
    return 1.0 if b > a else 0.0


def eq(a: float, b: float) -> float:
    return 1.0 if a == b else 0.0 

def max(a: float, b: float) -> float:
    return a if a>b else b


def is_close(a: float, b: float) -> float:
    return 1.0 if math.fabs(a - b) < 1e-2 else 0.0

def sigmoid(a: float) -> float:
    return 1.0/ (1.0 + math.exp(-a)) if a >=0 else math.exp(a)/ (1.0 + math.exp(a))

def relu(a:float) -> float:
    return max(a, 0.0)

def log(a:float) -> float:
    return math.log(a)

def exp(a: float) -> float:
    return math.exp(a)

def log_back(x:float, d:float)-> float:
    return d/x

def inv(a : float)-> float:
    return 1/a

def inv_back(a: float, d: float) -> float:
    return -d/(a * a)

def relu_back(a: float, d: float)-> float:
    return d if a > 0 else 0.0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# Implement for Task 0.3.

def map(fn: Callable[[float], float], ls: Iterable[float]) -> Iterable[float]:
    return [fn(i) for i in ls]

def zipWith(
    fn: Callable[[float, float], float],
    ls1: Iterable[float],
    ls2: Iterable[float],
) -> Iterable[float]:
    return[fn(a,b) for a,b in zip(ls1, ls2)]

def reduce(
    fn: Callable[[float, float], float],
    ls: Iterable[float],
    start: float,
) -> float:
    st = start 
    for el in ls:
        st = fn(st, el)
    return st

        

# Временные заглушки, чтобы импорт в тестах не падал.
# Заменить реализациями при выполнении задачи 0.3.
def negList(ls: Iterable[float]) -> Iterable[float]:
    return map(neg, ls)
    # raise NotImplementedError("Task 0.3")


def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    return zipWith(add, ls1, ls2)
    # raise NotImplementedError("Task 0.3")


def prod(ls: Iterable[float]) -> float:
    return reduce(mul, ls, 1.0)
    # raise NotImplementedError("Task 0.3")

def sum(ls: Iterable[float]) -> float:
    return reduce(add, ls, 0.0)
