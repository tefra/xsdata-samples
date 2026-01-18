from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.fault import Fault
from datexii.models.eu.datexii.v2.vms_fault_enum import VmsFaultEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsFault(Fault):
    """
    Details of the fault which is being reported for the specified variable
    message sign panel.

    :ivar vms_fault: The type of fault which is being reported for the
        specified variable message sign panel.
    :ivar vms_fault_extension:
    """

    vms_fault: VmsFaultEnum | None = field(
        default=None,
        metadata={
            "name": "vmsFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    vms_fault_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "vmsFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
