import pandas as pd


def main():
    df = pd.read_json("Output/execution-time.json").T
    df.drop(['Crescente', 'Decrescente'], inplace=True, axis=1)
    df.to_latex("Output/table-latex.out")

if __name__ == "__main__":
    main()