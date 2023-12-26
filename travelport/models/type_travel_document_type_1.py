from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeTravelDocumentType1(Enum):
    """
    Specify the type of Travel Document.
    """

    VISA = "Visa"
    PASSPORT = "Passport"
    DRIVERS_LICENSE = "Drivers License"
    PERMANENT_RESIDENCE_CARD = "Permanent Residence Card"
    NATIONAL_IDENTITY_CARD = "National Identity Card"
    REDRESS_NUMBER = "Redress Number"
    KNOWN_TRAVELER_NUMBER = "Known Traveler Number"
    MILITARY_CARD = "Military Card"
    OTHER = "Other"
