from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VmsMessageInformationTypeEnum(Enum):
    """
    Types of information displayable on a VMS.

    :cvar CAMPAIGN_MESSAGE: Campaign type information which is non time
        specific that may request certain actions (e.g. "do not drink
        and drive") or which is intended to influence drivers'
        behaviour.
    :cvar DATE_TIME: Current date and/or time information.
    :cvar FUTURE_INFORMATION: Information which may inform road users
        about future situations which potentially may cause congestion
        or influence future travel plans (e.g. future roadworks,
        closures, sporting events, public concerts, suspension of train
        or ferry services).
    :cvar INSTRUCTION_OR_MESSAGE: Instructions or messages to road users
        which are relevant at the current time, (e.g. "do not throw out
        any burning objects" or an Amber alert message).
    :cvar SITUATION_WARNING: Information warning of a current situation
        likely to affect traffic on the road ahead.
    :cvar TEMPERATURE: Temperature information.
    :cvar TRAFFIC_MANAGEMENT: Information comprising traffic management
        instructions.
    :cvar TRAVEL_TIME: Travel time information.
    """

    CAMPAIGN_MESSAGE = "campaignMessage"
    DATE_TIME = "dateTime"
    FUTURE_INFORMATION = "futureInformation"
    INSTRUCTION_OR_MESSAGE = "instructionOrMessage"
    SITUATION_WARNING = "situationWarning"
    TEMPERATURE = "temperature"
    TRAFFIC_MANAGEMENT = "trafficManagement"
    TRAVEL_TIME = "travelTime"
