from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AlertCPoint:
    """
    A single point on the road network defined by reference to a pre-defined
    ALERT-C location table and which has an associated direction of traffic flow.

    :ivar alert_clocation_country_code: EBU country code.
    :ivar alert_clocation_table_number: Number allocated to an ALERT-C
        table in a country. Ref. EN ISO 14819-3 for the allocation of a
        location table number.
    :ivar alert_clocation_table_version: Version number associated with
        an ALERT-C table reference.
    :ivar alert_cpoint_extension:
    """

    alert_clocation_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_cpoint_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
