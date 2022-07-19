from turtle import forward
from flask import Flask, render_template, request
from neuralnetwork.model import Network
import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = './images/' + imagefile.filename
    imagefile.save(image_path)

    model = Network()
    model.load_state_dict(torch.load('./neuralnetwork/checkpoint_14.pth'))

    image = Image.open(image_path)
    convert_tensor = transforms.ToTensor()
    image_tensor = convert_tensor(image)
    img = image_tensor.view(1, 784)
    

    with torch.no_grad():
        logits = model.forward(img)
    
    ps = F.softmax(logits, dim=1)

    classification = ps.argmax()

    return render_template('index.html', prediction = classification.item())

if __name__ == '__main__':
    app.run("0.0.0.0", port=3000, debug=True)
