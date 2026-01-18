from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vehicle_characteristics import (
    VehicleCharacteristics,
)
from datexii.models.eu.datexii.v2.vehicle_flow_value import VehicleFlowValue

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VehicleRate:
    """
    Gives information about fill and exit rates OR vehicle flow rate
    (without direction).

    If the time stamp is omitted, 'measurementTimeDefault' is used.

    :ivar measurement_or_calculation_time: Point in time at which this
        specific value or set of values has been measured or calculated.
        It may also be a future time at which a data value is predicted.
    :ivar fill_rate: The rate at which vehicles are entering the
        parking.
    :ivar exit_rate: The rate at which vehicles are exiting the parking.
    :ivar vehicle_flow_rate: A value of vehicle flow rate expressed in
        vehicles per hour.
    :ivar measured_vehicles:
    :ivar vehicle_rate_extension:
    """

    measurement_or_calculation_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "measurementOrCalculationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    fill_rate: VehicleFlowValue | None = field(
        default=None,
        metadata={
            "name": "fillRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    exit_rate: VehicleFlowValue | None = field(
        default=None,
        metadata={
            "name": "exitRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_flow_rate: VehicleFlowValue | None = field(
        default=None,
        metadata={
            "name": "vehicleFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measured_vehicles: VehicleCharacteristics | None = field(
        default=None,
        metadata={
            "name": "measuredVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_rate_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "vehicleRateExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
