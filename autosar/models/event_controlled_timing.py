from dataclasses import dataclass, field
from typing import Optional
from .annotation import (
    AdminData,
    DocumentationBlock,
)
from .category_string import CategoryString
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .time_range_type import TimeRangeType

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EventControlledTiming:
    """Specification of a event driven sending behavior. The PDU is sent n
    (numberOfRepeat + 1) times separated by the repetitionPeriod. If
    numberOfRepeats.

    = 0, then the Pdu is sent just once.

    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particlar
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Describable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar admin_data: This represents the administrative data for the
        describable object.
    :ivar number_of_repetitions: Defines the number of repetitions for
        the Direct/N-Times transmission mode and the event driven part
        of Mixed transmission mode.
    :ivar repetition_period: The repetitionPeriod specifies the time in
        seconds that elapses before the pdu can be sent the next time
        (Minimum repeat gap between two pdus). The repetitionPeriod is
        optional in case that no repetitions are configured.
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
        name = "EVENT-CONTROLLED-TIMING"

    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    number_of_repetitions: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "NUMBER-OF-REPETITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    repetition_period: Optional[TimeRangeType] = field(
        default=None,
        metadata={
            "name": "REPETITION-PERIOD",
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
