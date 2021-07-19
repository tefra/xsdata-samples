from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RequestorRef:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[str] = field(
        default=None
    )
