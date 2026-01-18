from dataclasses import dataclass, field
from typing import Optional

from xcbl.models.planning_schedule_response import (
    LocationGroupedPlanningDetail,
    MaterialGroupedPlanningDetail,
    PlanningScheduleHeader,
    PlanningScheduleSummary,
)


@dataclass(kw_only=True)
class ListOfLocationGroupedPlanningDetail:
    location_grouped_planning_detail: list[LocationGroupedPlanningDetail] = (
        field(
            default_factory=list,
            metadata={
                "name": "LocationGroupedPlanningDetail",
                "type": "Element",
                "min_occurs": 1,
            },
        )
    )


@dataclass(kw_only=True)
class ListOfMaterialGroupedPlanningDetail:
    material_grouped_planning_detail: list[MaterialGroupedPlanningDetail] = (
        field(
            default_factory=list,
            metadata={
                "name": "MaterialGroupedPlanningDetail",
                "type": "Element",
                "min_occurs": 1,
            },
        )
    )


@dataclass(kw_only=True)
class PlanningSchedule:
    planning_schedule_header: PlanningScheduleHeader = field(
        metadata={
            "name": "PlanningScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_grouped_planning_detail: ListOfLocationGroupedPlanningDetail | None = field(
        default=None,
        metadata={
            "name": "ListOfLocationGroupedPlanningDetail",
            "type": "Element",
        },
    )
    list_of_material_grouped_planning_detail: ListOfMaterialGroupedPlanningDetail | None = field(
        default=None,
        metadata={
            "name": "ListOfMaterialGroupedPlanningDetail",
            "type": "Element",
        },
    )
    planning_schedule_summary: PlanningScheduleSummary | None = field(
        default=None,
        metadata={
            "name": "PlanningScheduleSummary",
            "type": "Element",
        },
    )
