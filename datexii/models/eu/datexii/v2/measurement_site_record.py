from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.computation_method_enum import (
    ComputationMethodEnum,
)
from datexii.models.eu.datexii.v2.direction_enum import DirectionEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_locations import GroupOfLocations
from datexii.models.eu.datexii.v2.measurement_site_record_index_measurement_specific_characteristics import (
    MeasurementSiteRecordIndexMeasurementSpecificCharacteristics,
)
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MeasurementSiteRecord:
    """
    An identifiable single measurement site entry/record in the Measurement
    Site table.

    :ivar measurement_site_record_version_time: The date/time that this
        version of the measurement site record was defined. The identity
        and version of the measurement site record are defined by the
        class stereotype implementation.
    :ivar computation_method: Method of computation which is used to
        compute the measured value(s) at the measurement site.
    :ivar measurement_equipment_reference: The reference given to the
        measurement equipment at the site.
    :ivar measurement_equipment_type_used: The type of equipment used to
        gather the raw information from which the data values are
        determined, e.g. 'loop', 'ANPR' (automatic number plate
        recognition) or 'urban traffic management system' (such as
        SCOOT).
    :ivar measurement_site_name: Name of a measurement site.
    :ivar measurement_site_number_of_lanes: The number of lanes over
        which the measured value is determined.
    :ivar measurement_site_identification: Identification of a
        measurement site used by the supplier or consumer systems.
    :ivar measurement_side: Side of the road on which measurements are
        acquired, corresponding to the direction of the road.
    :ivar measurement_specific_characteristics: Composition to the
        indexed measurement specific characteristics associated with the
        measurement site. The index uniquely associates the measurement
        characteristics with the corresponding indexed measurement
        values for the measurement site.
    :ivar measurement_site_location:
    :ivar measurement_site_record_extension:
    :ivar id:
    :ivar version:
    """

    measurement_site_record_version_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "measurementSiteRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    computation_method: None | ComputationMethodEnum = field(
        default=None,
        metadata={
            "name": "computationMethod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_equipment_reference: None | str = field(
        default=None,
        metadata={
            "name": "measurementEquipmentReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    measurement_equipment_type_used: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "measurementEquipmentTypeUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_site_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "measurementSiteName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_site_number_of_lanes: None | int = field(
        default=None,
        metadata={
            "name": "measurementSiteNumberOfLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_site_identification: None | str = field(
        default=None,
        metadata={
            "name": "measurementSiteIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    measurement_side: None | DirectionEnum = field(
        default=None,
        metadata={
            "name": "measurementSide",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_specific_characteristics: list[
        MeasurementSiteRecordIndexMeasurementSpecificCharacteristics
    ] = field(
        default_factory=list,
        metadata={
            "name": "measurementSpecificCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_site_location: None | GroupOfLocations = field(
        default=None,
        metadata={
            "name": "measurementSiteLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    measurement_site_record_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "measurementSiteRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
