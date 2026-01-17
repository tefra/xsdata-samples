from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.lane_enum import LaneEnum
from datexii.models.eu.datexii.v2.measured_or_derived_data_type_enum import (
    MeasuredOrDerivedDataTypeEnum,
)
from datexii.models.eu.datexii.v2.vehicle_characteristics import (
    VehicleCharacteristics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MeasurementSpecificCharacteristics:
    """
    Characteristics which are specific to an individual measurement type
    (specified in a known order) at the given measurement site.

    :ivar accuracy: The extent to which the value is expected to be free
        from error, measured as a percentage of the data value. 100%
        means fully accurate.
    :ivar period: The time elapsed between the beginning and the end of
        the sampling or measurement period. This item may differ from
        the unit attribute; e.g. an hourly flow can be estimated from a
        5-minute measurement period.
    :ivar smoothing_factor: Coefficient required when a moving average
        is computed to give specific weights to the former average and
        the new data. A typical formula is, F being the smoothing
        factor: New average = (old average) F + (new data) (1 - F).
    :ivar specific_lane: The lane to which the specific measurement at
        the measurement site relates. This overrides any lane specified
        for the measurement site as a whole.
    :ivar specific_measurement_value_type: The type of this specific
        measurement at the measurement site.
    :ivar specific_vehicle_characteristics:
    :ivar measurement_specific_characteristics_extension:
    """

    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    period: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    smoothing_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "smoothingFactor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    specific_lane: Optional[LaneEnum] = field(
        default=None,
        metadata={
            "name": "specificLane",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    specific_measurement_value_type: Optional[
        MeasuredOrDerivedDataTypeEnum
    ] = field(
        default=None,
        metadata={
            "name": "specificMeasurementValueType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    specific_vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "specificVehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_specific_characteristics_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "measurementSpecificCharacteristicsExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
