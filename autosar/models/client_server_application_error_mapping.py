from __future__ import annotations

from dataclasses import dataclass, field

from .application_error_subtypes_enum import ApplicationErrorSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ClientServerApplicationErrorMapping:
    """
    This meta-class represents the ability to map ApplicationErrors onto
    each other.

    :ivar first_application_error_ref: This represents the first
        ApplicationError in the context of the
        ClientServerApplicationErrorMapping.
    :ivar second_application_error_ref: This represents the second
        ApplicationError in the context of the
        ClientServerApplicationErrorMapping.
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
        name = "CLIENT-SERVER-APPLICATION-ERROR-MAPPING"

    first_application_error_ref: (
        None | ClientServerApplicationErrorMapping.FirstApplicationErrorRef
    ) = field(
        default=None,
        metadata={
            "name": "FIRST-APPLICATION-ERROR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    second_application_error_ref: (
        None | ClientServerApplicationErrorMapping.SecondApplicationErrorRef
    ) = field(
        default=None,
        metadata={
            "name": "SECOND-APPLICATION-ERROR-REF",
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
    class FirstApplicationErrorRef(Ref):
        dest: ApplicationErrorSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class SecondApplicationErrorRef(Ref):
        dest: ApplicationErrorSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
