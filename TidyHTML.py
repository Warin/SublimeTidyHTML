import sublime
import sublime_plugin
import os

class TidyHtmlCommand(sublime_plugin.TextCommand):
    def run(self, edit):


        #windows require full path. Where is the binary stored relative to /Packages
        if sublime.platform() == "windows":
            path = sublime.packages_path() + "\\TidyHTML5\\bin\\tidy.exe"
        else:
            path = "tidy"

        #defining command to run
        cmdToRun = [path, "-imq"]

        #reading settings file
        settingsFile = sublime.load_settings('TidyHTML.sublime-settings')
        settings= settingsFile.get('TidyHTML')
        options = settings.get('options')
        filetypes = settings.get('filetypes')

        #extending command to run in case settings are defined
        if options!=None:
            for option in options:
                for key in option:
                    cmdToRun.append("--"+ key)
                    cmdToRun.append(option[key])

        #setting default file extentions
        if filetypes==None:
            filetypes=[".htm","html"]
        
        #limited to html files
        if len(self.view.file_name()) > 0 and self.view.file_name().endswith(tuple(filetypes)):

            folder_name, file_name = os.path.split(self.view.file_name())
            cmdToRun.append(file_name)

            self.view.window().run_command('exec', {
                'cmd': cmdToRun,
                'working_dir': folder_name
            })
            sublime.status_message(("Cleanup HTML in %s...") % file_name)
            #flushing the buffer
            sublime.set_timeout(self.refresh, 1000)

    def refresh(self):
        self.view.window().run_command('revert')
