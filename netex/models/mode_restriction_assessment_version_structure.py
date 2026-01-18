from __future__ import annotations

from dataclasses import dataclass, field

from .data_managed_object_view_structure import DataManagedObjectViewStructure
from .flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from .personal_mode_of_operation_ref import PersonalModeOfOperationRef
from .scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from .transport_modes_rel_structure import TransportModesRelStructure
from .vehicle_pooling_ref import VehiclePoolingRef
from .vehicle_rental_ref import VehicleRentalRef
from .vehicle_sharing_ref import VehicleSharingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ModeRestrictionAssessmentVersionStructure(
    DataManagedObjectViewStructure
):
    class Meta:
        name = "ModeRestrictionAssessment_VersionStructure"

    exclude: bool | None = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_modes: TransportModesRelStructure | None = field(
        default=None,
        metadata={
            "name": "transportModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref: (
        PersonalModeOfOperationRef
        | VehiclePoolingRef
        | VehicleSharingRef
        | VehicleRentalRef
        | FlexibleModeOfOperationRef
        | ScheduledModeOfOperationRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperationRef",
                    "type": PersonalModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingRef",
                    "type": VehiclePoolingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingRef",
                    "type": VehicleSharingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalRef",
                    "type": VehicleRentalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleModeOfOperationRef",
                    "type": FlexibleModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledModeOfOperationRef",
                    "type": ScheduledModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    minimum_number_of_passengers: int | None = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfPassengers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
