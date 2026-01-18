from __future__ import annotations

from dataclasses import dataclass, field

from .delivery_variant_type_enumeration import DeliveryVariantTypeEnumeration
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .type_of_delivery_variant_ref import TypeOfDeliveryVariantRef
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeliveryVariantVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "DeliveryVariant_VersionStructure"

    parent_ref: None | VersionOfObjectRefStructure = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    delivery_variant_media_type: None | DeliveryVariantTypeEnumeration = field(
        default=None,
        metadata={
            "name": "DeliveryVariantMediaType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_delivery_variant_ref: None | TypeOfDeliveryVariantRef = field(
        default=None,
        metadata={
            "name": "TypeOfDeliveryVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    variant_text: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "VariantText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
