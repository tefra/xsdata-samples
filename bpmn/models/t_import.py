from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TImport:
    class Meta:
        name = "tImport"

    namespace: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    location: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    import_type: str = field(
        metadata={
            "name": "importType",
            "type": "Attribute",
            "required": True,
        }
    )
