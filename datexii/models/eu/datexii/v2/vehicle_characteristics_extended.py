from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.fuel_type2_enum import FuelType2Enum
from datexii.models.eu.datexii.v2.load_type2_enum import LoadType2Enum
from datexii.models.eu.datexii.v2.vehicle_type2_enum import VehicleType2Enum
from datexii.models.eu.datexii.v2.vehicle_usage2_enum import VehicleUsage2Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VehicleCharacteristicsExtended:
    """
    Extension point for 'VehicleCharacteristics' to support additional attributes
    and literals like additional fuel types, load types etc.

    :ivar emission_classification: The valid list of entries for this
        attribute has to be specified between the communication-
        partners. Usually it's some country specific classification code
        for emissions, which must be scored by vehicles to be valid.
    :ivar operation_free_of_emission: Only vehicles that do not produce
        emissions (e.g. electric driven). Hybrid driven cars are
        allowed, when they switch to emission free mode within the
        considered situation.
    :ivar load_type2: Loads currently not supported in 'LoadTypeEnum'.
    :ivar vehicle_type2: Vehicle types currently not supported in
        'VehicleTypeEnum'.
    :ivar fuel_type2: Fuel types currently not supported in
        'FuelTypeEnum'.
    :ivar vehicle_usage2: Usage types currently not supported in
        'VehicleUsageTypeEnum'.
    """

    emission_classification: List[str] = field(
        default_factory=list,
        metadata={
            "name": "emissionClassification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    operation_free_of_emission: Optional[bool] = field(
        default=None,
        metadata={
            "name": "operationFreeOfEmission",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    load_type2: Optional[LoadType2Enum] = field(
        default=None,
        metadata={
            "name": "loadType2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_type2: Optional[VehicleType2Enum] = field(
        default=None,
        metadata={
            "name": "vehicleType2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    fuel_type2: Optional[FuelType2Enum] = field(
        default=None,
        metadata={
            "name": "fuelType2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_usage2: Optional[VehicleUsage2Enum] = field(
        default=None,
        metadata={
            "name": "vehicleUsage2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
