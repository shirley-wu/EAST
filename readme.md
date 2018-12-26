Modified version of repo [EAST](https://github.com/argman/EAST). Add word recognition implemented by this repo [crnn.pytorch](https://github.com/meijieru/crnn.pytorch).

### How to run this demo

Download the pretrained models of these two repos. Put crnn.pth under recognizer/data, and unzip east\_icdar2015\_resnet\_v1\_50\_rbox.zip into east_model_dir.

Then, create a config file by ```mv config.dat.template config.dat```, and change the checkpoint_path param in this file. This is to avoid weird tensorflow errors. You may as well change other params.

Finally, run ```python run_demo_server.py```.

Note:
+ The ```requirements.txt``` is the original one in repo [EAST](https://github.com/argman/EAST), and it's not complete. The packages are out of date: you may try to install newer ones. However, I haven't try newer versions, so I won't change ```requirements.txt``` in case the newer packages wouldn't work.
+ Besides those packages in ```requirements.txt```, you should at least install tensorflow and pytorch. Again, I'm too lazy to fix it.

### How to train the models

Go to the repos listed above and follow their instructions. This demo is just for presentation.
