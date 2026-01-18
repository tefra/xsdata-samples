from __future__ import annotations

from dataclasses import dataclass

from .geographical_unit_ref_structure import GeographicalUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalUnitRef(GeographicalUnitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
