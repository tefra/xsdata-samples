from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.configurable_arrays import ConfigurableArrays
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.format_type import FormatType
from ipxact.models.parameter_type_prefix import ParameterTypePrefix
from ipxact.models.parameter_type_resolve import ParameterTypeResolve
from ipxact.models.parameter_type_unit import ParameterTypeUnit
from ipxact.models.short_description import ShortDescription
from ipxact.models.sign_type import SignType
from ipxact.models.value import Value
from ipxact.models.vectors import Vectors
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ParameterType:
    """
    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar vectors:
    :ivar arrays:
    :ivar value:
    :ivar vendor_extensions:
    :ivar id:
    :ivar parameter_id: ID attribute for uniquely identifying a
        parameter within its document. Attribute is used to refer to
        this from a configurable element.
    :ivar prompt: Provides a string used to prompt the user for user-
        resolved property values.
    :ivar choice_ref: For user defined properties, refers the choice
        element enumerating the values to choose from.
    :ivar order: For components with auto-generated configuration forms,
        the user-resolved properties with order attibutes will be
        presented in ascending order.
    :ivar config_groups: Tags configurable properties so that they may
        be grouped together.  Configurable properties with matching
        values for this attribute are contained in the same group. The
        format of this attribute is a string. There is no semantic
        meaning to this attribute.
    :ivar minimum: For user-resolved properties with numeric values,
        this indicates the minimum value allowed. Only valid for the
        types: byte, shortint, int, longint, shortreal and real. The
        type of this value is the same as the type of the parameter-
        value, which is specified by the parameter-type attribute.
    :ivar maximum: For user-resolved properties with numeric values,
        this indicates the maximum value allowed. Only valid for the
        types: byte, shortint, int, longint, shortreal and real. The
        type of this value is the same as the type of the parameter-
        value, which is specified by the parameter-type attribute.
    :ivar type_value: Specifies the type of the value of the parameter.
        A parameter of type byte is resolved to an 8-bit integer value,
        shortint is resolved to a 16-bit integer value, int is resolved
        to a 32-bit integer value, longint is resolved to a 64-bit
        integer value, shortreal is resolved to a 32-bit floating point
        value, real is resolved to a 64-bit floating point value, bit is
        by default resolved to a one bit value, unless a vector size has
        been specified and the string type is resolved to a string
        value.
    :ivar sign: Specify the signedness explicitly. The data types byte,
        shortint, int, longint default to signed. The data type bit
        defaults to unsigned. When setting this values for the data
        types string, real and shortreal the setting is ignored.
    :ivar prefix: Defines the prefix that precedes the unit of a value.
        The prefix is not applied to the value (e.g. in calculations).
    :ivar unit: Defines the unit of the value.
    :ivar resolve: Determines how a property value can be configured.
    :ivar other_attributes:
    """

    class Meta:
        name = "parameterType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: Optional[ShortDescription] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vectors: Optional[Vectors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    arrays: Optional[ConfigurableArrays] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    parameter_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterId",
            "type": "Attribute",
        },
    )
    prompt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    choice_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "choiceRef",
            "type": "Attribute",
        },
    )
    order: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    config_groups: list[str] = field(
        default_factory=list,
        metadata={
            "name": "configGroups",
            "type": "Attribute",
            "tokens": True,
        },
    )
    minimum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maximum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: FormatType = field(
        default=FormatType.STRING,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    sign: Optional[SignType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    prefix: Optional[ParameterTypePrefix] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    unit: Optional[ParameterTypeUnit] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    resolve: ParameterTypeResolve = field(
        default=ParameterTypeResolve.IMMEDIATE,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
