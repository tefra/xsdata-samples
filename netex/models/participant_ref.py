from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParticipantRef:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[str] = field(
        default=None
    )
