from .xml_style import XMLDataset
from .registry import DATASETS

@DATASETS.register_module
class ClothDataset(XMLDataset):
    CLASSES = ('weft_shrinking', 'burning_mark', 'flower_board_jump', 'jumping_flower', 'rolling_mark', 'double_weft', 'hanging', 'kou_lu', 'duan_jing', 'mao_li', 'stains', 'broken_hole', 'song_jing', 'slurry_spot', 'three_wire', 'wear_marks', 'scratch', 'thickness', 'rough', 'knot_head', 'rough_dimension', '100_feet', 'star_jump', 'water_stain', 'broken_spandex', 'dead_wrinkle', 'wave_pattern', 'greasy', 'shuangjing', 'zhengjingjie', 'weft_bad', 'yunzhi', 'color_difference', 'jumping_yarn')

    def __init__(self, **kwargs):
        super(ClothDataset, self).__init__(**kwargs)
        self.year = 2012
        