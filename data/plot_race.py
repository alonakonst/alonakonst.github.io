import sys

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def main() -> None:
    fig, ax = plt.subplots(1, 2, figsize=(20, 20 / 2.414))
    gradient = True

    columns_race = ["Branca", "Preta", "Amarela", "Parda", "Indígena"]

    for i, year in enumerate([2014, 2022]):
        file = gpd.read_file(f"merged_{year}_v1.gpkg")
        file[columns_race + ["Total"]] = file[columns_race + ["Total"]].apply(pd.to_numeric, errors="coerce")
        title = f"{year} Percentage of white people"

        if gradient:
            norm = colors.Normalize(vmin=0, vmax=1)
            cmap = plt.get_cmap("binary_r")

            file["color_grad"] = file.apply(
                lambda row: cmap(norm(row["Branca"] / row["Total"])),
                axis=1,
            )

            file.plot(color=file["color_grad"], ax=ax[i])

        else:
            file.plot(color=file["color"], ax=ax[i])

        ax[i].set_title(title)
        ax[i].axis("off")
        fig.tight_layout()

    show()


def show() -> None:  # pragma: no cover
    if len(sys.argv) == 1:
        plt.show(block=False)
        plt.pause(0.001)
        input("hit[enter] to end.\n")
        plt.close("all")


if __name__ == "__main__":
    main()
