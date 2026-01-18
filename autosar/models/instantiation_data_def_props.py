from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .autosar_parameter_ref import AutosarParameterRef
from .autosar_variable_ref import AutosarVariableRef
from .sw_data_def_props import SwDataDefProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class InstantiationDataDefProps:
    """
    This is a general class allowing to apply additional SwDataDefProps to
    particular instantiations of a DataPrototype.

    Typically the accessibility and further information like alias names
    for a particular data is modeled on the level of DataPrototypes
    (especially VariableDataPrototypes, ParameterDataPrototypes). But due
    to the recursive structure of the meta-model concerning data types (a
    composite (data) type consists out of data prototypes) a part of the
    MCD information is described in the data type (in case of
    ApplicationCompositeDataType). This is a strong restriction in the
    reuse of data typed because the data type should be re-used for
    different VariableDataPrototypes and ParameterDataPrototypes to
    guarantee type compatibility on C-implementation level (e.g. data of a
    Port is stored in PIM or a ParameterDataPrototype used as ROM Block and
    shall be typed by the same data type as NVRAM Block). This class
    overcomes such a restriction if applied properly.

    :ivar parameter_instance: This is the particular
        ParameterDataPrototypes on which the swDataDefProps shall be
        applied.
    :ivar sw_data_def_props: These are the particular data definition
        properties which shall be applied
    :ivar variable_instance: This is the particular
        VariableDataPrototypes on which the swDataDefProps shall be
        applied.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "INSTANTIATION-DATA-DEF-PROPS"

    parameter_instance: AutosarParameterRef | None = field(
        default=None,
        metadata={
            "name": "PARAMETER-INSTANCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_data_def_props: SwDataDefProps | None = field(
        default=None,
        metadata={
            "name": "SW-DATA-DEF-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variable_instance: AutosarVariableRef | None = field(
        default=None,
        metadata={
            "name": "VARIABLE-INSTANCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
