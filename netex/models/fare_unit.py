from __future__ import annotations

from dataclasses import dataclass, field

from .fare_unit_version_structure import FareUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareUnit(FareUnitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_class: None | str = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        },
    )
