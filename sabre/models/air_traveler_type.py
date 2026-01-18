from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from sabre.models.address_type import AddressType
from sabre.models.air_traveler_type_gender import AirTravelerTypeGender
from sabre.models.air_traveler_type_share_market_ind import (
    AirTravelerTypeShareMarketInd,
)
from sabre.models.air_traveler_type_share_synch_ind import (
    AirTravelerTypeShareSynchInd,
)
from sabre.models.cust_loyalty_type import CustLoyaltyType
from sabre.models.document_type import DocumentType
from sabre.models.email_type import EmailType
from sabre.models.passenger_type_quantity_type import PassengerTypeQuantityType
from sabre.models.person_name_type import PersonNameType
from sabre.models.telephone_type import TelephoneType
from sabre.models.traveler_ref_number_type import TravelerRefNumberType
from sabre.models.unique_id_type import UniqueIdType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class AirTravelerType:
    """
    Information about the person traveling.

    Gender - the gender of the customer, if needed. BirthDate - Date of
    Birth. Currency - the preferred currency in which monetary amounts
    should be returned.

    Attributes:
        profile_ref: Stored information about a customer. May contain
            readily available information relevant to the booking.
        person_name:
        telephone:
        email:
        address:
        cust_loyalty: Specify a customer loyalty program.
        document:
        passenger_type_quantity: Define information on the number of
            passengers of a specific type.
        traveler_ref_number: Direct reference of traveler assigned by
            requesting system. Used as a cross reference between data
            segments.
        flight_segment_rphs: Reference pointers to flight segments
        gender:
        share_synch_ind:
        share_market_ind:
        birth_date: Date of Birth.
        currency_code: The preferred currency in which monetary amounts
            should be returned.
        passenger_type_code: A three-letter code representing passenger
            type (e.g. .ADT. for adult, .CNN. for child)
        accompanied_by_infant: Indicates if an infant accompanying a
            traveler is with or without a seat.
    """

    profile_ref: None | AirTravelerType.ProfileRef = field(
        default=None,
        metadata={
            "name": "ProfileRef",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    person_name: PersonNameType = field(
        metadata={
            "name": "PersonName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    telephone: list[TelephoneType] = field(
        default_factory=list,
        metadata={
            "name": "Telephone",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
        },
    )
    email: list[EmailType] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
        },
    )
    address: list[AddressType] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
        },
    )
    cust_loyalty: list[CustLoyaltyType] = field(
        default_factory=list,
        metadata={
            "name": "CustLoyalty",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
        },
    )
    document: list[DocumentType] = field(
        default_factory=list,
        metadata={
            "name": "Document",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 10,
        },
    )
    passenger_type_quantity: None | PassengerTypeQuantityType = field(
        default=None,
        metadata={
            "name": "PassengerTypeQuantity",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    traveler_ref_number: TravelerRefNumberType = field(
        metadata={
            "name": "TravelerRefNumber",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    flight_segment_rphs: None | AirTravelerType.FlightSegmentRphs = field(
        default=None,
        metadata={
            "name": "FlightSegmentRPHs",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    gender: None | AirTravelerTypeGender = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
        },
    )
    share_synch_ind: None | AirTravelerTypeShareSynchInd = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        },
    )
    share_market_ind: None | AirTravelerTypeShareMarketInd = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        },
    )
    birth_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Attribute",
        },
    )
    currency_code: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    passenger_type_code: str = field(
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    accompanied_by_infant: None | bool = field(
        default=None,
        metadata={
            "name": "AccompaniedByInfant",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ProfileRef:
        unique_id: UniqueIdType = field(
            metadata={
                "name": "UniqueID",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class FlightSegmentRphs:
        """
        Attributes:
            flight_segment_rph: Reference to the flight segments for
                this traveler
        """

        flight_segment_rph: list[str] = field(
            default_factory=list,
            metadata={
                "name": "FlightSegmentRPH",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 99,
                "pattern": r"[0-9]{1,8}",
            },
        )
