from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class HotelRateByDate:
    """
    The daily rate details.

    Parameters
    ----------
    effective_date
    expire_date
    base
        This attribute is used to describe the Hotel Supplier Base Rate
    tax
        This attribute used to describe Tax associated with the room
    total
        This attribute used to describe Hotel Supplier Total Rate
    surcharge
        This attribute used to describe Surcharge associated with the room
    approximate_base
        Hotel base rate expressed in another currency
    approximate_total
        Hotel total rate expressed in another currency.  Supported
        Providers: 1P
    contents
        Contents will be representing all unformatted data returned by HOST,
        those are not uAPI supported. Support provider 1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    effective_date: None | str = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
        },
    )
    expire_date: None | str = field(
        default=None,
        metadata={
            "name": "ExpireDate",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Attribute",
        },
    )
    tax: None | str = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Attribute",
        },
    )
    total: None | str = field(
        default=None,
        metadata={
            "name": "Total",
            "type": "Attribute",
        },
    )
    surcharge: None | str = field(
        default=None,
        metadata={
            "name": "Surcharge",
            "type": "Attribute",
        },
    )
    approximate_base: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateBase",
            "type": "Attribute",
        },
    )
    approximate_total: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotal",
            "type": "Attribute",
        },
    )
    contents: None | str = field(
        default=None,
        metadata={
            "name": "Contents",
            "type": "Attribute",
        },
    )
