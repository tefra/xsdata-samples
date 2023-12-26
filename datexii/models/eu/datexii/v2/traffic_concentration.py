from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.concentration_of_vehicles_value import (
    ConcentrationOfVehiclesValue,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.percentage_value import PercentageValue
from datexii.models.eu.datexii.v2.traffic_data import TrafficData

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TrafficConcentration(TrafficData):
    """
    Averaged measurements or calculations of traffic concentration.

    :ivar concentration: An averaged measurement or calculation of the
        concentration of vehicles at the specified measurement site.
    :ivar occupancy: An averaged measurement or calculation of the
        percentage of time that a section of road at the specified
        measurement site is occupied by vehicles.
    :ivar traffic_concentration_extension:
    """

    concentration: Optional[ConcentrationOfVehiclesValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    occupancy: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    traffic_concentration_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficConcentrationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
