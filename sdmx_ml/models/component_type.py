from dataclasses import dataclass, field

from sdmx_ml.models.component_base_type import ComponentBaseType
from sdmx_ml.models.representation_type import RepresentationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ComponentType(ComponentBaseType):
    """
    ComponentType is an abstract base type for all components.

    It contains information pertaining to a component, including an
    optional reference to a concept, an optional role played by the
    concept, an optional text format description, and an optional local
    representation.

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
    """

    concept_identity: str | None = field(
        default=None,
        metadata={
            "name": "ConceptIdentity",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.conceptscheme\.Concept=.+",
        },
    )
    local_representation: RepresentationType | None = field(
        default=None,
        metadata={
            "name": "LocalRepresentation",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
