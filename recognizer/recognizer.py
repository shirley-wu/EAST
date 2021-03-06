import torch
from torch.autograd import Variable
from . import utils
from . import dataset
import cv2
from .models import crnn


model_path = './recognizer/data/crnn.pth'
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'

model = crnn.CRNN(32, 1, 37, 256)
if torch.cuda.is_available():
    model = model.cuda()
print('loading pretrained model from %s' % model_path)
model.load_state_dict(torch.load(model_path))

converter = utils.strLabelConverter(alphabet)

transformer = dataset.resizeNormalize(32)


def recognize(img):
    if img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = transformer(img)
    # print("image_size", img.size())
    if torch.cuda.is_available():
        img = img.cuda()
    img = img.view(1, *img.size())
    img = Variable(img)

    model.eval()
    preds = model(img)

    _, preds = preds.max(2)
    preds = preds.transpose(1, 0).contiguous().view(-1)

    preds_size = Variable(torch.IntTensor([preds.size(0)]))
    raw_pred = converter.decode(preds.data, preds_size.data, raw=True)
    sim_pred = converter.decode(preds.data, preds_size.data, raw=False)
    return raw_pred + ' => ' + sim_pred
