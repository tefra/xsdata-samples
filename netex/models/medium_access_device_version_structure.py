from __future__ import annotations

from dataclasses import dataclass, field

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

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_ref: CustomerRef | None = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    identity_token: str | None = field(
        default=None,
        metadata={
            "name": "IdentityToken",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_medium_access_device_ref: TypeOfMediumAccessDeviceRef | None = (
        field(
            default=None,
            metadata={
                "name": "TypeOfMediumAccessDeviceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    application_instances: MediumApplicationInstanceRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "applicationInstances",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
