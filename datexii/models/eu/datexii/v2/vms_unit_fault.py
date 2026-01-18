from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.fault import Fault
from datexii.models.eu.datexii.v2.vms_fault_enum import VmsFaultEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsUnitFault(Fault):
    """
    Details of the fault which is being reported for the specified variable
    message sign control unit.

    :ivar vms_unit_fault: The type of fault which is being reported for
        the VMS unit.
    :ivar vms_unit_fault_extension:
    """

    vms_unit_fault: VmsFaultEnum | None = field(
        default=None,
        metadata={
            "name": "vmsUnitFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    vms_unit_fault_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "vmsUnitFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
