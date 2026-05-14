import argparse
import random
import csv

def generate_means(n, repeats, k_values):
    all_rows = []

    for k in k_values:
        for i in range(repeats):

            values = []

            for j in range(k):
                values.append(random.randint(1, n))

            avg = sum(values) / len(values)

            row = {
                "k": k,
                "mean": avg
            }

            all_rows.append(row)

    return all_rows


def save_csv(data, filename):

    with open(filename, "w", newline="") as file:

        writer = csv.DictWriter(file, fieldnames=["k", "mean"])

        writer.writeheader()

        for row in data:
            writer.writerow(row)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--repeats", type=int, required=True)
    parser.add_argument("--k_values", nargs="+", type=int, required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    data = generate_means(
        args.n,
        args.repeats,
        args.k_values
    )

    save_csv(data, args.output)

    print("Data saved to", args.output)


if __name__ == "__main__":
    main()