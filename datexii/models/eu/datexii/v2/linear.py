from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.alert_clinear import AlertCLinear
from datexii.models.eu.datexii.v2.linear_extension_type import (
    LinearExtensionType,
)
from datexii.models.eu.datexii.v2.linear_within_linear_element import (
    LinearWithinLinearElement,
)
from datexii.models.eu.datexii.v2.network_location import NetworkLocation
from datexii.models.eu.datexii.v2.tpeg_linear_location import (
    TpegLinearLocation,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Linear(NetworkLocation):
    """
    A linear section along a single road with optional directionality
    defined between two points on the same road.
    """

    tpeg_linear_location: TpegLinearLocation | None = field(
        default=None,
        metadata={
            "name": "tpegLinearLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    alert_clinear: AlertCLinear | None = field(
        default=None,
        metadata={
            "name": "alertCLinear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    linear_within_linear_element: LinearWithinLinearElement | None = field(
        default=None,
        metadata={
            "name": "linearWithinLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    linear_extension: LinearExtensionType | None = field(
        default=None,
        metadata={
            "name": "linearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
