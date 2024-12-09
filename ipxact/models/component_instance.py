from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.configurable_library_ref_type import (
    ConfigurableLibraryRefType,
)
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.instance_name import InstanceName
from ipxact.models.power_domain_links import PowerDomainLinks
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ComponentInstance:
    """Component instance element.

    The instance name is contained in the unique-value instanceName
    attribute.

    :ivar instance_name:
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar component_ref: References a component to be found in an
        external library.  The four attributes define the VLNV of the
        referenced element.
    :ivar power_domain_links:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "componentInstance"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    instance_name: Optional[InstanceName] = field(
        default=None,
        metadata={
            "name": "instanceName",
            "type": "Element",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    short_description: Optional[ShortDescription] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    component_ref: Optional[ConfigurableLibraryRefType] = field(
        default=None,
        metadata={
            "name": "componentRef",
            "type": "Element",
            "required": True,
        },
    )
    power_domain_links: Optional[PowerDomainLinks] = field(
        default=None,
        metadata={
            "name": "powerDomainLinks",
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
