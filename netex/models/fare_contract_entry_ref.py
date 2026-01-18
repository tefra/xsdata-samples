from __future__ import annotations

from dataclasses import dataclass

from .fare_contract_entry_ref_structure import FareContractEntryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContractEntryRef(FareContractEntryRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
