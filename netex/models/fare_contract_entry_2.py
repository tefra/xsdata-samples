from dataclasses import dataclass
from netex.models.fare_contract_entry_version_structure import FareContractEntryVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractEntry2(FareContractEntryVersionStructure):
    class Meta:
        name = "FareContractEntry"
        namespace = "http://www.netex.org.uk/netex"
