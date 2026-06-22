class BHIVError(Exception):

    pass


class ValidationError(
    BHIVError
):

    pass


class ExtractionError(
    BHIVError
):

    pass


class ReplayError(
    BHIVError
):

    pass


class RAGError(
    BHIVError
):

    pass