from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.assertions import Assertions
from ipxact.models.choices import Choices
from ipxact.models.configurable_library_ref_type import (
    ConfigurableLibraryRefType,
)
from ipxact.models.description import Description
from ipxact.models.generator import Generator
from ipxact.models.generator_selector_type import GeneratorSelectorType
from ipxact.models.group_selector import GroupSelector
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class GeneratorChain:
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
    :ivar generator_chain_selector: Select other generator chain files
        for inclusion into this chain. The boolean attribute "unique"
        (default false) specifies that only a single generator is valid
        in this context. If more that one generator is selected based on
        the selection criteria, DE will prompt the user to resolve to a
        single generator.
    :ivar component_generator_selector: Selects generators declared in
        components of the current design for inclusion into this
        generator chain.
    :ivar generator:
    :ivar chain_group: Identifies this generator chain as belonging to
        the named group. This is used by other generator chains to
        select this chain for programmatic inclusion.
    :ivar choices:
    :ivar parameters:
    :ivar assertions:
    :ivar vendor_extensions:
    :ivar hidden: If this attribute is true then the generator should
        not be presented to the user, it may be part of a chain and has
        no useful meaning when invoked standalone.
    :ivar id:
    """

    class Meta:
        name = "generatorChain"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    vendor: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    library: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    version: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
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
    generator_chain_selector: list[GeneratorChain.GeneratorChainSelector] = (
        field(
            default_factory=list,
            metadata={
                "name": "generatorChainSelector",
                "type": "Element",
            },
        )
    )
    component_generator_selector: list[GeneratorSelectorType] = field(
        default_factory=list,
        metadata={
            "name": "componentGeneratorSelector",
            "type": "Element",
        },
    )
    generator: list[Generator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    chain_group: list[GeneratorChain.ChainGroup] = field(
        default_factory=list,
        metadata={
            "name": "chainGroup",
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
    hidden: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass(kw_only=True)
    class ChainGroup:
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

    @dataclass(kw_only=True)
    class GeneratorChainSelector:
        """
        :ivar group_selector:
        :ivar generator_chain_ref: Select another generator chain using
            the unique identifier of this generator chain.
        :ivar unique: Specifies that only a single generator is valid in
            this context. If more that one generator is selcted based on
            the selection criteria, DE will prompt the user to resolve
            to a single generator.
        :ivar id:
        """

        group_selector: None | GroupSelector = field(
            default=None,
            metadata={
                "name": "groupSelector",
                "type": "Element",
            },
        )
        generator_chain_ref: None | ConfigurableLibraryRefType = field(
            default=None,
            metadata={
                "name": "generatorChainRef",
                "type": "Element",
            },
        )
        unique: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
            },
        )
        id: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
