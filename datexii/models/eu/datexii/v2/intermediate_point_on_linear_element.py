from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.referent import Referent

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class IntermediatePointOnLinearElement:
    class Meta:
        name = "_IntermediatePointOnLinearElement"

    referent: Referent = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
