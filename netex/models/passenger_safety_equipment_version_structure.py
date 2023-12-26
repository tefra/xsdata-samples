from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .audio_announcement_type_enumeration import (
    AudioAnnouncementTypeEnumeration,
)
from .audio_trigger_method_enumeration import AudioTriggerMethodEnumeration
from .lighting_enumeration import LightingEnumeration
from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerSafetyEquipmentVersionStructure(
    PassengerEquipmentVersionStructure
):
    class Meta:
        name = "PassengerSafetyEquipment_VersionStructure"

    cctv: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cctv",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mobile_phone_coverage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MobilePhoneCoverage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    panic_button: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PanicButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sos_phones: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SosPhones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_of_sos_panel: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightOfSosPanel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lighting: Optional[LightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_announcements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    acoustic_announcements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcousticAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_announcement_type: Optional[
        AudioAnnouncementTypeEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "AudioAnnouncementType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_announcements_trigger: Optional[
        AudioTriggerMethodEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "AudioAnnouncementsTrigger",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
