from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.assertions import Assertions
from ipxact.models.choices import Choices
from ipxact.models.description import Description
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.unsigned_int_expression import UnsignedIntExpression
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class BusDefinition:
    """
    Defines the structural information associated with a bus type,
    independent of the abstraction level.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar display_name: Name for display purposes. Typically a few words
        providing a more detailed and/or user-friendly name than the
        vlnv.
    :ivar short_description:
    :ivar description:
    :ivar direct_connection: This element indicates that a initiator
        interface may be directly connected to a target interface (under
        certain conditions) for busses of this type.
    :ivar broadcast: This element indicates that this bus definition
        supports 'broadcast' mode. This means that it is legal to make
        one-to-many interface connections.
    :ivar is_addressable: If true, indicates that this is an addressable
        bus.
    :ivar extends: Optional name of bus type that this bus definition is
        compatible with. This bus definition may change the definitions
        in the existing bus definition
    :ivar max_initiators: Indicates the maximum number of initiators
        this bus supports.  If this element is not present, the number
        of initiators allowed is unbounded.
    :ivar max_targets: Indicates the maximum number of targets this bus
        supports.  If the element is not present, the number of targets
        allowed is unbounded.
    :ivar system_group_names: Indicates the list of system group names
        that are defined for this bus definition.
    :ivar choices:
    :ivar parameters:
    :ivar assertions:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "busDefinition"
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
    direct_connection: None | bool = field(
        default=None,
        metadata={
            "name": "directConnection",
            "type": "Element",
            "required": True,
        },
    )
    broadcast: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    is_addressable: None | bool = field(
        default=None,
        metadata={
            "name": "isAddressable",
            "type": "Element",
            "required": True,
        },
    )
    extends: None | LibraryRefType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    max_initiators: None | UnsignedIntExpression = field(
        default=None,
        metadata={
            "name": "maxInitiators",
            "type": "Element",
        },
    )
    max_targets: None | UnsignedIntExpression = field(
        default=None,
        metadata={
            "name": "maxTargets",
            "type": "Element",
        },
    )
    system_group_names: None | BusDefinition.SystemGroupNames = field(
        default=None,
        metadata={
            "name": "systemGroupNames",
            "type": "Element",
        },
    )
    choices: None | Choices = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameters: None | Parameters = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    assertions: None | Assertions = field(
        default=None,
        metadata={
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

    @dataclass
    class SystemGroupNames:
        """
        :ivar system_group_name: Indicates the name of a system group
            defined for this bus definition.
        """

        system_group_name: list[
            BusDefinition.SystemGroupNames.SystemGroupName
        ] = field(
            default_factory=list,
            metadata={
                "name": "systemGroupName",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass
        class SystemGroupName:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            id: None | str = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )
