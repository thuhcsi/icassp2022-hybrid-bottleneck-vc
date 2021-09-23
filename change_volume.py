import subprocess
from math import log1p
import os

from numpy.lib.npyio import save
import librosa
import librosa.filters
import numpy as np
from scipy.io import wavfile

wav_path = './audios/PPG_BN/CTC'
save_path = './audios/PPG_BN_/CTC'
def save_wav(wav, path, sr, k=None):
  if k:
    norm_wav = wav * 32767 / max(0.01, np.max(np.abs(wav))) * k
  else:
    norm_wav = wav * 32767
  wavfile.write(path, sr, norm_wav.astype(np.int16))
  return

if __name__=='__main__':
    wavs = os.listdir(wav_path)
    for wav in wavs:
        wav_ = os.path.join(wav_path,wav)
        sav_path = os.path.join(save_path,wav)
        sig, _ = librosa.load(wav_,16000)

        save_wav(sig,sav_path,sr=16000,k=0.1)