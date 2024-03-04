
#ilk bölüm
"""
#clone YOLOv5 and
!git clone https://github.com/ultralytics/yolov5  # clone repo
%cd yolov5
%pip install -qr requirements.txt # install dependencies
%pip install -q roboflow

import torch
import os
from IPython.display import Image, clear_output  # to display images

print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

"""



#roboflowdan çekmek için
"""
from roboflow import Roboflow 
rf = Roboflow(model_format="yolov5", notebook="ultralytics") 
"""


#environment kurma
"""
os.environ["DATASET_DIRECTORY"] = "/content/datasets"
"""   


#roboflowdan aldığımız api kodlarını kopyalıyoruz çalıştırınca indirecek
"""
rf = Roboflow(api_key="nhRthX32t5YyR84gj0I2")
project = rf.workspace("samet-yilmaz").project("bottles-kr43e")
dataset = project.version(1).download("yolov5")
"""

#biliyoz bu kısmı
"""
!python train.py --img 416 --batch 16 --epochs 100 --data {dataset.location}/data.yaml --weights yolov5s.pt --cache
"""


# tensorboard'ı başlatıyoruz     
#"runs" isimli dosyanın içine kaydediyoruz
"""
%load_ext tensorboard
%tensorboard --logdir runs
"""
    
#test resimlerimizi modele sokuyoruz ve sonuçlar en sonda belirtilen dosya konumuna kaydediliyor
#her farklı resim veya video eklediğinizde en sondaki exp1 exp2 diye artar. runs/detect/exp
"""
!python detect.py --weights /content/yolov5/best.pt --img 416 --conf 0.2 --source {dataset.location}/valid/images
"""    


#modelden çıkmış olan tüm test verilerini ekrana bastırarak sonuçları inceliyoruz.
"""
import glob
from IPython.display import Image, display

i = 0
# lütfen glob.glob un içine doğru dosya konumunu yazınız üst satırda en altta yazan results saved to runs/detects/exp1 veya runs/detects/exp2 veya runs/detects/exp3
for imageName in glob.glob('/content/yolov5/runs/detect/exp6/*.jpg'): #dosya uzantısını resimlerinizin formatına göre değiştirin jpg olmak zorunda değil.
    i += 1

    if i < 12:
      display(Image(filename=imageName))
      print("\n")
"""



#Modelin ağırlıklarını daha sonra kullanmak için bilgisayarımıza kaydediyoruz
"""
from google.colab import files
files.download('./runs/train/exp/weights/best.pt')
"""

