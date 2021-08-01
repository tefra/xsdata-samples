from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.measurement_site_record_versioned_reference import MeasurementSiteRecordVersionedReference
from datexii.models.eu.datexii.v2.site_measurements_index_measured_value import SiteMeasurementsIndexMeasuredValue

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SiteMeasurements:
    """
    A  measurement data set derived from a specific measurement site.

    :ivar measurement_site_reference: A reference to a versioned
        measurement site record defined in a Measurement Site table.
    :ivar measurement_time_default: The time associated with the set of
        measurements. It may be the time of the beginning, the end or
        the middle of the measurement period.
    :ivar measured_value: Composition to the indexed measured value
        associated with the measurement site. The index uniquely
        associates the measurement value with the corresponding indexed
        measurement characteristics defined for the measurement site.
    :ivar site_measurements_extension:
    """
    measurement_site_reference: Optional[MeasurementSiteRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "measurementSiteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    measurement_time_default: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementTimeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    measured_value: List[SiteMeasurementsIndexMeasuredValue] = field(
        default_factory=list,
        metadata={
            "name": "measuredValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    site_measurements_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "siteMeasurementsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
