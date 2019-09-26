import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = pd.read_json("Output/execution-time.json").T
    df.drop(['Crescente', 'Decrescente'], inplace=True, axis=1)
    # df.to_latex("Output/table-latex.out")
    # df = df.T
    df = df.rename(columns={"Eficiente": "Greedy",
                         "GRASP": "GRASP",
                         "Exato": "Dynamic Programming"})
    # df = df.set_index('Instance')
    # plt.figure()
    df.rename_axis("Intances", inplace=True, axis="columns")
    df.plot.bar(stacked=True, figsize=(7, 5))
    plt.ylabel("Execution Time (min)")
    plt.savefig("Graphics/execution-time.png")
    # plt.show()

if __name__ == "__main__":
    main()