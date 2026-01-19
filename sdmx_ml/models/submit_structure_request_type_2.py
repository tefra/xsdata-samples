from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.registry_interface_type import RegistryInterfaceType
from sdmx_ml.models.submit_structure_request_type_1 import (
    SubmitStructureRequestType1,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/message"


@dataclass(frozen=True, kw_only=True)
class SubmitStructureRequestType2(RegistryInterfaceType):
    """
    SubmitStructureRequestType defines the structure of a registry submit
    structure request document.
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
    submit_structure_request: SubmitStructureRequestType1 = field(
        metadata={
            "name": "SubmitStructureRequest",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/message",
            "required": True,
        }
    )
