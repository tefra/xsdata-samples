from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.axle_flow_value import AxleFlowValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.pcu_flow_value import PcuFlowValue
from datexii.models.eu.datexii.v2.percentage_value import PercentageValue
from datexii.models.eu.datexii.v2.traffic_data import TrafficData
from datexii.models.eu.datexii.v2.vehicle_flow_value import VehicleFlowValue

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TrafficFlow(TrafficData):
    """
    Averaged measurements or calculations of traffic flow rates.

    :ivar axle_flow: An averaged measurement or calculation of flow rate
        defined in terms of the number of vehicle axles passing the
        specified measurement site.
    :ivar pcu_flow: An averaged measurement or calculation of flow rate
        defined in terms of the number of passenger car units passing
        the specified measurement site.
    :ivar percentage_long_vehicles: An averaged measurement or
        calculation of the percentage of long vehicles contained in the
        traffic flow at the specified measurement site.
    :ivar vehicle_flow: An averaged measurement of flow rate defined in
        terms of the number of vehicles passing the specified
        measurement site.
    :ivar traffic_flow_extension:
    """

    axle_flow: Optional[AxleFlowValue] = field(
        default=None,
        metadata={
            "name": "axleFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pcu_flow: Optional[PcuFlowValue] = field(
        default=None,
        metadata={
            "name": "pcuFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    percentage_long_vehicles: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "name": "percentageLongVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_flow: Optional[VehicleFlowValue] = field(
        default=None,
        metadata={
            "name": "vehicleFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    traffic_flow_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficFlowExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
