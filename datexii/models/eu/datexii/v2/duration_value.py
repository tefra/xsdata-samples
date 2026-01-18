from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class DurationValue(DataValue):
    """
    A measured or calculated value of a period of time.

    :ivar duration: A period of time expressed in seconds.
    :ivar duration_value_extension:
    """

    duration: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    duration_value_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "durationValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
