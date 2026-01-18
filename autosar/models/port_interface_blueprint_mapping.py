from __future__ import annotations

from dataclasses import dataclass, field

from .port_interface_subtypes_enum import PortInterfaceSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class PortInterfaceBlueprintMapping:
    """
    This meta-class represents the ability to map two PortInterfaces of
    which one acts as the blueprint for the other.

    :ivar port_interface_blueprint_ref: This represents the interface
        blueprint. Note that this interface needs to live in a package
        of category BLUEPRINT.
    :ivar derived_port_interface_ref: This represents the derived
        interface.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "PORT-INTERFACE-BLUEPRINT-MAPPING"

    port_interface_blueprint_ref: (
        None | PortInterfaceBlueprintMapping.PortInterfaceBlueprintRef
    ) = field(
        default=None,
        metadata={
            "name": "PORT-INTERFACE-BLUEPRINT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    derived_port_interface_ref: (
        None | PortInterfaceBlueprintMapping.DerivedPortInterfaceRef
    ) = field(
        default=None,
        metadata={
            "name": "DERIVED-PORT-INTERFACE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass(kw_only=True)
    class PortInterfaceBlueprintRef(Ref):
        dest: PortInterfaceSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class DerivedPortInterfaceRef(Ref):
        dest: PortInterfaceSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
