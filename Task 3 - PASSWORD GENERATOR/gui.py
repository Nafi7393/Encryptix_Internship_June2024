import wx
import pyperclip
import main


class PasswordGeneratorFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(PasswordGeneratorFrame, self).__init__(*args, **kw)

        self.generate_btn = None
        self.copy_btn = None
        self.result_lbl = None
        self.special_chars_cb = None
        self.digits_cb = None
        self.uppercase_cb = None
        self.length_txt = None
        self.init_ui()

    def init_ui(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # Password length input
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        length_lbl = wx.StaticText(panel, label="Enter the desired length of the password:")
        hbox1.Add(length_lbl, flag=wx.RIGHT, border=8)
        self.length_txt = wx.TextCtrl(panel)
        hbox1.Add(self.length_txt, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Uppercase checkbox
        self.uppercase_cb = wx.CheckBox(panel, label="Include uppercase letters")
        vbox.Add(self.uppercase_cb, flag=wx.LEFT, border=10)

        # Digits checkbox
        self.digits_cb = wx.CheckBox(panel, label="Include digits")
        vbox.Add(self.digits_cb, flag=wx.LEFT, border=10)

        # Special characters checkbox
        self.special_chars_cb = wx.CheckBox(panel, label="Include special characters")
        vbox.Add(self.special_chars_cb, flag=wx.LEFT, border=10)

        # Generate button
        self.generate_btn = wx.Button(panel, label="Generate Password")
        self.generate_btn.Bind(wx.EVT_BUTTON, self.on_generate)
        vbox.Add(self.generate_btn, flag=wx.ALIGN_CENTER|wx.TOP, border=10)

        # Result label
        self.result_lbl = wx.StaticText(panel, label="Generated Password: ")
        vbox.Add(self.result_lbl, flag=wx.LEFT|wx.TOP, border=10)

        # Copy button
        self.copy_btn = wx.Button(panel, label="Copy to Clipboard")
        self.copy_btn.Bind(wx.EVT_BUTTON, self.on_copy)
        vbox.Add(self.copy_btn, flag=wx.ALIGN_CENTER|wx.TOP, border=10)
        self.copy_btn.Disable()

        panel.SetSizer(vbox)

        self.SetTitle("Password Generator")
        self.Centre()

    def on_generate(self, event):
        try:
            length = int(self.length_txt.GetValue())
            if length <= 0:
                raise ValueError("Password length must be greater than 0")
        except ValueError as e:
            wx.MessageBox(str(e), "Invalid Input", wx.OK | wx.ICON_ERROR)
            return

        use_uppercase = self.uppercase_cb.GetValue()
        use_digits = self.digits_cb.GetValue()
        use_special_chars = self.special_chars_cb.GetValue()

        password = main.generate_password(length, use_uppercase, use_digits, use_special_chars)
        self.result_lbl.SetLabel(f"Generated Password: {password}")
        self.copy_btn.Enable()

    def on_copy(self, event):
        password = self.result_lbl.GetLabel().replace("Generated Password: ", "")
        pyperclip.copy(password)
        wx.MessageBox("Password copied to clipboard!", "Info", wx.OK | wx.ICON_INFORMATION)


def main_app():
    app = wx.App()
    frame = PasswordGeneratorFrame(None)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main_app()
