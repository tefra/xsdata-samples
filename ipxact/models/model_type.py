from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.component_instantiation_type import (
    ComponentInstantiationType,
)
from ipxact.models.description import Description
from ipxact.models.design_configuration_instantiation_type import (
    DesignConfigurationInstantiationType,
)
from ipxact.models.design_instantiation_type import DesignInstantiationType
from ipxact.models.display_name import DisplayName
from ipxact.models.port import Port
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ModelType:
    """
    Model information.

    :ivar views: Views container
    :ivar instantiations: Instantiations container
    :ivar ports: Port container
    """

    class Meta:
        name = "modelType"

    views: Optional["ModelType.Views"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    instantiations: Optional["ModelType.Instantiations"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    ports: Optional["ModelType.Ports"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )

    @dataclass
    class Views:
        """
        :ivar view: Single view of a component
        """

        view: list["ModelType.Views.View"] = field(
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
            :ivar design_instantiation_ref:
            :ivar design_configuration_instantiation_ref:
            :ivar vendor_extensions:
            :ivar id:
            """

            name: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    "required": True,
                },
            )
            display_name: Optional[DisplayName] = field(
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
            env_identifier: list["ModelType.Views.View.EnvIdentifier"] = field(
                default_factory=list,
                metadata={
                    "name": "envIdentifier",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            component_instantiation_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "componentInstantiationRef",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            design_instantiation_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "designInstantiationRef",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            design_configuration_instantiation_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "designConfigurationInstantiationRef",
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
            class EnvIdentifier:
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                        "pattern": r"[a-zA-Z0-9_+\*\.]*:[a-zA-Z0-9_+\*\.]*:[a-zA-Z0-9_+\*\.]*",
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
    class Instantiations:
        """
        :ivar component_instantiation: Component Instantiation
        :ivar design_instantiation: Design Instantiation
        :ivar design_configuration_instantiation: Design Configuration
            Instantiation
        """

        component_instantiation: list[ComponentInstantiationType] = field(
            default_factory=list,
            metadata={
                "name": "componentInstantiation",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        design_instantiation: list[DesignInstantiationType] = field(
            default_factory=list,
            metadata={
                "name": "designInstantiation",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        design_configuration_instantiation: list[
            DesignConfigurationInstantiationType
        ] = field(
            default_factory=list,
            metadata={
                "name": "designConfigurationInstantiation",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )

    @dataclass
    class Ports:
        port: list[Port] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )
