from __future__ import annotations

from dataclasses import dataclass

from .fare_contract_version_structure import FareContractVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContract(FareContractVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
