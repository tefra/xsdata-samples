from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.percentage_value import PercentageValue

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Humidity:
    """
    Details of atmospheric humidity.

    :ivar relative_humidity: The amount of water vapour in the air, as a
        percentage of the amount of water vapour in saturated air at the
        same temperature and at atmospheric pressure. The measurement is
        taken between 1.5 and 2 m above the ground and behind a
        meteorological screen.
    :ivar humidity_extension:
    """

    relative_humidity: PercentageValue | None = field(
        default=None,
        metadata={
            "name": "relativeHumidity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    humidity_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "humidityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
