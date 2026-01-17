from dataclasses import dataclass

from sdmx_ml.models.submit_structure_request_type_2 import (
    SubmitStructureRequestType2,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class SubmitStructureRequest(SubmitStructureRequestType2):
    """
    SubmitStructureRequest is used to submit structure definitions to the
    repository.

    The structure resources (key families, agencies, concepts and concept
    schemes, code lists, etc.) to be submitted may be communicated in-line
    or be supplied in a referenced SDMX-ML Structure messages external to
    the registry. A response will indicate status and contain any relevant
    error information.
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"
