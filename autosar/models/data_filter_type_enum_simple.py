from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DataFilterTypeEnumSimple(Enum):
    """
    :cvar ALWAYS: No filtering is performed so that the message always
        passes.
    :cvar MASKED_NEW_DIFFERS_MASKED_OLD: Pass messages where the masked
        value has changed. (new_value&amp;mask) !=(old_value&amp;mask)
        new_value: current value of the message old_value: last value of
        the message (initialized with the initial value of the message,
        updated with new_value if the new message value is not filtered
        out)
    :cvar MASKED_NEW_DIFFERS_X: Pass messages whose masked value is not
        equal to a specific value x (new_value&amp;mask) != x new_value:
        current value of the message
    :cvar MASKED_NEW_EQUALS_X: Pass messages whose masked value is equal
        to a specific value x (new_value&amp;mask) == x new_value:
        current value of the message
    :cvar NEVER: The filter removes all messages.
    :cvar NEW_IS_OUTSIDE: Pass a message if its value is outside a
        predefined boundary. (min &gt; new_value) OR (new_value &gt;
        max)
    :cvar NEW_IS_WITHIN: Pass a message if its value is within a
        predefined boundary. min &lt;= new_value &lt;= max
    :cvar ONE_EVERY_N: Pass a message once every N message occurrences.
        Algorithm: occurrence % period == offset Start: occurrence = 0.
        Each time the message is received or transmitted, occurrence is
        incremented by 1 after filtering. Length of occurrence is 8 bit
        (minimum).
    """

    ALWAYS = "ALWAYS"
    MASKED_NEW_DIFFERS_MASKED_OLD = "MASKED-NEW-DIFFERS-MASKED-OLD"
    MASKED_NEW_DIFFERS_X = "MASKED-NEW-DIFFERS-X"
    MASKED_NEW_EQUALS_X = "MASKED-NEW-EQUALS-X"
    NEVER = "NEVER"
    NEW_IS_OUTSIDE = "NEW-IS-OUTSIDE"
    NEW_IS_WITHIN = "NEW-IS-WITHIN"
    ONE_EVERY_N = "ONE-EVERY-N"
