import pandas as pd


def main() -> None:
    df2010 = pd.read_csv("tabela9605-2010.csv", skiprows=4)

    df2022 = pd.read_csv("tabela9605-2022.csv", skiprows=4)

    colunas_racas = ["Branca", "Preta", "Amarela", "Parda", "Indígena"]
    df2010[colunas_racas + ["Total"]] = df2010[colunas_racas + ["Total"]].apply(pd.to_numeric, errors="coerce")
    df2022[colunas_racas + ["Total"]] = df2022[colunas_racas + ["Total"]].apply(pd.to_numeric, errors="coerce")

    print_race_percentage(df2010, year=2010)
    print_race_percentage(df2022, year=2022)


def print_race_percentage(df: pd.DataFrame, year: int) -> None:
    total = df["Total"].sum()
    white = df["Branca"].sum() / total * 100.0
    black = df["Preta"].sum() / total * 100.0
    mixed = df["Parda"].sum() / total * 100.0
    yellow = df["Amarela"].sum() / total * 100.0
    indian = df["Indígena"].sum() / total * 100.0

    print(f"{year} - {total:,.0f}")
    print("\twhite ", f"{white:.2f}%")
    print("\tblack ", f"{black:.2f}%")
    print("\tmixed ", f"{mixed:.2f}%")
    print("\tyellow", f"{yellow:.2f}%")
    print("\tindian", f"{indian:.2f}%")
    print()


if __name__ == "__main__":
    print()
    main()
