#!/usr/bin/env python3

from datetime import datetime as dt
import locale
import random

print(locale.getlocale())

print(dt.now())


probabilidade = random.random()

if probabilidade < 0.5:
	print("Menor que 0.5")
else:
	print("Maior que 0.5")
