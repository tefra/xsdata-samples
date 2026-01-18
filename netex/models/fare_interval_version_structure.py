from __future__ import annotations

from dataclasses import dataclass, field

from .priceable_object_version_structure import PriceableObjectVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareIntervalVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "FareInterval_VersionStructure"

    name_of_class_of_unit: None | str = field(
        default=None,
        metadata={
            "name": "nameOfClassOfUnit",
            "type": "Attribute",
        },
    )
