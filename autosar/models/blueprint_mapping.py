from __future__ import annotations

from dataclasses import dataclass, field

from .atp_blueprint_subtypes_enum import AtpBlueprintSubtypesEnum
from .atp_blueprintable_subtypes_enum import AtpBlueprintableSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BlueprintMapping:
    """
    This meta-class represents the ability to map two an object and its
    blueprint.

    :ivar blueprint_ref: This represents the mapped blueprint.
    :ivar derived_object_ref: This represents the object which was
        derived from the blueprint.
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
        name = "BLUEPRINT-MAPPING"

    blueprint_ref: None | BlueprintMapping.BlueprintRef = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    derived_object_ref: None | BlueprintMapping.DerivedObjectRef = field(
        default=None,
        metadata={
            "name": "DERIVED-OBJECT-REF",
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

    @dataclass
    class BlueprintRef(Ref):
        dest: None | AtpBlueprintSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DerivedObjectRef(Ref):
        dest: None | AtpBlueprintableSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
