from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Tezrad:
    class Meta:
        name = "tezrad"

    fak: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
