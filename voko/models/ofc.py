from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Ofc:
    class Meta:
        name = "ofc"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
