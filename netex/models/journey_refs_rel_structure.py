from dataclasses import dataclass, field
from typing import List, Union
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .journey_designator import JourneyDesignator
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .service_designator import ServiceDesignator
from .service_journey_ref import ServiceJourneyRef
from .special_service_ref import SpecialServiceRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "journeyRefs_RelStructure"

    choice: List[Union[DatedVehicleJourneyRef, DatedSpecialServiceRef, SpecialServiceRef, TemplateServiceJourneyRef, ServiceJourneyRef, DeadRunRef, VehicleJourneyRef, JourneyDesignator, ServiceDesignator]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedVehicleJourneyRef",
                    "type": DatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyDesignator",
                    "type": JourneyDesignator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceDesignator",
                    "type": ServiceDesignator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
