from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location import Location
from datexii.models.eu.datexii.v2.text_display_area_settings import (
    TextDisplayAreaSettings,
)
from datexii.models.eu.datexii.v2.vms_dynamic_characteristics import (
    VmsDynamicCharacteristics,
)
from datexii.models.eu.datexii.v2.vms_fault import VmsFault
from datexii.models.eu.datexii.v2.vms_managed_logical_location import (
    VmsManagedLogicalLocation,
)
from datexii.models.eu.datexii.v2.vms_message_index_vms_message import (
    VmsMessageIndexVmsMessage,
)
from datexii.models.eu.datexii.v2.vms_pictogram_display_area_index_pictogram_display_area_settings import (
    VmsPictogramDisplayAreaIndexPictogramDisplayAreaSettings,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class Vms:
    """
    Provides the current status and settings of the VMS and the currently
    displayed information.

    Where a VMS is displaying a sequence or alternating set of messages
    these are ordered according to the messageIndex qualifier.

    :ivar vms_working: Indicates whether the VMS is usable. Note it may
        still be usable with minor faults.
    :ivar vms_message_sequencing_interval: The time duration that each
        message is displayed for before the VMS displays the next
        message in the sequence.
    :ivar vms_message:
    :ivar text_display_area_settings:
    :ivar pictogram_display_area_settings:
    :ivar vms_location_override: The current point location of the VMS
        which overrides that stated in the associated VMSTable entry.
        Typically it is used for giving the updated location of a mobile
        VMS which has recently been moved.
    :ivar managed_logical_location_override: The current location that
        is being managed by the VMS which overrides any stated in the
        associated VMSTable entry. Typically it is used for giving the
        updated managed location of a mobile VMS which has recently been
        moved.
    :ivar vms_dynamic_characteristics:
    :ivar vms_fault:
    :ivar vms_extension:
    """

    vms_working: bool = field(
        metadata={
            "name": "vmsWorking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_message_sequencing_interval: None | float = field(
        default=None,
        metadata={
            "name": "vmsMessageSequencingInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_message: list[VmsMessageIndexVmsMessage] = field(
        default_factory=list,
        metadata={
            "name": "vmsMessage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_display_area_settings: None | TextDisplayAreaSettings = field(
        default=None,
        metadata={
            "name": "textDisplayAreaSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pictogram_display_area_settings: list[
        VmsPictogramDisplayAreaIndexPictogramDisplayAreaSettings
    ] = field(
        default_factory=list,
        metadata={
            "name": "pictogramDisplayAreaSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_location_override: None | Location = field(
        default=None,
        metadata={
            "name": "vmsLocationOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    managed_logical_location_override: None | VmsManagedLogicalLocation = (
        field(
            default=None,
            metadata={
                "name": "managedLogicalLocationOverride",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    vms_dynamic_characteristics: None | VmsDynamicCharacteristics = field(
        default=None,
        metadata={
            "name": "vmsDynamicCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_fault: list[VmsFault] = field(
        default_factory=list,
        metadata={
            "name": "vmsFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "vmsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
