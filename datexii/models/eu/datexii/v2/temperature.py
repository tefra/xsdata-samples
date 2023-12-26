from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.temperature_value import TemperatureValue

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Temperature:
    """
    Details of atmospheric temperature.

    :ivar air_temperature: The air temperature measured in the shade
        between 1.5 and 2 metres above ground level.
    :ivar dew_point_temperature: The temperature to which the air would
        have to cool (at constant pressure and water vapour content) in
        order to reach saturation.
    :ivar maximum_temperature: The maximum temperature during the
        forecast or measurement period.
    :ivar minimum_temperature: The minimum temperature during the
        forecast or measurement period.
    :ivar temperature_extension:
    """

    air_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "airTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dew_point_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "dewPointTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    maximum_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "maximumTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    minimum_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "minimumTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    temperature_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "temperatureExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
