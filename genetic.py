import random
import datetime

def _generate_parent(length,geneSet):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)

def _mutate(parent,geneSet):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    # print("{0}\t{1}".format(newGene,alternate))
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    # print('MUTATE!\n')
    return ''.join(childGenes)

def get_best(get_fitness, targetLen, optimalFitness, geneSet, display,target):
    random.seed()
    startTime = datetime.datetime.now()
    bestParent = _generate_parent(len(target))
    bestFitness = get_fitness(bestParent)
    display(bestParent)

    while True:
        child = _mutate(bestParent)
        # print("Mutacion: ",child)
        childFitness = get_fitness(child)
        if bestFitness >= childFitness:
            # print("Sigue probando")
            continue
        display(child)
        if childFitness >= len(bestParent):
            break
        bestFitness = childFitness
        bestParent = child