from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class DomainTypeDef:
    """
    Definition of a single domain type defintion that can relate to
    multiple views.

    :ivar type_name: The name of the domain.
    :ivar type_definition: Where the definition of the type is
        contained.
    :ivar view_ref: A reference to a view in the file for which this
        type applies.
    :ivar id:
    """

    class Meta:
        name = "domainTypeDef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    type_name: None | DomainTypeDef.TypeName = field(
        default=None,
        metadata={
            "name": "typeName",
            "type": "Element",
        },
    )
    type_definition: list[DomainTypeDef.TypeDefinition] = field(
        default_factory=list,
        metadata={
            "name": "typeDefinition",
            "type": "Element",
        },
    )
    view_ref: list[DomainTypeDef.ViewRef] = field(
        default_factory=list,
        metadata={
            "name": "viewRef",
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

    @dataclass(kw_only=True)
    class TypeName:
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

    @dataclass(kw_only=True)
    class ViewRef:
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
