Modified version of repo [EAST](https://github.com/argman/EAST). Add word recognition implemented by this repo [crnn.pytorch](https://github.com/meijieru/crnn.pytorch).

### How to run this demo

Download the pretrained models of these two repos. Put crnn.pth under recognizer/data, and unzip east\_icdar2015\_resnet\_v1\_50\_rbox.zip into your directory.

Then run ```python run_demo_server.py --checkpoint_path [east_model_dir]```.

Note:
+ Debug is off by default. If you need to turn it on, better turn it on in the codes; otherwise you will get tensorflow parse errors. I am too lazy to fix this LOL.
+ The ```requirements.txt``` is not complete. You should at least install tensorflow and pytorch. Again, I'm too lazy to fix it.

### How to train the models

Go to the repos listed above and follow their instructions. This demo is just for presentation.
