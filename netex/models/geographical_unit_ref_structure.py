from __future__ import annotations

from dataclasses import dataclass

from .fare_unit_ref_structure import FareUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnitRefStructure(FareUnitRefStructure):
    pass
