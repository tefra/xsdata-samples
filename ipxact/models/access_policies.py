from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.access_type import AccessType
from ipxact.models.mode_ref import ModeRef
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AccessPolicies:
    class Meta:
        name = "accessPolicies"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    access_policy: list["AccessPolicies.AccessPolicy"] = field(
        default_factory=list,
        metadata={
            "name": "accessPolicy",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class AccessPolicy:
        mode_ref: list[ModeRef] = field(
            default_factory=list,
            metadata={
                "name": "modeRef",
                "type": "Element",
            },
        )
        access: Optional[AccessType] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        vendor_extensions: Optional[VendorExtensions] = field(
            default=None,
            metadata={
                "name": "vendorExtensions",
                "type": "Element",
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
