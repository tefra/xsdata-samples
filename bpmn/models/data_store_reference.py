from __future__ import annotations

from dataclasses import dataclass

from .t_data_store_reference import TDataStoreReference

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class DataStoreReference(TDataStoreReference):
    class Meta:
        name = "dataStoreReference"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
