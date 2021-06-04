from dataclasses import dataclass, field
from typing import List
from netex.models.dated_special_service_ref import DatedSpecialServiceRef
from netex.models.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from netex.models.dead_run_ref import DeadRunRef
from netex.models.journey_designator import JourneyDesignator
from netex.models.journey_ref import JourneyRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.service_designator import ServiceDesignator
from netex.models.service_journey_ref import ServiceJourneyRef
from netex.models.special_service_ref import SpecialServiceRef
from netex.models.template_service_journey_ref import TemplateServiceJourneyRef
from netex.models.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "journeyRefs_RelStructure"

    dated_vehicle_journey_ref: List[DatedVehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_special_service_ref: List[DatedSpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    special_service_ref: List[SpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "SpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    template_service_journey_ref: List[TemplateServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_ref: List[ServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_ref: List[DeadRunRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journey_ref: List[VehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_ref: List[JourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_designator: List[JourneyDesignator] = field(
        default_factory=list,
        metadata={
            "name": "JourneyDesignator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_designator: List[ServiceDesignator] = field(
        default_factory=list,
        metadata={
            "name": "ServiceDesignator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
