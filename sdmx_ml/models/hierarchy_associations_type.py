from dataclasses import dataclass, field

from sdmx_ml.models.hierarchy_association_type import HierarchyAssociationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class HierarchyAssociationsType:
    """
    HiearchyAssociationsType describes the structure of the hierarchy
    assoications container.

    It contains one or more hiearchy associations, which can be explicitly
    detailed or referenced from an external structure document or registry
    service.

    :ivar hierarchy_association: HierarchyAssociation provides the
        details of a hiearchy assoication, which associates a hiearchy
        with an identifiable object in the context of another object.
    """

    hierarchy_association: tuple[HierarchyAssociationType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HierarchyAssociation",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
