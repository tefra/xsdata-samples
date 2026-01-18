from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.vms_text import VmsText

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class TextPage:
    class Meta:
        name = "_TextPage"

    vms_text: VmsText = field(
        metadata={
            "name": "vmsText",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    page_number: int = field(
        metadata={
            "name": "pageNumber",
            "type": "Attribute",
            "required": True,
        }
    )
