from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Sncref:
    class Meta:
        name = "sncref"

    ref: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
