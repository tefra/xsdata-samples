from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.data_structure_components_type import (
    DataStructureComponentsType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class DataStructureComponents(DataStructureComponentsType):
    """
    DataStructureComponents defines the grouping of the sets of metadata
    concepts that have a defined structural role in the data structure
    definition.

    Note that for any component or group defined in a data structure
    definition, its id must be unique. This applies to the identifiers
    explicitly defined by the components as well as those inherited from
    the concept identity of a component. For example, if two dimensions
    take their identity from concepts with same identity (regardless of
    whether the concepts exist in different schemes) one of the dimensions
    must be provided a different explicit identifier. Although there are
    XML schema constraints to help enforce this, these only apply to
    explicitly assigned identifiers. Identifiers inherited from a concept
    from which a component takes its identity cannot be validated against
    this constraint. Therefore, systems processing data structure
    definitions will have to perform this check outside of the XML
    validation. There is also one reserved identifier in a data structure
    definition, TIME_PERIOD. This identifier may not be used outside of its
    definition, TimeDimension. This applies to both the explicit
    identifiers that can be assigned to the components or groups as well as
    an identifier inherited by a component from its concept identity. For
    example, if an ordinary dimension (i.e. not the time dimension) takes
    its concept identity from a concept with the identifier TIME_PERIOD,
    that dimension must provide a different explicit identifier.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"
        )
