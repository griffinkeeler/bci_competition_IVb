from scipy.io import loadmat


def load_eeg_data(filepath:str):
    """
    Loads continuous EEG data from a Matlab file. The
    data is stored as microvolts.

    Args:
        filepath (str): The path to the file.

    Returns:
         cnt (ndarray): The continuous EEG signals with
          shape [time x channels].
    """
    # Loads the file
    file = loadmat(filepath)

    # Converts the datatype from INT16 to a float
    # Converted to microvolts for MNE
    return file['cnt'].astype('float32') * 0.1


def load_info(filepath: str):
    """
    Loads the structure providing additional information
    for the dataset.

    Args:
        filepath (str): The path to the file.

    Returns:
        nfo (ndarray): An array containing:
        'name': name of the dataset,
        'fs': sampling rate,
        'clab': cell array of channel labels,
        'xpos': x-position of electrodes in a 2d-projections,
        'ypos': y-position of electrodes in a 2d-projection.
    """
    # Loads the file
    file = loadmat(filepath)

    # Steps into the info structure
    return file['nfo'][0, 0]


def load_sampling_rate(filepath: str):
    """
    Loads the sampling rate in Hz from a file.

    Args:
        filepath (str): The path to the file.

    Returns:
        fs (float): The sampling rate in Hz.
    """
    # Loads the info structure
    info = load_info(filepath)

    # Steps into the sampling frequency
    return float(info['fs'][0, 0])


def load_channel_labels(filepath: str):
    """
    Loads a cell array of channel labels from a file.

    Args:
        filepath: The path to the file.

    Returns:
        clab (list): A list of channel labels.
    """
    # Loads the info structure.
    info = load_info(filepath)

    # Steps into the channel labels
    channels = info['clab'][0]

    # Returns the labels as a list
    return [str(ch[0]) for ch in channels]


