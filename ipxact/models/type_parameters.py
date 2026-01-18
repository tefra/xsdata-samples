from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.type_parameter import TypeParameter

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class TypeParameters:
    """
    list of port type parameters (e.g. template or constructor parameters
    for a systemC port or socket).
    """

    class Meta:
        name = "typeParameters"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    type_parameter: list[TypeParameter] = field(
        default_factory=list,
        metadata={
            "name": "typeParameter",
            "type": "Element",
        },
    )
    service_type_def: list[ServiceTypeDef] = field(
        default_factory=list,
        metadata={
            "name": "serviceTypeDef",
            "type": "Element",
        },
    )


@dataclass
class ServiceTypeDef:
    """
    Definition of a single service type defintion.

    :ivar type_name: The name of the service type. Can be any predefined
        type such as booean or integer or any user-defined type such as
        addr_type or data_type.
    :ivar type_definition: Where the definition of the type is contained
        if the type if not part of the language. For SystemC and
        SystemVerilog it is the include file containing the type
        definition.
    :ivar type_parameters:
    :ivar id:
    """

    class Meta:
        name = "serviceTypeDef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    type_name: None | ServiceTypeDef.TypeName = field(
        default=None,
        metadata={
            "name": "typeName",
            "type": "Element",
            "required": True,
        },
    )
    type_definition: list[ServiceTypeDef.TypeDefinition] = field(
        default_factory=list,
        metadata={
            "name": "typeDefinition",
            "type": "Element",
        },
    )
    type_parameters: None | TypeParameters = field(
        default=None,
        metadata={
            "name": "typeParameters",
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
    class TypeName:
        """
        :ivar value:
        :ivar implicit: Defines that the typeName supplied for this
            service is implicit and a netlister should not declare this
            service in a language specific top-level netlist
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        implicit: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
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
        id: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
