from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal

from .access_equipment_version_structure import AccessEquipmentVersionStructure
from .compass_bearing8_enumeration import CompassBearing8Enumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LiftCallEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "LiftCallEquipment_VersionStructure"

    call_button_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "CallButtonHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    raised_buttons: bool | None = field(
        default=None,
        metadata={
            "name": "RaisedButtons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    braille_buttons: bool | None = field(
        default=None,
        metadata={
            "name": "BrailleButtons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ground_mark_aligned_with_button: bool | None = field(
        default=None,
        metadata={
            "name": "GroundMarkAlignedWithButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_announcements: bool | None = field(
        default=None,
        metadata={
            "name": "AudioAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    magnetic_induction_loop: bool | None = field(
        default=None,
        metadata={
            "name": "MagneticInductionLoop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    door_orientation: Iterable[CompassBearing8Enumeration] = field(
        default_factory=list,
        metadata={
            "name": "DoorOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        },
    )
    monitoring_remote_control: bool | None = field(
        default=None,
        metadata={
            "name": "MonitoringRemoteControl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
