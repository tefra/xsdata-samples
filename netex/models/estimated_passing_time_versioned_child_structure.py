from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import ForwardRef

from xsdata.models.datatype import XmlDuration, XmlTime

from .dated_passing_time_versioned_child_structure import (
    DatedPassingTimeVersionedChildStructure,
)
from .headway_interval_structure import HeadwayIntervalStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EstimatedPassingTimeVersionedChildStructure(
    DatedPassingTimeVersionedChildStructure
):
    class Meta:
        name = "EstimatedPassingTime_VersionedChildStructure"

    choice_1: Sequence[
        EstimatedPassingTimeVersionedChildStructure.ExpectedArrivalTime
        | EstimatedPassingTimeVersionedChildStructure.ArrivalDayOffset
        | EstimatedPassingTimeVersionedChildStructure.ExpectedDepartureTime
        | EstimatedPassingTimeVersionedChildStructure.DepartureDayOffset
        | XmlDuration
        | EstimatedPassingTimeVersionedChildStructure.ExpectedNonstopPassingTime
        | EstimatedPassingTimeVersionedChildStructure.PassingTimeDayOffset
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExpectedArrivalTime",
                    "type": ForwardRef(
                        "EstimatedPassingTimeVersionedChildStructure.ExpectedArrivalTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": ForwardRef(
                        "EstimatedPassingTimeVersionedChildStructure.ArrivalDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedDepartureTime",
                    "type": ForwardRef(
                        "EstimatedPassingTimeVersionedChildStructure.ExpectedDepartureTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": ForwardRef(
                        "EstimatedPassingTimeVersionedChildStructure.DepartureDayOffset"
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
                        "EstimatedPassingTimeVersionedChildStructure.ExpectedNonstopPassingTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeDayOffset",
                    "type": ForwardRef(
                        "EstimatedPassingTimeVersionedChildStructure.PassingTimeDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 5,
        },
    )
    expected_headway: None | HeadwayIntervalStructure = field(
        default=None,
        metadata={
            "name": "ExpectedHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class ExpectedArrivalTime:
        value: XmlTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ArrivalDayOffset:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ExpectedDepartureTime:
        value: XmlTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class DepartureDayOffset:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ExpectedNonstopPassingTime:
        value: XmlTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class PassingTimeDayOffset:
        value: int = field(
            metadata={
                "required": True,
            }
        )
