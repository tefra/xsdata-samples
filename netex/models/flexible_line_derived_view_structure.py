from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration, XmlTime

from .booking_access_enumeration import BookingAccessEnumeration
from .booking_method_enumeration import BookingMethodEnumeration
from .contact_structure import ContactStructure
from .flexible_line_type_enumeration import FlexibleLineTypeEnumeration
from .line_derived_view_structure import LineDerivedViewStructure
from .multilingual_string import MultilingualString
from .purchase_moment_enumeration import PurchaseMomentEnumeration
from .purchase_when_enumeration import PurchaseWhenEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleLineDerivedViewStructure(LineDerivedViewStructure):
    class Meta:
        name = "FlexibleLine_DerivedViewStructure"

    flexible_line_type: None | FlexibleLineTypeEnumeration = field(
        default=None,
        metadata={
            "name": "FlexibleLineType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_contact: None | ContactStructure = field(
        default=None,
        metadata={
            "name": "BookingContact",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_methods: Iterable[BookingMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BookingMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    booking_access: None | BookingAccessEnumeration = field(
        default=None,
        metadata={
            "name": "BookingAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    book_when: None | PurchaseWhenEnumeration = field(
        default=None,
        metadata={
            "name": "BookWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    buy_when: Iterable[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BuyWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    latest_booking_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "LatestBookingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_booking_period: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MinimumBookingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_booking_period: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MaximumBookingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_url: None | str = field(
        default=None,
        metadata={
            "name": "BookingUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_note: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "BookingNote",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
