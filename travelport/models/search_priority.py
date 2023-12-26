from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.criteria_type import CriteriaType

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class SearchPriority:
    """
    Override the search order for hotel availability request.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    criteria: list[SearchPriority.Criteria] = field(
        default_factory=list,
        metadata={
            "name": "Criteria",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 8,
        },
    )

    @dataclass
    class Criteria:
        """
        Parameters
        ----------
        order
            Criteria order for hotel search Highest Priority=1  Lowest
            Priority=7
        type_value
            Search type
        """

        order: None | int = field(
            default=None,
            metadata={
                "name": "Order",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1,
                "max_inclusive": 8,
            },
        )
        type_value: None | CriteriaType = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
                "required": True,
            },
        )
