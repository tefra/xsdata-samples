from __future__ import annotations

from dataclasses import dataclass, field

from .compu_generic_math import CompuGenericMath
from .sw_data_dependency_args import SwDataDependencyArgs

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwDataDependency:
    """
    This element describes the interdependencies of data objects, e.g.
    variables and parameters.

    Use cases: * Calculate the value of a calibration parameter (by the MCD
    system) from the value(s) of other calibration parameters. * Virtual
    data - that means the data object is not directly in the ecu and this
    property describes how the "virtual variable" can be computed from the
    real ones (by the MCD system).

    :ivar sw_data_dependency_formula: This element describes the formula
        with which the dependencies between the participating objects
        are defined.
    :ivar sw_data_dependency_args: Specifies the arguments used in the
        data dependency. Note that this is 0..1 since the aggregated
        class is a container (atpMixed).
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
        name = "SW-DATA-DEPENDENCY"

    sw_data_dependency_formula: None | CompuGenericMath = field(
        default=None,
        metadata={
            "name": "SW-DATA-DEPENDENCY-FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_data_dependency_args: None | SwDataDependencyArgs = field(
        default=None,
        metadata={
            "name": "SW-DATA-DEPENDENCY-ARGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
