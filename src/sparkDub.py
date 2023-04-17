from pyspark import SparkContext, SparkConf
from pydub import AudioSegment, effects, scipy_effects
import os

def process_audio(file_path):
    audio = AudioSegment.from_file(file_path, format="wav")
    
    ##  FILTERS PARAMETERS ##
    lpf_freq =  4000 # LowPassFilter frequency, To Be Defined (TBD)
    hpf_freq = 300 # HighPassFilter frequency, TBD
    lbpf_freq = 1000 # LowBandPassFilter frequency, To Be Defined (TBD)
    hbpf_freq= 8000 # HighBandPassFilter frequency, TBD

    ## FILTERS ##
    sound_lpf = effects.low_pass_filter(audio, lpf_freq)
    sound_hpf= effects.high_pass_filter(sound_lpf, hpf_freq)
    #sound_bpf = scipy_effects.band_pass_filter(sound_hpf, lbpf_freq, hbpf_freq)    
    # Normalize filter
    headroom = 3 # Normalize-headroom is how close to the maximum volume to boost the signal up to (specified in dB)
    audio_normalized = effects.normalize(sound_hpf, headroom)

    return audio_normalized



conf = SparkConf().setAppName("AudioProcessingApp")
sc = SparkContext(conf=conf)

audio_folder = "/data"
audio_files = [os.path.join(audio_folder, f) for f in os.listdir(audio_folder) if f.endswith('.wav')]
audio_rdd = sc.parallelize(audio_files)

processed_audio_rdd = audio_rdd.map(process_audio)

output_folder = "/output/audiouts"
processed_audio_rdd.foreach(lambda audio: audio.export(os.path.join(output_folder, "processed_audio.wav"), format="wav"))


