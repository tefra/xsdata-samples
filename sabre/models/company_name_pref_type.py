from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.carrier_type import CarrierType
from sabre.models.company_name_type import CompanyNameType
from sabre.models.prefer_level_type import PreferLevelType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class CompanyNamePrefType(CompanyNameType):
    """
    Identifies a preferred company by name.

    Attributes:
        prefer_level:
        type_value: Specify what type  of carrier it comes to.
    """

    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        },
    )
    type_value: None | CarrierType = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
