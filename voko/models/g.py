from dataclasses import dataclass, field


@dataclass(kw_only=True)
class G:
    class Meta:
        name = "g"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
