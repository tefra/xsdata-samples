from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .delivery_variant_type_enumeration import DeliveryVariantTypeEnumeration
from .multilingual_string import MultilingualString
from .type_of_delivery_variant_ref import TypeOfDeliveryVariantRef
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeliveryVariantVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "DeliveryVariant_VersionStructure"

    parent_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    delivery_variant_media_type: Optional[DeliveryVariantTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DeliveryVariantMediaType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_delivery_variant_ref: Optional[TypeOfDeliveryVariantRef] = field(
        default=None,
        metadata={
            "name": "TypeOfDeliveryVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    variant_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "VariantText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
