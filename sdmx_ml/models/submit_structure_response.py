from dataclasses import dataclass

from sdmx_ml.models.submit_structure_response_type_2 import (
    SubmitStructureResponseType2,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class SubmitStructureResponse(SubmitStructureResponseType2):
    """SubmitStructureResponse is returned by the registry when a structure
    submission request is received.

    It indicates the status of the submission, and carries any error
    messages which are generated, if relevant.
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"
