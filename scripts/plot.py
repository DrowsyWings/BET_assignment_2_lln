import argparse
import csv
import matplotlib.pyplot as plt

def load_data(filename):

    grouped = {}

    with open(filename, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            k = int(row["k"])
            mean = float(row["mean"])

            if k not in grouped:
                grouped[k] = []

            grouped[k].append(mean)

    return grouped


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--n", type=int, required=True)

    args = parser.parse_args()

    grouped_data = load_data(args.input)

    k_values = sorted(grouped_data.keys())

    plot_data = []

    labels = []

    for k in k_values:
        plot_data.append(grouped_data[k])
        labels.append("k=" + str(k))

    plt.figure(figsize=(10, 5))

    plt.boxplot(plot_data, tick_labels=labels)

    expected_mean = (args.n + 1) / 2

    plt.axhline(y=expected_mean,linestyle="--")

    plt.xlabel("k values")
    plt.ylabel("Sample Mean")
    plt.title(f"Testing Draws for {args.n}")

    plt.savefig(args.output)

    print("Plot saved to", args.output)


if __name__ == "__main__":
    main()