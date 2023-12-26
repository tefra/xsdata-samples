from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SearchAccount:
    """
    Search restriction by Account.

    Parameters
    ----------
    client_id
        Identifier of the corporation this account is for.
    branch_id
        Account Branch ID.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    client_id: None | str = field(
        default=None,
        metadata={
            "name": "ClientID",
            "type": "Attribute",
        },
    )
    branch_id: None | str = field(
        default=None,
        metadata={
            "name": "BranchID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        },
    )
