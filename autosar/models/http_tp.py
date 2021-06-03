from dataclasses import dataclass, field
from typing import Optional
from autosar.models.request_method_enum import RequestMethodEnum
from autosar.models.string import String
from autosar.models.tcp_tp import TcpTp
from autosar.models.uri_string import UriString

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

    content_type: Optional[String] = field(
        default=None,
        metadata={
            "name": "CONTENT-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    protocol_version: Optional[String] = field(
        default=None,
        metadata={
            "name": "PROTOCOL-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    request_method: Optional[RequestMethodEnum] = field(
        default=None,
        metadata={
            "name": "REQUEST-METHOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_tp_config: Optional[TcpTp] = field(
        default=None,
        metadata={
            "name": "TCP-TP-CONFIG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    uri: Optional[UriString] = field(
        default=None,
        metadata={
            "name": "URI",
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
