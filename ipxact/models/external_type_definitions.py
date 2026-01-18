from dataclasses import dataclass, field

from ipxact.models.configurable_library_ref_type import (
    ConfigurableLibraryRefType,
)
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.mode_links import ModeLinks
from ipxact.models.reset_type_links import ResetTypeLinks
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.view_links import ViewLinks

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ExternalTypeDefinitions:
    """
    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar type_definitions_ref: References a type definitions to be
        found in an external file.  The four attributes define the VLNV
        of the referenced document.
    :ivar view_links:
    :ivar mode_links:
    :ivar reset_type_links:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "externalTypeDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    display_name: DisplayName | None = field(
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
    type_definitions_ref: ConfigurableLibraryRefType | None = field(
        default=None,
        metadata={
            "name": "typeDefinitionsRef",
            "type": "Element",
            "required": True,
        },
    )
    view_links: ViewLinks | None = field(
        default=None,
        metadata={
            "name": "viewLinks",
            "type": "Element",
        },
    )
    mode_links: ModeLinks | None = field(
        default=None,
        metadata={
            "name": "modeLinks",
            "type": "Element",
        },
    )
    reset_type_links: ResetTypeLinks | None = field(
        default=None,
        metadata={
            "name": "resetTypeLinks",
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
