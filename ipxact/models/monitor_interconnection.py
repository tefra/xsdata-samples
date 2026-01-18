from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.monitor_interface_type import MonitorInterfaceType
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class MonitorInterconnection:
    """
    Describes a connection from the interface of one component to any
    number of monitor interfaces in the design.

    An active interface can be connected to unlimited number of monitor
    interfaces.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar monitored_active_interface: Describes an active interface of
        the design that all the monitors will be connected to. The
        componentInterfaceRef and busRef attributes indicate the
        instance name and bus interface name. The optional path
        attribute indicates the hierarchical instance name path to the
        component.
    :ivar monitor_interface: Describes a list of monitor interfaces that
        are connected to the single active interface. The
        componentInterfaceRef and busRef attributes indicate the
        instance name and bus interface name. The optional path
        attribute indicates the hierarchical instance name path to the
        component.
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "monitorInterconnection"
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
    monitored_active_interface: MonitorInterfaceType = field(
        metadata={
            "name": "monitoredActiveInterface",
            "type": "Element",
            "required": True,
        }
    )
    monitor_interface: list[MonitorInterfaceType] = field(
        default_factory=list,
        metadata={
            "name": "monitorInterface",
            "type": "Element",
            "min_occurs": 1,
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
