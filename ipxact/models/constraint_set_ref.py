from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ConstraintSetRef:
    """
    A reference to a set of port constraints.
    """

    class Meta:
        name = "constraintSetRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    local_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "localName",
            "type": "Element",
            "required": True,
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
