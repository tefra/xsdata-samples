from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .headway_interval_structure import HeadwayIntervalStructure
from .passing_time_view_structure import PassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TargetPassingTimeViewStructure(PassingTimeViewStructure):
    class Meta:
        name = "TargetPassingTime_ViewStructure"

    choice: List[
        Union[
            "TargetPassingTimeViewStructure.AimedArrivalTime",
            "TargetPassingTimeViewStructure.ArrivalDayOffset",
            "TargetPassingTimeViewStructure.AimedDepartureTime",
            "TargetPassingTimeViewStructure.DepartureDayOffset",
            XmlDuration,
            "TargetPassingTimeViewStructure.AimedNonstopPassingTime",
            "TargetPassingTimeViewStructure.PassingDayOffset",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AimedArrivalTime",
                    "type": ForwardRef(
                        "TargetPassingTimeViewStructure.AimedArrivalTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": ForwardRef(
                        "TargetPassingTimeViewStructure.ArrivalDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AimedDepartureTime",
                    "type": ForwardRef(
                        "TargetPassingTimeViewStructure.AimedDepartureTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": ForwardRef(
                        "TargetPassingTimeViewStructure.DepartureDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AimedWaitingTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AimedNonstopPassingTime",
                    "type": ForwardRef(
                        "TargetPassingTimeViewStructure.AimedNonstopPassingTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingDayOffset",
                    "type": ForwardRef(
                        "TargetPassingTimeViewStructure.PassingDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 5,
        },
    )
    aimed_headway: Optional[HeadwayIntervalStructure] = field(
        default=None,
        metadata={
            "name": "AimedHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class AimedArrivalTime:
        value: Optional[XmlTime] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class ArrivalDayOffset:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class AimedDepartureTime:
        value: Optional[XmlTime] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class DepartureDayOffset:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class AimedNonstopPassingTime:
        value: Optional[XmlTime] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class PassingDayOffset:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
