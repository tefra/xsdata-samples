from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .dated_service_journey import DatedServiceJourney
from .dated_vehicle_journey import DatedVehicleJourney
from .dead_run import DeadRun
from .normal_dated_vehicle_journey import NormalDatedVehicleJourney
from .service_journey_1 import ServiceJourney1
from .special_service import SpecialService
from .template_service_journey import TemplateServiceJourney
from .vehicle_journey_1 import VehicleJourney1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeysInFrame_RelStructure"

    vehicle_journey: List[VehicleJourney1] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_vehicle_journey: List[DatedVehicleJourney] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    normal_dated_vehicle_journey: List[NormalDatedVehicleJourney] = field(
        default_factory=list,
        metadata={
            "name": "NormalDatedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey: List[ServiceJourney1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_service_journey: List[DatedServiceJourney] = field(
        default_factory=list,
        metadata={
            "name": "DatedServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run: List[DeadRun] = field(
        default_factory=list,
        metadata={
            "name": "DeadRun",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    special_service: List[SpecialService] = field(
        default_factory=list,
        metadata={
            "name": "SpecialService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    template_service_journey: List[TemplateServiceJourney] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
