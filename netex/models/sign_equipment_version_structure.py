from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .audio_trigger_method_enumeration import AudioTriggerMethodEnumeration
from .font_size_enumeration import FontSizeEnumeration
from .multilingual_string import MultilingualString
from .place_equipment_version_structure import PlaceEquipmentVersionStructure
from .print_presentation_structure import PrintPresentationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SignEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "SignEquipment_VersionStructure"

    height: Decimal | None = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Decimal | None = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_from_floor: Decimal | None = field(
        default=None,
        metadata={
            "name": "HeightFromFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    placement: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Placement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    brand_graphic: str | None = field(
        default=None,
        metadata={
            "name": "BrandGraphic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sign_graphic: str | None = field(
        default=None,
        metadata={
            "name": "SignGraphic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    machine_readable: bool | None = field(
        default=None,
        metadata={
            "name": "MachineReadable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    as_braille: bool | None = field(
        default=None,
        metadata={
            "name": "AsBraille",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_trigger_method: AudioTriggerMethodEnumeration | None = field(
        default=None,
        metadata={
            "name": "AudioTriggerMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    printed_presentation: PrintPresentationStructure | None = field(
        default=None,
        metadata={
            "name": "PrintedPresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contrast: Decimal | None = field(
        default=None,
        metadata={
            "name": "Contrast",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    font_size: FontSizeEnumeration | None = field(
        default=None,
        metadata={
            "name": "FontSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
