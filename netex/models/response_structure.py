from __future__ import annotations

from dataclasses import dataclass, field

from .response_timestamp import ResponseTimestamp

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ResponseStructure:
    response_timestamp: None | ResponseTimestamp = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
