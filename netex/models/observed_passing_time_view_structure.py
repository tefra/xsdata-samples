from dataclasses import dataclass, field
from typing import List, Optional, Type, Union
from xsdata.models.datatype import XmlDuration, XmlTime
from .headway_interval_structure import HeadwayIntervalStructure
from .passing_time_view_structure import PassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ObservedPassingTimeViewStructure(PassingTimeViewStructure):
    class Meta:
        name = "ObservedPassingTime_ViewStructure"

    choice: List[
        Union[
            "ObservedPassingTimeViewStructure.ActualArrivalTime",
            "ObservedPassingTimeViewStructure.ArrivalDayOffset",
            "ObservedPassingTimeViewStructure.ActualDepartureTime",
            "ObservedPassingTimeViewStructure.DepartureDayOffset",
            XmlDuration,
            "ObservedPassingTimeViewStructure.ActualNonstopPassingTime",
            "ObservedPassingTimeViewStructure.PassingTimeDayOffset",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ActualArrivalTime",
                    "type": Type[
                        "ObservedPassingTimeViewStructure.ActualArrivalTime"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": Type[
                        "ObservedPassingTimeViewStructure.ArrivalDayOffset"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualDepartureTime",
                    "type": Type[
                        "ObservedPassingTimeViewStructure.ActualDepartureTime"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": Type[
                        "ObservedPassingTimeViewStructure.DepartureDayOffset"
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
                        "ObservedPassingTimeViewStructure.ActualNonstopPassingTime"
                    ],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeDayOffset",
                    "type": Type[
                        "ObservedPassingTimeViewStructure.PassingTimeDayOffset"
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
