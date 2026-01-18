from collections.abc import Iterable
from dataclasses import dataclass, field

from .car_pooling_service_ref import CarPoolingServiceRef
from .chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .online_service_ref import OnlineServiceRef
from .taxi_service_ref import TaxiServiceRef
from .vehicle_rental_service_ref import VehicleRentalServiceRef
from .vehicle_sharing_service_ref import VehicleSharingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityServiceRefsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "mobilityServiceRefs_RelStructure"

    mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref: Iterable[
        OnlineServiceRef
        | VehicleRentalServiceRef
        | VehicleSharingServiceRef
        | ChauffeuredVehicleServiceRef
        | TaxiServiceRef
        | CarPoolingServiceRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnlineServiceRef",
                    "type": OnlineServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
