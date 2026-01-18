from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location import Location
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.physical_mounting_enum import (
    PhysicalMountingEnum,
)
from datexii.models.eu.datexii.v2.url_link import UrlLink
from datexii.models.eu.datexii.v2.vms_managed_logical_location import (
    VmsManagedLogicalLocation,
)
from datexii.models.eu.datexii.v2.vms_record_pictogram_display_area_index_vms_pictogram_display_characteristics import (
    VmsRecordPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics,
)
from datexii.models.eu.datexii.v2.vms_text_display_characteristics import (
    VmsTextDisplayCharacteristics,
)
from datexii.models.eu.datexii.v2.vms_type_enum import VmsTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class VmsRecord:
    """
    A sub-record in the VMS Unit table defining the characteristics of a
    single variable message sign that is controlled by a specific VMS unit.

    Locations are on or adjacent to the road network but may be updated
    over time if relating to a mobile VMS unit.

    :ivar vms_description: The description of the VMS (possibly giving a
        description of its location or its normal use).
    :ivar vms_owner: Owner (authority or organisation) of the VMS. This
        may not necessarily be the same as the authority or organisation
        which is currently controlling the VMS.
    :ivar vms_physical_mounting: Description of how the VMS is
        physically mounted or deployed on the road.
    :ivar vms_type: Broad classification of the type of variable message
        sign.
    :ivar vms_type_code: Specification of the type of VMS defined by a
        code, normally country or even manufacturer specific (e.g. MS4).
    :ivar number_of_pictogram_display_areas: Number of pictogram display
        areas which the VMS contains.
    :ivar dynamically_configurable_display_areas: Identifies (when True)
        that the VMS has a display area that may be dynamically
        configured to display different combinations of text and
        pictogram areas. The current configuration will normally be
        given with each published current VMS setting.
    :ivar vms_display_height: Height in metres of the sign's overall
        display area.
    :ivar vms_display_width: Width in metres of the sign's overall
        display area.
    :ivar vms_height_above_roadway: Height in metres of the mounted sign
        above the roadway, measured to the bottom of the display area.
    :ivar vms_text_display_characteristics:
    :ivar vms_pictogram_display_characteristics:
    :ivar vms_location: The point location of the variable message sign.
        For mobile VMS which are regularly moved this need not be
        provided. Instead the VMS location should be provided in the
        VmsPublication along with current settings.
    :ivar vms_managed_logical_location:
    :ivar background_image_url: A URL reference from where an image of
        the "painted" static background on the VMS can be obtained.
    :ivar vms_record_extension:
    """

    vms_description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "vmsDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_owner: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "vmsOwner",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_physical_mounting: None | PhysicalMountingEnum = field(
        default=None,
        metadata={
            "name": "vmsPhysicalMounting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_type: None | VmsTypeEnum = field(
        default=None,
        metadata={
            "name": "vmsType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_type_code: None | str = field(
        default=None,
        metadata={
            "name": "vmsTypeCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    number_of_pictogram_display_areas: None | int = field(
        default=None,
        metadata={
            "name": "numberOfPictogramDisplayAreas",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dynamically_configurable_display_areas: None | bool = field(
        default=None,
        metadata={
            "name": "dynamicallyConfigurableDisplayAreas",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_display_height: None | float = field(
        default=None,
        metadata={
            "name": "vmsDisplayHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_display_width: None | float = field(
        default=None,
        metadata={
            "name": "vmsDisplayWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_height_above_roadway: None | float = field(
        default=None,
        metadata={
            "name": "vmsHeightAboveRoadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_text_display_characteristics: None | VmsTextDisplayCharacteristics = (
        field(
            default=None,
            metadata={
                "name": "vmsTextDisplayCharacteristics",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    vms_pictogram_display_characteristics: list[
        VmsRecordPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics
    ] = field(
        default_factory=list,
        metadata={
            "name": "vmsPictogramDisplayCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_location: None | Location = field(
        default=None,
        metadata={
            "name": "vmsLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_managed_logical_location: None | VmsManagedLogicalLocation = field(
        default=None,
        metadata={
            "name": "vmsManagedLogicalLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    background_image_url: None | UrlLink = field(
        default=None,
        metadata={
            "name": "backgroundImageUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_record_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "vmsRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
