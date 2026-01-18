from __future__ import annotations

from dataclasses import dataclass, field

from .search_intention_enum import SearchIntentionEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RPortPrototypeProps:
    """
    PortPrototypeProps for a RPort.

    :ivar search_intention: This attribute is used to specify the
        intention of the developer of the enclosing software-component
        in terms of whether the respective PortPrototype shall be use to
        search for a specific service instance or all instances of the
        given service. Please note that the value of this attribute does
        not create a binding contract. The actual search behavior is
        defined as part of the service instance manifest.
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
        name = "R-PORT-PROTOTYPE-PROPS"

    search_intention: SearchIntentionEnum | None = field(
        default=None,
        metadata={
            "name": "SEARCH-INTENTION",
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
