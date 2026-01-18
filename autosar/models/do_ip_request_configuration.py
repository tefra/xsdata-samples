from dataclasses import dataclass, field

from .positive_integer import PositiveInteger
from .request_type_enum import RequestTypeEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DoIpRequestConfiguration:
    """
    This meta-class specifies a range of target addresses and its
    interpretation as either physical or functional request.

    :ivar end_address: End address for range of target-addresses
        (including this address).
    :ivar request_type: Determines the type of request.
    :ivar start_address: Start address for range of target-addresses
        (including this address).
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
        name = "DO-IP-REQUEST-CONFIGURATION"

    end_address: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "END-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    request_type: RequestTypeEnum | None = field(
        default=None,
        metadata={
            "name": "REQUEST-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    start_address: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "START-ADDRESS",
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
