from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.contact import Contact
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vms_unit_record_versioned_reference import (
    VmsUnitRecordVersionedReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingVMS:
    """
    A reference to a record that contains the metadata for a specific VMS unit that
    may be used to manage the parking site (e.g. to indicate to drivers the current
    availability of spaces).

    :ivar vms_unit_used_to_manage_parking: A reference to a record that
        contains the metadata for a specific VMS unit that may be used
        to manage the parking site (e.g. to indicate to drivers the
        current availability of spaces).
    :ivar vms_operator:
    :ivar parking_vmsextension:
    """

    vms_unit_used_to_manage_parking: Optional[
        VmsUnitRecordVersionedReference
    ] = field(
        default=None,
        metadata={
            "name": "vmsUnitUsedToManageParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    vms_operator: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "vmsOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_vmsextension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingVMSExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
