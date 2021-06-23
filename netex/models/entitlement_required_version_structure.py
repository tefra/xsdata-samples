from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .capped_discount_right_ref import CappedDiscountRightRef
from .entitlement_constraint_structure import EntitlementConstraintStructure
from .entitlement_product_ref import EntitlementProductRef
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
class EntitlementRequiredVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "EntitlementRequired_VersionStructure"

    entitlement_product_ref: Optional[EntitlementProductRef] = field(
        default=None,
        metadata={
            "name": "EntitlementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    supplement_product_ref: Optional[SupplementProductRef] = field(
        default=None,
        metadata={
            "name": "SupplementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    preassigned_fare_product_ref: Optional[PreassignedFareProductRef] = field(
        default=None,
        metadata={
            "name": "PreassignedFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    amount_of_price_unit_product_ref: Optional[AmountOfPriceUnitProductRef] = field(
        default=None,
        metadata={
            "name": "AmountOfPriceUnitProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    usage_discount_right_ref: Optional[UsageDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "UsageDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    third_party_product_ref: Optional[ThirdPartyProductRef] = field(
        default=None,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    capped_discount_right_ref: Optional[CappedDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    sale_discount_right_ref: Optional[SaleDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "SaleDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    fare_product_ref: Optional[FareProductRef] = field(
        default=None,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
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
