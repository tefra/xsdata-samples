from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from .capped_discount_right_ref import CappedDiscountRightRef
from .capping_period_enumeration import CappingPeriodEnumeration
from .capping_rule_prices_rel_structure import CappingRulePricesRelStructure
from .cell_versioned_child_structure import PriceableObjectVersionStructure
from .generic_parameter_assignment_version_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
    GenericParameterAssignmentsRelStructure,
)
from .preassigned_fare_product_ref import PreassignedFareProductRef
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
        }
    )
    capping_period: Optional[CappingPeriodEnumeration] = field(
        default=None,
        metadata={
            "name": "CappingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capped_discount_right_ref: List[CappedDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    supplement_product_ref: List[SupplementProductRef] = field(
        default_factory=list,
        metadata={
            "name": "SupplementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    preassigned_fare_product_ref: List[PreassignedFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "PreassignedFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_element_ref: Optional[ValidableElementRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_assignments: Optional[GenericParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    generic_parameter_assignment: Optional[GenericParameterAssignment] = field(
        default=None,
        metadata={
            "name": "GenericParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    generic_parameter_assignment_in_context: Optional[GenericParameterAssignmentInContext] = field(
        default=None,
        metadata={
            "name": "GenericParameterAssignmentInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[CappingRulePricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
