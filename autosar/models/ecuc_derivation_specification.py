from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import MlFormula
from .ecuc_parameter_derivation_formula import EcucParameterDerivationFormula
from .ecuc_query import EcucQuery

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucDerivationSpecification:
    """Allows to define configuration items that are calculated based on the value of
    * other parameter values
    * elements (attributes/classes) defined in other AUTOSAR templates such as System template and SW component template

    :ivar calculation_formula: Definition of the formula used to
        calculate the value of the configuration element.
    :ivar ecuc_querys: Query to the ECU Configuration Description.
    :ivar informal_formula: Informal description of the derivation used
        to calculate the value of the configuration element.
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
        name = "ECUC-DERIVATION-SPECIFICATION"

    calculation_formula: Optional[EcucParameterDerivationFormula] = field(
        default=None,
        metadata={
            "name": "CALCULATION-FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecuc_querys: Optional["EcucDerivationSpecification.EcucQuerys"] = field(
        default=None,
        metadata={
            "name": "ECUC-QUERYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    informal_formula: Optional[MlFormula] = field(
        default=None,
        metadata={
            "name": "INFORMAL-FORMULA",
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
    class EcucQuerys:
        ecuc_query: List[EcucQuery] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-QUERY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
