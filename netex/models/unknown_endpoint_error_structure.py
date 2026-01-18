from __future__ import annotations

from dataclasses import dataclass, field

from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnknownEndpointErrorStructure(ErrorCodeStructure):
    endpoint: None | str = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
