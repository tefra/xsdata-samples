from dataclasses import dataclass, field
from typing import Any, Optional

from sdmx_ml.models.registry_interface_type import RegistryInterfaceType
from sdmx_ml.models.submit_structure_response_type_1 import (
    SubmitStructureResponseType1,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class SubmitStructureResponseType2(RegistryInterfaceType):
    """
    SubmitStructureResponseType defines the structure of a registry submit
    registration response document.
    """

    class Meta:
        name = "SubmitStructureResponseType"

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    submit_structure_response: Optional[SubmitStructureResponseType1] = field(
        default=None,
        metadata={
            "name": "SubmitStructureResponse",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "required": True,
        },
    )
