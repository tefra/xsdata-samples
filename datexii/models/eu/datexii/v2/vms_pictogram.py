from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.vms_datex_pictogram_enum import (
    VmsDatexPictogramEnum,
)
from datexii.models.eu.datexii.v2.vms_supplementary_panel import (
    VmsSupplementaryPanel,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsPictogram:
    """
    A main pictogram displayable on the VMS panel.

    Note a main pictogram may have an associated supplementary panel which
    may itself contain a further pictogram and line of text.

    :ivar pictogram_description: Description of the (main) displayed
        pictogram.
    :ivar pictogram_code: The code of the pictogram from the pictogram
        code list referenced in the VmsPictogramDisplayCharacteristics
        for the VMS that is identified in the relevant VMS Unit table.
    :ivar pictogram_url: Reference to a URL from where an image of the
        displayed pictogram can be be obtained.
    :ivar additional_pictogram_description: Additional description of
        the pictogram.
    :ivar pictogram_flashing: Indication of whether the pictogram is
        flashing.
    :ivar pictogram_in_inverse_colour: The pictogram is displayed in
        inverse colour (i.e. the colours are the inverse of normal).
    :ivar presence_of_red_triangle: Indication of the presence of a red
        triangle around the pictogram, often used to indicate imminence,
        typically within 2km, of signed danger.
    :ivar vienna_convention_compliant: Indicates that the displayed
        pictogram conforms with the Vienna Convention defined pictogram
        list as modified by "UNECE Consolidated Resolution on Road Signs
        and Signals".
    :ivar distance_attribute: Value of distance that is displayable as
        part of the pictogram (e.g. for keep minimum safe distance).
    :ivar height_attribute: Value of height that is displayable as part
        of the pictogram (e.g. for a vehicle height restriction).
    :ivar length_attribute: Value of length that is displayable as part
        of the pictogram (e.g. for a vehicle length restriction).
    :ivar speed_attribute: Value of speed that is displayable as part of
        the pictogram (e.g. for a maximum speed limit).
    :ivar weight_attribute: Value of weight that is displayable as part
        of the pictogram (e.g. for a maximum weight restriction).
    :ivar weight_per_axle_attribute: Value of axle weight that is
        displayable as part of the pictogram (e.g. for a maximum axle
        weight restriction).
    :ivar width_attribute: Value of width that is displayable as part of
        the pictogram (e.g. for a vehicle width restriction).
    :ivar vms_supplementary_panel:
    :ivar vms_pictogram_extension:
    """

    pictogram_description: list[VmsDatexPictogramEnum] = field(
        default_factory=list,
        metadata={
            "name": "pictogramDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_code: str | None = field(
        default=None,
        metadata={
            "name": "pictogramCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    pictogram_url: str | None = field(
        default=None,
        metadata={
            "name": "pictogramUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    additional_pictogram_description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "additionalPictogramDescription",
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
    pictogram_in_inverse_colour: bool | None = field(
        default=None,
        metadata={
            "name": "pictogramInInverseColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    presence_of_red_triangle: bool | None = field(
        default=None,
        metadata={
            "name": "presenceOfRedTriangle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    vienna_convention_compliant: bool | None = field(
        default=None,
        metadata={
            "name": "viennaConventionCompliant",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    distance_attribute: int | None = field(
        default=None,
        metadata={
            "name": "distanceAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    height_attribute: float | None = field(
        default=None,
        metadata={
            "name": "heightAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    length_attribute: float | None = field(
        default=None,
        metadata={
            "name": "lengthAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    speed_attribute: float | None = field(
        default=None,
        metadata={
            "name": "speedAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    weight_attribute: float | None = field(
        default=None,
        metadata={
            "name": "weightAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    weight_per_axle_attribute: float | None = field(
        default=None,
        metadata={
            "name": "weightPerAxleAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    width_attribute: float | None = field(
        default=None,
        metadata={
            "name": "widthAttribute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_supplementary_panel: VmsSupplementaryPanel | None = field(
        default=None,
        metadata={
            "name": "vmsSupplementaryPanel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_pictogram_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "vmsPictogramExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
