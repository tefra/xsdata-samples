from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

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

    height: None | Decimal = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: None | Decimal = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_from_floor: None | Decimal = field(
        default=None,
        metadata={
            "name": "HeightFromFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    placement: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Placement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    brand_graphic: None | str = field(
        default=None,
        metadata={
            "name": "BrandGraphic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sign_graphic: None | str = field(
        default=None,
        metadata={
            "name": "SignGraphic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    machine_readable: None | bool = field(
        default=None,
        metadata={
            "name": "MachineReadable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    as_braille: None | bool = field(
        default=None,
        metadata={
            "name": "AsBraille",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_trigger_method: None | AudioTriggerMethodEnumeration = field(
        default=None,
        metadata={
            "name": "AudioTriggerMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    printed_presentation: None | PrintPresentationStructure = field(
        default=None,
        metadata={
            "name": "PrintedPresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contrast: None | Decimal = field(
        default=None,
        metadata={
            "name": "Contrast",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    font_size: None | FontSizeEnumeration = field(
        default=None,
        metadata={
            "name": "FontSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
