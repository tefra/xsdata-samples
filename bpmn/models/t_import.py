from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TImport:
    class Meta:
        name = "tImport"

    namespace: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    location: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    import_type: str | None = field(
        default=None,
        metadata={
            "name": "importType",
            "type": "Attribute",
            "required": True,
        },
    )
