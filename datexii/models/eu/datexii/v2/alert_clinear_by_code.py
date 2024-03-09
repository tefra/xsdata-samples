from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.alert_cdirection import AlertCDirection
from datexii.models.eu.datexii.v2.alert_clinear import AlertCLinear
from datexii.models.eu.datexii.v2.alert_clocation import AlertCLocation
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AlertCLinearByCode(AlertCLinear):
    """
    A linear section along a road defined by reference to a linear section in a
    pre-defined ALERT-C location table.

    :ivar alert_cdirection:
    :ivar location_code_for_linear_location: Linear location defined by
        a specific Alert-C location.
    :ivar alert_clinear_by_code_extension:
    """

    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    location_code_for_linear_location: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "locationCodeForLinearLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    alert_clinear_by_code_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLinearByCodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
