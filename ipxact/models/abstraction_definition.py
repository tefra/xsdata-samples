from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.assertions import Assertions
from ipxact.models.choices import Choices
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.kind import Kind
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.on_initiator_initiative import OnInitiatorInitiative
from ipxact.models.on_system_initiative import OnSystemInitiative
from ipxact.models.on_target_initiative import OnTargetInitiative
from ipxact.models.packets import Packets
from ipxact.models.parameters import Parameters
from ipxact.models.presence import Presence
from ipxact.models.protocol import Protocol
from ipxact.models.qualifier_type import QualifierType
from ipxact.models.short_description import ShortDescription
from ipxact.models.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.wire import Wire

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AbstractionDefinition:
    """
    Define the ports and other information of a particular abstraction of the bus.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar display_name: Name for display purposes. Typically a few words
        providing a more detailed and/or user-friendly name than the
        vlnv.
    :ivar short_description:
    :ivar description:
    :ivar bus_type: Reference to the busDefinition that this
        abstractionDefinition implements.
    :ivar extends: Optional name of abstraction type that this
        abstraction definition is compatible with. This abstraction
        definition may change the definitions of ports in the existing
        abstraction definition and add new ports, the ports in the
        original abstraction are not deleted but may be marked illegal
        to disallow their use. This abstraction definition may only
        extend another abstraction definition if the bus type of this
        abstraction definition extends the bus type of the extended
        abstraction definition
    :ivar ports: This is a list of logical ports defined by the bus.
    :ivar choices:
    :ivar parameters:
    :ivar assertions:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "abstractionDefinition"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    library: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    display_name: Optional[str] = field(
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
    bus_type: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "name": "busType",
            "type": "Element",
            "required": True,
        },
    )
    extends: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ports: Optional["AbstractionDefinition.Ports"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    choices: Optional[Choices] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    assertions: Optional[Assertions] = field(
        default=None,
        metadata={
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

    @dataclass
    class Ports:
        port: list["AbstractionDefinition.Ports.Port"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass
        class Port:
            """
            :ivar logical_name: The assigned name of this port in bus
                specifications.
            :ivar display_name:
            :ivar short_description:
            :ivar description:
            :ivar match: If this element is enabled (true) it is an
                error if the port is not mapped on both sides of the
                connection.
            :ivar wire:
            :ivar transactional: A port that carries complex information
                modeled at a high level of abstraction.
            :ivar packets:
            :ivar vendor_extensions:
            :ivar id:
            """

            logical_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "logicalName",
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
            match: Optional[bool] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            wire: Optional[Wire] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            transactional: Optional[
                "AbstractionDefinition.Ports.Port.Transactional"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            packets: Optional[Packets] = field(
                default=None,
                metadata={
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

            @dataclass
            class Transactional:
                """
                :ivar qualifier: The type of information this port
                    carries A transactional port can carry both address
                    and data information.
                :ivar on_system: Defines constraints for this port when
                    present in a system bus interface with a matching
                    group name.
                :ivar on_initiator: Defines constraints for this port
                    when present in a initiator bus interface.
                :ivar on_target: Defines constraints for this port when
                    present in a target bus interface.
                """

                qualifier: Optional[QualifierType] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                on_system: list[
                    "AbstractionDefinition.Ports.Port.Transactional.OnSystem"
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "onSystem",
                        "type": "Element",
                    },
                )
                on_initiator: Optional[
                    "AbstractionDefinition.Ports.Port.Transactional.OnInitiator"
                ] = field(
                    default=None,
                    metadata={
                        "name": "onInitiator",
                        "type": "Element",
                    },
                )
                on_target: Optional[
                    "AbstractionDefinition.Ports.Port.Transactional.OnTarget"
                ] = field(
                    default=None,
                    metadata={
                        "name": "onTarget",
                        "type": "Element",
                    },
                )

                @dataclass
                class OnSystem:
                    """
                    :ivar group: Used to group system ports into
                        different groups within a common bus.
                    :ivar presence:
                    :ivar initiative: If this element is present, the
                        type of access is restricted to the specified
                        value.
                    :ivar kind:
                    :ivar bus_width: If this element is present, the
                        width must match
                    :ivar protocol: If this element is present, the name
                        must match
                    :ivar id:
                    """

                    group: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    presence: Optional[Presence] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    initiative: Optional[OnSystemInitiative] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    kind: Optional[Kind] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    bus_width: Optional[UnsignedPositiveIntExpression] = field(
                        default=None,
                        metadata={
                            "name": "busWidth",
                            "type": "Element",
                        },
                    )
                    protocol: Optional[Protocol] = field(
                        default=None,
                        metadata={
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

                @dataclass
                class OnInitiator:
                    """
                    :ivar presence:
                    :ivar initiative: If this element is present, the
                        type of access is restricted to the specified
                        value.
                    :ivar kind:
                    :ivar bus_width: If this element is present, the
                        width must match
                    :ivar protocol: If this element is present, the name
                        must match
                    """

                    presence: Optional[Presence] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    initiative: Optional[OnInitiatorInitiative] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    kind: Optional[Kind] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    bus_width: Optional[UnsignedPositiveIntExpression] = field(
                        default=None,
                        metadata={
                            "name": "busWidth",
                            "type": "Element",
                        },
                    )
                    protocol: Optional[Protocol] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass
                class OnTarget:
                    """
                    :ivar presence:
                    :ivar initiative: If this element is present, the
                        type of access is restricted to the specified
                        value.
                    :ivar kind:
                    :ivar bus_width: If this element is present, the
                        width must match
                    :ivar protocol: If this element is present, the name
                        must match
                    """

                    presence: Optional[Presence] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    initiative: Optional[OnTargetInitiative] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    kind: Optional[Kind] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    bus_width: Optional[UnsignedPositiveIntExpression] = field(
                        default=None,
                        metadata={
                            "name": "busWidth",
                            "type": "Element",
                        },
                    )
                    protocol: Optional[Protocol] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
