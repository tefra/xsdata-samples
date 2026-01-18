from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class TemperatureValue(DataValue):
    """
    A measured or calculated value of temperature.

    :ivar temperature: A value of temperature expressed in degrees
        Celsius.
    :ivar temperature_value_extension:
    """

    temperature: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    temperature_value_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "temperatureValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
