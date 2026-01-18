from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vms_text_line_index_vms_text_line import (
    VmsTextLineIndexVmsTextLine,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsText:
    """
    A page of text (comprising one or more ordered lines) that are
    displayed simultaneously on the VMS.

    Where more than one page is defined these are sequentially displayed
    according to their "pageNumber".

    :ivar vms_legend_code: The code of the legend/text from the legend
        code list referenced in the VmsTextDisplayCharacteristics.
    :ivar vms_text_image_url: Reference to a URL from where an image of
        the displayed legend text can be be obtained.
    :ivar vms_text_line:
    :ivar vms_text_extension:
    """

    vms_legend_code: str | None = field(
        default=None,
        metadata={
            "name": "vmsLegendCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    vms_text_image_url: str | None = field(
        default=None,
        metadata={
            "name": "vmsTextImageUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_text_line: list[VmsTextLineIndexVmsTextLine] = field(
        default_factory=list,
        metadata={
            "name": "vmsTextLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_text_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "vmsTextExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
