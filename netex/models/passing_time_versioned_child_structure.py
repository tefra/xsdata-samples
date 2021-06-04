from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.dated_special_service_ref import DatedSpecialServiceRef
from netex.models.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from netex.models.dead_run_ref import DeadRunRef
from netex.models.fare_point_in_pattern_ref import FarePointInPatternRef
from netex.models.journey_ref import JourneyRef
from netex.models.point_in_journey_pattern_ref import PointInJourneyPatternRef
from netex.models.service_journey_ref import ServiceJourneyRef
from netex.models.special_service_ref import SpecialServiceRef
from netex.models.stop_point_in_journey_pattern_ref import StopPointInJourneyPatternRef
from netex.models.template_service_journey_ref import TemplateServiceJourneyRef
from netex.models.timing_point_in_journey_pattern_ref import TimingPointInJourneyPatternRef
from netex.models.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassingTimeVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "PassingTime_VersionedChildStructure"

    dated_vehicle_journey_ref: List[DatedVehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    dated_special_service_ref: List[DatedSpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    special_service_ref: List[SpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "SpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    template_service_journey_ref: List[TemplateServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_journey_ref: List[ServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    dead_run_ref: List[DeadRunRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    vehicle_journey_ref: List[VehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    journey_ref: Optional[JourneyRef] = field(
        default=None,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alight_and_reboard: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlightAndReboard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_point_in_pattern_ref: List[FarePointInPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "FarePointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    stop_point_in_journey_pattern_ref: List[StopPointInJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    timing_point_in_journey_pattern_ref: List[TimingPointInJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "TimingPointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    point_in_journey_pattern_ref: Optional[PointInJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "PointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
