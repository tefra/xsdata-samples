from __future__ import annotations

from dataclasses import dataclass

from .geographical_unit_version_structure import (
    GeographicalUnitVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnit(GeographicalUnitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
