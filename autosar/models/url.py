from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Url:
    """
    This meta-class specifies an Uniform Resource Locator (URL).

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
    :ivar mime_type: this denotes the mime type of the resource located
        by the url.
    """

    class Meta:
        name = "URL"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    mime_type: str | None = field(
        default=None,
        metadata={
            "name": "MIME-TYPE",
            "type": "Attribute",
        },
    )
