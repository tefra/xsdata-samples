from __future__ import annotations

from dataclasses import dataclass, field

from .request_timestamp import RequestTimestamp

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractRequestStructure:
    request_timestamp: RequestTimestamp = field(
        metadata={
            "name": "RequestTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
