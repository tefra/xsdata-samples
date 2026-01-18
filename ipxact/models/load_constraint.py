from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.cell_specification import CellSpecification
from ipxact.models.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class LoadConstraint:
    """
    Defines a constraint indicating the type of load on an output port.

    :ivar cell_specification:
    :ivar count: Indicates how many loads of the specified cell are
        connected. If not present, 3 is assumed.
    """

    class Meta:
        name = "loadConstraint"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    cell_specification: CellSpecification = field(
        metadata={
            "name": "cellSpecification",
            "type": "Element",
            "required": True,
        }
    )
    count: None | UnsignedPositiveIntExpression = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
