from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vms_unit_record import VmsUnitRecord

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsUnitTable:
    """
    A versioned VMS Unit Table comprising a number of data records, each record
    defining the characteristics of a specific deployed variable message sign
    unit.

    :ivar vms_unit_table_identification: An alphanumeric identification
        for the VMS Unit table, possibly human readable.
    :ivar vms_unit_record:
    :ivar vms_unit_table_extension:
    :ivar id:
    :ivar version:
    """
    vms_unit_table_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsUnitTableIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vms_unit_record: List[VmsUnitRecord] = field(
        default_factory=list,
        metadata={
            "name": "vmsUnitRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    vms_unit_table_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsUnitTableExtension",
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
