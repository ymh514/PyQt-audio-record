import time
import sys

import PyQt5.QtGui
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot,QSize,QRect
from PyQt5.QtWidgets import QApplication, QPushButton, QTextEdit, QVBoxLayout, QWidget,QMainWindow,QApplication,QPlainTextEdit
from PyQt5.QtGui import QMovie
from PyQt5 import QtGui, QtCore,QtWidgets

from mainwindow import Ui_MainWindow

import pyaudio
import wave
import numpy as np
import struct
import subprocess
import shlex

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
LEVEL = 100 # threshold

# TODO : inference thread

class Recorder(QObject):
    """
    Must derive from QObject in order to emit signals, connect slots to other signals, and operate in a QThread.
    """

    sig_step = pyqtSignal(np.ndarray)  # return record array for draw chart



    frames=[]

    def __init__(self):
        super().__init__()
        self.__abort = False

    def read_data(self,block):
        count = len(block)/2
        format = "%dh"%(count)
        shorts = struct.unpack( format, block )
        return np.array(shorts)

    @pyqtSlot()
    def work(self):
        """
        Pretend this worker method does work that takes a long time. During this time, the thread's
        event loop is blocked, except if the application's processEvents() is called: this gives every
        thread (incl. main) a chance to process events, which in this sample means processing signals
        received from GUI (such as abort).
        """
        print("*  recording")

        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format=FORMAT,
                                   channels=CHANNELS,
                                   rate=RATE,
                                   input=True,
                                   frames_per_buffer=CHUNK)

        while 1:
            # record
            data = self.stream.read(CHUNK)
            # audio_data = np.fromstring(data, dtype=np.short)
            # print(np.max(audio_data))

            self.frames.append(data)
            r_data = self.read_data(data)

            ###
            self.sig_step.emit(r_data)
            app.processEvents()  # this could cause change to self.__abort
            if self.__abort:
                break

    def abort(self):
        print("* end recording")
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()

        # WAVE_OUTPUT_FILENAME = self.nameText.toPlainText() + ".wav"
        WAVE_OUTPUT_FILENAME = "test.wav"

        # original version
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)
        wf.setframerate(RATE)
        wf.writeframes(np.array(self.frames).tostring())
        wf.close()

        self.__abort = True

class Inference(QObject):
<<<<<<< HEAD

    sig_result = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    @pyqtSlot()
    def work(self):
        print("*  Inference")
        p = subprocess.Popen(["./test.sh","-p"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (stdoutput, erroutput) = p.communicate()
        str = stdoutput.decode("utf-8")
        self.sig_result.emit(str)
        self.__abort = True
    def abort(self):
        print("* end Inference")

class MainGui(QMainWindow, Ui_MainWindow):

=======

    sig_result = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    @pyqtSlot()
    def work(self):
        print("*  Inference")
        p = subprocess.Popen(["./test.sh","-p"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (stdoutput, erroutput) = p.communicate()
        str = stdoutput.decode("utf-8")
        self.sig_result.emit(str)
        self.__abort = True
    def abort(self):
        print("* end Inference")

class MainGui(QMainWindow, Ui_MainWindow):

>>>>>>> d21c9d1683c015ef41af7968ff52e94887df48dc
    sig_recorder_abort_workers = pyqtSignal()

    def __init__(self, parent=None):

        super(MainGui, self).__init__(parent)
        self.setupUi(self)
        self.initial_ui()

        # Make any cross object connections.
        self._connectSignals()
        QThread.currentThread().setObjectName('main')  # threads can be named, useful for log output
        self.__threads = None

    def _connectSignals(self):
        ## 放btn connect function
        self.startBtn.clicked.connect(self.start_record)
        self.stopBtn.clicked.connect(self.abort_workers)

    def initial_ui(self):
        # PushButton
        self.startBtn.setEnabled(True)
        self.stopBtn.setDisabled(True)
        # GraphicsView
        self.graphicsView.paused = False
        self.graphicsView.logScale = False
        self.graphicsView.showPeaks = False
        self.graphicsView.downsample = True

        self.graphicsView.p1 = self.graphicsView.addPlot()
        self.graphicsView.p1.setLabel('bottom', 'RowData', 'PCM')
        self.graphicsView.p1.setYRange(0,300)

        self.infoText.setDisabled(True)

        # set waiting gif
        self.movie = QMovie("wait.gif",QtCore.QByteArray(),self)

        self.movie.setCacheMode(QtGui.QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.statusLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.movie.setCacheMode(QtGui.QMovie.CacheAll)

        self.statusLabel.setMovie(self.movie)
        self.movie.start()

        self.statusLabel.hide()

    def get_spectrum(self, data):
        T = 1.0/RATE
        N = data.shape[0]
        Pxx = (1./N)*np.fft.fft(data)
        f = np.fft.fftfreq(N,T)
        Pxx = np.fft.fftshift(Pxx)
        f = np.fft.fftshift(f)
        return f.tolist(), (np.absolute(Pxx)).tolist()

    def start_record(self):
        self.startBtn.setDisabled(True)
        self.stopBtn.setEnabled(True)

        self.__threads = []

        # create a recorder object
        record = Recorder()
        record_thread = QThread()
        record_thread.setObjectName('record thread')
        self.__threads.append((record_thread, record))  # need to store worker too otherwise will be gc'd

        record.moveToThread(record_thread)

        # get progress messages from worker:
        record.sig_step.connect(self.on_recorder_worker_step)

        # control worker:
        self.sig_recorder_abort_workers.connect(record.abort)

        # get read to start worker:record

        record_thread.started.connect(record.work)
        record_thread.start()  # this will emit 'started' and start thread's event loop


    @pyqtSlot(np.ndarray)
    def on_recorder_worker_step(self,r_data):
        # draw gui chart
        f, Pxx = self.get_spectrum(r_data)
        self.graphicsView.p1.plot(x=f, y=Pxx, clear=True)

    def abort_workers(self):
        self.sig_recorder_abort_workers.emit()
        print('Asking each worker to abort')
        for record_thread, record in self.__threads:  # note nice unpacking by Python, avoids indexing
            record_thread.quit()  # this will quit **as soon as thread event loop unblocks**
            record_thread.wait()  # <- so you need to wait for it to *actually* quit
        self.stopBtn.setDisabled(True)
        self.statusLabel.show()

        inference = Inference()
        inference_thread = QThread()
        inference_thread.setObjectName('Inference Thread')
        self.__threads.append((inference_thread, inference))  # need to store worker too otherwise will be gc'd

        inference.moveToThread(inference_thread)
        inference.sig_result.connect(self.on_inference_worker_end)

        inference_thread.started.connect(inference.work)
        inference_thread.start()  # this will emit 'started' and start thread's event loop

    @pyqtSlot(str)
    def on_inference_worker_end(self,str):
        self.statusLabel.hide()
        self.infoText.setEnabled(True)
        self.infoText.setPlainText(str)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName("Audio Device Test")

    audio = MainGui()
    audio.show()

sys.exit(app.exec_())