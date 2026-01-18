from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectServicePermissionStructure:
    value: float | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
