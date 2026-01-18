from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.header_information import HeaderInformation
from datexii.models.eu.datexii.v2.measurement_site_table import (
    MeasurementSiteTable,
)
from datexii.models.eu.datexii.v2.payload_publication import PayloadPublication

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MeasurementSiteTablePublication(PayloadPublication):
    """
    A publication containing one or more Measurment Site Tables.
    """

    header_information: HeaderInformation | None = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    measurement_site_table: list[MeasurementSiteTable] = field(
        default_factory=list,
        metadata={
            "name": "measurementSiteTable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    measurement_site_table_publication_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "measurementSiteTablePublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
