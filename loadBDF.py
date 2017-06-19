# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 16:06:38 2017

@author: inaki
"""

# 0- Cargar archivo BDF - raw data

import mne
import numpy as np

raw = mne.io.read_raw_edf("Part_1_N_Trial1_emotion.bdf", stim_channel=None, preload=True) # Se lee el archivo bdf mediante mne

picks = mne.pick_types(raw.info, meg=False, eeg=True, exclude='bads')

array_raw = np.asarray(raw[picks]) # Se pasa a numpy
rows = len(array_raw[0][0]) # numero de filas
frecuencia = int(raw.info['sfreq']) # frecuencia
canales = raw.info['nchan']

# 1.- Acceso a datos raw
# 1.1.- Informacion del archivo
print('Información del archivo BDF leido:')
print(raw.info)

# 1.2.- Canales del archivo BDF
print('Canales del archivo')
print(raw.ch_names)

# 1.3.- Mostrar los datos RAW
start, stop = raw.time_as_index([100, 150])  # segmento de tiempo de 100 a 150
data, times = raw[:, start:stop]
print(data.shape)
print(times.shape)
data, times = raw[2:20:3, start:stop]  # access underlying data
#raw.plot()
#Save a segment of 150s of raw data (MEG only):
picks = mne.pick_types(raw.info, meg=True, eeg=False, stim=True, exclude='bads')
raw.save('sample_audvis_meg_raw.fif', tmin=0, tmax=150, picks=picks, overwrite=True)


# 2.- Lectura y definicion de epochs
#mne.set_config('MNE_STIM_CHANNEL', 'STI101', set_env=True) # Para cambiar el STIM channel
#events = mne.find_events(raw, stim_channel='STI 014')
#print(events[:5])




























