from __future__ import annotations

from dataclasses import dataclass, field

from .priceable_object_ref_structure import PriceableObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintRefStructure2(PriceableObjectRefStructure):
    class Meta:
        name = "SeriesConstraintRefStructure_"

    order: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
