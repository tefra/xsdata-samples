from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Baz:
    class Meta:
        name = "baz"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
