import wfdb
import numpy as np
import matplotlib.pyplot as plt

# Ref:
# 1. https://kknews.cc/code/amrjjrj.html
# 2. https://stackoverflow.com/questions/58300602/how-to-download-databases-using-wfdb-package

# API:
# 1. https://wfdb.readthedocs.io/en/latest/


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


    # download data
    # wfdb.show_ann_classes()
    # record = wfdb.rdrecord('data/MIT-BIH/100', sampfrom=0, sampto=10000, physical=False, channels=[0, 1])

    # download data
    wfdb.io.get_dbs()
    wfdb.get_record_list('mitdb')
    wfdb.io.dl_database('mitdb', r'./data/mitdb', records='all', annotators='all', keep_subdirs=True, overwrite=False)


    # 讀取本地的100號記錄，從0到25000，通道0
    record = wfdb.rdrecord('./data/mitdb/100', sampfrom=0, sampto=25000, physical=False, channels=[0, ])
    print("record frequency：" + str(record.fs))
    # 讀取前1000數據
    ventricular_signal = record.d_signal[0:1000]
    print('signal shape: ' + str(ventricular_signal.shape))
    # 繪製波形
    plt.plot(ventricular_signal)
    plt.title("ventricular signal")
    plt.show()


    tzu = 1


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
