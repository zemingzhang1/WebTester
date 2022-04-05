from functools import partial
import pywebio
from pywebio.input import *
from pywebio.output import *
from zipfile import ZipFile


class APP:

    def __init__(self):
        self.ALIVE = False
        self.figureID = 1
        self.content = None
        self.imgs = []
        self.imgsNames = []


    def START(self):
        put_text("hello world!")


if __name__ == '__main__':
    app = APP()
    pywebio.start_server(app.START, port=511)


