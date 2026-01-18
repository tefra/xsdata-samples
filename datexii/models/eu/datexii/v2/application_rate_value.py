from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ApplicationRateValue(DataValue):
    """
    A measured or calculated value of the application rate of a substance.

    :ivar application_rate: A value of the rate of application of a
        substance expressed in kilogrammes per square metre.
    :ivar application_rate_value_extension:
    """

    application_rate: float | None = field(
        default=None,
        metadata={
            "name": "applicationRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    application_rate_value_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "applicationRateValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
