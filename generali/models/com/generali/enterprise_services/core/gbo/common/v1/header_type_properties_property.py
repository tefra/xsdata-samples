from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class HeaderTypePropertiesProperty:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    key: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
