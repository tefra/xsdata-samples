from dataclasses import dataclass

from .abstract_geometric_aggregate_type import AbstractGeometricAggregateType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometricAggregate(AbstractGeometricAggregateType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
