from __future__ import annotations

from dataclasses import dataclass

from .t_parallel_gateway import TParallelGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class ParallelGateway(TParallelGateway):
    class Meta:
        name = "parallelGateway"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
