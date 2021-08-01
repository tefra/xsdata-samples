from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TemperatureValue(DataValue):
    """
    A measured or calculated value of temperature.

    :ivar temperature: A value of temperature expressed in degrees
        Celsius.
    :ivar temperature_value_extension:
    """
    temperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    temperature_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "temperatureValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
