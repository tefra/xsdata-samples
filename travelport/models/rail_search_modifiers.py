from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.rail_supplier import RailSupplier
from travelport.models.type_rail_direction import TypeRailDirection

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailSearchModifiers:
    """
    Controls and switches for the Rail Availability Search request.

    Parameters
    ----------
    preferred_suppliers
    max_changes
        The maximum number of stops within a connection.
    direction
        The direction of travel.
    class_value
    max_solutions
        The maximum number of solutions to return. Decreasing this number
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    preferred_suppliers: None | RailSearchModifiers.PreferredSuppliers = field(
        default=None,
        metadata={
            "name": "PreferredSuppliers",
            "type": "Element",
        },
    )
    max_changes: int = field(
        default=2,
        metadata={
            "name": "MaxChanges",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 3,
        },
    )
    direction: None | TypeRailDirection = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Attribute",
        },
    )
    max_solutions: int = field(
        default=300,
        metadata={
            "name": "MaxSolutions",
            "type": "Attribute",
        },
    )

    @dataclass
    class PreferredSuppliers:
        rail_supplier: list[RailSupplier] = field(
            default_factory=list,
            metadata={
                "name": "RailSupplier",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
