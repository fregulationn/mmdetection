import pdb
import os
import json
import argparse
from lxml.etree import Element, SubElement, tostring, ElementTree
from xml.dom.minidom import parseString
import pickle

json_path = "/home/junjie/Code/tianchi/guangdong/guangdong1_round1_train1_20190818/Annotations/anno_train.json"
output_dir = "/home/junjie/Code/tianchi/guangdong/Label/Annotations/"
name_dict_path = "/home/junjie/Code/tianchi/guangdong/Label/ImageSets/Main/name.pickle"


height = 1000
width = 2446

with open(name_dict_path, 'rb') as handle:
    name_dict = pickle.load(handle)

print(name_dict)

with open(json_path, 'r') as load_f:
    load_dict = json.load(load_f)

for i,load_ann in enumerate(load_dict):
    # build the xml structure
    file_name = load_ann["name"];
    node_root = Element('annotation')
    node_floder = SubElement(node_root, 'floder')
    node_floder.text = 'Cloth'
    node_filename = SubElement(node_root, 'filename')
    node_filename.text = file_name

    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = str(width)
    node_height = SubElement(node_size, 'height')  
    node_height.text = str(height)  
    node_depth = SubElement(node_size, 'depth')  
    node_depth.text = '3'
    
    #every image only has a bbox
    node_object = SubElement(node_root, 'object')    
    node_name = SubElement(node_object, 'name')  
    node_name.text = name_dict[load_ann["defect_name"]]
    node_pose = SubElement(node_object, 'pose')
    node_pose.text = 'Unspecified'
    node_truncated = SubElement(node_object, 'truncated')
    node_truncated.text = str(0)
    node_difficult = SubElement(node_object, 'difficult')
    node_difficult.text = str(0)

    node_bndbox = SubElement(node_object, 'bndbox')  
    node_xmin = SubElement(node_bndbox, 'xmin')  
    node_xmin.text = str(int(load_ann["bbox"][0]))
    node_ymin = SubElement(node_bndbox, 'ymin')  
    node_ymin.text = str(int(load_ann["bbox"][1]))
    node_xmax = SubElement(node_bndbox, 'xmax')  
    node_xmax.text = str(int(load_ann["bbox"][2]))
    node_ymax = SubElement(node_bndbox, 'ymax')  
    node_ymax.text = str(int(load_ann["bbox"][3]))

    xml_dir=output_dir
    if not os.path.exists(xml_dir):
        os.makedirs(xml_dir)
    xml_file = os.path.join(xml_dir, file_name[:-4]+'.xml')
    xml = tostring(node_root, pretty_print=True) 
    dom = parseString(xml)  
    ElementTree(node_root).write(xml_file, pretty_print=True)
