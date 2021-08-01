from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.charging_station_usage_type_enum import ChargingStationUsageTypeEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ElectricCharging:
    """Additional information for the equipment 'electricChargingStation'.

    This component refers to the number of charging stations specified
    in the attribute 'numberOfEquipmentOrServiceFacilities'.

    :ivar charging_station_usage_type: Usage type of the electric
        charging station(s).
    :ivar charging_station_model_type: Model type of the electric
        charging station(s). Brand or company information can be
        specified in 'ParkingEquipmentOrServiceFacility'. For more than
        one type of model, use several instances of
        'ParkingEquipmentOrServiceFacility'.
    :ivar maximum_current: The maximum current of the electric charging
        station(s) (in Ampere).
    :ivar voltage: Available Voltage(s) of the electric charging
        station(s).
    :ivar charging_station_connector_type: Connector type(s) for the
        electric charging station(s).
    :ivar number_of_charging_points: Number of vehicles or devices,
        which can be charged simultaneously (sum over all electric
        charing stations specified with the 'numberOf...' attribute). If
        omitted, 1 charging point per station is assumed.
    :ivar electric_charging_extension:
    """
    charging_station_usage_type: List[ChargingStationUsageTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "chargingStationUsageType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    charging_station_model_type: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "chargingStationModelType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    maximum_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumCurrent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    voltage: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charging_station_connector_type: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "chargingStationConnectorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    number_of_charging_points: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfChargingPoints",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    electric_charging_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "electricChargingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
