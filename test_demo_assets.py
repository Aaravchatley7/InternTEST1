import os


def test_demo_assets_exist():

    assert os.path.exists(
        "demo"
    )

    assert os.path.exists(
        "demo/sample_requests"
    )

    assert os.path.exists(
        "demo/sample_outputs"
    )