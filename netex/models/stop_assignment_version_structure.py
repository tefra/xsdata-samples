from dataclasses import dataclass, field
from typing import Optional, Union

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .private_code import PrivateCode
from .scheduled_stop_point import ScheduledStopPoint
from .scheduled_stop_point_ref import ScheduledStopPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "StopAssignment_VersionStructure"

    boarding_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BoardingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alighting_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlightingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point: Optional[
        Union[
            FareScheduledStopPointRef,
            ScheduledStopPointRef,
            ScheduledStopPoint,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPoint",
                    "type": ScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
