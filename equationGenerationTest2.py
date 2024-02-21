import unittest
import datetime
import genetic13
import random

def evaluate(genes, prioritizedOperations):
    results = genes[0]
    
    for i in range(1, len(genes), 2):
        operation = genes[i]
        nextValue = genes[i + 1]
        if operation == '+':
            result += nextValue
        elif operation == '-':
            result -= nextValue
    return result

class EquationGenerationTests(unittest.TestCase):
    def test(self):
        numbers = [1,2,3,4,5,6,7]
        operations = ['+','-']

def create(numbers, operations, minNumbers, maxNumbers):
    genes = [random.choice(numbers)]
    count = random.randint(minNumbers, 1 + maxNumbers)
    while count > 1:
        count -= 1
        genes.append(random.choice(operations))
        genes.append(random.choice(numbers))
    return genes

def mutate(genes, numbers, operations, minNumbers, maxNumbers):
    numberCount = (1 +len(genes))/2

    appending = numberCount < maxNumbers and random.randint(0,100) == 0

    if appending:
        genes.append(random.choice(operations))
        genes.append(random.choice(numbers))
        return
    
    removing = numberCount > minNumbers and random.randint(0, 20) == 0

    if removing:
        index = random.randrange(0, len(genes) - 1)
        del genes[index]
        del genes[index]
        return
    

    index = random.randrange(0, len(genes))
    genes[index] = random.choice(operations) if (index & 1) == 1 else random.choice(numbers)