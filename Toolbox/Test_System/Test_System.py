import sys
import json
import importlib
import queue
from time import sleep
from threading import Thread

from TSMaster import *
# if app.is_tsmaster_host(): # only vaid in TSMaster App
#     app.import_mini_program_header("lib_demo2")
#     globals()["lib_demo2"] = sys.modules.get("lib_demo2")
#     app.import_mini_program_header("lib_demo")
#     globals()["lib_demo"] = sys.modules.get("lib_demo")

if app.is_tsmaster_host(): # only vaid in TSMaster App
    import TSMaster.lib_demo2 as lib_demo2
    import TSMaster.lib_demo as lib_demo


blacklist = ["tkinter"] # modules such as tkinter will release GIL by itself, which is not allowed in TSMster Toolbox
for mod in blacklist:
    if sys.modules.get(mod):
        tmp_import = __import__ (mod)
        sys.modules[mod] = None

print("test system")
sleep(3)
# lib_demo.lib_test_1(10, 20)
print("test system test")




# Auto Generated Python Code, do not modify START [UI] --------------
class Test_System(frmTSForm):
    def __init__(self):
        # set type name internally
        self.ExternalTypeName = type(self).__name__
        if hasattr(self, "on_before_ui_creation"):
            method = getattr(self, "on_before_ui_creation")
            method()
        try:
            # Form properties
            if not self.IsConfigurationLoaded:
                self.Left = 152
                self.Top = 152
                self.Caption = 'Test_System'
                self.ClientHeight = 813
                self.ClientWidth = 1241
            self.Color = clBtnFace
            self.DoubleBuffered = True
            self.Font.Charset = DEFAULT_CHARSET
            self.Font.Color = clWindowText
            self.Font.Height = -12
            self.Font.Name = 'Segoe UI'
            self.Font.Style = []
            self.KeyPreview = True
            self.Position = "poDesigned"
            self.Visible = True
            self.TextHeight = 15
            # Create control: TSTreelist = TSTreelist(self)
            self.TSTreelist = TSTreelist(self)
            self.TSTreelist.Name = "TSTreelist"
            self.TSTreelist.Parent = self
            self.TSTreelist.Tag = 8847463
            self.TSTreelist.Left = 61
            self.TSTreelist.Top = 90
            self.TSTreelist.Width = 515
            self.TSTreelist.Height = 640
            self.TSTreelist.Cursor = crArrow
            self.TSTreelist.Images = app.get_system_imagelist_16px()
            self.TSTreelist.OptionsBehavior.CellHints = True
            self.TSTreelist.OptionsCustomizing.ColumnVertSizing = False
            self.TSTreelist.OptionsSelection.MultiSelect = True
            self.TSTreelist.OptionsView.ColumnAutoWidth = True
            self.TSTreelist.TabOrder = 0
            # Create control: Button_Start = Button(self)
            self.Button_Start = Button(self)
            self.Button_Start.Name = "Button_Start"
            self.Button_Start.Parent = self
            self.Button_Start.Tag = 8848236
            self.Button_Start.Left = 584
            self.Button_Start.Top = 90
            self.Button_Start.Width = 75
            self.Button_Start.Height = 25
            self.Button_Start.Cursor = crArrow
            self.Button_Start.CustomHint = app.ui_get_default_ballon_hint()
            self.Button_Start.Caption = "开始"
            self.Button_Start.Images = app.get_system_imagelist_16px()
            self.Button_Start.TabOrder = 1
            # Create control: Button_LoadJSON = Button(self)
            self.Button_LoadJSON = Button(self)
            self.Button_LoadJSON.Name = "Button_LoadJSON"
            self.Button_LoadJSON.Parent = self
            self.Button_LoadJSON.Tag = 4850540
            self.Button_LoadJSON.Left = 584
            self.Button_LoadJSON.Top = 49
            self.Button_LoadJSON.Width = 75
            self.Button_LoadJSON.Height = 25
            self.Button_LoadJSON.Cursor = crArrow
            self.Button_LoadJSON.CustomHint = app.ui_get_default_ballon_hint()
            self.Button_LoadJSON.Caption = "加载JSON"
            self.Button_LoadJSON.Images = app.get_system_imagelist_16px()
            self.Button_LoadJSON.TabOrder = 2
            # Create control: Edit_JSONPath = Edit(self)
            self.Edit_JSONPath = Edit(self)
            self.Edit_JSONPath.Name = "Edit_JSONPath"
            self.Edit_JSONPath.Parent = self
            self.Edit_JSONPath.Left = 61
            self.Edit_JSONPath.Top = 51
            self.Edit_JSONPath.Width = 515
            self.Edit_JSONPath.Height = 23
            self.Edit_JSONPath.Cursor = crArrow
            self.Edit_JSONPath.TabOrder = 3
            self.Edit_JSONPath.TextHint = "请输入JSON文件路径"
        finally:
            # End UI auto creation
            self.EndUIAutoCreation()
