from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .j_1939_controller_application_subtypes_enum import (
    J1939ControllerApplicationSubtypesEnum,
)
from .j_1939_nm_node_subtypes_enum import J1939NmNodeSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class J1939ControllerApplicationToJ1939NmNodeMapping:
    """
    This meta-class represents the ability to map a
    J1939ControllerApplication to a J1939NmNode.

    Note that this is similar but not identical to the mapping of
    SwComponentPrototypes to EcuInstances; for J1939 the semantics of an
    EcuInstance itself is basically replaced by a J1939NmNode.

    :ivar j_1939_controller_application_ref: Reference to the J1939
        Controller Application that is mapped to the referenced
        J1939NmNode.
    :ivar j_1939_nm_node_ref: J1939NmNode that is the target of the
        J1939ControllerApplicationTo1939NmNodeMapping.
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
        name = "J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPING"

    j_1939_controller_application_ref: J1939ControllerApplicationToJ1939NmNodeMapping.J1939ControllerApplicationRef | None = field(
        default=None,
        metadata={
            "name": "J-1939-CONTROLLER-APPLICATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    j_1939_nm_node_ref: J1939ControllerApplicationToJ1939NmNodeMapping.J1939NmNodeRef | None = field(
        default=None,
        metadata={
            "name": "J-1939-NM-NODE-REF",
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
    class J1939ControllerApplicationRef(Ref):
        dest: J1939ControllerApplicationSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class J1939NmNodeRef(Ref):
        dest: J1939NmNodeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
