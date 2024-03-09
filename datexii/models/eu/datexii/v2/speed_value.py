from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SpeedValue(DataValue):
    """
    A measured or calculated value of speed.

    :ivar speed: A value of speed expressed in kilometres per hour.
    :ivar speed_value_extension:
    """

    speed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    speed_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "speedValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
