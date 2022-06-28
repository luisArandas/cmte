

# todo

# check
# https://kuleshov.github.io/audio-super-res/
# https://github.com/shun60s/FFT-Wav-UpSampling2

# import soundfile as sf
# from speechbrain.pretrained import WaveformEnhancement

# enhance_model = WaveformEnhancement.from_hparams(
#     source="speechbrain/mtl-mimic-voicebank",
#     savedir="pretrained_models/mtl-mimic-voicebank",
# )

# enhanced = enhance_model.enhance_file("speechbrain/mtl-mimic-voicebank/example.wav")

# sf.write("output.wav", enhanced.unsqueeze(0)[0].cpu, 16000, 'PCM_24')

# # torchaudio.save("enhanced.wav", enhanced.unsqueeze(0).cpu, 16000)

# print("yo")