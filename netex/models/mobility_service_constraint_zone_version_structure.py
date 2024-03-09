from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from .car_pooling_service_ref import CarPoolingServiceRef
from .chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from .online_service_ref import OnlineServiceRef
from .taxi_service_ref import TaxiServiceRef
from .transport_zone_use_enumeration import TransportZoneUseEnumeration
from .vehicle_rental_service_ref import VehicleRentalServiceRef
from .vehicle_sharing_service_ref import VehicleSharingServiceRef
from .vehicle_type_zone_restrictions_rel_structure import (
    VehicleTypeZoneRestrictionsRelStructure,
)
from .zone_rule_applicability_enumeration import (
    ZoneRuleApplicabilityEnumeration,
)
from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityServiceConstraintZoneVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "MobilityServiceConstraintZone_VersionStructure"

    rule_applicability: Optional[ZoneRuleApplicabilityEnumeration] = field(
        default=None,
        metadata={
            "name": "RuleApplicability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    zone_use: Optional[TransportZoneUseEnumeration] = field(
        default=None,
        metadata={
            "name": "ZoneUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_speed: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumSpeed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref: Optional[
        Union[
            OnlineServiceRef,
            VehicleRentalServiceRef,
            VehicleSharingServiceRef,
            ChauffeuredVehicleServiceRef,
            TaxiServiceRef,
            CarPoolingServiceRef,
        ]
    ] = field(
        default=None,
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
    vehicle_restrictions: Optional[VehicleTypeZoneRestrictionsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "vehicleRestrictions",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
