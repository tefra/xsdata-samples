from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class AccessEquipmentEnum(Enum):
    """
    Specifies additional equipment for this access.

    :cvar BARRIER: There is a barrier on this entrance or exit. Usually
        access is granted through tickets, buttons or electronic
        systems.
    :cvar TRAFFIC_SIGNAL: There is a traffic signal installation
        controlling this access.
    :cvar TICKET_BUTTON_MACHINE: A machine at this entrance provides a
        parking ticket by pressing a button.
    :cvar TICKET_CARD_MACHINE: A machine at this entrance provides a
        parking ticket by inserting some payment or identity card.
    :cvar PAY_AND_EXIT_MACHINE: A machine at this exit enables payment
        directly by inserting a payment or identity card.
    :cvar OTHER: Other.
    """
    BARRIER = "barrier"
    TRAFFIC_SIGNAL = "trafficSignal"
    TICKET_BUTTON_MACHINE = "ticketButtonMachine"
    TICKET_CARD_MACHINE = "ticketCardMachine"
    PAY_AND_EXIT_MACHINE = "payAndExitMachine"
    OTHER = "other"
