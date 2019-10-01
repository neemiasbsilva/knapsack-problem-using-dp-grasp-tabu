import numpy as np
import re


def greedy_knapsack(Id, Value, Weight, capacity):
    solution = []
    item = {}
    capacidade_restante = capacity
    current_weight = 0
    for i in range(len(Id)):
        item[i] = np.divide(Value[i], Weight[i]), Value[i], Weight[i], i
    item = sorted(item.values(), reverse=True)
    max_value = 0
    for i in range(len(Value)):
        if item[i][2] <= capacidade_restante:
            capacidade_restante -= item[i][2]
            current_weight += item[i][2]
            solution.append(item[i][3])
            max_value += item[i][1]

    begin_solution = [0 for i in range(len(Value))]
    for i in solution:
        begin_solution[i] = 1

    return begin_solution, current_weight


def f(begin_solution, item, capacity):
    max_value = 0
    for i in range(len(item)):
        if begin_solution[i] == 1 and capacity >= 0:
            max_value += item[i][0]
            capacity -= item[i][1]

    if capacity < 0:
        max_value = -1
    return max_value


def tabu_search(begin_solution, current_weight, value, weight, capacity):
    item = {}
    for i in range(len(value)):
        item[i] = value[i], weight[i]
    T = []
    It = 0
    BestIt = 0
    best_solution = begin_solution[:]  # Best solution until then.
    capacity_rest = capacity
    temp = best_solution[:]
    solution_partial = []
    while It - BestIt <= 100:
        It += 1
        save_solution = temp[:]
        solutuion_tabu = list()
        valor = -1
        valorTabu = -1
        mov = -1
        movTabu = -1
        for i in range(len(item)):
            if temp[i] == 1:
                temp[i] = 0
            else:
                temp[i] = 1


            solution_partial = temp[:]
            if f(solution_partial, item, capacity_rest) > valor and not (i in T):
                save_solution = solution_partial[:]
                valor = f(save_solution, item, capacity)
                mov = i
                if f(solution_partial, item, capacity) > f(best_solution, item, capacity_rest):
                    best_solution = solution_partial[:]
                    BestIt = It
            elif f(solution_partial, item, capacity_rest) > f(best_solution, item, capacity_rest):
                save_solution = solution_partial[:]
                valor = f(save_solution, item, capacity_rest)
                best_solution = solution_partial[:]
                BestIt = It
                mov = i
            elif i in T and f(solution_partial, item, capacity_rest) > valorTabu:
                solutuion_tabu = solution_partial[:]
                valorTabu = f(solutuion_tabu, item, capacity)
                movTabu = i

            if temp[i] == 1:
                temp[i] = 0
            else:
                temp[i] = 1

        if mov == -1 and movTabu == -1:
            break
        if mov != -1:
            if not(mov in T):
                if len(T) == 3:
                    del T[0]
                T.append(mov)
            temp = save_solution[:]
        else:
            temp = solutuion_tabu[:]


    print(f(best_solution, item, capacity))



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

        begin_solution, current_weight = greedy_knapsack(id, value, weight, capacity)
        tabu_search(begin_solution, current_weight, value, weight, capacity)
        s = "Instancia " + str(iterator - 1) + " : "+str(max_value)+"\n"
        file = open("Output/tabu.out", "a+")
        file.write(s)

if __name__ == "__main__":
    main()
