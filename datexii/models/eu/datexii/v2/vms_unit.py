from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vms_setting import VmsSetting
from datexii.models.eu.datexii.v2.vms_unit_fault import VmsUnitFault
from datexii.models.eu.datexii.v2.vms_unit_record_versioned_reference import VmsUnitRecordVersionedReference
from datexii.models.eu.datexii.v2.vms_unit_table_versioned_reference import VmsUnitTableVersionedReference
from datexii.models.eu.datexii.v2.vms_unit_vms_index_vms import VmsUnitVmsIndexVms

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsUnit(VmsSetting):
    """
    Status of a VMS unit which may control one or more variable message signs
    on a single gantry or on different gantries.

    :ivar vms_unit_table_reference: A reference to a versioned VMS Unit
        table.
    :ivar vms_unit_reference: A reference to a versioned VMS unit record
        in a VMS Unit table which defines the characteristics of the VMS
        unit.
    :ivar vms:
    :ivar vms_unit_fault:
    :ivar vms_unit_extension:
    """
    vms_unit_table_reference: Optional[VmsUnitTableVersionedReference] = field(
        default=None,
        metadata={
            "name": "vmsUnitTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_unit_reference: Optional[VmsUnitRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "vmsUnitReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms: List[VmsUnitVmsIndexVms] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_unit_fault: List[VmsUnitFault] = field(
        default_factory=list,
        metadata={
            "name": "vmsUnitFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_unit_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsUnitExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
