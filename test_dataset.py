import json


def test_dataset_size():

    with open(
        "evaluation/dataset.json",
        "r"
    ) as f:

        dataset = json.load(f)

    assert (

        len(dataset)

        >=

        50
    )