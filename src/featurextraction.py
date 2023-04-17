# Beat tracking example
import librosa
import numpy as np
from sklearn.preprocessing import StandardScaler

# Carga de audio
audio, sr = librosa.load('/data/miaudio1.wav')

# Extracción de características
zero_crossing_rate = librosa.feature.zero_crossing_rate(audio)
chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
mfcc = librosa.feature.mfcc(y=audio, sr=sr)
rms = librosa.feature.rms(y=audio)
melspectrogram = librosa.feature.melspectrogram(y=audio, sr=sr)

# Concatenación de características
features = np.concatenate((zero_crossing_rate, chroma_stft, mfcc, rms, melspectrogram))

# Normalización características
scaler = StandardScaler()
normalized_features = scaler.fit_transform(features)

print(normalized_features.shape)  # Imprime la forma de la matriz de características normalizadas