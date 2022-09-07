from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class ArticleDtdVersion(Enum):
    VALUE_0_4 = "0.4"
    VALUE_1_0 = "1.0"
    VALUE_1_1 = "1.1"
    VALUE_1_1D1 = "1.1d1"
    VALUE_1_1D2 = "1.1d2"
    VALUE_1_1D3 = "1.1d3"
    VALUE_1_2 = "1.2"
    VALUE_1_2D1 = "1.2d1"
    VALUE_1_2D2 = "1.2d2"
    VALUE_1_3D1 = "1.3d1"
    VALUE_1_3D2 = "1.3d2"
    VALUE_3_0 = "3.0"
