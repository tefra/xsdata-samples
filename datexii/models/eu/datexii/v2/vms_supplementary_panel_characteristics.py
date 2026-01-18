from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.position_relative_enum import (
    PositionRelativeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsSupplementaryPanelCharacteristics:
    """
    Characteristics of a panel which may display details (sometimes
    regulatory in nature) that are supplemental to the main pictogram,
    comprising an additional line of text and/or a pictogram.

    :ivar supplementary_pictogram_code_list_identifier: Indicates which
        supplementary pictogram code list is referenced.
    :ivar supplementary_panel_pixels_across: Number of pixels
        horizontally across the supplementary panel display area.
    :ivar supplementary_panel_pixels_down: Number of pixels vertically
        down the supplementary panel display area.
    :ivar supplementary_panel_display_height: The vertical height
        measured in metres of the supplementary panel display area.
    :ivar supplementary_panel_display_width: The horizontal width
        measured in metres of the supplementary panel display area.
    :ivar supplementary_panel_position_x: The X-coordinate (horizontal)
        position of the supplementary panel measured from the bottom
        left of the sign's overall display area to the bottom left of
        the supplementary panel.
    :ivar supplementary_panel_position_y: The Y-coordinate (vertical)
        position of the supplementary panel measured from the bottom
        left of the sign's overall display area to the bottom left of
        the supplementary panel.
    :ivar relative_position_to_pictogram_area: The position of the panel
        in which the supplementary details are displayed relative to the
        position of the pictogram display area which it is used to
        qualify (e.g. below).
    :ivar vms_supplementary_panel_characteristics_extension:
    """

    supplementary_pictogram_code_list_identifier: str | None = field(
        default=None,
        metadata={
            "name": "supplementaryPictogramCodeListIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    supplementary_panel_pixels_across: int | None = field(
        default=None,
        metadata={
            "name": "supplementaryPanelPixelsAcross",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    supplementary_panel_pixels_down: int | None = field(
        default=None,
        metadata={
            "name": "supplementaryPanelPixelsDown",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    supplementary_panel_display_height: float | None = field(
        default=None,
        metadata={
            "name": "supplementaryPanelDisplayHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    supplementary_panel_display_width: float | None = field(
        default=None,
        metadata={
            "name": "supplementaryPanelDisplayWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    supplementary_panel_position_x: float | None = field(
        default=None,
        metadata={
            "name": "supplementaryPanelPositionX",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    supplementary_panel_position_y: float | None = field(
        default=None,
        metadata={
            "name": "supplementaryPanelPositionY",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    relative_position_to_pictogram_area: PositionRelativeEnum | None = field(
        default=None,
        metadata={
            "name": "relativePositionToPictogramArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_supplementary_panel_characteristics_extension: ExtensionType | None = (
        field(
            default=None,
            metadata={
                "name": "vmsSupplementaryPanelCharacteristicsExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
