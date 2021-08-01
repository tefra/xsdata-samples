from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.vms_supplementary_pictogram import VmsSupplementaryPictogram
from datexii.models.eu.datexii.v2.vms_text_line import VmsTextLine

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsSupplementaryPanel:
    """
    A panel which may display information or a regulatory instruction which is
    supplemental to the associated pictogram, comprising either an additional
    line of text or a pictogram or both.

    :ivar supplementary_message_description: Free text description of
        the message that is displayed in the panel which is supplemental
        to the main pictogram display.
    :ivar vms_supplementary_pictogram:
    :ivar vms_supplementary_text: One line of text displayed in the
        panel which is supplemental to the pictogram display.
    :ivar vms_supplementary_panel_extension:
    """
    supplementary_message_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "supplementaryMessageDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_supplementary_pictogram: Optional[VmsSupplementaryPictogram] = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryPictogram",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_supplementary_text: Optional[VmsTextLine] = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryText",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_supplementary_panel_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryPanelExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
