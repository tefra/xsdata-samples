from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vms_luminance_level_enum import (
    VmsLuminanceLevelEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PictogramDisplayAreaSettings:
    """
    Settings specific to a distinct pictogram display area on the VMS (where
    pictogramIndex indicates which pictogram area it relates to if there is more
    than one pictogram display area on the VMS).

    :ivar pictogram_lanterns_on: Indicates if the lanterns are turned on
        or off for the pictogram display area.
    :ivar pictogram_luminance_override: Indicates whether the automatic
        luminance level of the VMS for the pictogram display area is
        being overriden (i.e. by a level set by the instation or
        operator).
    :ivar pictogram_luminance_level: Luminance level, expressed as an
        integer, that is set for the pictogram display area of the VMS.
        This may be set automatically by the VMS or by the instation or
        operator.
    :ivar pictogram_luminance_level_name: Luminance level, expressed as
        a symbolic name, that is set for the pictogram display area of
        the VMS. This may be set automatically by the VMS or by the
        instation or operator.
    :ivar pictogram_display_area_settings_extension:
    """

    pictogram_lanterns_on: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramLanternsOn",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_luminance_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pictogramLuminanceOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_luminance_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramLuminanceLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_luminance_level_name: Optional[VmsLuminanceLevelEnum] = field(
        default=None,
        metadata={
            "name": "pictogramLuminanceLevelName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_display_area_settings_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pictogramDisplayAreaSettingsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
