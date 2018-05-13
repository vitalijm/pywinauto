import time

if __package__ is None:
    import sys
    import os

    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

    from pywinauto.application import Application
    from pywinauto.uia_defines import IUIA

    from pywinauto.recorder.uia.uia_recorder import UiaRecorder, ControlTree
else:
    from ...application import Application
    from ...uia_defines import IUIA

    from .uia_recorder import UiaRecorder, ControlTree

import ctypes


def run_tree_test():
    app_path = 'notepad.exe'

    app = Application(backend="uia").start(app_path)
    time.sleep(0.3)

    top_window = app.top_window().wrapper_object()
    # top_window.menu_select('Help->AboutNotepad')
    time.sleep(0.5)

    control_tree = ControlTree(top_window)
    control_tree.print_tree()

    print(app.Dialog.OKButton.element_info)

    # ctypes.wintypes.POINT for ElementFromPoint()
    element = IUIA().iuia.ElementFromPoint(ctypes.wintypes.POINT(10, 10))


def run_recorder_test():
    app_path = os.path.join(os.path.dirname(__file__), r"..\..\..\apps\WPF_samples\WpfApplication1.exe")
    # app_path = 'notepad.exe'

    app = Application(backend="uia").start(app_path)

    rec = UiaRecorder(app=app, record_props=True, record_focus=False, record_struct=False, hot_output=True)
    rec.start()

    rec.wait()

    if not rec.hot_output:
        print("\n===========================================\n")
        print("\n".join(rec.event_log))

    print("\n===========================================\n")
    print(rec.script)


if __name__ == "__main__":
    run_recorder_test()
