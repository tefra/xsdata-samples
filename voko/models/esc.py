from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Esc:
    class Meta:
        name = "esc"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
