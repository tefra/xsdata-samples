from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_agency_info_history_ursync_data_2 import TypeAgencyInfoHistoryUrsyncData2
from travelport.models.type_profile_info_2 import TypeProfileInfo2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeAgencyInfoHistory2(TypeProfileInfo2):
    """
    History Element for Agency Info.

    Parameters
    ----------
    name
        Agency name
    iata_number
        Agency IATA number
    agency_code
        Zircon site ID
    uses_template
        If set to true, it denotes that the customer uses templates and
        during parent data inheritance, templates will be used. Value can be
        altered through modify service.Default is false.
    ursync_data
        If set to 'Masked' then Form Of Payment card number will be masked
        when Universal Record is sent to EventHandler.
    ursync_to
        Identify if Universal Record synch is activated at Agency Level.
    """
    class Meta:
        name = "typeAgencyInfoHistory"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    iata_number: None | str = field(
        default=None,
        metadata={
            "name": "IataNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    agency_code: None | str = field(
        default=None,
        metadata={
            "name": "AgencyCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    uses_template: None | bool = field(
        default=None,
        metadata={
            "name": "UsesTemplate",
            "type": "Attribute",
        }
    )
    ursync_data: None | TypeAgencyInfoHistoryUrsyncData2 = field(
        default=None,
        metadata={
            "name": "URSyncData",
            "type": "Attribute",
        }
    )
    ursync_to: None | bool = field(
        default=None,
        metadata={
            "name": "URSyncTo",
            "type": "Attribute",
        }
    )
