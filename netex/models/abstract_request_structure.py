from __future__ import annotations

from dataclasses import dataclass, field

from .request_timestamp import RequestTimestamp

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractRequestStructure:
    request_timestamp: None | RequestTimestamp = field(
        default=None,
        metadata={
            "name": "RequestTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
