from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.part_select import PartSelect
from ipxact.models.sub_port_reference import SubPortReference
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ExternalPortReference:
    """
    :ivar sub_port_reference:
    :ivar part_select:
    :ivar vendor_extensions:
    :ivar port_ref: A port on the on the referenced component from
        componentInterfaceRef.
    :ivar id:
    """

    class Meta:
        name = "externalPortReference"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    sub_port_reference: list[SubPortReference] = field(
        default_factory=list,
        metadata={
            "name": "subPortReference",
            "type": "Element",
        },
    )
    part_select: PartSelect | None = field(
        default=None,
        metadata={
            "name": "partSelect",
            "type": "Element",
        },
    )
    vendor_extensions: VendorExtensions | None = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )
    port_ref: str | None = field(
        default=None,
        metadata={
            "name": "portRef",
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
