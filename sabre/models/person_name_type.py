from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.person_name_type_share_market_ind import (
    PersonNameTypeShareMarketInd,
)
from sabre.models.person_name_type_share_synch_ind import (
    PersonNameTypeShareSynchInd,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class PersonNameType:
    """
    This is an XML Schema representing the OTA Person Name object.

    Attributes:
        name_prefix: Salutation of honorific. (e.g., Mr. Mrs., Ms.,
            Miss, Dr.)
        given_name: Given name, first name or names
        middle_name: Person's middle name
        surname_prefix: e.g "van der", "von", "de"
        surname: Family name, last name.
        name_suffix: Hold various name suffixes and letters (e.g. Jr.,
            Sr., III, Ret., Esq.).
        name_title: Degree or honors (e.g., Ph.D., M.D.)
        share_synch_ind:
        share_market_ind:
        name_type: Type of name of the individual, such as former,
            nickname, alternate or alias name. Refer to OTA Code List
            Name Type (NAM).
    """

    name_prefix: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NamePrefix",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 16,
        },
    )
    given_name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "GivenName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 64,
        },
    )
    middle_name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MiddleName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 64,
        },
    )
    surname_prefix: None | str = field(
        default=None,
        metadata={
            "name": "SurnamePrefix",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    surname: str = field(
        metadata={
            "name": "Surname",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        }
    )
    name_suffix: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 16,
        },
    )
    name_title: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NameTitle",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 16,
        },
    )
    share_synch_ind: None | PersonNameTypeShareSynchInd = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        },
    )
    share_market_ind: None | PersonNameTypeShareMarketInd = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        },
    )
    name_type: None | str = field(
        default=None,
        metadata={
            "name": "NameType",
            "type": "Attribute",
        },
    )
