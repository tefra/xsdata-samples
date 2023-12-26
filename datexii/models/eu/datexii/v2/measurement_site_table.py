from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.measurement_site_record import (
    MeasurementSiteRecord,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MeasurementSiteTable:
    """A Measurement Site Table comprising a number of sets of data, each
    describing the location from where a stream of measured data may be derived.

    Each location is known as a "measurement site" which can be a point,
    a linear road section or an area.

    :ivar measurement_site_table_identification: An alphanumeric
        identification for the measurement site table, possibly human
        readable.
    :ivar measurement_site_record:
    :ivar measurement_site_table_extension:
    :ivar id:
    :ivar version:
    """

    measurement_site_table_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    measurement_site_record: List[MeasurementSiteRecord] = field(
        default_factory=list,
        metadata={
            "name": "measurementSiteRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    measurement_site_table_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
