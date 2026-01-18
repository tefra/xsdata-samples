from __future__ import annotations

from dataclasses import dataclass, field

from .border_point_ref import BorderPointRef
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .garage_point_ref import GaragePointRef
from .journey_headway_versioned_child_structure import (
    JourneyHeadwayVersionedChildStructure,
)
from .journey_pattern_ref import JourneyPatternRef
from .parking_point_ref import ParkingPointRef
from .relief_point_ref import ReliefPointRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef
from .timing_point_ref import TimingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternHeadwayVersionedChildStructure(
    JourneyHeadwayVersionedChildStructure
):
    class Meta:
        name = "JourneyPatternHeadway_VersionedChildStructure"

    journey_pattern_ref: (
        None
        | ServiceJourneyPatternRef
        | ServicePatternRef
        | DeadRunJourneyPatternRef
        | JourneyPatternRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice: (
        None
        | BorderPointRef
        | FareScheduledStopPointRef
        | ScheduledStopPointRef
        | GaragePointRef
        | ParkingPointRef
        | ReliefPointRef
        | TimingPointRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BorderPointRef",
                    "type": BorderPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointRef",
                    "type": TimingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
