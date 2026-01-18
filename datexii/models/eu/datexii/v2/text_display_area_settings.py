from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vms_luminance_level_enum import (
    VmsLuminanceLevelEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TextDisplayAreaSettings:
    """
    Settings specific to a distinct text display area on the VMS.

    :ivar text_lanterns_on: Indicates if the lanterns are turned on or
        off for the text display area.
    :ivar text_luminance_override: Indicates whether the automatic
        luminance level of the VMS for the text display area is being
        overriden (i.e. by a level set by the instation or operator).
    :ivar text_luminance_level: Luminance level, expressed as an
        integer, that is set for the text display area of the VMS. This
        may be set automatically by the VMS or by the instation or
        operator.
    :ivar text_luminance_level_name: Luminance level, expressed as a
        symbolic name, that is set for the text display area of the VMS.
        This may be set automatically by the VMS or by the instation or
        operator.
    :ivar text_display_area_settings_extension:
    """

    text_lanterns_on: bool | None = field(
        default=None,
        metadata={
            "name": "textLanternsOn",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_luminance_override: bool | None = field(
        default=None,
        metadata={
            "name": "textLuminanceOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_luminance_level: int | None = field(
        default=None,
        metadata={
            "name": "textLuminanceLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_luminance_level_name: VmsLuminanceLevelEnum | None = field(
        default=None,
        metadata={
            "name": "textLuminanceLevelName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_display_area_settings_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "textDisplayAreaSettingsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
