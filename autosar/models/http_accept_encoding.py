from dataclasses import dataclass, field
from typing import Optional
from .http_accept_encoding_enum import HttpAcceptEncodingEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class HttpAcceptEncoding:
    """
    This meta-class represents the ability to specify the accept-encoding of an
    exchange using HTTP.

    :ivar accept_encoding: This attribute is only used on the client
        side of the configuration for the purpose of stating the
        accepted compression algorithm.
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
        name = "HTTP-ACCEPT-ENCODING"

    accept_encoding: Optional[HttpAcceptEncodingEnum] = field(
        default=None,
        metadata={
            "name": "ACCEPT-ENCODING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
