

# todo

# check
# https://kuleshov.github.io/audio-super-res/
# https://github.com/shun60s/FFT-Wav-UpSampling2

import torch
import torchaudio
from speechbrain.pretrained import SpectralMaskEnhancement

print("yo")

enhance_model = SpectralMaskEnhancement.from_hparams(
    source="speechbrain/metricgan-plus-voicebank",
    savedir="pretrained_models/metricgan-plus-voicebank",
)

noisy = enhance_model.load_audio("gminor.wav").unsqueeze(0)

enhanced = enhance_model.enhance_batch(noisy, lengths=torch.tensor([1.])) # "speechbrain/mtl-mimic-voicebank/example.wav")

torchaudio.save("output.wav", enhanced.cpu, 16000, 'PCM_24')

#torchaudio.save("enhanced.wav", enhanced.unsqueeze(0).cpu, 16000)

print("yo")