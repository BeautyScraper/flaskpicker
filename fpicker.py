from flask import Flask, render_template
import shutil
from pathlib import Path
import random

inputDir = r'D:\paradise\stuff\Images\walls'
# inputDir = r'D:\paradise\stuff\Essence\FS\SachMe'
inputDirP = Path(inputDir)

app = Flask(__name__)

@app.route('/')
def hello_world():
   imgfp = random.choice([x for x in inputDirP.glob('*.jpg')]) 
   dstfp = Path(__file__).parent / 'static' / 'images' / imgfp.name
   dstfp.parent.mkdir(parents=True,exist_ok=True)
   shutil.copy(imgfp,dstfp)
   return render_template("template.html",name=imgfp.name)
   # return 'hello worlfd'

if __name__ == '__main__':
   app.run(host="0.0.0.0")