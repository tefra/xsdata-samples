from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SomeipMessageTypeEnumSimple(Enum):
    """
    :cvar ERROR: The response containing an error.
    :cvar NOTIFICATION: A request of a notification expecting no
        response.
    :cvar REQUEST: A request expecting a response.
    :cvar REQUEST_NO_RETURN: A fire&amp;forget request.
    :cvar RESPONSE: The response message.
    """

    ERROR = "ERROR"
    NOTIFICATION = "NOTIFICATION"
    REQUEST = "REQUEST"
    REQUEST_NO_RETURN = "REQUEST-NO-RETURN"
    RESPONSE = "RESPONSE"
