from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticProcessingStyleEnumSimple(Enum):
    """
    :cvar PROCESSING_STYLE_ASYNCHRONOUS: The software-component
        processes the request in background but still the Dcm has to
        issue the call again to eventually obtain the result of the
        request.
    :cvar PROCESSING_STYLE_ASYNCHRONOUS_WITH_ERROR: The software-
        component processes the request in background but still the Dcm
        has to issue the call again to eventually obtain the result of
        the request or handle error code.
    :cvar PROCESSING_STYLE_SYNCHRONOUS: The software-component is
        supposed to react synchronously on the request.
    """

    PROCESSING_STYLE_ASYNCHRONOUS = "PROCESSING-STYLE-ASYNCHRONOUS"
    PROCESSING_STYLE_ASYNCHRONOUS_WITH_ERROR = (
        "PROCESSING-STYLE-ASYNCHRONOUS-WITH-ERROR"
    )
    PROCESSING_STYLE_SYNCHRONOUS = "PROCESSING-STYLE-SYNCHRONOUS"
