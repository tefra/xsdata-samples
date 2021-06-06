from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .capped_discount_right_ref import CappedDiscountRightRef
from .entitlement_constraint_structure import EntitlementConstraintStructure
from .entitlement_product_ref import EntitlementProductRef
from .entitlement_type_enumeration import EntitlementTypeEnumeration
from .fare_product_ref import FareProductRef
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .sale_discount_right_ref import SaleDiscountRightRef
from .service_access_right_ref import ServiceAccessRightRef
from .supplement_product_ref import SupplementProductRef
from .third_party_product_ref import ThirdPartyProductRef
from .usage_discount_right_ref import UsageDiscountRightRef
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitlementGivenVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "EntitlementGiven_VersionStructure"

    entitlement_product_ref: List[EntitlementProductRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    supplement_product_ref: List[SupplementProductRef] = field(
        default_factory=list,
        metadata={
            "name": "SupplementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 10,
            "sequential": True,
        }
    )
    preassigned_fare_product_ref: List[PreassignedFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "PreassignedFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    amount_of_price_unit_product_ref: List[AmountOfPriceUnitProductRef] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfPriceUnitProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    usage_discount_right_ref: List[UsageDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    third_party_product_ref: List[ThirdPartyProductRef] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    capped_discount_right_ref: List[CappedDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 10,
            "sequential": True,
        }
    )
    sale_discount_right_ref: List[SaleDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "SaleDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 6,
            "sequential": True,
        }
    )
    fare_product_ref: List[FareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_access_right_ref: Optional[ServiceAccessRightRef] = field(
        default=None,
        metadata={
            "name": "ServiceAccessRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    minimum_qualification_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumQualificationPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_constraint: Optional[EntitlementConstraintStructure] = field(
        default=None,
        metadata={
            "name": "EntitlementConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_type: Optional[EntitlementTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "EntitlementType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
