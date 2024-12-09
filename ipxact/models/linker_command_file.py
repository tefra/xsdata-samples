from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.generator_ref import GeneratorRef
from ipxact.models.string_expression import StringExpression
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class LinkerCommandFile:
    """
    Specifies a linker command file.

    :ivar name: Linker command file name.
    :ivar command_line_switch: The command line switch to specify the
        linker command file.
    :ivar enable: Specifies whether to generate and enable the linker
        command file.
    :ivar generator_ref:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "linkerCommandFile"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    name: Optional[StringExpression] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    command_line_switch: Optional[StringExpression] = field(
        default=None,
        metadata={
            "name": "commandLineSwitch",
            "type": "Element",
            "required": True,
        },
    )
    enable: Optional[UnsignedBitExpression] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    generator_ref: list[GeneratorRef] = field(
        default_factory=list,
        metadata={
            "name": "generatorRef",
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
