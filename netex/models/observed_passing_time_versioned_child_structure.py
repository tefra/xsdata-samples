from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .dated_passing_time_versioned_child_structure import (
    DatedPassingTimeVersionedChildStructure,
)
from .headway_interval_structure import HeadwayIntervalStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ObservedPassingTimeVersionedChildStructure(
    DatedPassingTimeVersionedChildStructure
):
    class Meta:
        name = "ObservedPassingTime_VersionedChildStructure"

    choice_1: List[
        Union[
            "ObservedPassingTimeVersionedChildStructure.ActualArrivalTime",
            "ObservedPassingTimeVersionedChildStructure.ArrivalDayOffset",
            "ObservedPassingTimeVersionedChildStructure.ActualDepartureTime",
            "ObservedPassingTimeVersionedChildStructure.DepartureDayOffset",
            XmlDuration,
            "ObservedPassingTimeVersionedChildStructure.ActualNonstopPassingTime",
            "ObservedPassingTimeVersionedChildStructure.PassingTimeDayOffset",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ActualArrivalTime",
                    "type": Type[
                        "ObservedPassingTimeVersionedChildStructure.ActualArrivalTime"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": Type[
                        "ObservedPassingTimeVersionedChildStructure.ArrivalDayOffset"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualDepartureTime",
                    "type": Type[
                        "ObservedPassingTimeVersionedChildStructure.ActualDepartureTime"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": Type[
                        "ObservedPassingTimeVersionedChildStructure.DepartureDayOffset"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualWaitingTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualNonstopPassingTime",
                    "type": Type[
                        "ObservedPassingTimeVersionedChildStructure.ActualNonstopPassingTime"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeDayOffset",
                    "type": Type[
                        "ObservedPassingTimeVersionedChildStructure.PassingTimeDayOffset"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 5,
        },
    )
    actual_headway: Optional[HeadwayIntervalStructure] = field(
        default=None,
        metadata={
            "name": "ActualHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class ActualArrivalTime:
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
    class ActualDepartureTime:
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
    class ActualNonstopPassingTime:
        value: Optional[XmlTime] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class PassingTimeDayOffset:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
