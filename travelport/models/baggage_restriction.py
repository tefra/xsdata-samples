from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.dimension import Dimension
from travelport.models.text_info import TextInfo
from travelport.models.type_unit_of_measure import TypeUnitOfMeasure

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BaggageRestriction:
    """
    Information related to  Baggage restriction rules .
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    dimension: list[Dimension] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    max_weight: list[TypeUnitOfMeasure] = field(
        default_factory=list,
        metadata={
            "name": "MaxWeight",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    text_info: list[TextInfo] = field(
        default_factory=list,
        metadata={
            "name": "TextInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
