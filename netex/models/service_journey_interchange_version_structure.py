from __future__ import annotations

from dataclasses import dataclass, field

from .interchange_version_structure import InterchangeVersionStructure
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .service_journey_pattern_interchange_ref import (
    ServiceJourneyPatternInterchangeRef,
)
from .vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyInterchangeVersionStructure(InterchangeVersionStructure):
    class Meta:
        name = "ServiceJourneyInterchange_VersionStructure"

    from_point_ref: ScheduledStopPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_visit_number: int | None = field(
        default=None,
        metadata={
            "name": "FromVisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_point_ref: ScheduledStopPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_visit_number: int | None = field(
        default=None,
        metadata={
            "name": "ToVisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_journey_ref: VehicleJourneyRefStructure | None = field(
        default=None,
        metadata={
            "name": "FromJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to_journey_ref: VehicleJourneyRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    service_journey_pattern_interchange_ref: (
        ServiceJourneyPatternInterchangeRef | None
    ) = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
