# labeling
tools for labeling

---

## labelimg

### Installation

1. Creating an Anaconda virtual environment
```buildoutcfg
conda create --name labeling python=3.8 -y
activate labeling
```

2. Git clone 'labelimg'
```buildoutcfg
cd {work_dir}
git clone https://github.com/heartexlabs/labelImg.git
cd labelImg
```

3. Installing required libraries
```buildoutcfg
pip install pyqt5
pip install lxml
```

4. Enter the 'pyrcc5' command
```buildoutcfg
pyrcc5 -o libs/resources.py resources.qrc
```

5. Run the 'labelimg.py' file in the terminal window
```buildoutcfg
python labelimg.py
```

### Modify the Label class

You can specify labels from the predefined_classes.txt file
```
├─labelImg
│  └─data
│     └─predefined_classes.txt
```

```
# predefined_classes.txt
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