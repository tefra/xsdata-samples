from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class CodedReasonForSettingMessageEnum(Enum):
    """
    Coded reasons why a message has been selected for display on the sign.

    :cvar SITUATION: Message selected as the result of a situation
        occuring either on or off the road which may affect road users.
    :cvar OPERATOR_CREATED: Message selected by operator as the result
        of an unmanaged event or situation.
    :cvar TRAFFIC_MANAGEMENT: Message selected as part of the
        implementation of a traffic management action. This may or may
        not be part of a specific traffic management or diversion plan.
    :cvar TRAVEL_TIME: VMS is currently selected to display travel
        times.
    :cvar CAMPAIGN: VMS is currently selected to display a campaign
        message.
    :cvar DEFAULT: VMS is currently selected to display default
        information (e.g. time, date, temperature).
    """
    SITUATION = "situation"
    OPERATOR_CREATED = "operatorCreated"
    TRAFFIC_MANAGEMENT = "trafficManagement"
    TRAVEL_TIME = "travelTime"
    CAMPAIGN = "campaign"
    DEFAULT = "default"
