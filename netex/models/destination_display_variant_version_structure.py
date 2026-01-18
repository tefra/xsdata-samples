from __future__ import annotations

from dataclasses import dataclass, field

from .delivery_variant_type_enumeration import DeliveryVariantTypeEnumeration
from .destination_display_context_enumeration import (
    DestinationDisplayContextEnumeration,
)
from .destination_display_ref import DestinationDisplayRef
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .presentation_structure import PresentationStructure
from .vias_rel_structure import ViasRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayVariantVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "DestinationDisplayVariant_VersionStructure"

    destination_display_ref: None | DestinationDisplayRef = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_display_context: (
        None | DestinationDisplayContextEnumeration
    ) = field(
        default=None,
        metadata={
            "name": "DestinationDisplayContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_display_variant_media_type: DeliveryVariantTypeEnumeration = (
        field(
            default=DeliveryVariantTypeEnumeration.ANY,
            metadata={
                "name": "DestinationDisplayVariantMediaType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            },
        )
    )
    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    side_text: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "SideText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    front_text: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "FrontText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    driver_display_text: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "DriverDisplayText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    presentation: None | PresentationStructure = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vias: None | ViasRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
