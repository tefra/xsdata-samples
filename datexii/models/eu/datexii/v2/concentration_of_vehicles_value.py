from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ConcentrationOfVehiclesValue(DataValue):
    """
    A measured or calculated value of the concentration of vehicles on a unit
    stretch of road in a given direction.

    :ivar concentration_of_vehicles: A value of traffic density
        expressed in the number of vehicles per kilometre of road.
    :ivar concentration_of_vehicles_value_extension:
    """

    concentration_of_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "concentrationOfVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    concentration_of_vehicles_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "concentrationOfVehiclesValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
