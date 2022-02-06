from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TImport:
    class Meta:
        name = "tImport"

    namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    import_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "importType",
            "type": "Attribute",
            "required": True,
        }
    )
