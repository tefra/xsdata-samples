from dataclasses import dataclass, field

from ipxact.models.drive_constraint import DriveConstraint
from ipxact.models.load_constraint import LoadConstraint
from ipxact.models.timing_constraint import TimingConstraint

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AbstractionDefPortConstraintsType:
    """
    Defines constraints that apply to a wire type port in an abstraction
    definition.
    """

    class Meta:
        name = "abstractionDefPortConstraintsType"

    timing_constraint: list[TimingConstraint] = field(
        default_factory=list,
        metadata={
            "name": "timingConstraint",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
        },
    )
    drive_constraint: list[DriveConstraint] = field(
        default_factory=list,
        metadata={
            "name": "driveConstraint",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "max_occurs": 2,
        },
    )
    load_constraint: list[LoadConstraint] = field(
        default_factory=list,
        metadata={
            "name": "loadConstraint",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "max_occurs": 3,
        },
    )
