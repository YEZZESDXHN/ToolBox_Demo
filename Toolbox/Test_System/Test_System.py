import sys
import json
import queue
from threading import Event, Thread

from TSMaster import *
# if app.is_tsmaster_host(): # only vaid in TSMaster App
#     app.import_mini_program_header("my_mp")
#     globals()["my_mp"] = sys.modules.get("my_mp")
# my_mp.my_fun_1()
blacklist = ["tkinter"]
for mod in blacklist:
    if sys.modules.get(mod):
        tmp_import = __import__(mod)
        sys.modules[mod] = None

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
            # Create control: Button_Stop = Button(self)
            self.Button_Stop = Button(self)
            self.Button_Stop.Name = "Button_Stop"
            self.Button_Stop.Parent = self
            self.Button_Stop.Left = 672
            self.Button_Stop.Top = 91
            self.Button_Stop.Width = 75
            self.Button_Stop.Height = 24
            self.Button_Stop.Cursor = crArrow
            self.Button_Stop.CustomHint = app.ui_get_default_ballon_hint()
            self.Button_Stop.Caption = 'Stop'
            self.Button_Stop.Images = app.get_system_imagelist_16px()
            self.Button_Stop.TabOrder = 4
        finally:
            # End UI auto creation
            self.EndUIAutoCreation()
# Auto Generated Python Code, do not modify END [UI] ----------------
        self._case_map = {}
        self._result_queue = queue.Queue()
        self._is_running = False
        self.FNeedRefresh = False

        self._init_treelist()
        self.Button_LoadJSON.OnClick = self._on_load_json
        self.Button_Start.OnClick = self._on_start
        self.Button_Stop.OnClick = self._on_stop
        self.OnRefreshEvent = self._on_refresh
        self.OnClose = self._on_close
        self._stop_event=Event()
        self._stop_event.clear()


    def _on_close(self, sender, action):
      print("close, action:", action.Value)
      # action.Value = 1 表示隐藏，2 表示释放
      if action.Value == 2:
        self._stop_event.set()
    #   if self.run_case_thread.is_alive():
    #       self.run_case_thread.join(timeout=1)

    # --- Treelist setup ---
    def _init_treelist(self):
        col_name = self.TSTreelist.CreateColumn(None)
        col_name.PropertiesClassName = 'TcxLabelProperties'
        col_name.Caption.AlignHorz = "taCenter"
        col_name.Caption.Text = 'Case Name'
        col_name.MinWidth = 13
        col_name.Options.VertSizing = False
        col_name.Width = 250
        col_name.Position.ColIndex = 0
        col_name.Position.RowIndex = 0
        col_name.Position.BandIndex = 0

        col_result = self.TSTreelist.CreateColumn(None)
        col_result.PropertiesClassName = 'TcxLabelProperties'
        col_result.Caption.AlignHorz = "taCenter"
        col_result.Caption.Text = 'Result'
        col_result.MinWidth = 13
        col_result.Options.VertSizing = False
        col_result.Width = 120
        col_result.Position.ColIndex = 1
        col_result.Position.RowIndex = 0
        col_result.Position.BandIndex = 0

        self.TSTreelist.OptionsView.CheckGroups = True
        self.TSTreelist.Root.CheckGroupType = 'ncgCheckGroup'

    # --- Helpers ---
    @staticmethod
    def _is_checked(node):
        cs = node.CheckState
        return cs == 'cbsChecked' or cs == 1

    def _on_refresh(self):
        if not self.FNeedRefresh:
            return
        while True:
            try:
                case_id, result = self._result_queue.get_nowait()
            except queue.Empty:
                break
            entry = self._case_map.get(case_id)
            if entry is not None:
                entry[2].SetValue(1, result)
        self.FNeedRefresh = False

    def _reset_results(self):
        for lib, func_name, node in self._case_map.values():
            node.SetValue(1, 'Not Run')

    # --- Load JSON ---
    def _on_load_json(self, sender):
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
                case_node.SetValue(1, 'Not Run')
                case_id = case_node.AbsoluteIndex
                self._case_map[case_id] = (case['library'], case['function'], case_node)

        self.TSTreelist.FullExpand()

    def _on_stop(self, sender):
        self._stop_event.set()

    # --- Start tests ---
    def _on_start(self, sender):
        if self._is_running:
            return

        self._reset_results()

        checked = [
            (case_id, lib, func_name)
            for case_id, (lib, func_name, node) in self._case_map.items()
            if self._is_checked(node)
        ]
        if not checked:
            return

        self._is_running = True

        def run_tests():
            for case_id, lib, func_name in checked:
                if self._stop_event.is_set():
                    self._stop_event.clear()
                    self._is_running = False
                    return
                self._result_queue.put((case_id, 'Running'))
                self.FNeedRefresh = True
                try:
                    print(f"get{lib}")
                    mod = sys.modules.get(lib)
                    # sys.modules.get(f'TSMaster.{lib}')
                    if mod is None:
                        self._result_queue.put((case_id, 'No Case'))
                        continue
                    func = getattr(mod, func_name)
                    func()
                    self._result_queue.put((case_id, 'Passed'))
                except (ModuleNotFoundError, AttributeError):
                    self._result_queue.put((case_id, 'No Case'))
                except Exception:
                    self._result_queue.put((case_id, 'Failed'))
                self.FNeedRefresh = True
            self._is_running = False
            self._stop_event.clear()

        thread = Thread(target=run_tests)
        thread.daemon = True
        thread.start()

# Auto Generated Python Code, do not modify START [MAIN] ------------
if __name__ == "__main__":
    try:
        Test_System().Show()
        Application.Run()
    except SystemExit:
        pass
# Auto Generated Python Code, do not modify END [MAIN] --------------
