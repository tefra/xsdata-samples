from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PercentageValue(DataValue):
    """
    A measured or calculated value expressed as a percentage.

    :ivar percentage: A value expressed as a percentage.
    :ivar percentage_value_extension:
    """

    percentage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    percentage_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "percentageValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
