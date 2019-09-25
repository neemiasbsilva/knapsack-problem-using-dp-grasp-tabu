import numpy as np
import re
import time

dp = np.ones((30000, 100000), dtype=int)


def knapsack(size, value, weight, capacity):
    if size == 0 or capacity == 0:
        return 0
    if dp[size - 1][capacity] == 0:
        return dp[size - 1][capacity]
    if weight[size - 1] > capacity:
        dp[size - 1][capacity] = knapsack(size - 1, value, weight, capacity)
        return dp[size - 1][capacity]
    a = value[size - 1] + knapsack(size - 1, value, weight, capacity - weight[size - 1])
    b = knapsack(size - 1, value, weight, capacity)
    dp[size - 1][capacity] = max(a, b)
    return dp[size - 1][capacity]


def main():
    iterator = 1
    output_max_value = []
    output_fractions = []
    # start = time.time()
    while iterator <= 16:
        file = open("entradas/input" + str(iterator) + ".in", "r")
        # file = open("entradas/input6.in", "r")
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

        dp = np.zeros((n, capacity), dtype=int)
        max_value = knapsack(n, value, weight, capacity)
        s = "Instancia " + str(iterator - 1) + " : " + str(max_value) + "\n"
        # s = "Instancia 6 : "+str(max_value)+"\n"
        # print(s)
        file = open("Output/dynamic.out", "a+")
        file.write(s)
        output_max_value.append(max_value)

    # file = open("Output/dynamic.out", "a+")
    # file.write(str("Execution time: "+time.time() - start))


if __name__ == "__main__":
    main()
