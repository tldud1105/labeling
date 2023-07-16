# Utils
useful codes related to labeling
### Last Updated : 2023.07.16


---

## Conver_labels.py



### 1. Copy and Paste xml files

Data Structure
```buildoutcfg
[--example]
├─data
│  └─acne
│      ├─raw
│      │  ├─images
│      │  ├─labels(txt)
│      │  ├─labels(xml)
```

### 2. Write old/new classes.txt files

Data Structure
```buildoutcfg
[--example]
├─data
│  └─acne
│      └─raw
│          │  new_classes.txt
│          │  old_classes.txt
│          │
│          ├─images
│          ├─labels(txt)
│          └─labels(xml)
│                  01na00sy000001kr.xml
│                  01na00sy000002kr.xml
```
```buildoutcfg
# old_classes.txt
dog
person
cat
tv
car
meatballs
marinara sauce
tomato soup
chicken noodle soup
french onion soup
chicken breast
ribs
pulled pork
hamburger
cavity
```
```buildoutcfg
# new_classes.txt
wolf    <- change
gorilla    <- change
cat
tv
car
meatballs
marinara sauce
tomato soup
chicken noodle soup
french onion soup
chicken breast
ribs
pulled pork
```

### 3. CLI command
```buildoutcfg
[--h]
cd utils
python conver_labels.py --old_classes {old_classes} --new_classes {new_classes} --old_ann_dir {old_ann_dir} --ext {ext} --new_ann_dir {new_ann_dir}
[--example]
cd utils
python conver_labels.py --old_classes ../data/acne/raw/old_classes.txt --new_classes ../data/acne/raw/new_classes.txt --old_ann_dir ../data/acne/raw/labels(xml) --ext xml --new_ann_dir ../data/acne/raw/new_labels(xml)
```
- old_classes : The location of the "old_classes.txt" file
- new_classes : The location of the "new_classes.txt" file
- old_ann_dir : The annotation folder you want to convert. (Ex. "labels(xml)" directory)
- ext : The file extension of the annotation you want to convert. (Ex. 'xml') (Currently, only the XML extension is available)
- new_ann_dir : The location where you want to save the converted results

After execution, you will be able to obtain the desired results in the new_ann_dir as follows:
```buildoutcfg
├─data
│  └─acne
│      └─raw
│          │  new_classes.txt
│          │  old_classes.txt
│          │
│          ├─images
│          ├─labels(txt)
│          ├─labels(xml)
│          │      01na00sy000001kr.xml
│          │      01na00sy000002kr.xml
│          │
│          └─new_labels(xml)
│                  01na00sy000001kr.xml
│                  01na00sy000002kr.xml
```
