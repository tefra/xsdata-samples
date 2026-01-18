from __future__ import annotations

from dataclasses import dataclass

from .fare_table_ref_structure import FareTableRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StandardFareTableRefStructure(FareTableRefStructure):
    pass
