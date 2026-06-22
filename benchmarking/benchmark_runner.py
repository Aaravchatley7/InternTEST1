import json


def load_results():

    with open(
        "evaluation/evaluation_results.json",
        "r"
    ) as f:

        return json.load(f)


def generate_report():

    metrics = load_results()

    report = {

        "accuracy":
            metrics["accuracy"],

        "precision":
            metrics["precision"],

        "recall":
            metrics["recall"],

        "f1_score":
            metrics["f1_score"],

        "false_positive_rate":
            metrics["false_positive_rate"],

        "false_negative_rate":
            metrics["false_negative_rate"]
    }

    with open(
        "benchmarking/benchmark_results.json",
        "w"
    ) as f:

        json.dump(
            report,
            f,
            indent=4
        )

    return report


if __name__ == "__main__":

    print(
        generate_report()
    )