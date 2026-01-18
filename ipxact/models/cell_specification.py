from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.cell_class_value_type import CellClassValueType
from ipxact.models.cell_function_value_type import CellFunctionValueType
from ipxact.models.cell_strength_value_type import CellStrengthValueType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class CellSpecification:
    """
    Used to provide a generic description of a technology library cell.

    :ivar cell_function: Defines a technology library cell in library
        independent fashion, based on specification of a cell function
        and strength.
    :ivar cell_class: Defines a technology library cell in library
        independent fashion, based on specification of a cell class and
        strength.
    :ivar cell_strength: Indicates the desired strength of the specified
        cell.
    """

    class Meta:
        name = "cellSpecification"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    cell_function: CellSpecification.CellFunction | None = field(
        default=None,
        metadata={
            "name": "cellFunction",
            "type": "Element",
        },
    )
    cell_class: CellClassValueType | None = field(
        default=None,
        metadata={
            "name": "cellClass",
            "type": "Element",
        },
    )
    cell_strength: CellStrengthValueType | None = field(
        default=None,
        metadata={
            "name": "cellStrength",
            "type": "Attribute",
        },
    )

    @dataclass
    class CellFunction:
        value: CellFunctionValueType | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        other: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
