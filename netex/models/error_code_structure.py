from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ErrorCodeStructure:
    error_text: str | None = field(
        default=None,
        metadata={
            "name": "ErrorText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    number: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
