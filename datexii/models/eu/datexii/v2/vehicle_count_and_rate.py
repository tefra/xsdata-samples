from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.measurement_site_record_versioned_reference import (
    MeasurementSiteRecordVersionedReference,
)
from datexii.models.eu.datexii.v2.parking_access_reference import (
    ParkingAccessReference,
)
from datexii.models.eu.datexii.v2.vehicle_count_within_interval import (
    VehicleCountWithinInterval,
)
from datexii.models.eu.datexii.v2.vehicle_rate import VehicleRate

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VehicleCountAndRate:
    """
    Vehicle rates can be assigned to a parking site or to assigned parking
    spaces.

    Furthermore, they can reference to a measurement site or to an
    entrance/exit.

    :ivar measurement_site_reference: A reference to a versioned
        measurement site record defined in a Measurement Site table.
    :ivar measured_value_index: If a measurement site is specified, the
        index of the measured value can be specified here.
    :ivar dedicated_access: Specifies a reference to an access, object
        (i.e. an entrance, an exit or both). A Point location and
        further characteristics can be specified for those objects.
    :ivar measurement_time_default: The time associated with the set of
        measurements. It may be the time of the beginning, the end or
        the middle of the measurement period.
    :ivar last_calibration: Date of last calibration of the detection
        system in question.
    :ivar covering_petrol_station_area: Indication, if this detector
        also covers the area of a petrol station.
    :ivar vehicle_count_within_interval:
    :ivar vehicle_rate:
    :ivar vehicle_count_and_rate_extension:
    """

    measurement_site_reference: (
        MeasurementSiteRecordVersionedReference | None
    ) = field(
        default=None,
        metadata={
            "name": "measurementSiteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measured_value_index: int | None = field(
        default=None,
        metadata={
            "name": "measuredValueIndex",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dedicated_access: ParkingAccessReference | None = field(
        default=None,
        metadata={
            "name": "dedicatedAccess",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_time_default: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "measurementTimeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    last_calibration: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "lastCalibration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    covering_petrol_station_area: bool | None = field(
        default=None,
        metadata={
            "name": "coveringPetrolStationArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_count_within_interval: list[VehicleCountWithinInterval] = field(
        default_factory=list,
        metadata={
            "name": "vehicleCountWithinInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_rate: list[VehicleRate] = field(
        default_factory=list,
        metadata={
            "name": "vehicleRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_count_and_rate_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "vehicleCountAndRateExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
