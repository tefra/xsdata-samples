from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.abstractor_port_type import AbstractorPortType
from ipxact.models.component_instantiation_type import (
    ComponentInstantiationType,
)
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AbstractorModelType:
    """
    Model information for an abstractor.

    :ivar views: Views container
    :ivar instantiations: Instantiations container
    :ivar ports: Port container
    """

    class Meta:
        name = "abstractorModelType"

    views: AbstractorModelType.Views | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    instantiations: AbstractorModelType.Instantiations | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    ports: AbstractorModelType.Ports | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )

    @dataclass
    class Views:
        """
        :ivar view: Single view of an abstracto
        """

        view: list[AbstractorModelType.Views.View] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

        @dataclass
        class View:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
            :ivar env_identifier: Defines the hardware environment in
                which this view applies. The format of the string is
                language:tool:vendor_extension, with each piece being
                optional. The language must be one of the types from
                ipxact:fileType. The tool values are defined by the
                Accellera Systems Initiative, and include generic values
                "*Simulation" and "*Synthesis" to imply any tool of the
                indicated type. Having more than one envIdentifier
                indicates that the view applies to multiple
                environments.
            :ivar component_instantiation_ref:
            :ivar vendor_extensions:
            :ivar id:
            """

            name: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    "required": True,
                },
            )
            display_name: DisplayName | None = field(
                default=None,
                metadata={
                    "name": "displayName",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            short_description: ShortDescription | None = field(
                default=None,
                metadata={
                    "name": "shortDescription",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            description: Description | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            env_identifier: list[
                AbstractorModelType.Views.View.EnvIdentifier
            ] = field(
                default_factory=list,
                metadata={
                    "name": "envIdentifier",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            component_instantiation_ref: str | None = field(
                default=None,
                metadata={
                    "name": "componentInstantiationRef",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            vendor_extensions: VendorExtensions | None = field(
                default=None,
                metadata={
                    "name": "vendorExtensions",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            id: str | None = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )

            @dataclass
            class EnvIdentifier:
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                        "pattern": r"[a-zA-Z0-9_+\*\.]*:[a-zA-Z0-9_+\*\.]*:[a-zA-Z0-9_+\*\.]*",
                    },
                )
                id: str | None = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.w3.org/XML/1998/namespace",
                    },
                )

    @dataclass
    class Instantiations:
        """
        :ivar component_instantiation: Component Instantiation
        """

        component_instantiation: list[ComponentInstantiationType] = field(
            default_factory=list,
            metadata={
                "name": "componentInstantiation",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Ports:
        port: list[AbstractorPortType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
