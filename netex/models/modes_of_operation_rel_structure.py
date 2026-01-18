from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .alternative_mode_of_operation import AlternativeModeOfOperation
from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_operation import FlexibleOperation
from .personal_mode_of_operation import PersonalModeOfOperation
from .scheduled_operation import ScheduledOperation
from .vehicle_pooling import VehiclePooling
from .vehicle_rental import VehicleRental
from .vehicle_sharing import VehicleSharing

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModesOfOperationRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "modesOfOperationRelStructure"

    mode_of_operation_or_alternative_mode_of_operation_or_conventional_mode_of_operation: Iterable[
        PersonalModeOfOperation
        | AlternativeModeOfOperation
        | VehiclePooling
        | VehicleSharing
        | VehicleRental
        | FlexibleOperation
        | ScheduledOperation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperation",
                    "type": PersonalModeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AlternativeModeOfOperation",
                    "type": AlternativeModeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePooling",
                    "type": VehiclePooling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharing",
                    "type": VehicleSharing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRental",
                    "type": VehicleRental,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleOperation",
                    "type": FlexibleOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledOperation",
                    "type": ScheduledOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
