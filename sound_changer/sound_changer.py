import pyaudio
import numpy as np
import time

# 初始化PyAudio对象
p = pyaudio.PyAudio()

info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

# for i in range(0, numdevices):
#     if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
#         print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

# 设置音频输入流和输出流
input_stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True, frames_per_buffer=1024)
# Verify the supported channels for the output device
output_device_index = 3
output_device_info = p.get_device_info_by_index(output_device_index)
output_channels = output_device_info.get('maxOutputChannels')

print(output_channels)
if output_channels > 0:
    # Adjust the channels parameter based on the supported channels
    output_stream = p.open(format=pyaudio.paFloat32, channels=min(1, output_channels), rate=44100, output=True, frames_per_buffer=1024, output_device_index=output_device_index)
else:
    raise ValueError(f"Output device {output_device_index} does not support any output channels.")

# 定义变声函数
def pitch_shift(signal, shift=0):
    # 使用傅里叶变换将信号从时域转换到频域
    fft_signal = np.fft.fft(signal)
    fft_freqs = np.fft.fftfreq(len(signal))

    # 计算频率偏移
    shift_amount = int(shift * len(signal) / 44100)

    # 对频域信号进行频率偏移
    fft_signal_shifted = np.roll(fft_signal, shift_amount)
    fft_signal_shifted[:shift_amount] = 0  # 防止频率溢出

    # 使用逆傅里叶变换将信号从频域转换回时域
    signal_shifted = np.fft.ifft(fft_signal_shifted).real
    # 变声实现代码
    return signal_shifted

# 实时变声
while True:
    # 读取音频信号
    data = input_stream.read(1024)

    # 转换为numpy数组
    signal = np.frombuffer(data, dtype=np.float32)

    # 实时变声
    signal_shifted = pitch_shift(signal, shift=2)

    # 将处理后的信号输出
    output_stream.write(signal_shifted.tobytes())

# 关闭流和PyAudio对象
input_stream.stop_stream()
output_stream.stop_stream()
input_stream.close()
output_stream.close()
p.terminate()
