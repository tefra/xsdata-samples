from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.component_type import ComponentType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class GroupDimensionBaseType(ComponentType):
    """
    GroupDimensionBaseType is an abstract base type which refines the base
    ComponentType in order to form the basis for the GroupDimensionType.

    :ivar concept_identity: ConceptIdentity allows for the referencing
        of a concept in a concept scheme. The component takes its
        semantic from this concept, and if an id is not specified, it
        takes its identification as well. If a representation
        (LocalRepresentation) is not supplied, then the representation
        of the component is also inherited from the concept. Note that
        in the case of the component representation being inherited from
        the concept, the allowable representations for the component
        still apply. Therefore, if a component references a concept with
        a core representation that is not allowed for the concept, that
        representation must be locally overridden. For components which
        can specify a concept role, it is implied that the concept which
        is referenced also identifies a role for the component.
    :ivar local_representation: LocalRepresentation references item
        schemes that may be used to create the representation of a
        component. The type of this must be refined such that a concrete
        item scheme reference is used.
    :ivar link:
    :ivar annotations:
    :ivar id:
    :ivar urn:
    :ivar uri:
    """

    concept_identity: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    local_representation: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    link: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    annotations: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    id: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    urn: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    uri: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
