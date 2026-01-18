from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vms_unit_record import VmsUnitRecord

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class VmsUnitTable:
    """
    A versioned VMS Unit Table comprising a number of data records, each
    record defining the characteristics of a specific deployed variable
    message sign unit.

    :ivar vms_unit_table_identification: An alphanumeric identification
        for the VMS Unit table, possibly human readable.
    :ivar vms_unit_record:
    :ivar vms_unit_table_extension:
    :ivar id:
    :ivar version:
    """

    vms_unit_table_identification: None | str = field(
        default=None,
        metadata={
            "name": "vmsUnitTableIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    vms_unit_record: list[VmsUnitRecord] = field(
        default_factory=list,
        metadata={
            "name": "vmsUnitRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    vms_unit_table_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "vmsUnitTableExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
