import winreg


class ContextMenu:

    # NOTE: Path arg must lead to python executable, followed by scripts to execute
    def __init__(self,
                 path="\"C:\\Windows\\py.exe\"",
                 stax_path=" \"D:\\Projects\\Python\\Context Menu\\handler.py\" \"%1\"",
                 unstax_path=" \"D:\\Projects\\Python\\Context Menu\\handler.py\" \"%1\""):
        self.python_path = path
        self.stax_path = stax_path
        self.unstax_path = unstax_path

        self.stax_command = self.python_path + self.stax_path
        self.unstax_command = self.python_path + self.unstax_path

    """
            Code taken from http://sbirch.net/tidbits/context_menu.html
            All credit belongs to the author.

            define_action_on(filetype, registry_title, command, title=None)
                filetype: either an extension type (ex. ".txt") or one of the special
                values ("*" or "Directory"). Note that "*" is files only--if you'd like
                everything to have your action, it must be defined under "*" and "Directory"
                registry_title: the title of the subkey, not important, but probably ought
                to be relevant. If title=None, this is the text that will show up in the context menu.
            """
    def define_action_on(self, filetype, registry_title, command, title=None):
        # all these opens/creates might not be the most efficient way to do it, but it was the best I could do safely,
        # without assuming any keys were defined.
        reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Classes", 0, winreg.KEY_SET_VALUE)
        k1 = winreg.CreateKey(reg, filetype)  # handily, this won't delete a key if it's already there.
        k2 = winreg.CreateKey(k1, "shell")
        k3 = winreg.CreateKey(k2, registry_title)
        k4 = winreg.CreateKey(k3, "command")
        if title != None:
            winreg.SetValueEx(k3, None, 0, winreg.REG_SZ, title)
        winreg.SetValueEx(k4, None, 0, winreg.REG_SZ, command)
        winreg.CloseKey(k3)
        winreg.CloseKey(k2)
        winreg.CloseKey(k1)
        winreg.CloseKey(reg)

    def remove_action_from(self, filetype, registry_title):
        reg1 = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                              "Software\\Classes\\" + filetype + "\\shell\\",
                              0,
                              winreg.KEY_SET_VALUE)
        reg2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                              "Software\\Classes\\" + filetype + "\\shell\\" + registry_title,
                              0,
                              winreg.KEY_SET_VALUE)
        winreg.DeleteKey(reg2, "command")
        try:
            winreg.DeleteKey(reg1, registry_title)
        except FileNotFoundError:
            a = 0
        winreg.CloseKey(reg1)
        winreg.CloseKey(reg2)

    """"======== Connect file types to proper script here ======="""
    def edit_registry(self):
        # .txt CONTEXT
        self.define_action_on(".txt", "Stax", self.stax_command, title="Stack")
        # .jpg CONTEXT
        self.define_action_on(".jpg", "Stax", self.stax_command, title="Stack")
        # DIRECTORY CONTEXT
        self.define_action_on("Directory", "Unstax", self.unstax_command, title="Unstack")

    """===========Remove items from context menu=============="""
    def clear_registry(self):
        # .txt CONTEXT
        self.remove_action_from(".txt", "Stax")
        # .jpg CONTEXT
        self.remove_action_from(".jpg", "Stax")
        # DIRECTORY CONTEXT
        self.remove_action_from("Directory", "Unstax")

    """===========Call this to add file types at run time=========="""
    def add_context_item(self, filetype):
        self.define_action_on(filetype, "Stax", self.stax_command, title="Stack")

    def remove_context_item(self, filetype):
        self.remove_action_from(filetype, "Stax")


cm = ContextMenu()
cm.clear_registry()
