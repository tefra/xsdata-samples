from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.position_absolute_enum import (
    PositionAbsoluteEnum,
)
from datexii.models.eu.datexii.v2.position_relative_enum import (
    PositionRelativeEnum,
)
from datexii.models.eu.datexii.v2.vms_supplementary_panel_characteristics import (
    VmsSupplementaryPanelCharacteristics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class VmsPictogramDisplayCharacteristics:
    """
    Characteristics specific to the pictogram display area(s) on the VMS
    where pictogramDisplayAreaIndex indicates which pictogram area it
    relates to.

    :ivar pictogram_lanterns_present: Indicates whether the VMS is
        equipped with flashing lanterns associated with the pictogram
        display area.
    :ivar pictogram_sequencing_capable: Indicates whether the pictogram
        display area on the VMS is capable of sequencing through
        multiple pictograms. True = capable.
    :ivar pictogram_pixels_across: Number of pixels horizontally across
        the pictogram display area of the VMS.
    :ivar pictogram_pixels_down: Number of pixels vertically down the
        pictogram display area of the VMS.
    :ivar pictogram_display_height: The vertical height measured in
        metres of the specific pictogram display area.
    :ivar pictogram_display_width: The horizontal width measured in
        metres of the specific pictogram display area.
    :ivar pictogram_code_list_identifier: Indicates which pictogram code
        list is referenced.
    :ivar max_pictogram_luminance_level: Maximum integer luminance level
        that is available on the pictogram display area of the VMS.
    :ivar pictogram_number_of_colours: The number of colours the
        pictogram display area is capable of rendering.
    :ivar max_number_of_sequential_pictograms: The maximum number of
        pictograms that can be sequenced through on the pictogram
        display area.
    :ivar pictogram_position_absolute: The position of the area in which
        the pictogram is displayed, i.e. at the left, right, top or
        bottom of the VMS display.
    :ivar pictogram_position_x: The X-coordinate (horizontal) position
        of the area in which the pictogram is displayed measured from
        the bottom left of the sign's overall display area to the bottom
        left of the specific pictogram display area.
    :ivar pictogram_position_y: The Y-coordinate (vertical) position of
        the area in which the pictogram is displayed measured from the
        bottom left of the sign's overall display area to the bottom
        left of the specific pictogram display area.
    :ivar pictogram_position_relative_to_text: The position of the area
        in which the pictogram is displayed relative to the textual area
        of the VMS (e.g. to the left, to the right ....).
    :ivar vms_supplementary_panel_characteristics:
    :ivar vms_pictogram_display_characteristics_extension:
    """

    pictogram_lanterns_present: None | bool = field(
        default=None,
        metadata={
            "name": "pictogramLanternsPresent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_sequencing_capable: None | bool = field(
        default=None,
        metadata={
            "name": "pictogramSequencingCapable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_pixels_across: None | int = field(
        default=None,
        metadata={
            "name": "pictogramPixelsAcross",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_pixels_down: None | int = field(
        default=None,
        metadata={
            "name": "pictogramPixelsDown",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_display_height: None | float = field(
        default=None,
        metadata={
            "name": "pictogramDisplayHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_display_width: None | float = field(
        default=None,
        metadata={
            "name": "pictogramDisplayWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_code_list_identifier: None | str = field(
        default=None,
        metadata={
            "name": "pictogramCodeListIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    max_pictogram_luminance_level: None | int = field(
        default=None,
        metadata={
            "name": "maxPictogramLuminanceLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_number_of_colours: None | int = field(
        default=None,
        metadata={
            "name": "pictogramNumberOfColours",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    max_number_of_sequential_pictograms: None | int = field(
        default=None,
        metadata={
            "name": "maxNumberOfSequentialPictograms",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_position_absolute: None | PositionAbsoluteEnum = field(
        default=None,
        metadata={
            "name": "pictogramPositionAbsolute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_position_x: None | float = field(
        default=None,
        metadata={
            "name": "pictogramPositionX",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_position_y: None | float = field(
        default=None,
        metadata={
            "name": "pictogramPositionY",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_position_relative_to_text: None | PositionRelativeEnum = field(
        default=None,
        metadata={
            "name": "pictogramPositionRelativeToText",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_supplementary_panel_characteristics: (
        None | VmsSupplementaryPanelCharacteristics
    ) = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryPanelCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_pictogram_display_characteristics_extension: None | ExtensionType = (
        field(
            default=None,
            metadata={
                "name": "vmsPictogramDisplayCharacteristicsExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
