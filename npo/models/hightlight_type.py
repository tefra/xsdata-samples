from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class HightlightType:
    class Meta:
        name = "hightlightType"

    body: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    term: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
