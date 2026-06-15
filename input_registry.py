class InputRegistry:

    CAPABILITIES = {

        "identity_verification": {

            "inputs": [

                "aadhaar",

                "pan"
            ],

            "outputs": [

                "validation",

                "confidence",

                "evidence"
            ]
        },

        "knowledge_assistant": {

            "inputs": [

                "pdf"
            ],

            "outputs": [

                "answer",

                "confidence"
            ]
        }
    }

    @staticmethod
    def get_capabilities():

        return (

            InputRegistry
            .CAPABILITIES
        )
