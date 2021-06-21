from dataclasses import dataclass, field
from typing import List
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

    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EntitlementProductRef",
                    "type": EntitlementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRightRef",
                    "type": ServiceAccessRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                    "required": True,
                },
                {
                    "name": "MinimumQualificationPeriod",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementConstraint",
                    "type": EntitlementConstraintStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementType",
                    "type": EntitlementTypeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "min_occurs": 9,
            "max_occurs": 56,
        }
    )
