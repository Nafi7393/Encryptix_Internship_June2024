import wx
from main import calculator, get_number, get_operation, perform_calculation

class CalculatorFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Python Calculator", size=(400, 300))
        panel = wx.Panel(self)

        self.num1_text = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.num2_text = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.result_text = wx.StaticText(panel, label="Result: ")
        self.operation_choice = wx.Choice(panel, choices=[
            'Addition',
            'Subtraction',
            'Multiplication',
            'Division',
            'Power (Exponentiation)',
            'Modulus'
        ])
        self.operation_choice.SetSelection(0)

        calculate_button = wx.Button(panel, label="Calculate")
        calculate_button.Bind(wx.EVT_BUTTON, self.on_calculate)

        clear_button = wx.Button(panel, label="Clear")
        clear_button.Bind(wx.EVT_BUTTON, self.on_clear)

        self.result_display = wx.TextCtrl(panel, style=wx.TE_READONLY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(panel, label="Enter numbers and select operation:"), 0, wx.ALL, 5)
        sizer.Add(self.num1_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.num2_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.operation_choice, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(calculate_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(clear_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.result_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.result_display, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(sizer)
        self.Center()

    def on_calculate(self, event):
        num1 = self.get_number_from_textctrl(self.num1_text)
        num2 = self.get_number_from_textctrl(self.num2_text)
        operation = str(self.operation_choice.GetSelection() + 1)
        result = perform_calculation(num1, num2, operation)
        self.result_display.SetValue(str(result))

    def on_clear(self, event):
        self.num1_text.SetValue("")
        self.num2_text.SetValue("")
        self.result_display.SetValue("")

    def get_number_from_textctrl(self, text_ctrl):
        try:
            return float(text_ctrl.GetValue())
        except ValueError:
            wx.MessageBox("Invalid input. Please enter a valid number.", "Error", wx.OK | wx.ICON_ERROR)
            return None


class CalculatorApp(wx.App):
    def OnInit(self):
        frame = CalculatorFrame()
        frame.Show()
        return True


if __name__ == "__main__":
    app = CalculatorApp()
    app.MainLoop()
