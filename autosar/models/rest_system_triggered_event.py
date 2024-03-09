from dataclasses import dataclass, field
from typing import Optional

from .ref import Ref
from .rest_element_def_subtypes_enum import RestElementDefSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RestSystemTriggeredEvent:
    """
    This meta-class represents the ability to identify an element such that at
    runtime an event is generated when the value of the reference element changes.

    :ivar element_ref: This reference represent the element that is
        linked to the system triggered event.
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
        name = "REST-SYSTEM-TRIGGERED-EVENT"

    element_ref: Optional["RestSystemTriggeredEvent.ElementRef"] = field(
        default=None,
        metadata={
            "name": "ELEMENT-REF",
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
    class ElementRef(Ref):
        dest: Optional[RestElementDefSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
