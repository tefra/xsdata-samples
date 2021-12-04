from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .dated_service_journey import DatedServiceJourney
from .dated_vehicle_journey import DatedVehicleJourney
from .dead_run import DeadRun
from .normal_dated_vehicle_journey import NormalDatedVehicleJourney
from .service_journey import ServiceJourney
from .special_service import SpecialService
from .template_service_journey import TemplateServiceJourney
from .vehicle_journey import VehicleJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeysInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourney",
                    "type": VehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedVehicleJourney",
                    "type": DatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NormalDatedVehicleJourney",
                    "type": NormalDatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourney",
                    "type": ServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedServiceJourney",
                    "type": DatedServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRun",
                    "type": DeadRun,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialService",
                    "type": SpecialService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourney",
                    "type": TemplateServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
