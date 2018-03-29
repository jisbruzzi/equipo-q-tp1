#!coding=utf8
import os
import random

PREFS_DIR = os.path.join(os.getcwd(), 'prefs')


def generate(prefs: list, n: int, prefix: str):
    for i in range(n):
        current_filename = "{}_{}.prf".format(prefix, str(i + 1))
        path = os.path.join(PREFS_DIR, current_filename)

        random.shuffle(prefs)

        # With open(...) as f: -> estructura tipo RAII de C++, llama al close automáticamente
        with open(path, 'w') as f:
            for j in prefs:
                f.write(str(j) + '\n')
