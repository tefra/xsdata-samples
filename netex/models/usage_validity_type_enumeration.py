from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageValidityTypeEnumeration(StrEnum):
    SINGLE_RIDE = "singleRide"
    SINGLE_TRIP = "singleTrip"
    RETURN_TRIP = "returnTrip"
    CARNET = "carnet"
    DAY_PASS = "dayPass"
    WEEKLY_PASS = "weeklyPass"
    WEEKEND_PASS = "weekendPass"
    MONTHLY_PASS = "monthlyPass"
    ANNUAL_PASS = "annualPass"
    SEASON_TICKET = "seasonTicket"
    PROFILE_MEMBERSHIP = "profileMembership"
    SUBSCRIPTION = "subscription"
    OPEN_ENDED = "openEnded"
    CAP = "cap"
    OTHER = "other"
