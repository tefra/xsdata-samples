from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.occupancy_change_value import (
    OccupancyChangeValue,
)
from datexii.models.eu.datexii.v2.vehicle_characteristics import (
    VehicleCharacteristics,
)
from datexii.models.eu.datexii.v2.vehicle_count_value import VehicleCountValue

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VehicleCountWithinInterval:
    """
    Gives incoming and/or outgoing vehicles and/or change of occupied
    spaces within a given interval.

    The interval is given in positive or negative seconds related to
    'measurementOrCalculationTime' or 'measurementDefaultTime'.

    :ivar measurement_or_calcualtion_time: Point in time at which this
        specific value or set of values has been measured or calculated.
        It may also be a future time at which a data value is predicted.
    :ivar measurement_interval: Interval for which the data applies.
        Usually, this value should be negative. Example: - 300 = last 5
        minutes up to 'measurementOrCalculationTime' or
        'measurementTimeDefault'. Use a positive value only for
        predictions. Example: 600 = next ten minutes.
    :ivar number_of_incoming_vehicles: Number of vehicles of specified
        type that entered the specified parking within the given
        interval.
    :ivar number_of_outgoing_vehicles: Number of vehicles of specified
        type that left the specified parking within the given interval.
    :ivar change_of_occupied_spaces: The change in the number of
        occupied spaces for specified vehicles within the given
        interval. Negative values mean less occupied spaces than at the
        beginning of the interval.
    :ivar counted_vehicles:
    :ivar vehicle_count_within_interval_extension:
    """

    measurement_or_calcualtion_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "measurementOrCalcualtionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_interval: float | None = field(
        default=None,
        metadata={
            "name": "measurementInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    number_of_incoming_vehicles: VehicleCountValue | None = field(
        default=None,
        metadata={
            "name": "numberOfIncomingVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    number_of_outgoing_vehicles: VehicleCountValue | None = field(
        default=None,
        metadata={
            "name": "numberOfOutgoingVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    change_of_occupied_spaces: OccupancyChangeValue | None = field(
        default=None,
        metadata={
            "name": "changeOfOccupiedSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    counted_vehicles: VehicleCharacteristics | None = field(
        default=None,
        metadata={
            "name": "countedVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_count_within_interval_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "vehicleCountWithinIntervalExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
