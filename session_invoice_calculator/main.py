import os
from pydub import AudioSegment
from pydub.silence import detect_silence

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
        percent = format(str(int(100 * (duration - start) / (len(sound)))), '3')

        print(ms_print(duration - start), 'of', ms_print(len(sound)), '=', percent + '%', 'Noise', 'in', file.name)

    print(ms_print(duration), '=', 'Total Noise')


check_audio(src)
