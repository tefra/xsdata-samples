from __future__ import annotations

from dataclasses import dataclass, field

from .priceable_object_version_structure import PriceableObjectVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareUnitVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "FareUnit_VersionStructure"

    name_of_class_of_unit: str | None = field(
        default=None,
        metadata={
            "name": "nameOfClassOfUnit",
            "type": "Attribute",
        },
    )
