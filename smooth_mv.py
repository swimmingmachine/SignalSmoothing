import numpy as np
import matplotlib.pyplot as plt

def mv_filter(signal, window_size=5):
    kernel = np.ones(window_size) / window_size
    smooth_signal = np.convolve(signal, kernel, mode='same')
    return smooth_signal

if __name__ == "__main__":
    # simulate data
    t = np.linspace(0, 1, 500)
    ecg_clean = np.sin(2 * np.pi * 5 * t)
    ecg_noisy = ecg_clean + np.random.normal(0, 0.2, len(t))
    ecg_smooth = mv_filter(ecg_noisy)

    # plot
    plt.figure(figsize=(10, 5))
    plt.plot(t, ecg_noisy, label="Noise ECG", alpha=0.6)
    plt.plot(t, ecg_clean, label="Smoothed ECG", linewidth=2)
    plt.legend()
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("ECG Signal Smoothing with MV filter")
    plt.show()