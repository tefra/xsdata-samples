from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vms_unit_record_vms_index_vms_record import VmsUnitRecordVmsIndexVmsRecord

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsUnitRecord:
    """
    A versioned single VMS unit entry/record in the VMS Unit table that defines
    the characteristics of the VMS unit.

    :ivar number_of_vms: Number of variable message signs contolled by
        the unit.
    :ivar vms_unit_identifier: Identification of a VMS unit used by the
        supplier or consumer systems.
    :ivar vms_unit_ipaddress: IP network address of the VMS unit.
    :ivar vms_unit_electronic_address: Electronic address of the VMS
        unit (if not IP addressable).
    :ivar vms_record:
    :ivar vms_unit_record_extension:
    :ivar id:
    :ivar version:
    """
    number_of_vms: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVms",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_unit_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsUnitIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vms_unit_ipaddress: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsUnitIPAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vms_unit_electronic_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsUnitElectronicAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vms_record: List[VmsUnitRecordVmsIndexVmsRecord] = field(
        default_factory=list,
        metadata={
            "name": "vmsRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_unit_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsUnitRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
