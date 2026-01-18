from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.vms_datex_supplemental_pictogram_enum import (
    VmsDatexSupplementalPictogramEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsSupplementaryPictogram:
    """
    An additional pictogram that is displayed in the panel which is
    supplemental to the associated pictogram display.

    :ivar supplementary_pictogram_description: Description of the
        supplementary displayed pictogram.
    :ivar supplementary_pictogram_code: The code of the supplementary
        pictogram from the supplementary pictogram code list referenced
        in the VmsSupplementaryPanelCharacteristics for the VMS that is
        identified in the relevant VMS Unit table.
    :ivar supplementary_pictogram_url: Reference to a URL from where an
        image of the displayed supplementary pictogram can be be
        obtained.
    :ivar additional_supplementary_pictogram_description: Additional
        free text description of the supplementary pictogram.
    :ivar pictogram_flashing: Indication of whether the pictogram is
        flashing.
    :ivar vms_supplementary_pictogram_extension:
    """

    supplementary_pictogram_description: VmsDatexSupplementalPictogramEnum | None = field(
        default=None,
        metadata={
            "name": "supplementaryPictogramDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    supplementary_pictogram_code: str | None = field(
        default=None,
        metadata={
            "name": "supplementaryPictogramCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    supplementary_pictogram_url: str | None = field(
        default=None,
        metadata={
            "name": "supplementaryPictogramUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    additional_supplementary_pictogram_description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "additionalSupplementaryPictogramDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_flashing: bool | None = field(
        default=None,
        metadata={
            "name": "pictogramFlashing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_supplementary_pictogram_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryPictogramExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
