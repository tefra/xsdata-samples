from __future__ import annotations

from dataclasses import dataclass, field

from .bsw_entry_relationship_enum import BswEntryRelationshipEnum
from .bsw_module_entry_subtypes_enum import BswModuleEntrySubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswEntryRelationship:
    """
    Describes a relationship between two BswModuleEntrys and the type of
    relationship.

    :ivar from_ref: Type of relationship that refers to the abstract
        BswModuleEntry. Please notice that in this case the
        bswEntryRelationshipType shall be set to drivedFrom.
    :ivar to_ref: Type of relationship that refers to the concrete
        BswModuleEntry
    :ivar bsw_entry_relationship_type: Denotes the type of the
        relationship.
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
        name = "BSW-ENTRY-RELATIONSHIP"

    from_ref: None | BswEntryRelationship.FromRef = field(
        default=None,
        metadata={
            "name": "FROM-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    to_ref: None | BswEntryRelationship.ToRef = field(
        default=None,
        metadata={
            "name": "TO-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bsw_entry_relationship_type: None | BswEntryRelationshipEnum = field(
        default=None,
        metadata={
            "name": "BSW-ENTRY-RELATIONSHIP-TYPE",
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
    class FromRef(Ref):
        dest: None | BswModuleEntrySubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ToRef(Ref):
        dest: None | BswModuleEntrySubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
