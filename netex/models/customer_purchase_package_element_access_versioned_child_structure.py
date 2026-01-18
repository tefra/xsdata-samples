from __future__ import annotations

from dataclasses import dataclass, field

from .customer_purchase_package_element_ref import (
    CustomerPurchasePackageElementRef,
)
from .customer_purchase_parameter_assignments_rel_structure import (
    CustomerPurchaseParameterAssignmentsRelStructure,
)
from .entity_in_version_structure import VersionedChildStructure
from .fare_structure_element_in_sequence_ref import (
    FareStructureElementInSequenceRef,
)
from .fare_structure_element_ref import FareStructureElementRef
from .marked_as_enumeration import MarkedAsEnumeration
from .validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackageElementAccessVersionedChildStructure(
    VersionedChildStructure
):
    class Meta:
        name = "CustomerPurchasePackageElementAccess_VersionedChildStructure"

    customer_purchase_package_element_ref: (
        None | CustomerPurchasePackageElementRef
    ) = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validable_element_ref: None | ValidableElementRef = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_structure_element_ref: None | FareStructureElementRef = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_structure_element_in_sequence_ref: (
        None | FareStructureElementInSequenceRef
    ) = field(
        default=None,
        metadata={
            "name": "FareStructureElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    marked_as: None | MarkedAsEnumeration = field(
        default=None,
        metadata={
            "name": "MarkedAs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_number: None | int = field(
        default=None,
        metadata={
            "name": "AccessNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_assignments: (
        None | CustomerPurchaseParameterAssignmentsRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
