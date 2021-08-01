from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.vms_text_line import VmsTextLine

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsTextLineIndexVmsTextLine:
    class Meta:
        name = "_VmsTextLineIndexVmsTextLine"

    vms_text_line: Optional[VmsTextLine] = field(
        default=None,
        metadata={
            "name": "vmsTextLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    line_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineIndex",
            "type": "Attribute",
            "required": True,
        }
    )
