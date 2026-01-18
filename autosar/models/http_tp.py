from dataclasses import dataclass, field
from typing import Optional

from .request_method_enum import RequestMethodEnum
from .string import String
from .tcp_tp import TcpTp
from .uri_string import UriString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class HttpTp:
    """
    Http over TCP as transport protocol.

    :ivar content_type: Descriptor for the transported content.
    :ivar protocol_version: HTTP Protocol version (e.g. 1.1)
    :ivar request_method: HTTP request method to be used.
    :ivar tcp_tp_config: TcpTp Configuration.
    :ivar uri: URI to be called.
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
        name = "HTTP-TP"

    content_type: String | None = field(
        default=None,
        metadata={
            "name": "CONTENT-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    protocol_version: String | None = field(
        default=None,
        metadata={
            "name": "PROTOCOL-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    request_method: RequestMethodEnum | None = field(
        default=None,
        metadata={
            "name": "REQUEST-METHOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_tp_config: TcpTp | None = field(
        default=None,
        metadata={
            "name": "TCP-TP-CONFIG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    uri: UriString | None = field(
        default=None,
        metadata={
            "name": "URI",
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
