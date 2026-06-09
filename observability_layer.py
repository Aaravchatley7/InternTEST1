import os
import json
import uuid
import time
import logging


class ObservabilityLayer:

    METRICS_FILE = "metrics/metrics.json"

    @staticmethod
    def setup_logging():

        os.makedirs(
            "logs",
            exist_ok=True
        )

        logging.basicConfig(
            filename="logs/app.log",
            level=logging.INFO,
            format=(
                "%(asctime)s | "
                "%(levelname)s | "
                "%(message)s"
            )
        )

    @staticmethod
    def create_trace():

        return str(
            uuid.uuid4()
        )

    @staticmethod
    def start_timer():

        return time.time()

    @staticmethod
    def stop_timer(start):

        return round(
            (time.time() - start)
            * 1000,
            2
        )

    @staticmethod
    def initialize_metrics():

        os.makedirs(
            "metrics",
            exist_ok=True
        )

        if not os.path.exists(
            ObservabilityLayer.METRICS_FILE
        ):

            with open(
                ObservabilityLayer.METRICS_FILE,
                "w"
            ) as f:

                json.dump(
                    {
                        "total_requests": 0,
                        "total_errors": 0,
                        "average_latency": 0,
                        "latencies": []
                    },
                    f,
                    indent=4
                )
    @staticmethod
    def update_metrics(
        latency,
        error=False
    ):

        with open(
            ObservabilityLayer.METRICS_FILE,
            "r"
        ) as f:

            metrics = json.load(f)

        metrics["total_requests"] += 1

        if error:
            metrics["total_errors"] += 1

        metrics["latencies"].append(
            latency
        )

        metrics[
            "average_latency"
        ] = round(

            sum(
                metrics["latencies"]
            )

            /

            len(
                metrics["latencies"]
            ),

            2
        )

        with open(
            ObservabilityLayer.METRICS_FILE,
            "w"
        ) as f:

            json.dump(
                metrics,
                f,
                indent=4
            )

    @staticmethod
    def get_metrics():

        with open(
            ObservabilityLayer.METRICS_FILE,
            "r"
        ) as f:

            return json.load(f)

    @staticmethod
    def log_success(
        trace_id,
        message
    ):

        logging.info(
            f"{trace_id} | {message}"
        )

    @staticmethod
    def log_error(
        trace_id,
        message
    ):

        logging.error(
            f"{trace_id} | {message}"
        )