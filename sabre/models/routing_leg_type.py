from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class RoutingLegType:
    """
    Definition of individual routing legs, at least one leg must be
    present.
    """

    inbound_outbound_carrier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InboundOutboundCarrier",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"\*|[A-Z][A-Z0-9]{1}|[A-Z0-9][A-Z][A-Z0-9]?",
        },
    )
    inbound_carrier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InboundCarrier",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"\*|[A-Z][A-Z0-9]{1}|[A-Z0-9][A-Z][A-Z0-9]?",
        },
    )
    outbound_carrier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OutboundCarrier",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"\*|[A-Z][A-Z0-9]{1}|[A-Z0-9][A-Z][A-Z0-9]?",
        },
    )
    connect_point: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ConnectPoint",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"\*|\?|\+|\.|[A-Z]{3,5}",
        },
    )
