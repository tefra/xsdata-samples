from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate, XmlTime
from travelport.models.cabin_info import CabinInfo

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class CruiseStay:
    """
    Provides Cruise information.

    Parameters
    ----------
    package
        Cruise package Details
    cabin_info
    dining_info
        Cruise Dining Details
    ship_name
        Ship name
    duration_of_stay
        Length of stay
    unit_of_stay
        Unit of duration of stay in Days or Night(Value - Day/Night)
    booking_date
        Date when cruise was booked
    booking_agent
        Name of the travel agent booking itinerary.
    booking_credit
        Credit Paid at the time of booking
    other_party_conf_nbr
        Confirm number of the other parties travelling with this party.
    passenger_origin
        Origination city for passenger (not necessarily the city from which
        the cruise embarks).
    confirmation_number
        Confirmation number of cruise segment.
    linked_conf_number
        Linked Cruise Confirmation Number.
    cancellation_number
        Cancellation Number of Cruise Segment.
    cancellation_date
        The date  at which the booking was cancelled.
    cancellation_time
        The time at which the booking was cancelled.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    package: None | CruiseStay.Package = field(
        default=None,
        metadata={
            "name": "Package",
            "type": "Element",
        }
    )
    cabin_info: None | CabinInfo = field(
        default=None,
        metadata={
            "name": "CabinInfo",
            "type": "Element",
        }
    )
    dining_info: None | CruiseStay.DiningInfo = field(
        default=None,
        metadata={
            "name": "DiningInfo",
            "type": "Element",
        }
    )
    ship_name: None | str = field(
        default=None,
        metadata={
            "name": "ShipName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    duration_of_stay: None | int = field(
        default=None,
        metadata={
            "name": "DurationOfStay",
            "type": "Attribute",
        }
    )
    unit_of_stay: None | str = field(
        default=None,
        metadata={
            "name": "UnitOfStay",
            "type": "Attribute",
        }
    )
    booking_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BookingDate",
            "type": "Attribute",
        }
    )
    booking_agent: None | str = field(
        default=None,
        metadata={
            "name": "BookingAgent",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 12,
        }
    )
    booking_credit: None | str = field(
        default=None,
        metadata={
            "name": "BookingCredit",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        }
    )
    other_party_conf_nbr: None | int = field(
        default=None,
        metadata={
            "name": "OtherPartyConfNbr",
            "type": "Attribute",
        }
    )
    passenger_origin: None | str = field(
        default=None,
        metadata={
            "name": "PassengerOrigin",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    confirmation_number: None | str = field(
        default=None,
        metadata={
            "name": "ConfirmationNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    linked_conf_number: None | str = field(
        default=None,
        metadata={
            "name": "LinkedConfNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    cancellation_number: None | str = field(
        default=None,
        metadata={
            "name": "CancellationNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    cancellation_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "CancellationDate",
            "type": "Attribute",
        }
    )
    cancellation_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "CancellationTime",
            "type": "Attribute",
        }
    )

    @dataclass
    class Package:
        """
        Parameters
        ----------
        name
            Cruise package Name
        identifier
            Vendor Package/Tour identifier
        passenger_count
            Number in party
        package_identifier
            Vendor Package/Tour Identifier
        """
        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 30,
            }
        )
        identifier: None | str = field(
            default=None,
            metadata={
                "name": "Identifier",
                "type": "Attribute",
                "max_length": 30,
            }
        )
        passenger_count: None | int = field(
            default=None,
            metadata={
                "name": "PassengerCount",
                "type": "Attribute",
            }
        )
        package_identifier: None | str = field(
            default=None,
            metadata={
                "name": "PackageIdentifier",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 14,
            }
        )

    @dataclass
    class DiningInfo:
        """
        Parameters
        ----------
        seating
            Seating Arrangement. Can be of the following values : '1' -
            First seating, '2' - Second seating
        status
            Status of this dining
        table_size
            Size of the table in number of persons
        """
        seating: None | str = field(
            default=None,
            metadata={
                "name": "Seating",
                "type": "Attribute",
                "length": 1,
            }
        )
        status: None | str = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Attribute",
                "length": 2,
                "white_space": "collapse",
            }
        )
        table_size: None | int = field(
            default=None,
            metadata={
                "name": "TableSize",
                "type": "Attribute",
            }
        )
