from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .headway_interval_structure import HeadwayIntervalStructure
from .passing_time_view_structure import PassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EstimatedPassingTimeViewStructure(PassingTimeViewStructure):
    class Meta:
        name = "EstimatedPassingTime_ViewStructure"

    choice: List[
        Union[
            "EstimatedPassingTimeViewStructure.ExpectedArrivalTime",
            "EstimatedPassingTimeViewStructure.ArrivalDayOffset",
            "EstimatedPassingTimeViewStructure.ExpectedDepartureTime",
            "EstimatedPassingTimeViewStructure.DepartureDayOffset",
            XmlDuration,
            "EstimatedPassingTimeViewStructure.ExpectedNonstopPassingTime",
            "EstimatedPassingTimeViewStructure.PassingTimeDayOffset",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExpectedArrivalTime",
                    "type": ForwardRef(
                        "EstimatedPassingTimeViewStructure.ExpectedArrivalTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": ForwardRef(
                        "EstimatedPassingTimeViewStructure.ArrivalDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedDepartureTime",
                    "type": ForwardRef(
                        "EstimatedPassingTimeViewStructure.ExpectedDepartureTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": ForwardRef(
                        "EstimatedPassingTimeViewStructure.DepartureDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedWaitingTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedNonstopPassingTime",
                    "type": ForwardRef(
                        "EstimatedPassingTimeViewStructure.ExpectedNonstopPassingTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeDayOffset",
                    "type": ForwardRef(
                        "EstimatedPassingTimeViewStructure.PassingTimeDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 5,
        },
    )
    expected_headway: Optional[HeadwayIntervalStructure] = field(
        default=None,
        metadata={
            "name": "ExpectedHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class ExpectedArrivalTime:
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
    class ExpectedDepartureTime:
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
    class ExpectedNonstopPassingTime:
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
