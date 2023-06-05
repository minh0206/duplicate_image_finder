from dif import dif
from PyQt5.QtCore import pyqtSignal


class Search:
    def __init__(self) -> None:
        self.result = None

    def run(self, folder, processCallback):
        search = SearchEngine(directory=folder, processCallback=processCallback)
        self.result = search.result


class SearchEngine(dif):
    def __init__(
        self,
        *directory,
        processCallback=None,
        fast_search=True,
        recursive=True,
        limit_extensions=False,
        similarity="duplicates",
        px_size=50,
        show_progress=True,
        show_output=False,
        move_to=None,
        delete=False,
        silent_del=False,
        logs=False,
    ):
        super().__init__(
            *directory,
            fast_search=fast_search,
            recursive=recursive,
            limit_extensions=limit_extensions,
            similarity=similarity,
            px_size=px_size,
            show_progress=show_progress,
            show_output=show_output,
            move_to=move_to,
            delete=delete,
            silent_del=silent_del,
            logs=logs,
        )

        self.processCallback = processCallback

    def _show_progress(
        self,
        count,
        total_count,
        task="processing images",
    ):
        # Function that displays a progress bar during the search
        if count + 1 == total_count:
            print(
                f"difPy {task}: [{count}/{total_count}] [{count/total_count:.0%}]",
                end="\r",
            )
            print(
                f"difPy {task}: [{count+1}/{total_count}] [{(count+1)/total_count:.0%}]"
            )
        else:
            print(
                f"difPy {task}: [{count}/{total_count}] [{count/total_count:.0%}]",
                end="\r",
            )
        if self.processCallback != None:
            self.processCallback.emit((count, total_count, task))
