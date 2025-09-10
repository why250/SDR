#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def gibbs_phenomenon(max_harmonics=9, sample_rate=1000, duration=5):
    # 时间向量
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # 初始化叠加波形
    wavesum = np.zeros_like(t)

    # 创建图形和轴
    fig, ax = plt.subplots()
    line, = ax.plot(t, wavesum)
    ax.set_title('Gibbs Phenomenon - Sum of Sine Waves')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_ylim(-1.5, 1.5) # 调整Y轴范围以更好地显示波形

    for i in range(1, max_harmonics + 1, 2):
        # 生成正弦波: amplitude = 1/i, frequency = i Hz
        # MATLAB code used `i*2*pi` for frequency, which implies frequency in Hz, not rad/s.
        # So, in Python, we use i directly for frequency in Hz.
        wave = (1/i) * np.sin(2 * np.pi * i * t)
        wavesum = wavesum + wave

        # 更新绘图
        line.set_ydata(wavesum)
        fig.canvas.draw()
        plt.pause(0.5) # 模拟MATLAB的pause(.5)

    plt.show()

if __name__ == '__main__':
    gibbs_phenomenon()
