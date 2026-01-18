from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class IncludeTranslations:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
