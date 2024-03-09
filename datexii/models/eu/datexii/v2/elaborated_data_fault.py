from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.elaborated_data_fault_enum import (
    ElaboratedDataFaultEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.fault import Fault

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ElaboratedDataFault(Fault):
    """
    Details of a fault which is being reported for the related elaborated data.

    :ivar elaborated_data_fault: The type of fault which is being
        reported for the specified elaborated data.
    :ivar elaborated_data_fault_extension:
    """

    elaborated_data_fault: Optional[ElaboratedDataFaultEnum] = field(
        default=None,
        metadata={
            "name": "elaboratedDataFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    elaborated_data_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "elaboratedDataFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
