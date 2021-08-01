from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.parking_usage_scenario import ParkingUsageScenario

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingSiteScenarioIndexParkingUsageScenario:
    class Meta:
        name = "_ParkingSiteScenarioIndexParkingUsageScenario"

    parking_usage_scenario: Optional[ParkingUsageScenario] = field(
        default=None,
        metadata={
            "name": "parkingUsageScenario",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    scenario_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "scenarioIndex",
            "type": "Attribute",
            "required": True,
        }
    )
