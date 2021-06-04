from dataclasses import dataclass, field
from typing import Optional
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.delivery_variant_type_enumeration import DeliveryVariantTypeEnumeration
from netex.models.destination_display_context_enumeration import DestinationDisplayContextEnumeration
from netex.models.destination_display_ref import DestinationDisplayRef
from netex.models.multilingual_string import MultilingualString
from netex.models.vias_rel_structure import ViasRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DestinationDisplayVariantVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "DestinationDisplayVariant_VersionStructure"

    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_context: Optional[DestinationDisplayContextEnumeration] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_variant_media_type: DeliveryVariantTypeEnumeration = field(
        default=DeliveryVariantTypeEnumeration.ANY,
        metadata={
            "name": "DestinationDisplayVariantMediaType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    side_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "SideText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    front_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "FrontText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_display_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "DriverDisplayText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vias: Optional[ViasRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
