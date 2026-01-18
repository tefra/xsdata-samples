from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.alert_clocation import AlertCLocation
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AlertCArea:
    """
    An area defined by reference to a predefined ALERT-C location table.

    :ivar alert_clocation_country_code: EBU country code.
    :ivar alert_clocation_table_number: Number allocated to an ALERT-C
        table in a country. Ref. EN ISO 14819-3 for the allocation of a
        location table number.
    :ivar alert_clocation_table_version: Version number associated with
        an ALERT-C table reference.
    :ivar area_location: Area location defined by a specific Alert-C
        location.
    :ivar alert_carea_extension:
    """

    alert_clocation_country_code: str | None = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_number: str | None = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_version: str | None = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    area_location: AlertCLocation | None = field(
        default=None,
        metadata={
            "name": "areaLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    alert_carea_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "alertCAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
