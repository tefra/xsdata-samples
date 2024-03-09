from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_account_type_profile_info_1 import (
    TypeAccountTypeProfileInfo1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeAccountInfoHistory1(TypeAccountTypeProfileInfo1):
    """
    History Element for Account Info.

    Parameters
    ----------
    name
        The name of the account.
    local_language_name
        The name of the account in the user's local language.
    """

    class Meta:
        name = "typeAccountInfoHistory"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    local_language_name: None | str = field(
        default=None,
        metadata={
            "name": "LocalLanguageName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
