from dataclasses import dataclass, field
from typing import Optional, Union
from .flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from .parking_area_refs_rel_structure import ParkingAreaRefsRelStructure
from .personal_mode_of_operation_ref import PersonalModeOfOperationRef
from .scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from .site_entrance_version_structure import SiteEntranceVersionStructure
from .vehicle_pooling_ref import VehiclePoolingRef
from .vehicle_rental_ref import VehicleRentalRef
from .vehicle_sharing_ref import VehicleSharingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingEntranceForVehiclesVersionStructure(SiteEntranceVersionStructure):
    class Meta:
        name = "ParkingEntranceForVehicles__VersionStructure"

    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref: Optional[
        Union[
            PersonalModeOfOperationRef,
            VehiclePoolingRef,
            VehicleSharingRef,
            VehicleRentalRef,
            FlexibleModeOfOperationRef,
            ScheduledModeOfOperationRef,
        ]
    ] = field(
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
    areas: Optional[ParkingAreaRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
