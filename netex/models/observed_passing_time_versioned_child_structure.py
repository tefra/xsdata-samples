from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

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

    choice_1: Iterable[
        ObservedPassingTimeVersionedChildStructure.ActualArrivalTime | ObservedPassingTimeVersionedChildStructure.ArrivalDayOffset | ObservedPassingTimeVersionedChildStructure.ActualDepartureTime | ObservedPassingTimeVersionedChildStructure.DepartureDayOffset | XmlDuration | ObservedPassingTimeVersionedChildStructure.ActualNonstopPassingTime | ObservedPassingTimeVersionedChildStructure.PassingTimeDayOffset
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ActualArrivalTime",
                    "type": ForwardRef(
                        "ObservedPassingTimeVersionedChildStructure.ActualArrivalTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": ForwardRef(
                        "ObservedPassingTimeVersionedChildStructure.ArrivalDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualDepartureTime",
                    "type": ForwardRef(
                        "ObservedPassingTimeVersionedChildStructure.ActualDepartureTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": ForwardRef(
                        "ObservedPassingTimeVersionedChildStructure.DepartureDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualWaitingTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualNonstopPassingTime",
                    "type": ForwardRef(
                        "ObservedPassingTimeVersionedChildStructure.ActualNonstopPassingTime"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeDayOffset",
                    "type": ForwardRef(
                        "ObservedPassingTimeVersionedChildStructure.PassingTimeDayOffset"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 5,
        },
    )
    actual_headway: HeadwayIntervalStructure | None = field(
        default=None,
        metadata={
            "name": "ActualHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class ActualArrivalTime:
        value: XmlTime | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class ArrivalDayOffset:
        value: int | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class ActualDepartureTime:
        value: XmlTime | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class DepartureDayOffset:
        value: int | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class ActualNonstopPassingTime:
        value: XmlTime | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class PassingTimeDayOffset:
        value: int | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )
