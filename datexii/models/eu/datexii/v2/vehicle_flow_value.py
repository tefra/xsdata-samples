from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VehicleFlowValue(DataValue):
    """
    A measured or calculated value of the flow rate of vehicles.

    :ivar vehicle_flow_rate: A value of vehicle flow rate expressed in
        vehicles per hour.
    :ivar vehicle_flow_value_extension:
    """

    vehicle_flow_rate: int | None = field(
        default=None,
        metadata={
            "name": "vehicleFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    vehicle_flow_value_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "vehicleFlowValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
