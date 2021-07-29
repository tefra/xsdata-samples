from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParticipantRef:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
