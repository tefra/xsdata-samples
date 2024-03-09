from dataclasses import dataclass, field
from typing import Optional

from .customer_ref import CustomerRef
from .entity_in_version_structure import DataManagedObjectStructure
from .medium_application_instance_rel_structure import (
    MediumApplicationInstanceRelStructure,
)
from .multilingual_string import MultilingualString
from .type_of_medium_access_device_ref import TypeOfMediumAccessDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MediumAccessDeviceVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "MediumAccessDevice_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    identity_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityToken",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_medium_access_device_ref: Optional[TypeOfMediumAccessDeviceRef] = (
        field(
            default=None,
            metadata={
                "name": "TypeOfMediumAccessDeviceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    application_instances: Optional[MediumApplicationInstanceRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "applicationInstances",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