# Auto Generated Python Code, do not modify END [UI] ----------------
        # your init code starts here...
        self._case_map = {}
        self._result_queue = queue.Queue()
        self._is_running = False

        # --- Column 0: Case Name (read-only label) ---
        self.TSTreelist_Col0 = self.TSTreelist.CreateColumn(None)
        self.TSTreelist_Col0.PropertiesClassName = 'TcxLabelProperties'
        self.TSTreelist_Col0.Caption.AlignHorz = "taCenter"
        self.TSTreelist_Col0.Caption.Text = 'Case Name'
        self.TSTreelist_Col0.MinWidth = 13
        self.TSTreelist_Col0.Options.VertSizing = False
        self.TSTreelist_Col0.Width = 250
        self.TSTreelist_Col0.Position.ColIndex = 0
        self.TSTreelist_Col0.Position.RowIndex = 0
        self.TSTreelist_Col0.Position.BandIndex = 0

        # --- Column 1: Result (read-only label) ---
        self.TSTreelist_Col1 = self.TSTreelist.CreateColumn(None)
        self.TSTreelist_Col1.PropertiesClassName = 'TcxLabelProperties'
        self.TSTreelist_Col1.Caption.AlignHorz = "taCenter"
        self.TSTreelist_Col1.Caption.Text = 'Result'
        self.TSTreelist_Col1.MinWidth = 13
        self.TSTreelist_Col1.Options.VertSizing = False
        self.TSTreelist_Col1.Width = 120
        self.TSTreelist_Col1.Position.ColIndex = 1
        self.TSTreelist_Col1.Position.RowIndex = 0
        self.TSTreelist_Col1.Position.BandIndex = 0

        def _set_result(node, result):
            node.SetValue(1, result)

        def _find_node_by_index(idx):
            node = self.TSTreelist.TopNode
            while node is not None:
                if node.Index == idx:
                    return node
                node = node.GetNext()
            return None

        # --- UIRefreshEvent: main-thread callback to apply queued results ---
        self.FNeedRefresh = True

        def _ui_refresh_event():
            if not self.FNeedRefresh:
                return
            while True:
                try:
                    node_index, result = self._result_queue.get_nowait()
                except queue.Empty:
                    break
                node = _find_node_by_index(node_index)
                if node is not None:
                    _set_result(node, result)
            self.FNeedRefresh = False

        self.OnRefreshEvent = _ui_refresh_event

        self.TSTreelist.OptionsView.CheckGroups = True
        self.TSTreelist.Root.CheckGroupType = 'ncgCheckGroup'

        # --- Button: Load JSON ---
        def on_load_json_click(sender):
            json_path = self.Edit_JSONPath.Text.strip()
            if not json_path:
                ShowMessage('Please enter JSON file path')
                return
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            except Exception as e:
                ShowMessage(f'Failed to load JSON: {e}')
                return

            self.TSTreelist.Clear()
            self._case_map.clear()

            for suite in config.get('test_suites', []):
                suite_node = self.TSTreelist.Add()
                suite_node.CheckGroupType = 'ncgCheckGroup'
                suite_node.SetValue(0, suite['suite_name'])
                suite_node.SetValue(1, '')

                for case in suite.get('cases', []):
                    case_node = suite_node.AddChild()
                    case_node.CheckState = 'cbsUnChecked'
                    case_node.SetValue(0, case['case_name'])
                    _set_result(case_node, 'Not Run')
                    self._case_map[case_node.Index] = {
                        'library': case['library'],
                        'function': case['function'],
                    }

            self.TSTreelist.FullExpand()

        self.Button_LoadJSON.OnClick = on_load_json_click

        # --- Button: Start ---
        def on_start_click(sender):
            if self._is_running:
                return

            # Collect checked leaf nodes in main thread (safe VCL access)
            checked = []
            node = self.TSTreelist.TopNode
            while node is not None:
                if not node.HasChildren and node.CheckState == 'cbsChecked':
                    info = self._case_map.get(node.Index)
                    if info is not None:
                        checked.append((node.Index, info['library'], info['function']))
                    else:
                        _set_result(node, 'No Case')
                node = node.GetNext()

            if not checked:
                return

            self._is_running = True
            for idx, lib, func_name in checked:
                node = _find_node_by_index(idx)
                if node is not None:
                    _set_result(node, 'Running')

            def run_tests():
                for idx, lib, func_name in checked:
                    try:
                        mod = importlib.import_module(f'TSMaster.{lib}')
                        func = getattr(mod, func_name)
                        func()
                        self._result_queue.put((idx, 'Passed'))
                    except (ModuleNotFoundError, AttributeError):
                        self._result_queue.put((idx, 'No Case'))
                    except Exception:
                        self._result_queue.put((idx, 'Failed'))
                    self.FNeedRefresh = True
                self._is_running = False

            thread = Thread(target=run_tests)
            thread.daemon = True
            thread.start()

        self.Button_Start.OnClick = on_start_click

# Auto Generated Python Code, do not modify START [MAIN] ------------
if __name__ == "__main__":
    try:
        Test_System().Show()
        Application.Run()
    except SystemExit:
        pass
# Auto Generated Python Code, do not modify END [MAIN] --------------
