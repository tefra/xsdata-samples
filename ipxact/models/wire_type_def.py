from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class WireTypeDef:
    """
    Definition of a single wire type defintion that can relate to multiple
    views.

    :ivar type_name: The name of the logic type. Examples could be
        std_logic, std_ulogic, std_logic_vector, sc_logic, ...
    :ivar type_definition: Where the definition of the type is
        contained. For std_logic, this is contained in
        IEEE.std_logic_1164.all. For sc_logic, this is contained in
        systemc.h. For VHDL this is the library and package as defined
        by the "used" statement. For SystemC and SystemVerilog it is the
        include file required. For verilog this is not needed.
    :ivar view_ref: A reference to a view name in the file for which
        this type applies.
    :ivar id:
    """

    class Meta:
        name = "wireTypeDef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    type_name: Optional["WireTypeDef.TypeName"] = field(
        default=None,
        metadata={
            "name": "typeName",
            "type": "Element",
        },
    )
    type_definition: list["WireTypeDef.TypeDefinition"] = field(
        default_factory=list,
        metadata={
            "name": "typeDefinition",
            "type": "Element",
        },
    )
    view_ref: list["WireTypeDef.ViewRef"] = field(
        default_factory=list,
        metadata={
            "name": "viewRef",
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
    class TypeName:
        """
        :ivar value:
        :ivar constrained: Defines the types for the port has
            constrained the number of bits in the vector
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        constrained: list[str] = field(
            default_factory=list,
            metadata={
                "type": "Attribute",
                "tokens": True,
            },
        )

    @dataclass
    class TypeDefinition:
        value: str = field(
            default="",
            metadata={
                "required": True,
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
    class ViewRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
