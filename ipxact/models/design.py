from dataclasses import dataclass, field

from ipxact.models.ad_hoc_connections import AdHocConnections
from ipxact.models.assertions import Assertions
from ipxact.models.choices import Choices
from ipxact.models.component_instances import ComponentInstances
from ipxact.models.description import Description
from ipxact.models.interconnections import Interconnections
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Design:
    """
    Root element for a platform design.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar display_name: Name for display purposes. Typically a few words
        providing a more detailed and/or user-friendly name than the
        vlnv.
    :ivar short_description:
    :ivar description:
    :ivar component_instances:
    :ivar interconnections:
    :ivar ad_hoc_connections:
    :ivar choices:
    :ivar parameters:
    :ivar assertions:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "design"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    vendor: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    library: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    display_name: str | None = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    short_description: ShortDescription | None = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
        },
    )
    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    component_instances: ComponentInstances | None = field(
        default=None,
        metadata={
            "name": "componentInstances",
            "type": "Element",
        },
    )
    interconnections: Interconnections | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ad_hoc_connections: AdHocConnections | None = field(
        default=None,
        metadata={
            "name": "adHocConnections",
            "type": "Element",
        },
    )
    choices: Choices | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameters: Parameters | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    assertions: Assertions | None = field(
        default=None,
        metadata={
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
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
