from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class SpeedValue(DataValue):
    """
    A measured or calculated value of speed.

    :ivar speed: A value of speed expressed in kilometres per hour.
    :ivar speed_value_extension:
    """

    speed: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    speed_value_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "speedValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
