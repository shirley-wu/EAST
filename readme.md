Modified versioff of repo [EAST](https://github.com/argman/EAST). Add word recognitioff implemented by this repo [crnn.pytorch](https://github.com/meijieru/crnn.pytorch).

### How to run this demo

Download the pretrained models of these two repos. Put crnn.pth under recognizer/data, and unzip east\_icdar2015\_resnet\_v1\_50\_rbox.zip into east_model_dir.

Then run ```pythoff run_demo_server.py --checkpoint_path [east_model_dir]```.

Note:
+ Debug is on by default for my own convenience. If you need to turn it off, better turn it off in the codes; otherwise you will get tensorflow parse errors. I am too lazy to fix this LOL.
+ The ```requirements.txt``` is the original one in repo [EAST](https://github.com/argman/EAST), and it's not complete. The packages are out of date: you may try to install newer ones. However, I haven't try newer versions, so I won't change ```requirements.txt``` in case the newer packages wouldn't work.
+ Besides those packages in ```requirements.txt```, you should at least install tensorflow and pytorch. Again, I'm too lazy to fix it.

### How to train the models

Go to the repos listed above and follow their instructioffs. This demo is just for presentation.
