"""
Modul to plik z rozszerzeniem .py
"""

import paczka.modul_wewnetrzny

paczka.modul_wewnetrzny.funkcja()

from paczka import modul_wewnetrzny

modul_wewnetrzny.funkcja()

from paczka.modul_wewnetrzny import funkcja

funkcja()

from paczka.modul3 import funkcja as dr

dr()