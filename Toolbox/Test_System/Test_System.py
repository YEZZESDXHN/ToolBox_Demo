import sys
from time import sleep

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
        import json
        import os

        # --- Data structures ---
        self._leaf_nodes = []       # list of leaf nodes for traversal
        self._is_running = False    # guard against double-click during test
        self._loaded_modules = {}   # module_name -> module_object
        self._node_func_map = {}    # node_id -> (library, function)
        self._updating_check = False  # guard against recursive check events

        # --- Initialize available modules ---
        def _init_loaded_modules():
            """Discover all loaded modules"""
            for module_name, module in sys.modules.items():
                if module is not None:
                    self._loaded_modules[module_name] = module
            self.log("Discovered " + str(len(self._loaded_modules)) + " loaded modules")

        # --- Column setup ---
        # Enable check groups for checkboxes
        self.TSTreelist.OptionsView.CheckGroups = True

        # Column 0: Case Name (read-only)
        self._col_case_name = self.TSTreelist.CreateColumn(None)
        self._col_case_name.Caption.Text = "Case Name"
        self._col_case_name.PropertiesClassName = 'TcxTextEditProperties'
        self._col_case_name.Options.Editing = False
        self._col_case_name.Position.ColIndex = 0
        self._col_case_name.Position.RowIndex = 0
        self._col_case_name.Position.BandIndex = 0

        # Column 1: Result (read-only)
        self._col_result = self.TSTreelist.CreateColumn(None)
        self._col_result.Caption.Text = "Result"
        self._col_result.PropertiesClassName = 'TcxTextEditProperties'
        self._col_result.Options.Editing = False
        self._col_result.Position.ColIndex = 1
        self._col_result.Position.RowIndex = 0
        self._col_result.Position.BandIndex = 0

        # Enable root check group
        self.TSTreelist.Root.CheckGroupType = 'ncgCheckGroup'

        # --- Helper functions ---
        def _set_node_result(node, result_text):
            """Set result text on a node's result column"""
            node.SetValue(1, result_text)

        def _load_json_to_treelist(json_path):
            """Load JSON file and populate TSTreelist"""
            # Clear existing state
            self._leaf_nodes.clear()
            self._node_func_map.clear()

            if not os.path.exists(json_path):
                self.log_error("JSON file not found: " + json_path)
                return False

            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception as e:
                self.log_error("Failed to parse JSON: " + str(e))
                return False

            for suite in data.get("test_suites", []):
                suite_node = self.TSTreelist.Add()
                suite_node.CheckGroupType = 'ncgCheckGroup'
                suite_node.SetValue(0, suite.get("suite_name", "Unnamed Suite"))
                suite_node.SetValue(1, "")

                for case in suite.get("cases", []):
                    child_node = suite_node.AddChild()
                    child_node.CheckGroupType = 'ncgCheckGroup'
                    child_node.SetValue(0, case.get("case_name", "Unnamed Case"))
                    child_node.SetValue(1, "Not Run")

                    # Store function mapping using node id
                    lib_name = case.get("library", "")
                    func_name = case.get("function", "")
                    node_id = id(child_node)
                    self._node_func_map[node_id] = (lib_name, func_name)
                    self.log("Mapped node " + str(node_id) + " -> " + lib_name + "." + func_name)

                    self._leaf_nodes.append(child_node)

            self.TSTreelist.FullExpand()
            self.log_ok("Loaded " + str(len(self._leaf_nodes)) + " test cases from JSON")
            return True

        def _run_selected_tests():
            """Execute all checked test cases sequentially"""
            if self._is_running:
                self.log_warning("Test is already running")
                return
            self._is_running = True

            checked_cases = []
            for node in self._leaf_nodes:
                # CheckState can be string or int: 1 or 'cbsChecked' means checked
                is_checked = (node.CheckState == 1) or (node.CheckState == 'cbsChecked')
                if is_checked:
                    checked_cases.append(node)

            if not checked_cases:
                self.log_warning("No test cases selected")
                self._is_running = False
                return

            total = len(checked_cases)
            passed = 0
            failed = 0
            no_case = 0
            self.log("Starting test execution: " + str(total) + " cases selected")

            for i, node in enumerate(checked_cases):
                case_name = node.GetValue(0)

                # Get library and function from node_func_map
                node_id = id(node)
                lib_name, func_name = self._node_func_map.get(node_id, ("", ""))

                self.log("[" + str(i+1) + "/" + str(total) + "] Running: " + case_name)
                _set_node_result(node, "Running")

                if not lib_name or not func_name:
                    _set_node_result(node, "No Case")
                    self.log_error("  No function mapped for: " + case_name + " (node_id: " + str(node_id) + ")")
                    self.log_error("  Available mappings: " + str(list(self._node_func_map.keys())))
                    no_case += 1
                    continue

                # Find module - try exact match first, then partial match
                module = self._loaded_modules.get(lib_name)
                if module is None:
                    # Try partial match
                    for mod_name, mod in self._loaded_modules.items():
                        if lib_name in mod_name or mod_name.endswith("." + lib_name):
                            module = mod
                            break

                if module is None:
                    _set_node_result(node, "No Case")
                    self.log_error("  Module not found: " + lib_name + " for " + case_name)
                    no_case += 1
                    continue

                # Get function from module
                func = getattr(module, func_name, None)
                if func is None or not callable(func):
                    _set_node_result(node, "No Case")
                    self.log_error("  Function not found: " + func_name + " in " + lib_name)
                    no_case += 1
                    continue

                try:
                    func()
                    _set_node_result(node, "Passed")
                    self.log_ok("  PASSED: " + case_name)
                    passed += 1
                except Exception as e:
                    _set_node_result(node, "Failed")
                    self.log_error("  FAILED: " + case_name + " - " + str(e))
                    failed += 1

            self.log("Test execution complete: " + str(passed) + " passed, " + str(failed) + " failed, " + str(no_case) + " no case, " + str(total) + " total")
            self._is_running = False

        def _update_parent_check_state(node):
            """Update parent node check state based on children"""
            parent = node.Parent
            if parent is None or parent == self.TSTreelist.Root:
                return

            # Find all leaf nodes with the same parent
            all_checked = True
            any_checked = False
            for leaf in self._leaf_nodes:
                if leaf.Parent == parent:
                    # CheckState can be string or int: 1 or 'cbsChecked' means checked
                    is_checked = (leaf.CheckState == 1) or (leaf.CheckState == 'cbsChecked')
                    if is_checked:
                        any_checked = True
                    else:
                        all_checked = False

            # Update parent state
            if all_checked:
                parent.CheckState = 'cbsChecked'
            elif any_checked:
                # Keep parent checked if any child is checked
                parent.CheckState = 'cbsChecked'
            else:
                parent.CheckState = 'cbsUnChecked'

        def _set_children_check_state(parent_node, check_state):
            """Set all children check state"""
            for leaf in self._leaf_nodes:
                if leaf.Parent == parent_node:
                    leaf.CheckState = check_state

        # --- Event bindings ---
        def on_load_json_click(sender):
            json_path = self.Edit_JSONPath.Text.strip()
            if not json_path:
                self.log_error("Please enter a JSON file path")
                return
            _load_json_to_treelist(json_path)

        def on_start_click(sender):
            _run_selected_tests()

        def on_node_check_changed(ATreeList, ANode, AState):
            """Handle node check state changes for parent-child synchronization"""
            # Guard against recursive calls
            if self._updating_check:
                return
            self._updating_check = True
            try:
                # AState: 0=unchecked, 1=checked, 2=grayed
                is_checked = (AState == 1) or (AState == 'cbsChecked')
                if ANode.Level == 0:
                    # Parent node: sync all children
                    if is_checked:
                        _set_children_check_state(ANode, 'cbsChecked')
                    else:
                        _set_children_check_state(ANode, 'cbsUnChecked')
                else:
                    # Child node: update parent
                    _update_parent_check_state(ANode)
            finally:
                self._updating_check = False

        self.Button_LoadJSON.OnClick = on_load_json_click
        self.Button_Start.OnClick = on_start_click
        self.TSTreelist.OnNodeCheckChanged = on_node_check_changed

        # Initialize modules on startup
        _init_loaded_modules()
# Auto Generated Python Code, do not modify START [MAIN] ------------
if __name__ == "__main__":
    try:
        Test_System().Show()
        Application.Run()
    except SystemExit:
        pass
# Auto Generated Python Code, do not modify END [MAIN] --------------
