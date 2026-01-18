from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.delay_band_enum import DelayBandEnum
from datexii.models.eu.datexii.v2.delays_type_enum import DelaysTypeEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Delays:
    """
    The details of the delays being caused by the situation element defined
    in the situation record.

    It is recommended to only use one of the optional attributes to avoid
    confusion.

    :ivar delay_band: The time band within which the additional travel
        time due to adverse travel conditions of any kind falls, when
        compared to "normal conditions".
    :ivar delays_type: Coarse classification of the delay.
    :ivar delay_time_value: The value of the additional travel time due
        to adverse travel conditions of any kind, when compared to
        "normal conditions", given in seconds.
    :ivar delays_extension:
    """

    delay_band: None | DelayBandEnum = field(
        default=None,
        metadata={
            "name": "delayBand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    delays_type: None | DelaysTypeEnum = field(
        default=None,
        metadata={
            "name": "delaysType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    delay_time_value: None | float = field(
        default=None,
        metadata={
            "name": "delayTimeValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    delays_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "delaysExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
