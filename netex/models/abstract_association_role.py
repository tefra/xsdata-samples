from dataclasses import dataclass
from netex.models.association_role_type import AssociationRoleType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractAssociationRole(AssociationRoleType):
    class Meta:
        name = "abstractAssociationRole"
        namespace = "http://www.opengis.net/gml/3.2"
