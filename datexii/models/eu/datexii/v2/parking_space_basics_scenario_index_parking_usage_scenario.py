from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.parking_usage_scenario import (
    ParkingUsageScenario,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingSpaceBasicsScenarioIndexParkingUsageScenario:
    class Meta:
        name = "_ParkingSpaceBasicsScenarioIndexParkingUsageScenario"

    parking_usage_scenario: ParkingUsageScenario | None = field(
        default=None,
        metadata={
            "name": "parkingUsageScenario",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    scenario_index: int | None = field(
        default=None,
        metadata={
            "name": "scenarioIndex",
            "type": "Attribute",
            "required": True,
        },
    )
