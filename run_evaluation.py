import json


def evaluate():

    with open(
        "evaluation/dataset.json",
        "r"
    ) as f:

        dataset = json.load(f)

    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for row in dataset:

        pred = row["predicted"]
        actual = row["actual"]

        if pred and actual:
            tp += 1

        elif pred and not actual:
            fp += 1

        elif not pred and actual:
            fn += 1

        else:
            tn += 1

    accuracy = (

        (tp + tn)

        /

        len(dataset)

    )

    precision = (

        tp

        /

        (tp + fp)

        if (tp + fp) > 0

        else 0
    )

    recall = (

        tp

        /

        (tp + fn)

        if (tp + fn) > 0

        else 0
    )

    f1 = (

        2 * precision * recall

        /

        (precision + recall)

        if (precision + recall) > 0

        else 0
    )

    fpr = (

        fp

        /

        (fp + tn)

        if (fp + tn) > 0

        else 0
    )

    fnr = (

        fn

        /

        (fn + tp)

        if (fn + tp) > 0

        else 0
    )

    results = {

        "samples":
            len(dataset),

        "true_positive":
            tp,

        "true_negative":
            tn,

        "false_positive":
            fp,

        "false_negative":
            fn,

        "accuracy":
            round(
                accuracy,
                4
            ),

        "precision":
            round(
                precision,
                4
            ),

        "recall":
            round(
                recall,
                4
            ),

        "f1_score":
            round(
                f1,
                4
            ),

        "false_positive_rate":
            round(
                fpr,
                4
            ),

        "false_negative_rate":
            round(
                fnr,
                4
            )
    }

    with open(
        "evaluation/evaluation_results.json",
        "w"
    ) as f:

        json.dump(
            results,
            f,
            indent=4
        )

    print(results)


if __name__ == "__main__":

    evaluate()