from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.description import Description
from ipxact.models.ipxact_files_type import IpxactFilesType
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Catalog:
    """
    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar display_name: Name for display purposes. Typically a few words
        providing a more detailed and/or user-friendly name than the
        vlnv.
    :ivar short_description:
    :ivar description:
    :ivar catalogs:
    :ivar bus_definitions:
    :ivar abstraction_definitions:
    :ivar components:
    :ivar abstractors:
    :ivar designs:
    :ivar design_configurations:
    :ivar generator_chains:
    :ivar type_definitions:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "catalog"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    vendor: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    library: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    version: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    display_name: None | str = field(
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
    catalogs: None | IpxactFilesType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    bus_definitions: None | IpxactFilesType = field(
        default=None,
        metadata={
            "name": "busDefinitions",
            "type": "Element",
        },
    )
    abstraction_definitions: None | IpxactFilesType = field(
        default=None,
        metadata={
            "name": "abstractionDefinitions",
            "type": "Element",
        },
    )
    components: None | IpxactFilesType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    abstractors: None | IpxactFilesType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    designs: None | IpxactFilesType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    design_configurations: None | IpxactFilesType = field(
        default=None,
        metadata={
            "name": "designConfigurations",
            "type": "Element",
        },
    )
    generator_chains: None | IpxactFilesType = field(
        default=None,
        metadata={
            "name": "generatorChains",
            "type": "Element",
        },
    )
    type_definitions: None | IpxactFilesType = field(
        default=None,
        metadata={
            "name": "typeDefinitions",
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
