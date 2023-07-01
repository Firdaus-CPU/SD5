import os
import math
import subprocess
import pickle
import sys

branchtype = 'lite'

if len(sys.argv) == 2:
    branchargs = sys.argv[1]
    branchtype = branchargs

import gradio as gr

everycolab = f'/content/drive/MyDrive/camendurus/{branchtype}'
everycolabname = []
colabnamepair = []
for colabname in os.listdir(everycolab):
  colabnamepruned = colabname.partition('_webui_colab.ipynb')[0]
  everycolabname.append(colabnamepruned)

sortedcolabname = sorted(everycolabname)

vclvarpath = '/content/drive/MyDrive/vclvariables'

def pickledump(vartodump, outputfile):
  outputpath = os.path.join(vclvarpath, outputfile + '.pkl')
  with open(outputpath, 'wb') as f:
      pickle.dump(vartodump, f)

pickledump(sortedcolabname, 'sortedcolabname')

# chosencolabname = ''

# while True:
#   choosenumber = input('Choose the number of the model you want: ')
#   if choosenumber.isdigit() and int(choosenumber) < totalcolabcount:
#     chosencolabname = sortedcolabname[int(choosenumber)] + '_webui_colab.ipynb'
#     print("Model from " + chosencolabname + " will be downloaded immediately after all the dependencies is installed. Please wait")
#     break
#   elif choosenumber == '':
#     print("No model will be pre-downloaded. Dependencies installation will continue.")
#     break

# aria2c_lines = []

# if chosencolabname:
#    if os.path.exists(os.path.join(everycolab, chosencolabname)):
#       with open(os.path.join(everycolab, chosencolabname), 'r', encoding='utf-8') as f:
#           for line in f:
#               stripped_line = line.strip()
#               if stripped_line.startswith('"!aria2c'):
#                   aria2c_lines.append(stripped_line)

# if aria2c_lines:
#   with open('/content/drive/MyDrive/arialist.pkl', 'wb') as f:
#       pickle.dump(aria2c_lines, f)
