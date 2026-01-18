from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.referent import Referent

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class IntermediatePointOnLinearElement:
    class Meta:
        name = "_IntermediatePointOnLinearElement"

    referent: Referent | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    index: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
