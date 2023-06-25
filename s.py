import wave
import numpy as np

def split_wav(filename, num_segments):
    # 打开WAV文件
    with wave.open(filename, 'rb') as wav_file:
        # 获取音频参数
        params = wav_file.getparams()
        num_frames = params.nframes
        sample_width = params.sampwidth
        sample_rate = params.framerate
        num_channels = params.nchannels

        # 读取音频数据
        wav_data = wav_file.readframes(num_frames)

        # 将音频数据转换为NumPy数组
        audio = np.frombuffer(wav_data, dtype=np.int16)

        # 计算每个段的帧数
        segment_size = num_frames // num_segments

        # 分割音频并保存为新的WAV文件
        for i in range(num_segments):
            segment_start = i * segment_size
            segment_end = (i + 1) * segment_size
            segment_audio = audio[segment_start:segment_end]

            # 创建新的WAV文件
            segment_filename = f'segment_{i+1}.wav'
            with wave.open(segment_filename, 'wb') as segment_wav:
                segment_wav.setparams(params)
                segment_wav.writeframes(segment_audio.tobytes())

            print(f'Segment {i+1} saved as {segment_filename}.')

# 使用示例
wav_filename = 'audio.wav'
num_segments = 10
split_wav(wav_filename, num_segments)
