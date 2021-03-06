import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
import re

def main():
    iterator = 1

    fileGreedy = open("Output/greedy.out", "r")
    fileGrasp = open("Output/grasp.out", "r")
    fileDynamic = open("Output/dynamic.out", "r")
    fileTabu = open("Output/tabu.out", "r")
    resultDynammic = []
    resultGreedy = []
    resultGrasp = []
    resultTabu = []
    for line in fileGreedy:
        line = line.rstrip()
        i, numbers = re.findall("[0-9]+", line)
        resultGreedy.append(int(numbers))

    for line in fileGrasp:
        line = line.rstrip()
        i, numbers = re.findall("[0-9]+", line)
        resultGrasp.append(int(numbers))

    for line in fileDynamic:
        line = line.rstrip()
        i, numbers = re.findall("[0-9]+", line)
        resultDynammic.append(int(numbers))

    for line in fileTabu:
        line = line.rstrip()
        i, numbers = re.findall("[0-9]+", line)
        resultTabu.append(int(numbers))

    fileDynamic.close()
    fileGrasp.close()
    fileGreedy.close()
    fileTabu.close()
    df = pd.DataFrame({"Greedy": resultGreedy, "Grasp": resultGrasp, "Dynamic": resultDynammic, "Tabu": resultTabu})
    # df.plot.hist(bins=20, figsize=(10, 5), cmap="viridis")
    # sns.heatmap(df, yticklabels=False, cbar=False)
    # sns.countplot(x="Grasp", data=df)
    ax1 = df.plot.scatter(x='Tabu', y='Dynamic', c='Dynamic', colormap='viridis', figsize=(10, 5))
    plt.savefig('Graphics/Tabu-dynamic.png')
    #ax1 = df.plot.scatter(x='Greedy', y='Dynamic', c='Dynamic', colormap='viridis', figsize=(10, 5))
    plt.savefig('Graphics/greedy-dynamic.png')
    df.plot.line()
    plt.savefig('Graphics/line-greedy-grasp-dynamic-tabu.png')
    df.to_csv('Output/knapsack-result-Tabu.csv')
    plt.show()

if __name__ == "__main__":
    main()