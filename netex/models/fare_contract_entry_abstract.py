from dataclasses import dataclass

from .fare_contract_entry_version_structure import (
    FareContractEntryVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractEntryAbstract(FareContractEntryVersionStructure):
    class Meta:
        name = "FareContractEntry"
        namespace = "http://www.netex.org.uk/netex"
