from dataclasses import dataclass, field
from typing import Any, Optional

from sdmx_ml.models.registry_interface_type import RegistryInterfaceType
from sdmx_ml.models.submit_structure_request_type_1 import (
    SubmitStructureRequestType1,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class SubmitStructureRequestType2(RegistryInterfaceType):
    """
    SubmitStructureRequestType defines the structure of a registry submit structure
    request document.
    """

    class Meta:
        name = "SubmitStructureRequestType"

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    footer: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    submit_structure_request: Optional[SubmitStructureRequestType1] = field(
        default=None,
        metadata={
            "name": "SubmitStructureRequest",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "required": True,
        },
    )
