from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.active_interface import ActiveInterface
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.hier_interface_type import HierInterfaceType
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class Interconnection:
    """
    Describes a connection between two active (not monitor) busInterfaces.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar active_interface: Describes one interface of the
        interconnection. The componentInterfaceRef and busRef attributes
        indicate the instance name and bus interface name of one end of
        the connection.
        This interface can be connected to one or more additional active
        and/or hierarchical interfaces, or to one or more hierarchical
        interfaces or to one or more monitor interfaces. The connected
        interfaces are all contained within the choice element below.
    :ivar hier_interface:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "interconnection"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    display_name: None | DisplayName = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    short_description: None | ShortDescription = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
        },
    )
    description: None | Description = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    active_interface: list[ActiveInterface] = field(
        default_factory=list,
        metadata={
            "name": "activeInterface",
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    hier_interface: list[HierInterfaceType] = field(
        default_factory=list,
        metadata={
            "name": "hierInterface",
            "type": "Element",
        },
    )
    vendor_extensions: None | VendorExtensions = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
