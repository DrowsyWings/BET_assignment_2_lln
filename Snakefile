configfile: "config.yaml"

N = config["n"]
K_VALUES = config["k_values"]
REPEATS = config["repeats"]


rule all:
    input:
        f"plots/lln_for_n_{N}.png"

rule simulate:
    output:
        "data/results.csv"

    params:
        k_values = " ".join([str(x) for x in K_VALUES])

    shell:
        "python scripts/simulate.py --n {N} --repeats {REPEATS} --k_values {params.k_values} --output {output}"

rule plot:
    input:
        "data/results.csv"

    output:
        f"plots/lln_for_n_{N}.png"
        
    shell:
        "python scripts/plot.py --input {input} --output {output} --n {N}"