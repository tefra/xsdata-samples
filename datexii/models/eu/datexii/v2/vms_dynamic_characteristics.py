from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vms_dynamic_characteristics_pictogram_display_area_index_vms_pictogram_display_characteristics import (
    VmsDynamicCharacteristicsPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics,
)
from datexii.models.eu.datexii.v2.vms_text_display_characteristics import (
    VmsTextDisplayCharacteristics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsDynamicCharacteristics:
    """
    Provides the current characteristic settings for the VMS which can be
    dynamically configured and therefore which override any corresponding
    characteristics set for the VMS in the relevant VmsUnitPublication.

    :ivar number_of_pictogram_display_areas: Number of pictogram display
        areas which the VMS contains.
    :ivar vms_text_display_characteristics:
    :ivar vms_pictogram_display_characteristics:
    :ivar vms_dynamic_characteristics_extension:
    """

    number_of_pictogram_display_areas: int | None = field(
        default=None,
        metadata={
            "name": "numberOfPictogramDisplayAreas",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_text_display_characteristics: VmsTextDisplayCharacteristics | None = (
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
        VmsDynamicCharacteristicsPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics
    ] = field(
        default_factory=list,
        metadata={
            "name": "vmsPictogramDisplayCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_dynamic_characteristics_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "vmsDynamicCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
