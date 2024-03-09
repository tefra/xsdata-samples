from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_unit_of_measure import TypeUnitOfMeasure

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Dimension(TypeUnitOfMeasure):
    """
    Information related to Length,Height,Width of a baggage.

    Parameters
    ----------
    type_value
        Type denotes Length,Height,Width of a baggage.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
