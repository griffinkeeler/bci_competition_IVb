import numpy as np
import mne


def create_info_object(ch_labels: list, fs: float, ch_type: str):
    """
    Creates the MNE info object holding metadata from the
    EEG recording.

    Args:
        ch_labels (list): A list of the channel labels.
        fs (float): The sampling rate in Hz.
        ch_type(str): The type of recording technique (e.g. EEG).

    Returns:
        An MNE data structure which tracks various
        recording details.
    """
    return mne.create_info(ch_names=ch_labels, sfreq=fs, ch_types=ch_type)


def create_raw_array(eeg_data: np.ndarray,
                     info: mne.Info):
    """
    Creates a Raw MNE object from a NumPy array containing
    EEG data and an info MNE object.

    Args:
        eeg_data (np.ndarray): EEG data of shape (time, channels).
        info (mne.Info): An MNE data structure holding metadata from the
        EEG recording.

    Returns:
        mne.io.RawArray: A Raw object from a NumPy array.
    """
    return mne.io.RawArray(data=eeg_data, info=info)