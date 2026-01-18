from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Url:
    class Meta:
        name = "url"

    ref: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
