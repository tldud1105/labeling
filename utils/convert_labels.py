import os
import argparse
import xml.etree.ElementTree as ET
from typing import Dict
from tqdm import tqdm


def make_dir(new_ann_dir):
    if not os.path.exists(new_ann_dir):
        os.makedirs(new_ann_dir)


def get_classes(classes_path: str) -> Dict[str, int]:
    with open(classes_path, 'r', encoding='utf-8') as f:
        classes_str = f.read().split()
    classes_ids = list(range(0, len(classes_str)))
    return dict(zip(classes_str, classes_ids))


def get_filenames(old_ann_dir: str):
    filenames = os.listdir(old_ann_dir)
    return filenames


def match_labels(old_classes, new_classes):
    keys_pairs = {key: value for key, value in zip(old_classes.keys(), new_classes.keys())}
    return keys_pairs


def convert_labels(old_ann_dir: str,
                   ext: str,
                   keys_pairs: Dict,
                   new_ann_dir: str):

    ann_filenames = get_filenames(old_ann_dir=old_ann_dir)

    if ext == ('xml' or 'XML'):
        for ann_file in tqdm(ann_filenames):
            ann_path = os.path.join(old_ann_dir, ann_file)
            # Read annotation xml
            ann_tree = ET.parse(ann_path)
            ann_root = ann_tree.getroot()
            for obj in ann_root.findall('object'):
                old_label = obj.findtext('name')
                new_label = keys_pairs.get(old_label)
                if old_label != new_label:
                    print(f"The label inside {ann_file} file has been changed from '{old_label}' to '{new_label}'")
                obj.find('name').text = new_label
            ann_tree.write(os.path.join(new_ann_dir, ann_file))
    return


def main():
    parser = argparse.ArgumentParser(
        description='This script support converting older label to new lable from voc format xmls')
    parser.add_argument('--old_classes', type=str, default=None,
                        help='path to old class list.')
    parser.add_argument('--new_classes', type=str, default=None,
                        help='path to new class list.')
    parser.add_argument('--old_ann_dir', type=str, default=None,
                        help='path to annotation files directory.')
    parser.add_argument('--new_ann_dir', type=str, default=None,
                        help='path of annotation files directory.')
    parser.add_argument('--ext', type=str, default='',
                        help='extension of annotation file')

    args = parser.parse_args()

    old_classes = get_classes(classes_path=args.old_classes)
    new_classes = get_classes(classes_path=args.new_classes)

    keys_pairs = match_labels(old_classes=old_classes, new_classes=new_classes)

    make_dir(args.new_ann_dir)

    convert_labels(old_ann_dir=args.old_ann_dir,
                   ext=args.ext,
                   keys_pairs=keys_pairs,
                   new_ann_dir=args.new_ann_dir)


if __name__ == "__main__":
    main()