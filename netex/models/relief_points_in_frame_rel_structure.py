from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .garage_point import GaragePoint
from .parking_point import ParkingPoint
from .relief_point import ReliefPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "reliefPointsInFrame_RelStructure"

    relief_point_or_parking_point: Sequence[
        ParkingPoint | GaragePoint | ReliefPoint
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingPoint",
                    "type": ParkingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePoint",
                    "type": GaragePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPoint",
                    "type": ReliefPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
