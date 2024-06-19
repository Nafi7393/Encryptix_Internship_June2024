import wx
from main import add_task, remove_task, list_tasks, mark_task_completed


class AddTaskDialog(wx.Dialog):

    def __init__(self, parent):
        super().__init__(parent, title="Add Task", size=(400, 300))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        name_label = wx.StaticText(panel, label="Task Name:")
        self.name_textctrl = wx.TextCtrl(panel)
        vbox.Add(name_label, 0, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.name_textctrl, 0, wx.EXPAND | wx.ALL, 10)

        desc_label = wx.StaticText(panel, label="Task Description:")
        self.desc_textctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        vbox.Add(desc_label, 0, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.desc_textctrl, 1, wx.EXPAND | wx.ALL, 10)

        btn_ok = wx.Button(panel, wx.ID_OK, "OK")
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, "Cancel")
        btn_box = wx.BoxSizer(wx.HORIZONTAL)
        btn_box.Add(btn_ok, 0, wx.EXPAND | wx.ALL, 10)
        btn_box.Add(btn_cancel, 0, wx.EXPAND | wx.ALL, 10)
        vbox.Add(btn_box, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        panel.SetSizer(vbox)
        self.Center()

    def get_task_info(self):
        name = self.name_textctrl.GetValue().strip()
        desc = self.desc_textctrl.GetValue().strip()
        return name, desc


class TaskPanel(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        self.tasks_listctrl = wx.ListCtrl(self, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.tasks_listctrl.InsertColumn(0, "ID", width=30)
        self.tasks_listctrl.InsertColumn(1, "Name", width=200)
        self.tasks_listctrl.InsertColumn(2, "Description", width=350)
        self.tasks_listctrl.InsertColumn(3, "Due Date", width=100)
        self.tasks_listctrl.InsertColumn(4, "Status", width=100)
        self.load_tasks()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tasks_listctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.SetSizer(sizer)

    def load_tasks(self):
        self.tasks_listctrl.DeleteAllItems()
        tasks = list_tasks()
        for task in tasks:
            index = self.tasks_listctrl.InsertItem(self.tasks_listctrl.GetItemCount(), str(task['id']))
            self.tasks_listctrl.SetItem(index, 1, task['name'])
            self.tasks_listctrl.SetItem(index, 2, task['description'])
            self.tasks_listctrl.SetItem(index, 3, task['due_date'])
            status = "Done" if task['completed'] else "Pending"
            self.tasks_listctrl.SetItem(index, 4, status)


class ToDoListApp(wx.Frame):

    def __init__(self, parent, title):
        super(ToDoListApp, self).__init__(parent, title=title, size=(840, 400))

        self.panel = wx.Panel(self)
        self.task_panel = TaskPanel(self.panel)

        add_btn = wx.Button(self.panel, wx.ID_ANY, "Add Task")
        remove_btn = wx.Button(self.panel, wx.ID_ANY, "Remove Task")
        complete_btn = wx.Button(self.panel, wx.ID_ANY, "Mark as Completed")
        exit_btn = wx.Button(self.panel, wx.ID_ANY, "Exit")

        add_btn.Bind(wx.EVT_BUTTON, self.on_add_task)
        remove_btn.Bind(wx.EVT_BUTTON, self.on_remove_task)
        complete_btn.Bind(wx.EVT_BUTTON, self.on_mark_completed)
        exit_btn.Bind(wx.EVT_BUTTON, self.on_exit)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(add_btn, proportion=0, flag=wx.EXPAND | wx.ALL, border=10)
        button_sizer.Add(remove_btn, proportion=0, flag=wx.EXPAND | wx.ALL, border=10)
        button_sizer.Add(complete_btn, proportion=0, flag=wx.EXPAND | wx.ALL, border=10)
        button_sizer.Add(exit_btn, proportion=0, flag=wx.EXPAND | wx.ALL, border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.task_panel, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(button_sizer, proportion=0, flag=wx.EXPAND | wx.ALL, border=10)

        self.panel.SetSizer(vbox)
        self.Center()
        self.Show()

    def on_add_task(self, event):
        dialog = AddTaskDialog(self)
        if dialog.ShowModal() == wx.ID_OK:
            name, desc = dialog.get_task_info()
            if name and desc:
                add_task(name, desc)
                self.task_panel.load_tasks()
        dialog.Destroy()

    def on_remove_task(self, event):
        selected_index = self.task_panel.tasks_listctrl.GetFirstSelected()
        if selected_index != -1:
            task_id = int(self.task_panel.tasks_listctrl.GetItemText(selected_index))
            removed_task = remove_task(task_id)
            if removed_task:
                wx.MessageBox(f"Task '{removed_task['name']}' with ID '{task_id}' removed successfully.",
                              'Task Removed', wx.OK | wx.ICON_INFORMATION)
                self.task_panel.load_tasks()
            else:
                wx.MessageBox(f"Task with ID '{task_id}' not found.", 'Error', wx.OK | wx.ICON_ERROR)

    def on_mark_completed(self, event):
        selected_index = self.task_panel.tasks_listctrl.GetFirstSelected()
        if selected_index != -1:
            task_id = int(self.task_panel.tasks_listctrl.GetItemText(selected_index))
            completed_task = mark_task_completed(task_id)
            if completed_task:
                wx.MessageBox(f"Task '{completed_task['name']}' with ID '{task_id}' marked as completed.",
                              'Task Completed', wx.OK | wx.ICON_INFORMATION)
                self.task_panel.load_tasks()
            else:
                wx.MessageBox(f"Task with ID '{task_id}' not found.", 'Error', wx.OK | wx.ICON_ERROR)

    def on_exit(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    ToDoListApp(None, title='To-Do List App')
    app.MainLoop()
