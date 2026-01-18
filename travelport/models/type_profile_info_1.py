from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.client_data_list import ClientDataList

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class TypeProfileInfo1:
    """
    Base type for Profile Infos.

    Parameters
    ----------
    client_data_list
    additional_identifier
        Additional identifier managed by an external system.
    description
    """

    class Meta:
        name = "typeProfileInfo"

    client_data_list: list[ClientDataList] = field(
        default_factory=list,
        metadata={
            "name": "ClientDataList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            "max_occurs": 99,
        },
    )
    additional_identifier: None | str = field(
        default=None,
        metadata={
            "name": "AdditionalIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
