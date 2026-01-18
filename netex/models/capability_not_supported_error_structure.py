from __future__ import annotations

from dataclasses import dataclass, field

from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilityNotSupportedErrorStructure(ErrorCodeStructure):
    capability_ref: str | None = field(
        default=None,
        metadata={
            "name": "CapabilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
