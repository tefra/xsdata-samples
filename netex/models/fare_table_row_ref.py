from __future__ import annotations

from dataclasses import dataclass

from .fare_table_row_ref_structure import FareTableRowRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareTableRowRef(FareTableRowRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
