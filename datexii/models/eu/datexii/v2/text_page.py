from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.vms_text import VmsText

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TextPage:
    class Meta:
        name = "_TextPage"

    vms_text: VmsText | None = field(
        default=None,
        metadata={
            "name": "vmsText",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    page_number: int | None = field(
        default=None,
        metadata={
            "name": "pageNumber",
            "type": "Attribute",
            "required": True,
        },
    )
