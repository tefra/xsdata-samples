from dataclasses import dataclass, field
from typing import Optional
from .boolean import Boolean
from .rest_array_property_def import RestArrayPropertyDef
from .rest_boolean_property_def import RestBooleanPropertyDef
from .rest_integer_property_def import RestIntegerPropertyDef
from .rest_number_property_def import RestNumberPropertyDef
from .rest_object_ref import RestObjectRef
from .rest_string_property_def import RestStringPropertyDef

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RestEndpointArgument:
    """
    This meta-class represents the ability to define an argument for a REST
    endpoint.

    :ivar mandatory: This attribute defines whether the argument is
        mandatory or whether it could be left out.
    :ivar parameter: This aggregation represents the concrete kind of
        argument to be used.
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
        name = "REST-ENDPOINT-ARGUMENT"

    mandatory: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "MANDATORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    parameter: Optional["RestEndpointArgument.Parameter"] = field(
        default=None,
        metadata={
            "name": "PARAMETER",
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
    class Parameter:
        rest_array_property_def: Optional[RestArrayPropertyDef] = field(
            default=None,
            metadata={
                "name": "REST-ARRAY-PROPERTY-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        rest_boolean_property_def: Optional[RestBooleanPropertyDef] = field(
            default=None,
            metadata={
                "name": "REST-BOOLEAN-PROPERTY-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        rest_integer_property_def: Optional[RestIntegerPropertyDef] = field(
            default=None,
            metadata={
                "name": "REST-INTEGER-PROPERTY-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        rest_number_property_def: Optional[RestNumberPropertyDef] = field(
            default=None,
            metadata={
                "name": "REST-NUMBER-PROPERTY-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        rest_object_ref: Optional[RestObjectRef] = field(
            default=None,
            metadata={
                "name": "REST-OBJECT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        rest_string_property_def: Optional[RestStringPropertyDef] = field(
            default=None,
            metadata={
                "name": "REST-STRING-PROPERTY-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
