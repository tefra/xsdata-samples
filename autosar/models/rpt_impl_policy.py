from dataclasses import dataclass, field
from typing import Optional
from .rpt_enabler_impl_type_enum import RptEnablerImplTypeEnum
from .rpt_preparation_enum import RptPreparationEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RptImplPolicy:
    """
    Describes the code preparation for rapid prototyping at data accesses.

    :ivar rpt_enabler_impl_type: For Level 2 or Level3 this property
        determines how the RTE implements the additional „RP enabler"
        flag.
    :ivar rpt_preparation_level: Mandates RP preparation level for
        access to VariableDataPrototype within generated RTE
        implementation.
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
        name = "RPT-IMPL-POLICY"

    rpt_enabler_impl_type: Optional[RptEnablerImplTypeEnum] = field(
        default=None,
        metadata={
            "name": "RPT-ENABLER-IMPL-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rpt_preparation_level: Optional[RptPreparationEnum] = field(
        default=None,
        metadata={
            "name": "RPT-PREPARATION-LEVEL",
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
