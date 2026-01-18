from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.openlr_extended_linear import (
    OpenlrExtendedLinear,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LinearExtensionType:
    class Meta:
        name = "_LinearExtensionType"

    openlr_extended_linear: None | OpenlrExtendedLinear = field(
        default=None,
        metadata={
            "name": "openlrExtendedLinear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
