from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.fuel_type_enum import FuelTypeEnum
from datexii.models.eu.datexii.v2.gross_weight_characteristic import (
    GrossWeightCharacteristic,
)
from datexii.models.eu.datexii.v2.heaviest_axle_weight_characteristic import (
    HeaviestAxleWeightCharacteristic,
)
from datexii.models.eu.datexii.v2.height_characteristic import (
    HeightCharacteristic,
)
from datexii.models.eu.datexii.v2.length_characteristic import (
    LengthCharacteristic,
)
from datexii.models.eu.datexii.v2.load_type_enum import LoadTypeEnum
from datexii.models.eu.datexii.v2.number_of_axles_characteristic import (
    NumberOfAxlesCharacteristic,
)
from datexii.models.eu.datexii.v2.vehicle_characteristics_extension_type import (
    VehicleCharacteristicsExtensionType,
)
from datexii.models.eu.datexii.v2.vehicle_equipment_enum import (
    VehicleEquipmentEnum,
)
from datexii.models.eu.datexii.v2.vehicle_type_enum import VehicleTypeEnum
from datexii.models.eu.datexii.v2.vehicle_usage_enum import VehicleUsageEnum
from datexii.models.eu.datexii.v2.width_characteristic import (
    WidthCharacteristic,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VehicleCharacteristics:
    """
    The characteristics of a vehicle, e.g. lorry of gross weight greater
    than 30 tonnes.

    :ivar fuel_type: The type of fuel used by the vehicle.
    :ivar load_type: The type of load carried by the vehicle, especially
        in respect of hazardous loads.
    :ivar vehicle_equipment: The type of equipment in use or on board
        the vehicle.
    :ivar vehicle_type: Vehicle type.
    :ivar vehicle_usage: The type of usage of the vehicle (i.e. for what
        purpose is the vehicle being used).
    :ivar gross_weight_characteristic:
    :ivar height_characteristic:
    :ivar length_characteristic:
    :ivar width_characteristic:
    :ivar heaviest_axle_weight_characteristic:
    :ivar number_of_axles_characteristic:
    :ivar vehicle_characteristics_extension:
    """

    fuel_type: Optional[FuelTypeEnum] = field(
        default=None,
        metadata={
            "name": "fuelType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    load_type: Optional[LoadTypeEnum] = field(
        default=None,
        metadata={
            "name": "loadType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_equipment: Optional[VehicleEquipmentEnum] = field(
        default=None,
        metadata={
            "name": "vehicleEquipment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_type: list[VehicleTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "vehicleType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_usage: Optional[VehicleUsageEnum] = field(
        default=None,
        metadata={
            "name": "vehicleUsage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    gross_weight_characteristic: list[GrossWeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "grossWeightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        },
    )
    height_characteristic: list[HeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "heightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        },
    )
    length_characteristic: list[LengthCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "lengthCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        },
    )
    width_characteristic: list[WidthCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "widthCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        },
    )
    heaviest_axle_weight_characteristic: list[
        HeaviestAxleWeightCharacteristic
    ] = field(
        default_factory=list,
        metadata={
            "name": "heaviestAxleWeightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        },
    )
    number_of_axles_characteristic: list[NumberOfAxlesCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "numberOfAxlesCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        },
    )
    vehicle_characteristics_extension: Optional[
        VehicleCharacteristicsExtensionType
    ] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
