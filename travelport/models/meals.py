from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_meal_service import TypeMealService

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Meals:
    """
    Available Meal Service.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: None | TypeMealService = field(
        default=None,
        metadata={
            "required": True,
        }
    )
