from dataclasses import dataclass
from .t_data_store_reference import TDataStoreReference

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class DataStoreReference(TDataStoreReference):
    class Meta:
        name = "dataStoreReference"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
