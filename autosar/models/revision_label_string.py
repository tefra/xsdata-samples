from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RevisionLabelString:
    """
    This primitive represents an internal AUTOSAR revision label which
    identifies an engineering object.

    It represents a pattern which * supports three integers representing
    from left to right MajorVersion, MinorVersion, PatchVersion. * may add
    an application specific suffix separated by one of ".", "_", ";". Legal
    patterns are for example: * 4.0.0 * 4.0.0.1234565 * 4.0.0_vendor
    specific;13 * 4.0.0;12.

    :ivar value:
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
        name = "REVISION-LABEL-STRING"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]+\.[0-9]+\.[0-9]+([\._;].*)?",
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
