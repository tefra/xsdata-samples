from __future__ import annotations

from dataclasses import dataclass, field

from .access_right_parameter_assignments_rel_structure import (
    AccessRightParameterAssignmentsRelStructure,
)
from .controllable_element_prices_rel_structure import (
    ControllableElementPricesRelStructure,
)
from .controllable_elements_in_sequence_rel_structure import (
    ControllableElementsInSequenceRelStructure,
)
from .priceable_object_version_structure import PriceableObjectVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "ControllableElement_VersionStructure"

    access_right_parameter_assignments: (
        None | AccessRightParameterAssignmentsRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "accessRightParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    controllable_elements_in_sequence: (
        None | ControllableElementsInSequenceRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "controllableElementsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: None | ControllableElementPricesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
