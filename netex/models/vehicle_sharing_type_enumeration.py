from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleSharingTypeEnumeration(StrEnum):
    CAR_SHARING_CLUB = "carSharingClub"
    PEER_TO_PEER_CAR_SHARING = "peerToPeerCarSharing"
    VEHICLE_SHARING = "vehicleSharing"
