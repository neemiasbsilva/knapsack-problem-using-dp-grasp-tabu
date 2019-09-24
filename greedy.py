import numpy as np
import pandas as pd
import re


# critério de parada do GRASP: critério de parada.
# busca local: n itens n vizinhos and flips
# quando eu sei que os meus vizinhos são inviáveis eu simplesmente ignoro a minha solução.

def greedy_knapsack(Id, Value, Weight, capacity):
    # contains ratios of values to weight
    ratio = [v / w for v, w in zip(Value, Weight)]
    # print("Ratio: %s" % ratio)
    # print("Length of the ratio: %s"% len(ratio))
    # index is sorted according to value-to-weight ration
    Id.sort(key=lambda x: ratio[x], reverse=True)

    max_value = 0
    fractions = [0] * len(Value)
    for it in Id:
        if Weight[it] <= capacity:
            fractions[it] = 1
            max_value += Value[it]
            capacity -= Weight[it]
        else:
            fractions[it] = capacity / Weight[it]
            max_value += Value[it] * capacity / Weight[it]
            break

    return max_value, fractions



def main():
    iterator = 1
    output_max_value = []
    output_fractions = []
    while iterator <= 16:
        file = open("entradas/input"+str(iterator)+".in", "r")
        iterator += 1
        weight = []
        value = []
        id = []
        i = 0
        n = int()
        capacity = int()
        for line in file:
            i += 1
            line = line.rstrip()
            numbers = re.findall("[0-9]+", line)
            if i == 1:
                n = int(numbers[0])
            elif 1 < i <= n + 1:
                id.append(int(numbers[0]) - 1)
                value.append(int(numbers[1]))
                weight.append(int(numbers[2]))
            else:
                capacity = int(numbers[0])

        # print("Length of the input: %d" % n)
        # print("Id: %s" % Id)
        # print("Values: %s" % Value)
        # print("Weights: %s" % Weight)
        # print("Capacity: %d" % capacity)
        max_value, fractions = greedy_knapsack(id, value, weight, capacity)
        output_max_value.append(max_value)
        output_fractions.append(fractions)

    for i in range(16):
        print('The maximum value of items that can be carried: %d'% int(output_max_value[i]))
        # print('The fractions in which the items should be taken:', output_fractions[i])


if __name__ == "__main__":
    main()
