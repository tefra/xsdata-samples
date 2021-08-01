from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AxleFlowValue(DataValue):
    """
    A measured or calculated value of the flow rate of vehicle axles.

    :ivar axle_flow_rate: A value of the flow rate of vehicle axles
        expressed in axles per hour.
    :ivar axle_flow_value_extension:
    """
    axle_flow_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "axleFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    axle_flow_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "axleFlowValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
