from dataclasses import dataclass, field
from typing import Optional

from .diagnostic_data_identifier_subtypes_enum import (
    DiagnosticDataIdentifierSubtypesEnum,
)
from .diagnostic_initial_event_status_enum import (
    DiagnosticInitialEventStatusEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticDataChangeTrigger:
    """
    This represents the ability to define a trigger based on the change of a given
    DiagnosticDataIdentifier.

    :ivar initial_event_status: This represents the initial status of
        the enclosing DiagnosticResponseOnEventTrigger.
    :ivar data_identifier_ref: This represents the corresponding
        DiagnosticDataIdentifier.
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
        name = "DIAGNOSTIC-DATA-CHANGE-TRIGGER"

    initial_event_status: Optional[DiagnosticInitialEventStatusEnum] = field(
        default=None,
        metadata={
            "name": "INITIAL-EVENT-STATUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_identifier_ref: Optional[
        "DiagnosticDataChangeTrigger.DataIdentifierRef"
    ] = field(
        default=None,
        metadata={
            "name": "DATA-IDENTIFIER-REF",
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
    class DataIdentifierRef(Ref):
        dest: Optional[DiagnosticDataIdentifierSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
