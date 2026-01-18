from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.comp_type import CompType
from sdmx_ml.models.metadata_set_type import MetadataSetType

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific"
)


@dataclass(frozen=True)
class GroupTypeAbstract(AnnotableType):
    """
    <ns1:p
    xmlns:ns1="http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific">GroupType
    is the abstract type which defines a structure which is used to
    communicate attribute values for a group defined in a data structure
    definition.

    The group can consist of either a subset of the dimensions defined by
    the data structure definition, or an association to an attachment
    constraint, which in turn defines key sets to which attributes can be
    attached. In the case that the group is based on an attachment
    constraint, only the identification of group is provided. It is
    expected that a system which is processing this will relate that
    identifier to the key sets defined in the constraint and apply the
    values provided for the attributes appropriately.</ns1:p> <ns1:p
    xmlns:ns1="http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific">Data
    structure definition schemas will drive types based on this for each
    group defined in the data structure definition. Both the dimension
    values which make up the key (if applicable) and the attribute values
    associated with the group will be represented with XML attributes. This
    is specified in the content model with the declaration of anyAttributes
    in the "local" namespace. The derived group type will refine this
    structure so that the attributes are explicit. The XML attributes will
    be given a name based on the attribute's identifier. These XML
    attributes will be unqualified (meaning they do not have a namespace
    associated with them). The dimension XML attributes will be required
    while the attribute XML attributes will be optional. To allow for
    generic processing, it is required that the only unqualified XML
    attributes in the derived group type be for the group dimensions and
    data or metadata attributes declared in the data structure definition.
    If additional attributes are required, these should be qualified with a
    namespace so that a generic application can easily distinguish them as
    not being meant to represent a data structure definition dimension or
    attribute.</ns1:p>.

    :ivar comp: Comp contains the details of group level attributes that
        have complex representation and cannot be expressed as XML
        attributes.
    :ivar metadata: Allows for attachment of reference metadata against
        to the group.
    :ivar type_value: The type attribute reference the identifier of the
        group as defined in the data structure definition. This is
        optional, but derived group types will provide a fixed value for
        this so that it always available in the post validation
        information set. This allows the group to be processed in a
        generic manner.
    :ivar local_attributes:
    """

    class Meta:
        name = "GroupType"

    comp: tuple[CompType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Comp",
            "type": "Element",
            "namespace": "",
        },
    )
    metadata: None | MetadataSetType = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    local_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )
