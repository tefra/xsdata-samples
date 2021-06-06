from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .fare_contract_entry_1 import FareContractEntry1
from .fare_contract_entry_2 import FareContractEntry2
from .fare_contract_entry_ref import FareContractEntryRef
from .offered_travel_specification import OfferedTravelSpecification
from .offered_travel_specification_ref import OfferedTravelSpecificationRef
from .requested_travel_specification import RequestedTravelSpecification
from .requested_travel_specification_ref import RequestedTravelSpecificationRef
from .sales_transaction import SalesTransaction
from .sales_transaction_ref import SalesTransactionRef
from .travel_specification_1 import TravelSpecification1
from .travel_specification_2 import TravelSpecification2
from .travel_specification_ref import TravelSpecificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractEntriesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fareContractEntries_RelStructure"

    sales_transaction_ref: List[SalesTransactionRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    offered_travel_specification_ref: List[OfferedTravelSpecificationRef] = field(
        default_factory=list,
        metadata={
            "name": "OfferedTravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requested_travel_specification_ref: List[RequestedTravelSpecificationRef] = field(
        default_factory=list,
        metadata={
            "name": "RequestedTravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_specification_ref: List[TravelSpecificationRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_entry_ref: List[FareContractEntryRef] = field(
        default_factory=list,
        metadata={
            "name": "FareContractEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_transaction: List[SalesTransaction] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransaction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    offered_travel_specification: List[OfferedTravelSpecification] = field(
        default_factory=list,
        metadata={
            "name": "OfferedTravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requested_travel_specification: List[RequestedTravelSpecification] = field(
        default_factory=list,
        metadata={
            "name": "RequestedTravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_specification: List[TravelSpecification1] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_travel_specification: List[TravelSpecification2] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_entry: List[FareContractEntry1] = field(
        default_factory=list,
        metadata={
            "name": "FareContractEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_fare_contract_entry: List[FareContractEntry2] = field(
        default_factory=list,
        metadata={
            "name": "FareContractEntry_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
