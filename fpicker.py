from flask import Flask, render_template, url_for, request, redirect
import shutil
from pathlib import Path
import random
import re
import argparse
import os


# inputDir = r'D:\paradise\stuff\Images\walls'
def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        try:
            _ = Path(string)
        except:
            raise NotADirectoryError(string)
    return string

parser = argparse.ArgumentParser()

parser.add_argument('--inputConfig', type=dir_path,default= 'config')
parser.add_argument('--port', type=int,default= 5000)

args = parser.parse_args()


cnffile = args.inputConfig
# inputDir = r'C:\Heaven\YummyBaked\SuperWemon4\SuperWemon1\club9'

cdir = []


# allImages =  random.shuffle(allImages)
app = Flask(__name__)

@app.route('/')
def main():
   if len(allImages) <= 0:
        return 'No images left in the directory'
   imgfp = imageRender()
   cpdir = [Path(x).name for x in cdir]
   return render_template("template.html", name=imgfp.name, outDirs=cpdir)
   # return 'hello world'

@app.route('/noteFilePaths',methods=['POST', 'GET'])
def noteDownFilename():
    print(request.args)
    filename = request.args['imgfilename']
    dstfp = Path(__file__).parent / 'static' / 'images' / filename
    for k in request.args:
        v = request.args[k]
        print(k,v)
        
        if 'category' not in k:
            continue
        # import pdb;pdb.set_trace()
        index = int(re.search('\d+',k)[0])
        outfilepath = Path(cdir[index]) / filename
        shutil.copy(dstfp, outfilepath)
    dstfp.unlink()
        
        
    # print(request.args['category1']).
    return redirect(url_for('main'))
   

def imageRender():
    imgfp = allImages.pop()
    dstfp = Path(__file__).parent / 'static' / 'images' / imgfp.name
    dstfp.parent.mkdir(parents=True,exist_ok=True)
    shutil.move(imgfp,dstfp)
    return imgfp

if __name__ == '__main__':
   with open(cnffile,'r+') as fp:
       inputDir = fp.readline().strip()
       for x in fp.readlines():
            line = x.strip()
            cdir.append(line)
   inputDirP = Path(inputDir)
   allImages = [x for x in inputDirP.glob('*.jpg')]
        
   app.run(host="0.0.0.0",port=args.port)