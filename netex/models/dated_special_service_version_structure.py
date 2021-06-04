from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.dated_calls_rel_structure import DatedCallsRelStructure
from netex.models.dated_special_service_ref import DatedSpecialServiceRef
from netex.models.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from netex.models.dead_run_ref import DeadRunRef
from netex.models.driver_ref import DriverRef
from netex.models.external_object_ref_structure import ExternalObjectRefStructure
from netex.models.journey_pattern_ref_structure import JourneyPatternRefStructure
from netex.models.journey_ref import JourneyRef
from netex.models.operating_day_ref import OperatingDayRef
from netex.models.service_journey_ref import ServiceJourneyRef
from netex.models.special_service_ref import SpecialServiceRef
from netex.models.special_service_version_structure import SpecialServiceVersionStructure
from netex.models.target_passing_times_rel_structure import TargetPassingTimesRelStructure
from netex.models.template_service_journey_ref import TemplateServiceJourneyRef
from netex.models.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedSpecialServiceVersionStructure(SpecialServiceVersionStructure):
    class Meta:
        name = "DatedSpecialService_VersionStructure"

    dated_vehicle_journey_ref: List[DatedVehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    dated_special_service_ref: List[DatedSpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    special_service_ref: List[SpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "SpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    template_service_journey_ref: List[TemplateServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    service_journey_ref: List[ServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    dead_run_ref: List[DeadRunRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    vehicle_journey_ref: List[VehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
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
    operating_day_ref: Optional[OperatingDayRef] = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    external_dated_vehicle_journey_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalDatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_journey_pattern_ref: Optional[JourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "DatedJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_ref: Optional[DriverRef] = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_passing_times: Optional[TargetPassingTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "datedPassingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_calls: Optional[DatedCallsRelStructure] = field(
        default=None,
        metadata={
            "name": "datedCalls",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
