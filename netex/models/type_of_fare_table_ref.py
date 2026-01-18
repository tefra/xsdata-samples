from __future__ import annotations

from dataclasses import dataclass

from .type_of_fare_table_ref_structure import TypeOfFareTableRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareTableRef(TypeOfFareTableRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
