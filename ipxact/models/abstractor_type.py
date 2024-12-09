from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.abstractor_bus_interface_type import (
    AbstractorBusInterfaceType,
)
from ipxact.models.abstractor_generators import AbstractorGenerators
from ipxact.models.abstractor_mode_type import AbstractorModeType
from ipxact.models.abstractor_model_type import AbstractorModelType
from ipxact.models.assertions import Assertions
from ipxact.models.choices import Choices
from ipxact.models.description import Description
from ipxact.models.file_sets import FileSets
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AbstractorType:
    """
    Abstractor-specific extension to abstractorType.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar display_name: Name for display purposes. Typically a few words
        providing a more detailed and/or user-friendly name than the
        vlnv.
    :ivar short_description:
    :ivar description:
    :ivar abstractor_mode: Define the mode for the interfaces on this
        abstractor. For initiator the first interface connects to the
        initiator, the second connects to the mirroredInitiator For
        target the first interface connects to the mirroredTarget the
        second connects to the target For direct the first interface
        connects to the initiator, the second connects to the target For
        system the first interface connects to the system, the second
        connects to the mirroredSystem. For system the group attribute
        is required
    :ivar bus_type: The bus type of both interfaces. Refers to bus
        definition using vendor, library, name, version attributes.
    :ivar abstractor_interfaces: The interfaces supported by this
        abstractor
    :ivar model: Model information.
    :ivar abstractor_generators: Generator list is tools-specific.
    :ivar choices:
    :ivar file_sets:
    :ivar parameters:
    :ivar assertions:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "abstractorType"

    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    library: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: Optional[ShortDescription] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    abstractor_mode: Optional["AbstractorType.AbstractorMode"] = field(
        default=None,
        metadata={
            "name": "abstractorMode",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    bus_type: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "name": "busType",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    abstractor_interfaces: Optional["AbstractorType.AbstractorInterfaces"] = (
        field(
            default=None,
            metadata={
                "name": "abstractorInterfaces",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
            },
        )
    )
    model: Optional[AbstractorModelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    abstractor_generators: Optional[AbstractorGenerators] = field(
        default=None,
        metadata={
            "name": "abstractorGenerators",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    choices: Optional[Choices] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    file_sets: Optional[FileSets] = field(
        default=None,
        metadata={
            "name": "fileSets",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    assertions: Optional[Assertions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class AbstractorMode:
        """
        :ivar value:
        :ivar group: Define the system group if the mode is set to
            system
        """

        value: Optional[AbstractorModeType] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        group: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class AbstractorInterfaces:
        """
        :ivar abstractor_interface: An abstractor must have exactly 2
            Interfaces.
        """

        abstractor_interface: list[AbstractorBusInterfaceType] = field(
            default_factory=list,
            metadata={
                "name": "abstractorInterface",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 2,
                "max_occurs": 2,
            },
        )
