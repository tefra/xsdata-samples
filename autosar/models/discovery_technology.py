from dataclasses import dataclass, field
from typing import Optional
from .discovery_technology_enum import DiscoveryTechnologyEnum
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiscoveryTechnology:
    """This element is deprecated and will be removed in future.

    This information is replaced by the runtimePortConfiguration and runtimeIpAddressConfiguration attributes in the SocketConnection.
    Old description:
    Discovery technology information.

    :ivar name: Discovery technology used.
    :ivar version: Version of the used Discovery protocol.
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
        name = "DISCOVERY-TECHNOLOGY"

    name: Optional[DiscoveryTechnologyEnum] = field(
        default=None,
        metadata={
            "name": "NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    version: Optional[String] = field(
        default=None,
        metadata={
            "name": "VERSION",
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
