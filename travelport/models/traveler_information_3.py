from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.phone_number_4 import PhoneNumber4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class TravelerInformation3:
    """
    Traveler Information required for File Finishing.

    Parameters
    ----------
    emergency_contact
    home_airport
    visa_expiration_date
    booking_traveler_ref
        A reference to a passenger.
    """

    class Meta:
        name = "TravelerInformation"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    emergency_contact: None | TravelerInformation3.EmergencyContact = field(
        default=None,
        metadata={
            "name": "EmergencyContact",
            "type": "Element",
        },
    )
    home_airport: None | str = field(
        default=None,
        metadata={
            "name": "HomeAirport",
            "type": "Attribute",
            "length": 3,
        },
    )
    visa_expiration_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "VisaExpirationDate",
            "type": "Attribute",
        },
    )
    booking_traveler_ref: str = field(
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class EmergencyContact:
        """
        Parameters
        ----------
        phone_number
        name
            Name of Emergency Contact Person
        relationship
            Relationship between Traveler and Emergency Contact Person
        """

        phone_number: None | PhoneNumber4 = field(
            default=None,
            metadata={
                "name": "PhoneNumber",
                "type": "Element",
            },
        )
        name: None | object = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            },
        )
        relationship: None | object = field(
            default=None,
            metadata={
                "name": "Relationship",
                "type": "Attribute",
            },
        )
