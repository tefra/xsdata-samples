from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .dated_passing_time_versioned_child_structure import (
    DatedPassingTimeVersionedChildStructure,
)
from .headway_interval_structure import HeadwayIntervalStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TargetPassingTimeVersionedChildStructure(
    DatedPassingTimeVersionedChildStructure
):
    class Meta:
        name = "TargetPassingTime_VersionedChildStructure"

    choice_1: List[
        Union[
            "TargetPassingTimeVersionedChildStructure.AimedArrivalTime",
            "TargetPassingTimeVersionedChildStructure.ArrivalDayOffset",
            "TargetPassingTimeVersionedChildStructure.AimedDepartureTime",
            "TargetPassingTimeVersionedChildStructure.DepartureDayOffset",
            XmlDuration,
            "TargetPassingTimeVersionedChildStructure.AimedNonstopPassingTime",
            "TargetPassingTimeVersionedChildStructure.PassingDayOffset",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AimedArrivalTime",
                    "type": ForwardRef(
                        "TargetPassingTimeVersionedChildStructure.AimedArrivalTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": ForwardRef(
                        "TargetPassingTimeVersionedChildStructure.ArrivalDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AimedDepartureTime",
                    "type": ForwardRef(
                        "TargetPassingTimeVersionedChildStructure.AimedDepartureTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": ForwardRef(
                        "TargetPassingTimeVersionedChildStructure.DepartureDayOffset"
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
                        "TargetPassingTimeVersionedChildStructure.AimedNonstopPassingTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingDayOffset",
                    "type": ForwardRef(
                        "TargetPassingTimeVersionedChildStructure.PassingDayOffset"
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
