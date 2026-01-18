from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class FareContractVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "FareContract_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_ref: None | CustomerRef = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_account_ref: None | CustomerAccountRef = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_fare_contract_ref: None | TypeOfFareContractRef = field(
        default=None,
        metadata={
            "name": "TypeOfFareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_contract_entries: None | FareContractEntriesRelStructure = field(
        default=None,
        metadata={
            "name": "fareContractEntries",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
