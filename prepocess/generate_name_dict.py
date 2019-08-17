import os
import json
import cv2 as cv


json_path = "/home/junjie/Code/tianchi/guangdong/guangdong1_round1_train1_20190809/Annotations/gt_result.json"
name_dict = "/home/junjie/Code/tianchi/guangdong/guangdong1_round1_train1_20190809/Annotations/name.pickle"

with open(json_path, 'r') as load_f:
    load_dict = json.load(load_f)

Set = set()
for load_ann in load_dict:
    Set.add(load_ann["defect_name"])
    
print(len(Set))


# names = ['纬缩', '烧毛痕', '花板跳', '跳花', '轧痕', '双纬', '吊经', '筘路', '断经', '毛粒', '污渍', '破洞', '松经', '浆斑', '三丝', '磨痕', '修痕', '稀密档', '粗经', '结头', '粗维', '百脚', '星跳', '水渍', '断氨纶', '死皱', '浪纹档', '油渍']
# translates = ['weft_shrinking', 'burning_mark', 'flower_board_jump', 'jumping_flower', 'rolling_mark', 'double_weft', 'hanging', 'kou_lu', 'duan_jing', 'mao_li', 'stains', 'broken_hole', 'song_jing', 'slurry_spot', 'three_wire', 'wear_marks', 'scratch', 'thickness', 'rough', 'knot_head', 'rough_dimension', '100_feet', 'star_jump', 'water_stain', 'broken_spandex', 'dead_wrinkle', 'wave_pattern', 'greasy']

# dict = {}
# for i,name in enumerate(names):
#     dict[name] = translates[i]

# print(dict)

    

# import pickle
# with open(name_dict, 'wb') as handle:
#     pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)







# PRINT_IMAGE_SIZE

# path = "/home/junjie/Code/tianchi/guangdong/guangdong1_round1_train1_20190809/defect_Images"
# filenames = os.listdir(path)

# for filename in filenames:
#     img = cv.imread(path+"/" + filename)
#     print(img.shape)
    


