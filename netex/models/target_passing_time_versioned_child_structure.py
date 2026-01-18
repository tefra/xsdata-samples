from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import ForwardRef

from xsdata.models.datatype import XmlDuration, XmlTime

from .dated_passing_time_versioned_child_structure import (
    DatedPassingTimeVersionedChildStructure,
)
from .headway_interval_structure import HeadwayIntervalStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TargetPassingTimeVersionedChildStructure(
    DatedPassingTimeVersionedChildStructure
):
    class Meta:
        name = "TargetPassingTime_VersionedChildStructure"

    choice_1: Iterable[
        TargetPassingTimeVersionedChildStructure.AimedArrivalTime
        | TargetPassingTimeVersionedChildStructure.ArrivalDayOffset
        | TargetPassingTimeVersionedChildStructure.AimedDepartureTime
        | TargetPassingTimeVersionedChildStructure.DepartureDayOffset
        | XmlDuration
        | TargetPassingTimeVersionedChildStructure.AimedNonstopPassingTime
        | TargetPassingTimeVersionedChildStructure.PassingDayOffset
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
    aimed_headway: None | HeadwayIntervalStructure = field(
        default=None,
        metadata={
            "name": "AimedHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class AimedArrivalTime:
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
    class AimedDepartureTime:
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
    class AimedNonstopPassingTime:
        value: XmlTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class PassingDayOffset:
        value: int = field(
            metadata={
                "required": True,
            }
        )
