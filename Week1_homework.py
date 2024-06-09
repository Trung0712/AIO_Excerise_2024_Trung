import math
import random

# Exercise 1: Classification model by F1-score
def calc_f1_score(tp: int, fp: int, fn: int) -> float:
    # Check type input
    assert isinstance(tp, int), "tp must be int"
    assert isinstance(fp, int), "fp must be int"
    assert isinstance(fn, int), "fn must be int"

    # Check value input
    assert tp > 0 and fp > 0 and fn >0, "tp and fp and fn must be greater than zero"

    precision = tp/ (tp+ fp)
    recall = tp/ (tp+ fn)
    f1_score = 2* precision* recall/(precision+ recall)

    return precision, recall, f1_score

# Excercise 2: Activation function( Sigmoid, Relu, Elu)
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True
def calc_logistic(x):
    return 1/(1+ math.exp(-x))

def calc_relu(x):
    return x if x>0 else 0

def calc_elu(x, a= 0.01):
    return x if x>0 else a*(math.exp(x)-1)

def activation_function():
    x = input("Input a number:\n")
    assert is_number(x) == True, "x must be a number"

    activation_name = input("Input activation Function ( sigmoid | relu | elu ) :\n")
    assert activation_name.lower() in ["sigmoid", "relu", "elu"], f"{activation_name} is not supported"

    if activation_name == "sigmoid":
        return calc_logistic(x)
    elif activation_name == "relu":
        return calc_relu(x)
    else:
        return calc_elu(x)

# Excerise 3: Calculating regression loss
def regression_loss(loss_name, num_samples):
    assert is_number(num_samples), "Number of samples must be integer"
    assert loss_name.lower() in ["mae", "mse", "rmse"], f"{loss_name} is not supported"
    diff = 0
    input_values = []
    
    for _ in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        input_values.append((predict, target))
        diff += abs(predict - target)
    
    if loss_name.lower() == "mae":
        loss = diff/ num_samples
    elif loss_name.lower() == "mse":
        loss = diff**2/ num_samples
    else:
        loss = math.sqrt(diff**2/ num_samples)
    return loss_name, num_samples, input_values, loss

# Excerise 4: 
def approx_sin(x, n):
    x= math.radians(x)
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    return sum(((-1) ** i) * (x ** (2*i + 1)) / math.factorial(2 * i + 1) for i in range(n))

def approx_cosin(x, n):
    x= math.radians(x)
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    return sum(((-1) ** i) * (x ** (2*i)) / math.factorial(2 * i) for i in range(n))

def approx_sinh(x, n):
    x= math.radians(x)
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    return sum((x ** (2*i + 1)) / math.factorial(2*i + 1) for i in range(n))

def approx_coshing(x, n):
    x= math.radians(x)
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    sum((x ** (2*i)) / math.factorial(2*i) for i in range(n))


# Excercise 5: Mean difference
def mean_diff(y, y_hat, n, p):
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    return abs((y ** (1 / n) - y_hat ** (1 / n)) ** p)