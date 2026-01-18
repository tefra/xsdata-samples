from dataclasses import dataclass, field
from typing import Optional

from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class GenericModelReference:
    """
    This meta-class represents the ability to express a late binding
    reference to a model element.

    The model element can be from every model. Even if it is modeled
    according to the association representation, it is not limited to refer
    to AUTOSAR model elements.

    :ivar ref: This is the full qualified name of the model element
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
    :ivar base: This establishes the reference base.
    :ivar dest: This attribute represents the class of the referenced
        model element. It is a String, since the model element can be in
        any model. Therefore we cannot have any assumption here.
    """

    class Meta:
        name = "GENERIC-MODEL-REFERENCE"

    ref: Ref | None = field(
        default=None,
        metadata={
            "name": "REF",
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
    base: str | None = field(
        default=None,
        metadata={
            "name": "BASE",
            "type": "Attribute",
        },
    )
    dest: str | None = field(
        default=None,
        metadata={
            "name": "DEST",
            "type": "Attribute",
        },
    )
