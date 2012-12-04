import sublime
import sublime_plugin
import os

class TidyHtmlCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #windows require full path. Where is the binary stored relative to /Packages
        if sublime.platform() == "windows":
            path = sublime.packages_path() + "\\TidyHTML\\bin\\tidy.exe"
        else:
            path = "tidy"

        #limited to html files
        if len(self.view.file_name()) > 0 and self.view.file_name().endswith((".html", ".htm")):

            folder_name, file_name = os.path.split(self.view.file_name())
            self.view.window().run_command('exec', {
                'cmd': [path, "-imq", "-wrap", "0", file_name],
                'working_dir': folder_name
            })
            sublime.status_message(("Cleanup HTML in %s...") % file_name)
            #flushing the buffer
            sublime.set_timeout(self.refresh, 1000)

    def refresh(self):
        self.view.window().run_command('revert')
