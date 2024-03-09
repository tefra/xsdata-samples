from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.vms_text import VmsText

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TextPage:
    class Meta:
        name = "_TextPage"

    vms_text: Optional[VmsText] = field(
        default=None,
        metadata={
            "name": "vmsText",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    page_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "pageNumber",
            "type": "Attribute",
            "required": True,
        },
    )
