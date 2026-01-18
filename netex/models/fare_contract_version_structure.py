from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .customer_account_ref import CustomerAccountRef
from .customer_ref import CustomerRef
from .entity_in_version_structure import DataManagedObjectStructure
from .fare_contract_entries_rel_structure import (
    FareContractEntriesRelStructure,
)
from .multilingual_string import MultilingualString
from .type_of_fare_contract_ref import TypeOfFareContractRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "FareContract_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    status: str | None = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_ref: CustomerRef | None = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_account_ref: CustomerAccountRef | None = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_fare_contract_ref: TypeOfFareContractRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfFareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_contract_entries: FareContractEntriesRelStructure | None = field(
        default=None,
        metadata={
            "name": "fareContractEntries",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
