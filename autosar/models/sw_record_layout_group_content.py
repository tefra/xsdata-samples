from dataclasses import dataclass, field
from typing import List, Optional
from .ref import Ref
from .sw_record_layout_group import SwRecordLayoutGroup
from .sw_record_layout_subtypes_enum import SwRecordLayoutSubtypesEnum
from .sw_record_layout_v import SwRecordLayoutV

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwRecordLayoutGroupContent:
    """This is the contents of a RecordLayout which is inserted for every
    iteration.

    Note that since this is atpMixed, multiple properties can be
    inserted for each iteration.

    :ivar sw_record_layout_ref: This association allows to support
        reusable "sub"-record layouts. In particluar, the contents of
        the referenced record layout shall be used as if the record
        layout group in the referenced record layout was aggregated in
        the current record layout group. So, semantically it would be
        equivalent to replace the particluar association with an
        aggregation of the  swRecordLayoutGroup of the referenced
        SwRecordLayout.
    :ivar sw_record_layout_v: Particular Value specification for this
        record layout group.
    :ivar sw_record_layout_group: This aggregation provides support for
        nested iterations. For example, if a map is to be handled, then
        we might have two nested SwRecordLayoutGroups, one for the
        x-axis and one for the y-axis. The inner iteration runs faster.
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
        name = "SW-RECORD-LAYOUT-GROUP-CONTENT"

    sw_record_layout_ref: List["SwRecordLayoutGroupContent.SwRecordLayoutRef"] = field(
        default_factory=list,
        metadata={
            "name": "SW-RECORD-LAYOUT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_record_layout_v: List[SwRecordLayoutV] = field(
        default_factory=list,
        metadata={
            "name": "SW-RECORD-LAYOUT-V",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_record_layout_group: List[SwRecordLayoutGroup] = field(
        default_factory=list,
        metadata={
            "name": "SW-RECORD-LAYOUT-GROUP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class SwRecordLayoutRef(Ref):
        dest: Optional[SwRecordLayoutSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
