from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .customer_service_version_structure import CustomerServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LeftLuggageServiceVersionStructure(CustomerServiceVersionStructure):
    class Meta:
        name = "LeftLuggageService_VersionStructure"

    counter_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CounterService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    self_service_lockers: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelfServiceLockers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fee_per_bag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FeePerBag",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LockerFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_depth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagDepth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
