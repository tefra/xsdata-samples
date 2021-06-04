from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.models.assignment_version_structure_2 import AssignmentVersionStructure2
from netex.models.check_constraint_ref import CheckConstraintRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintThroughputVersionStructure(AssignmentVersionStructure2):
    class Meta:
        name = "CheckConstraintThroughput_VersionStructure"

    check_constraint_ref: Optional[CheckConstraintRef] = field(
        default=None,
        metadata={
            "name": "CheckConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_passengers: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumPassengers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    average_passengers: Optional[int] = field(
        default=None,
        metadata={
            "name": "AveragePassengers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_passengers: Optional[int] = field(
        default=None,
        metadata={
            "name": "WheelchairPassengers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
