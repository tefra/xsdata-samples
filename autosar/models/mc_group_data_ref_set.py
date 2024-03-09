from dataclasses import dataclass, field
from typing import List, Optional

from .mc_group_data_ref_set_conditional import McGroupDataRefSetConditional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class McGroupDataRefSet:
    """Refers to a set of data assigned to an McGroup in a particular role.

    The data are given
    * either by entries in a FlatMap
    * or by data instances that are part of MC support data.
    These two possibilities can be mixed within a given McGroupDataRefSet.
    Which one to use depends on the process and tool environment.
    The set is subject to variability because the same functional model may be used with various representation of the data.

    :ivar mc_group_data_ref_set_variants: This element was
        generated/modified due to an atpVariation stereotype.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "MC-GROUP-DATA-REF-SET"

    mc_group_data_ref_set_variants: Optional[
        "McGroupDataRefSet.McGroupDataRefSetVariants"
    ] = field(
        default=None,
        metadata={
            "name": "MC-GROUP-DATA-REF-SET-VARIANTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class McGroupDataRefSetVariants:
        mc_group_data_ref_set_conditional: List[
            McGroupDataRefSetConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "MC-GROUP-DATA-REF-SET-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
