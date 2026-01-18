from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.parking_usage_scenario import (
    ParkingUsageScenario,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class ParkingSiteScenarioIndexParkingUsageScenario:
    class Meta:
        name = "_ParkingSiteScenarioIndexParkingUsageScenario"

    parking_usage_scenario: ParkingUsageScenario = field(
        metadata={
            "name": "parkingUsageScenario",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    scenario_index: int = field(
        metadata={
            "name": "scenarioIndex",
            "type": "Attribute",
            "required": True,
        }
    )
