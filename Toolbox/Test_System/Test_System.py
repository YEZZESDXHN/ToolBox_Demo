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
lib_demo.lib_test_1(10, 20)
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
            self.Button_Start.TabOrder = 9
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
            self.Button_LoadJSON.TabOrder = 10
            # Create control: Edit_JSONPath = Edit(self)
            self.Edit_JSONPath = Edit(self)
            self.Edit_JSONPath.Name = "Edit_JSONPath"
            self.Edit_JSONPath.Parent = self
            self.Edit_JSONPath.Left = 61
            self.Edit_JSONPath.Top = 51
            self.Edit_JSONPath.Width = 515
            self.Edit_JSONPath.Height = 23
            self.Edit_JSONPath.Cursor = crArrow
            self.Edit_JSONPath.TabOrder = 11
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
        self._available_funcs = {}  # function_name -> (module, func_obj)
        self._node_func_map = {}    # node_id -> function_name

        # --- Initialize available functions from imported libraries ---
        def _init_available_funcs():
            """Collect all available functions from all imported modules"""
            # Scan all loaded modules for lib_test_* functions
            for lib_name, module in sys.modules.items():
                if module is None:
                    continue
                # Look for functions starting with lib_test_
                try:
                    for attr_name in dir(module):
                        if attr_name.startswith("lib_test_"):
                            try:
                                attr = getattr(module, attr_name, None)
                                if attr and callable(attr):
                                    self._available_funcs[attr_name] = (lib_name, attr)
                            except:
                                pass
                except:
                    pass  # Skip modules that cause errors
            self.log("Initialized " + str(len(self._available_funcs)) + " test functions")

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
                    func_name = case.get("function", "")
                    self._node_func_map[id(child_node)] = func_name

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
                if node.CheckState == 'cbsChecked':
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

                # Get function name from node_func_map
                func_name = self._node_func_map.get(id(node), "")

                self.log("[" + str(i+1) + "/" + str(total) + "] Running: " + case_name)
                _set_node_result(node, "Running")

                if not func_name or func_name not in self._available_funcs:
                    _set_node_result(node, "No Case")
                    self.log_error("  No function mapped for: " + case_name + " (func: " + func_name + ")")
                    no_case += 1
                    continue

                lib_name, func = self._available_funcs[func_name]
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
                    if leaf.CheckState == 'cbsChecked':
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
            if ANode.Level == 0:
                # Parent node: sync all children
                if AState == 'cbsChecked':
                    _set_children_check_state(ANode, 'cbsChecked')
                else:
                    _set_children_check_state(ANode, 'cbsUnChecked')
            else:
                # Child node: update parent
                _update_parent_check_state(ANode)

        self.Button_LoadJSON.OnClick = on_load_json_click
        self.Button_Start.OnClick = on_start_click
        self.TSTreelist.OnNodeCheckChanged = on_node_check_changed

        # Initialize functions on startup
        _init_available_funcs()
# Auto Generated Python Code, do not modify START [MAIN] ------------
if __name__ == "__main__":
    try:
        Test_System().Show()
        Application.Run()
    except SystemExit:
        pass
# Auto Generated Python Code, do not modify END [MAIN] --------------
