from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class FlexrayNmScheduleVariantSimple(Enum):
    """
    :cvar SCHEDULE_VARIANT_1: NM-Vote and NM Data transmitted within one
        PDU in static segment. The NM-Vote has to be realized as
        separate bit within the PDU.
    :cvar SCHEDULE_VARIANT_2: NM-Vote and NM-Data transmitted within one
        PDU in dynamic segment. The presence (or non-presence) of the
        PDU corresponds to the NM-Vote
    :cvar SCHEDULE_VARIANT_3: NM-Vote and NM-Data are transmitted in the
        static segment in separate PDUs. This alternative is not
        recommended =&gt; Alternative 1 should be used instead.
    :cvar SCHEDULE_VARIANT_4: NM-Vote transmitted in static and NM-Data
        transmitted in dynamic segment.
    :cvar SCHEDULE_VARIANT_5: NM-Vote is transmitted in dynamic and NM-
        Data is transmitted in static segment. This alternative is not
        recommended =&gt; Variants 2 or 6 should be used instead.
    :cvar SCHEDULE_VARIANT_6: NM-Vote and NM-Data are transmitted in
        dynamic segment in separate PDUs.
    :cvar SCHEDULE_VARIANT_7: NM-Vote and a copy of the CBV are
        transmitted in the static segment (using the FlexRay NM Vector
        support) and NM-Data is transmitted in the dynamic segment
    """

    SCHEDULE_VARIANT_1 = "SCHEDULE-VARIANT-1"
    SCHEDULE_VARIANT_2 = "SCHEDULE-VARIANT-2"
    SCHEDULE_VARIANT_3 = "SCHEDULE-VARIANT-3"
    SCHEDULE_VARIANT_4 = "SCHEDULE-VARIANT-4"
    SCHEDULE_VARIANT_5 = "SCHEDULE-VARIANT-5"
    SCHEDULE_VARIANT_6 = "SCHEDULE-VARIANT-6"
    SCHEDULE_VARIANT_7 = "SCHEDULE-VARIANT-7"
