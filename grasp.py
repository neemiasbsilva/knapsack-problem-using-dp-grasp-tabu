import random
import re
import numpy as np


def cost(solution, weight, value, id, capacity):
    max_value = 0
    for j in range(len(solution)):
        if solution[j] == 1:
            max_value += value[j]

    return max_value


def local_search(solution, weight, value, id, capacity):
    temp = solution[:]
    # print(len(value))
    for i in range(len(temp)):
        max_temp_weight = 0
        max_value_temp = 0
        max_value = 0
        if temp[i] == 0:
            temp[i] = 1
            for j in range(len(temp)):
                if temp[j] == 1:
                    max_value_temp += value[id[j]]
                    max_temp_weight += weight[id[j]]
            temp[i] = 0
        elif temp[i] == 1:
            temp[i] = 0
            max_value_temp = 0
            max_value = 0
            for j in range(len(temp)):
                if temp[j] == 1:
                    max_value_temp += value[id[j]]
                    max_temp_weight += weight[id[j]]

            temp[i] = 1
        for j in range(len(solution)):
            if solution[j] == 1:
                max_value += value[id[j]]
        if capacity - max_temp_weight >= 0 and max_value_temp > max_value:
            solution = temp[:]

    return solution


def Greedy_Randomized_Construction(id, value, weight, capacity):
    solucao = []
    item = {}
    for i in range(len(id)):
        item[i] = np.divide(value[i], weight[i]), value[i], weight[i]
    item = sorted(item.values(), reverse=True)

    item_temp = item[:]
    capacidade_restante = capacity

    peso = 0

    while len(item) > 0:
        lcr = []
        for i in range(2):
            if i < len(item):
                lcr.append(item[i])

        s = random.choice(lcr)
        if s[2] <= capacidade_restante:
            solucao.append(s[1])
            capacidade_restante -= s[2]
            peso += s[2]

        item.pop(item.index(s))

    sol = [0 for i in range(len(value))]

    for item in value:
        if item in solucao:
            sol[value.index(item)] = 1

    return sol, peso


def grasp(max_iterations, id, value, weight, capacity):
    best = 0
    for k in range(max_iterations):
        id_temp = []
        for i in range(len(id)):
            id_temp.append(id[i])
        solution, peso = Greedy_Randomized_Construction(id_temp, value, weight, capacity)

        solution = local_search(solution, weight, value, id, capacity)
        solution = cost(solution, weight, value, id, capacity)
        if solution > best:
            best = solution
    return best


def main():
    iterator = 1
    while iterator <= 16:
        file = open("entradas/input" + str(iterator) + ".in", "r")

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

        max_iterations = 20
        s = "Instancia " + str(iterator - 1) + " : " + str(grasp(max_iterations, id, value, weight, capacity)) + "\n"
        file = open("Output/grasp.out", "a+")
        file.write(s)


if __name__ == "__main__":
    main()
