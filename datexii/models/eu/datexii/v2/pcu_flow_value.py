from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PcuFlowValue(DataValue):
    """
    A measured or calculated value of the flow rate of passenger car units.

    :ivar pcu_flow_rate: A value of passenger car unit flow rate
        expressed in passenger car units per hour.
    :ivar pcu_flow_value_extension:
    """

    pcu_flow_rate: None | int = field(
        default=None,
        metadata={
            "name": "pcuFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    pcu_flow_value_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "pcuFlowValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
