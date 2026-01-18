from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileRetrieveHierarchyReq(BaseReq5):
    """
    Request to retrieve the superset of profile levels within an
    agency,agency group or an account.

    Parameters
    ----------
    profile_id
        Agency,AgencyGroup or Account in which the hierarchy is created.
    agency_code
        Specify the AgencyCode Of the Agency in which the hierarchy was
        created.  Accounts and AgencyGroup do not have Provisioning IDs
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
        },
    )
    agency_code: None | str = field(
        default=None,
        metadata={
            "name": "AgencyCode",
            "type": "Element",
            "min_length": 1,
            "max_length": 25,
        },
    )
