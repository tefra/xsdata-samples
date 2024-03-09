from dataclasses import dataclass, field
from typing import Optional

from .port_prototype_blueprint_subtypes_enum import (
    PortPrototypeBlueprintSubtypesEnum,
)
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PortPrototypeBlueprintMapping:
    """
    This meta-class represents the ability to map a PortPrototypeBlueprint to a
    PortProtoype of which one acts as the blueprint for the other.

    :ivar port_prototype_blueprint_ref: The PortPrototypeBlueprint in
        the context of the mapping.
    :ivar derived_port_prototype_ref: The PortPrototype in the context
        of the mapping.
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
        name = "PORT-PROTOTYPE-BLUEPRINT-MAPPING"

    port_prototype_blueprint_ref: Optional[
        "PortPrototypeBlueprintMapping.PortPrototypeBlueprintRef"
    ] = field(
        default=None,
        metadata={
            "name": "PORT-PROTOTYPE-BLUEPRINT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    derived_port_prototype_ref: Optional[
        "PortPrototypeBlueprintMapping.DerivedPortPrototypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "DERIVED-PORT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class PortPrototypeBlueprintRef(Ref):
        dest: Optional[PortPrototypeBlueprintSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DerivedPortPrototypeRef(Ref):
        dest: Optional[PortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
