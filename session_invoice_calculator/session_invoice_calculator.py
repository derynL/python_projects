import os
from pydub import AudioSegment
from pydub.silence import detect_silence
import datetime

src = 'audioLibrary'


def check_audio(source):
    duration = 0

    # Time display in seconds to 2 decimal points within 8 spaces
    def ms_print(ms):
        return format(ms / 1000.0, '8.02f') + ' seconds'

    for file in os.scandir(source):
        start = duration
        sound = AudioSegment.from_file(file.path)
        duration += (len(sound))
        silent_ranges = detect_silence(sound, 2000, -30, 1000)
        # Step size 1000 (1s)    = 174.092
        # Step size 100  (1/10s) = 172.292
        # Step size 1    (1ms)   = 170.019

        for start_i, end_i in silent_ranges:
            duration -= end_i - start_i

        # Percentage of non-silent duration in audio formatted to 3 spaces
        # percent = format(str(int(100 * (duration - start) / (len(sound)))), '3')

        # print(ms_print(duration - start), 'of', ms_print(len(sound)), '=', percent + '%', 'Sound', 'in', file.name)

    # print('Total Sound: ', ms_print(duration))
    return duration / 1000


sound_in_seconds = check_audio(src)


def calc_invoice(total_sound):
    invoice_total = 0
    if total_sound <= 180:
        invoice_total = 100
    elif 180 < total_sound <= 360:
        invoice_total = 175
    elif 360 < total_sound <= 600:
        invoice_total = 300
    elif 600 < total_sound <= 750:
        invoice_total = 375
    elif 750 < total_sound <= 1000:
        invoice_total = 450
    elif 1000 < total_sound <= 1250:
        invoice_total = 525
    elif 1250 < total_sound <= 1500:
        invoice_total = 600
    else:
        print('Duration exceeds normal parameters')

    return invoice_total


total_fee = calc_invoice(sound_in_seconds)
print(f'£{total_fee}')
session_audio = str(datetime.timedelta(seconds=sound_in_seconds))
print(session_audio)
