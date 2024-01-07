geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Vamonos ATOMOS"

import random
import datetime
import genetic


def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)


def display(guess,startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

def test_Hello_World():
    target = "Hello World!"
    guess_password(target)

def guess_password(target):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()

    def fnGetFitness(genes):
        return get_fitness(genes, target)

    def fnDisplay(genes,startTime):
        display(genes, target, startTime)
    
optimalFitness = len(target)
genetic.get_best(fnGetFitness, len(target), optimalFitness, geneSet, fnDisplay)
