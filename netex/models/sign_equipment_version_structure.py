from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .audio_trigger_method_enumeration import AudioTriggerMethodEnumeration
from .installed_equipment_version_structure import InstalledEquipmentVersionStructure
from .multilingual_string import MultilingualString
from .print_presentation_structure import PrintPresentationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SignEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    class Meta:
        name = "SignEquipment_VersionStructure"

    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    height_from_floor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightFromFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    placement: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Placement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    brand_graphic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandGraphic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sign_graphic: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignGraphic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    machine_readable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MachineReadable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    as_braille: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AsBraille",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audio_trigger_method: Optional[AudioTriggerMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "AudioTriggerMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    printed_presentation: Optional[PrintPresentationStructure] = field(
        default=None,
        metadata={
            "name": "PrintedPresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    contrast: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Contrast",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
