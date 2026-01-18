from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ErrorCodeStructure:
    error_text: None | str = field(
        default=None,
        metadata={
            "name": "ErrorText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    number: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
