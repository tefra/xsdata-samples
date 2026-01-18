from __future__ import annotations

from dataclasses import dataclass

from .fare_table_ref_structure import FareTableRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareTableRef(FareTableRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
