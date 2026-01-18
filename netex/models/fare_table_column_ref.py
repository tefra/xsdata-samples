from __future__ import annotations

from dataclasses import dataclass

from .fare_table_column_ref_structure import FareTableColumnRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareTableColumnRef(FareTableColumnRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
