from __future__ import annotations

from dataclasses import dataclass

from .type_of_fare_contract_entry_ref_structure import (
    TypeOfFareContractEntryRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFareContractEntryRef(TypeOfFareContractEntryRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
