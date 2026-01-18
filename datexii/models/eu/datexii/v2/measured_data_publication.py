from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.header_information import HeaderInformation
from datexii.models.eu.datexii.v2.measurement_site_table_versioned_reference import (
    MeasurementSiteTableVersionedReference,
)
from datexii.models.eu.datexii.v2.payload_publication import PayloadPublication
from datexii.models.eu.datexii.v2.site_measurements import SiteMeasurements

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MeasuredDataPublication(PayloadPublication):
    """
    A publication containing one or more measurement data sets, each set
    being measured at a single measurement site.

    :ivar measurement_site_table_reference: A reference to a versioned
        Measurement Site table.
    :ivar header_information:
    :ivar site_measurements:
    :ivar measured_data_publication_extension:
    """

    measurement_site_table_reference: MeasurementSiteTableVersionedReference | None = field(
        default=None,
        metadata={
            "name": "measurementSiteTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    header_information: HeaderInformation | None = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    site_measurements: list[SiteMeasurements] = field(
        default_factory=list,
        metadata={
            "name": "siteMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    measured_data_publication_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "measuredDataPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
