import locale
import os
import subprocess
import sublime, sublime_plugin

class SourcetreeOpenCommand(sublime_plugin.WindowCommand):

    def is_enabled(self):
        return True

    def get_path(self):
        if self.window.folders():
            return self.window.folders()[0]
        else:
            sublime.status_message('No place to open Sourcetree to')
            return False

    def run(self, *args):
        sublime.status_message('Sourcetree: running')
        path = self.get_path()
        if not path:
            sublime.status_message('Sourcetree: No path')
            return False
        if os.path.isfile(path):
            path = os.path.dirname(path)

        app_path = '/Applications/Sourcetree.app'
        subprocess.call(['open', '-a', app_path, path])

class SideBarSourcetreeCommand(sublime_plugin.WindowCommand):

    def is_enabled(self):
        return True

    def get_path(self, paths):
        try:
            return paths[0]
        except IndexError:
            return self.window.active_view().file_name()

    def run(self, paths):
        sublime.status_message('Sourcetree: running')
        path = self.get_path(paths)
        if not path:
            sublime.status_message('Sourcetree: No path')
            return False
        if os.path.isfile(path):
            path = os.path.dirname(path)

        app_path = '/Applications/Sourcetree.app'
        subprocess.call(['open', '-a', app_path, path])
