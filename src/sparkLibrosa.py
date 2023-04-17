import os
from pyspark import SparkContext, SparkConf
import librosa
import numpy as np
from sklearn.preprocessing import StandardScaler


def process_audio(audio):
    l=list(audio)
    audio_np = np.array(l)
    # Extracción de características
    zero_crossing_rate = librosa.feature.zero_crossing_rate(audio_np) 

    return zero_crossing_rate #normalized_features



conf = SparkConf().setAppName("AudioProcessingApp")
sc = SparkContext(conf=conf)

# Carga de audio
audio, sr = librosa.load('/data/miaudio1.wav')

# Convierte el objeto de audio en un array NumPy
#audio_np = np.array(audio)

audio_rdd = sc.parallelize(audio) #RDD object

processed_audio_rdd = audio_rdd.mapPartitions(process_audio).collect()

print('-------')
print('-------')
print(f'RDD output: {processed_audio_rdd}')
print('-------')
print('-------')

#output_folder = "/output/librosout"
#processed_audio_rdd.saveAsTextFile(os.path.join(output_folder, "processed_audio.txt"))


