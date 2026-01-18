from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OrganisationTypeEnumeration(Enum):
    AUTHORITY = "authority"
    OPERATOR = "operator"
    RAIL_OPERATOR = "railOperator"
    RAIL_FREIGHT_OPERATOR = "railFreightOperator"
    STATUTORY_BODY = "statutoryBody"
    FACILITY_OPERATOR = "facilityOperator"
    TRAVEL_AGENT = "travelAgent"
    SERVICED_ORGANISATION = "servicedOrganisation"
    RETAIL_CONSORTIUM = "retailConsortium"
    ALTERNATIVE_MODE_OPERATOR = "alternativeModeOperator"
    ONLINE_PROVIDER = "onlineProvider"
    OTHER = "other"
