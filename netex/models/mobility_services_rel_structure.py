from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .car_pooling_service import CarPoolingService
from .chauffeured_vehicle_service import ChauffeuredVehicleService
from .containment_aggregation_structure import ContainmentAggregationStructure
from .online_service import OnlineService
from .taxi_service import TaxiService
from .vehicle_rental_service import VehicleRentalService
from .vehicle_sharing_service import VehicleSharingService

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityServicesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "mobilityServices_RelStructure"

    mobility_service_or_common_vehicle_service_or_vehicle_pooling_service: Iterable[
        OnlineService
        | VehicleRentalService
        | VehicleSharingService
        | ChauffeuredVehicleService
        | CarPoolingService
        | TaxiService
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnlineService",
                    "type": OnlineService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalService",
                    "type": VehicleRentalService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingService",
                    "type": VehicleSharingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleService",
                    "type": ChauffeuredVehicleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingService",
                    "type": CarPoolingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiService",
                    "type": TaxiService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
