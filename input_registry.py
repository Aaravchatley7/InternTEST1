class InputRegistry:

    SUPPORTED_INPUTS = {

        "document": {
            "enabled": True,
            "formats": [
                "pdf",
                "jpg",
                "jpeg",
                "png"
            ]
        },

        "image": {
            "enabled": True,
            "formats": [
                "jpg",
                "jpeg",
                "png"
            ]
        },

        "form": {
            "enabled": True
        },

        "structured_json": {
            "enabled": True
        }
    }

    @classmethod
    def get_supported_inputs(cls):

        return cls.SUPPORTED_INPUTS