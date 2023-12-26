from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.proprietary_data_1 import ProprietaryData1
from travelport.models.type_account_type_profile_info_1 import (
    TypeAccountTypeProfileInfo1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeTravelerInfoHistory1(TypeAccountTypeProfileInfo1):
    """
    History Element for Traveler Info.

    Parameters
    ----------
    proprietary_data
        ProprietaryData for a Traveler which can be overridden for immediate
        parent like BranchGroup,Branch,Account and TravelerGroup.
    passenger_type_code
        Three character code representing a passenger type.
    unique_profile_id
        Used as a primary identification for a traveler profile. Data
        transmitted must be unique for each traveler profile and will be
        validated system wide.
    title
        Util: ReferenceDataRetrieveReq, TypeCode MiscellaneousTable Category
        Code Title.
    nickname
    other_name
    suffix
    birth_date
        Date of Birth of Traveler - YYYY-MM-DD
    gender
        Util: ReferenceDataRetrieveReq, TypeCode PersonGenderType
    vip_status
    job_title
        The job title of the traveler.
    disability
        Text describing a traveler's disability
    home_city_or_airport
        The City or  Airport designated as Home for the traveler
    local_language
        A field to identify the Local Language of the traveler.  This field
        references the ISO 639-1 table and the IETF BCP 47 list to get
        languages.  The expected format would be a 2 letter language code if
        coming from the ISO 639-1 table (xx) or if coming from the IETF BCP
        47 list then it will be a 2 letter language code followed by a 2
        letter qualifier (xx-YY).
    local_language_given_name
    local_language_surname
    local_language_username
    given_name
    surname
    """

    class Meta:
        name = "typeTravelerInfoHistory"

    proprietary_data: list[ProprietaryData1] = field(
        default_factory=list,
        metadata={
            "name": "ProprietaryData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    passenger_type_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            "min_length": 3,
            "max_length": 5,
        },
    )
    unique_profile_id: None | str = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Attribute",
            "min_length": 6,
            "max_length": 128,
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    nickname: None | str = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    other_name: None | str = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    suffix: None | str = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    birth_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Attribute",
        },
    )
    gender: None | str = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        },
    )
    vip_status: bool = field(
        default=False,
        metadata={
            "name": "VipStatus",
            "type": "Attribute",
        },
    )
    job_title: None | str = field(
        default=None,
        metadata={
            "name": "JobTitle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
        },
    )
    disability: None | str = field(
        default=None,
        metadata={
            "name": "Disability",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    home_city_or_airport: None | str = field(
        default=None,
        metadata={
            "name": "HomeCityOrAirport",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    local_language: None | str = field(
        default=None,
        metadata={
            "name": "LocalLanguage",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    local_language_given_name: None | str = field(
        default=None,
        metadata={
            "name": "LocalLanguageGivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    local_language_surname: None | str = field(
        default=None,
        metadata={
            "name": "LocalLanguageSurname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    local_language_username: None | str = field(
        default=None,
        metadata={
            "name": "LocalLanguageUsername",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    given_name: None | str = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
