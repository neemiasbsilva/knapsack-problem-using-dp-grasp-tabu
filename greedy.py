import numpy as np
import pandas as pd
import re



def greedy_knapsack(Id, Value, Weight, capacity):
    # contains ratios of values to weight
    solucao = []
    item = {}
    capacidade_restante = capacity
    for i in range(len(Id)):
        item[i] = np.divide(Value[i], Weight[i]), Value[i], Weight[i]
    item = sorted(item.values(), reverse=True)
    max_value = 0
    for i in range(len(Value)):
        if item[i][2] <= capacidade_restante:
            capacidade_restante -= item[i][2]
            max_value += item[i][1]

    return max_value



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
        max_value = greedy_knapsack(id, value, weight, capacity)
        s = "Instancia " + str(iterator - 1) + " : "+str(max_value)+"\n"
        file = open("Output/greedy.out", "a+")
        file.write(s)
        output_max_value.append(max_value)

    #for i in range(16):
        #print('The maximum value of items that can be carried: %d'% int(output_max_value[i]))
        # print('The fractions in which the items should be taken:', output_fractions[i])


if __name__ == "__main__":
    main()
