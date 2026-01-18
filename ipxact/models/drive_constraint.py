from dataclasses import dataclass, field

from ipxact.models.cell_specification import CellSpecification

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class DriveConstraint:
    """
    Defines a constraint indicating how an input is to be driven.

    The preferred methodology is to specify a library cell in technology
    independent fashion. The implemention tool should assume that the
    associated port is driven by the specified cell, or that the drive
    strength of the input port is indicated by the specified resistance
    value.
    """

    class Meta:
        name = "driveConstraint"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    cell_specification: CellSpecification | None = field(
        default=None,
        metadata={
            "name": "cellSpecification",
            "type": "Element",
            "required": True,
        },
    )
