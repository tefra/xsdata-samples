from dataclasses import dataclass, field
from typing import Optional
from .fare_contract_ref import FareContractRef
from .log_entry_version_structure import LogEntryVersionStructure
from .type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractEntryVersionStructure(LogEntryVersionStructure):
    class Meta:
        name = "FareContractEntry_VersionStructure"

    is_valid: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsValid",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_fare_contract_entry_ref: Optional[
        TypeOfFareContractEntryRef
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfFareContractEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_contract_ref: Optional[FareContractRef] = field(
        default=None,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
