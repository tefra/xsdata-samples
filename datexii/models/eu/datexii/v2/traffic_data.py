from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.basic_data import BasicData
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vehicle_characteristics import (
    VehicleCharacteristics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class TrafficData(BasicData):
    """
    Measured or derived values relating to traffic or individual vehicle
    movements on a specific section or at a specific point on the road
    network.

    :ivar for_vehicles_with_characteristics_of: Used to define the
        vehicle characteristics to which the TrafficValue is applicable
        primarily in Elaborated Data Publications, but may also be used
        in Measured Data Publications to override vehicle
        characteristics defined for the measurement site.
    :ivar traffic_data_extension:
    """

    for_vehicles_with_characteristics_of: None | VehicleCharacteristics = (
        field(
            default=None,
            metadata={
                "name": "forVehiclesWithCharacteristicsOf",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    traffic_data_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "trafficDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
