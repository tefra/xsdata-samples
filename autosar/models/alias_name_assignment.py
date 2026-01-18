from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .flat_instance_descriptor_subtypes_enum import (
    FlatInstanceDescriptorSubtypesEnum,
)
from .identifiable_subtypes_enum import IdentifiableSubtypesEnum
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class AliasNameAssignment:
    """
    This meta-class represents the ability to associate an alternative name
    to a flat representations or an Identifiable.

    The usage of this name is defined outside of AUTOSAR. For example this
    name can be used by MCD tools or as a name for component instances in
    the ECU extract. Note that flatInstance and identifiable are mutually
    exclusive.

    :ivar short_label: This attribute represents the alias name. It is
        modeled as string because the alias name is used outside of
        AUTOSAR and therefore no naming conventions can be applied
        within AUTOSAR.
    :ivar label: This represents an "Alias LongName".
    :ivar identifiable_ref: Assignment of a unique name to an
        Identifiable.
    :ivar flat_instance_ref: Assignment of a unique name to a flat
        representation.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "ALIAS-NAME-ASSIGNMENT"

    short_label: String | None = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    label: MultilanguageLongName | None = field(
        default=None,
        metadata={
            "name": "LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    identifiable_ref: AliasNameAssignment.IdentifiableRef | None = field(
        default=None,
        metadata={
            "name": "IDENTIFIABLE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    flat_instance_ref: AliasNameAssignment.FlatInstanceRef | None = field(
        default=None,
        metadata={
            "name": "FLAT-INSTANCE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class IdentifiableRef(Ref):
        dest: IdentifiableSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class FlatInstanceRef(Ref):
        dest: FlatInstanceDescriptorSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
