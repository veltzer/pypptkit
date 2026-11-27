""" utils.py """

import os
import subprocess

from pptx import Presentation


def ensure_dir(f: str) -> None:
    folder = os.path.dirname(f)
    if folder != "" and not os.path.isdir(folder):
        os.makedirs(folder)


def touch(f: str) -> None:
    if os.path.isfile(f):
        os.utime(f, None)
    else:
        with open(f, "w"):
            pass


def touch_mkdir(f: str) -> None:
    ensure_dir(f)
    touch(f)


def touch_mkdir_many(filenames: list[str]) -> None:
    for filename in filenames:
        touch_mkdir(filename)


def no_err_run(args: list[str]) -> None:
    assert isinstance(args, list)
    subprocess.call(args)


def get_sorted_refs(filenames: list[str]) -> list[str]:
    refs = set()
    for filename in filenames:
        presentation = Presentation(filename)
        for slide in presentation.slides:
            for v in slide.part.rels.values():
                target: str = v.target_ref
                if target.startswith(".."):
                    continue
                refs.add(target)
    return sorted(refs)


# noinspection PyUnusedLocal
def download(link: str) -> None:
    pass
