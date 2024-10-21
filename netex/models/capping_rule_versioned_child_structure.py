from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from .capped_discount_right_ref import CappedDiscountRightRef
from .capping_period_enumeration import CappingPeriodEnumeration
from .capping_rule_prices_rel_structure import CappingRulePricesRelStructure
from .generic_parameter_assignments_rel_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
    GenericParameterAssignmentsRelStructure,
)
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .priceable_object_version_structure import PriceableObjectVersionStructure
from .supplement_product_ref import SupplementProductRef
from .validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CappingRuleVersionedChildStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "CappingRule_VersionedChildStructure"

    maximum_distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumDistance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    capping_period: Optional[CappingPeriodEnumeration] = field(
        default=None,
        metadata={
            "name": "CappingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    capped_discount_right_ref: Iterable[CappedDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    preassigned_fare_product_ref: Iterable[
        Union[SupplementProductRef, PreassignedFareProductRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    validable_element_ref: Optional[ValidableElementRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context: Optional[
        Union[
            GenericParameterAssignmentsRelStructure,
            GenericParameterAssignment,
            GenericParameterAssignmentInContext,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "validityParameterAssignments",
                    "type": GenericParameterAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    prices: Optional[CappingRulePricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
