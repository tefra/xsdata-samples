from dataclasses import dataclass, field

from .fulfilment_method_prices_rel_structure import (
    FulfilmentMethodPricesRelStructure,
)
from .fulfilment_method_type_enumeration import FulfilmentMethodTypeEnumeration
from .priceable_object_version_structure import PriceableObjectVersionStructure
from .type_of_travel_document_refs_rel_structure import (
    TypeOfTravelDocumentRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FulfilmentMethodVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "FulfilmentMethod_VersionStructure"

    fulfilment_method_type: FulfilmentMethodTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    requires_card: bool | None = field(
        default=None,
        metadata={
            "name": "RequiresCard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    requires_booking_reference: bool | None = field(
        default=None,
        metadata={
            "name": "RequiresBookingReference",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    types_of_travel_document: TypeOfTravelDocumentRefsRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "typesOfTravelDocument",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    prices: FulfilmentMethodPricesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
