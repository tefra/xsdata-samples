from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Autoro:
    class Meta:
        name = "autoro"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
