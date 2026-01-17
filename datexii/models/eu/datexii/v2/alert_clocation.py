from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AlertCLocation:
    """
    Identification of a specific point, linear or area location in an
    ALERT-C location table.

    :ivar alert_clocation_name: Name of ALERT-C location.
    :ivar specific_location: Unique code within the ALERT-C location
        table which identifies the specific point, linear or area
        location.
    :ivar alert_clocation_extension:
    """

    alert_clocation_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "alertCLocationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    specific_location: Optional[int] = field(
        default=None,
        metadata={
            "name": "specificLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    alert_clocation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
