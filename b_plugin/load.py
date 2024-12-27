import os
import tkinter
from typing import Any, cast
from plugin_dep import get_some_string

def plugin_app(parent: tkinter.Frame) -> tkinter.Frame:
    return parent


def plugin_start3(_path: str) -> str:
    return os.path.basename(os.path.dirname(__file__))

def plugin_prefs(parent_frame: tkinter.Frame, cmdr: str, _beta: bool):
    import myNotebook as nb
    root = cast(nb.Frame, parent_frame)

    frame = nb.Frame(root)
    nb.Label(frame, text=get_some_string()).grid()
    return cast(tkinter.Frame, frame)

def journal_entry(
    cmdr: str,
    _is_beta: bool,
    system: str,
    _station: str,
    entry: dict[str, Any],
    state: dict[str, Any],
):
   pass # Noop