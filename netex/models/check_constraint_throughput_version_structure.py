from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .check_constraint_ref import CheckConstraintRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintThroughputVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "CheckConstraintThroughput_VersionStructure"

    check_constraint_ref: CheckConstraintRef | None = field(
        default=None,
        metadata={
            "name": "CheckConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    period: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_passengers: int | None = field(
        default=None,
        metadata={
            "name": "MaximumPassengers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    average_passengers: int | None = field(
        default=None,
        metadata={
            "name": "AveragePassengers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_passengers: int | None = field(
        default=None,
        metadata={
            "name": "WheelchairPassengers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
