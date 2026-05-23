from TSMaster import *
import random
import sys
sys.path.append(app.get_current_toolbox_path('Toolbox_Guide'))
import ConfigDialog

f = None

# Auto Generated Python Code, do not modify START [UI] --------------
class Toolbox_Guide_Copy(frmTSForm):
    def __init__(self):
        # set type name internally
        self.ExternalTypeName = type(self).__name__
        if hasattr(self, "on_before_ui_creation"):
            method = getattr(self, "on_before_ui_creation")
            method()
        try:
            # Form properties
            if not self.IsConfigurationLoaded:
                self.Left = 15
                self.Top = 13
                self.Caption = 'Toolbox_Guide_Copy'
                self.ClientHeight = 508
                self.ClientWidth = 1395
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
            self.Maintainer = 'Link'
            self.TextHeight = 15
            # Create control: splitMM = Splitter(self)
            self.splitMM = Splitter(self)
            self.splitMM.Name = "splitMM"
            self.splitMM.Parent = self
            self.splitMM.Left = 0
            self.splitMM.Top = 378
            self.splitMM.Cursor = crArrow
            self.splitMM.Align = "alBottom"
            self.splitMM.Width = 1395
            self.splitMM.Height = 5
            self.splitMM.AutoSnap = False
            # Create control: MM = Memo(self)
            self.MM = Memo(self)
            self.MM.Name = "MM"
            self.MM.Parent = self
            self.MM.Left = 0
            self.MM.Top = 383
            self.MM.Width = 1395
            self.MM.Height = 125
            self.MM.Cursor = crArrow
            self.MM.Align = "alBottom"
            self.MM.Font.Charset = DEFAULT_CHARSET
            self.MM.Font.Color = clGreen
            self.MM.Font.Height = -16
            self.MM.Font.Name = 'Segoe UI'
            self.MM.Font.Style = ["fsBold"]
            self.MM.ParentFont = False
            self.MM.ReadOnly = True
            self.MM.ScrollBars = "ssVertical"
            self.MM.TabOrder = 1
            # Create control: pgFeatures = PageControl(self)
            self.pgFeatures = PageControl(self)
            self.pgFeatures.Name = "pgFeatures"
            self.pgFeatures.Parent = self
            self.pgFeatures.Left = 0
            self.pgFeatures.Top = 0
            self.pgFeatures.Width = 1395
            self.pgFeatures.Height = 378
            self.pgFeatures.Cursor = crArrow
            self.pgFeatures.Align = "alClient"
            self.pgFeatures.MultiLine = True
            self.pgFeatures.TabOrder = 0
            # Create control: shtForm = TabSheet(self)
            self.shtForm = TabSheet(self)
            self.shtForm.Name = "shtForm"
            self.shtForm.PageControl = self.pgFeatures
            self.shtForm.Cursor = crArrow
            self.shtForm.Caption = 'Form'
            # Create control: grpFormProperties = GroupBox(self)
            self.grpFormProperties = GroupBox(self)
            self.grpFormProperties.Name = "grpFormProperties"
            self.grpFormProperties.Parent = self.shtForm
            self.grpFormProperties.Left = 0
            self.grpFormProperties.Top = 0
            self.grpFormProperties.Width = 264
            self.grpFormProperties.Height = 308
            self.grpFormProperties.Cursor = crArrow
            self.grpFormProperties.Align = "alLeft"
            self.grpFormProperties.Caption = 'Form Properties'
            self.grpFormProperties.TabOrder = 0
            # Create control: btnMoveLeft = Button(self)
            self.btnMoveLeft = Button(self)
            self.btnMoveLeft.Name = "btnMoveLeft"
            self.btnMoveLeft.Parent = self.grpFormProperties
            self.btnMoveLeft.Left = 2
            self.btnMoveLeft.Top = 17
            self.btnMoveLeft.Width = 260
            self.btnMoveLeft.Height = 25
            self.btnMoveLeft.Cursor = crArrow
            self.btnMoveLeft.Align = "alTop"
            self.btnMoveLeft.Caption = 'Move Left (Left = Left - 10)'
            self.btnMoveLeft.TabOrder = 0
            # Create control: btnMoveRight = Button(self)
            self.btnMoveRight = Button(self)
            self.btnMoveRight.Name = "btnMoveRight"
            self.btnMoveRight.Parent = self.grpFormProperties
            self.btnMoveRight.Left = 2
            self.btnMoveRight.Top = 42
            self.btnMoveRight.Width = 260
            self.btnMoveRight.Height = 25
            self.btnMoveRight.Cursor = crArrow
            self.btnMoveRight.Align = "alTop"
            self.btnMoveRight.Caption = 'Move Right (Left = Left + 10)'
            self.btnMoveRight.TabOrder = 1
            # Create control: btnHide = Button(self)
            self.btnHide = Button(self)
            self.btnHide.Name = "btnHide"
            self.btnHide.Parent = self.grpFormProperties
            self.btnHide.Left = 2
            self.btnHide.Top = 67
            self.btnHide.Width = 260
            self.btnHide.Height = 25
            self.btnHide.Cursor = crArrow
            self.btnHide.Align = "alTop"
            self.btnHide.Caption = 'Hide 3s then Show'
            self.btnHide.TabOrder = 2
            # Create control: btnSetBounds = Button(self)
            self.btnSetBounds = Button(self)
            self.btnSetBounds.Name = "btnSetBounds"
            self.btnSetBounds.Parent = self.grpFormProperties
            self.btnSetBounds.Left = 2
            self.btnSetBounds.Top = 92
            self.btnSetBounds.Width = 260
            self.btnSetBounds.Height = 25
            self.btnSetBounds.Cursor = crArrow
            self.btnSetBounds.Align = "alTop"
            self.btnSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnSetBounds.TabOrder = 3
            # Create control: btnSetCaption = Button(self)
            self.btnSetCaption = Button(self)
            self.btnSetCaption.Name = "btnSetCaption"
            self.btnSetCaption.Parent = self.grpFormProperties
            self.btnSetCaption.Left = 2
            self.btnSetCaption.Top = 117
            self.btnSetCaption.Width = 260
            self.btnSetCaption.Height = 25
            self.btnSetCaption.Cursor = crArrow
            self.btnSetCaption.Align = "alTop"
            self.btnSetCaption.Caption = 'Set Caption = current timestamp'
            self.btnSetCaption.TabOrder = 4
            # Create control: btnGetCaption = Button(self)
            self.btnGetCaption = Button(self)
            self.btnGetCaption.Name = "btnGetCaption"
            self.btnGetCaption.Parent = self.grpFormProperties
            self.btnGetCaption.Left = 2
            self.btnGetCaption.Top = 142
            self.btnGetCaption.Width = 260
            self.btnGetCaption.Height = 25
            self.btnGetCaption.Cursor = crArrow
            self.btnGetCaption.Align = "alTop"
            self.btnGetCaption.Caption = 'Get Caption'
            self.btnGetCaption.TabOrder = 5
            # Create control: btnGetHandle = Button(self)
            self.btnGetHandle = Button(self)
            self.btnGetHandle.Name = "btnGetHandle"
            self.btnGetHandle.Parent = self.grpFormProperties
            self.btnGetHandle.Left = 2
            self.btnGetHandle.Top = 167
            self.btnGetHandle.Width = 260
            self.btnGetHandle.Height = 25
            self.btnGetHandle.Cursor = crArrow
            self.btnGetHandle.Align = "alTop"
            self.btnGetHandle.Caption = 'Get Form Handle'
            self.btnGetHandle.TabOrder = 6
            # Create control: btnTriggerSysVarChange = Button(self)
            self.btnTriggerSysVarChange = Button(self)
            self.btnTriggerSysVarChange.Name = "btnTriggerSysVarChange"
            self.btnTriggerSysVarChange.Parent = self.grpFormProperties
            self.btnTriggerSysVarChange.Left = 2
            self.btnTriggerSysVarChange.Top = 192
            self.btnTriggerSysVarChange.Width = 260
            self.btnTriggerSysVarChange.Height = 25
            self.btnTriggerSysVarChange.Cursor = crArrow
            self.btnTriggerSysVarChange.Align = "alTop"
            self.btnTriggerSysVarChange.Caption = 'Trigger On System Var Change Event'
            self.btnTriggerSysVarChange.TabOrder = 7
            # Create control: grpFormApis = GroupBox(self)
            self.grpFormApis = GroupBox(self)
            self.grpFormApis.Name = "grpFormApis"
            self.grpFormApis.Parent = self.shtForm
            self.grpFormApis.Left = 264
            self.grpFormApis.Top = 0
            self.grpFormApis.Width = 264
            self.grpFormApis.Height = 308
            self.grpFormApis.Cursor = crArrow
            self.grpFormApis.Align = "alLeft"
            self.grpFormApis.Caption = 'Form APIs'
            self.grpFormApis.TabOrder = 1
            # Create control: btnLog = Button(self)
            self.btnLog = Button(self)
            self.btnLog.Name = "btnLog"
            self.btnLog.Parent = self.grpFormApis
            self.btnLog.Left = 2
            self.btnLog.Top = 17
            self.btnLog.Width = 260
            self.btnLog.Height = 25
            self.btnLog.Cursor = crArrow
            self.btnLog.Align = "alTop"
            self.btnLog.Caption = 'Log events in different colors'
            self.btnLog.TabOrder = 0
            # Create control: btnToolbar = Button(self)
            self.btnToolbar = Button(self)
            self.btnToolbar.Name = "btnToolbar"
            self.btnToolbar.Parent = self.grpFormApis
            self.btnToolbar.Left = 2
            self.btnToolbar.Top = 42
            self.btnToolbar.Width = 260
            self.btnToolbar.Height = 25
            self.btnToolbar.Cursor = crArrow
            self.btnToolbar.Align = "alTop"
            self.btnToolbar.Caption = 'Register toolbar buttons'
            self.btnToolbar.TabOrder = 1
            # Create control: btnSaveConfiguration = Button(self)
            self.btnSaveConfiguration = Button(self)
            self.btnSaveConfiguration.Name = "btnSaveConfiguration"
            self.btnSaveConfiguration.Parent = self.grpFormApis
            self.btnSaveConfiguration.Left = 2
            self.btnSaveConfiguration.Top = 67
            self.btnSaveConfiguration.Width = 260
            self.btnSaveConfiguration.Height = 25
            self.btnSaveConfiguration.Cursor = crArrow
            self.btnSaveConfiguration.Align = "alTop"
            self.btnSaveConfiguration.Caption = 'Save Configurations for Left and Top'
            self.btnSaveConfiguration.TabOrder = 2
            # Create control: btnLoadConfiguration = Button(self)
            self.btnLoadConfiguration = Button(self)
            self.btnLoadConfiguration.Name = "btnLoadConfiguration"
            self.btnLoadConfiguration.Parent = self.grpFormApis
            self.btnLoadConfiguration.Left = 2
            self.btnLoadConfiguration.Top = 92
            self.btnLoadConfiguration.Width = 260
            self.btnLoadConfiguration.Height = 25
            self.btnLoadConfiguration.Cursor = crArrow
            self.btnLoadConfiguration.Align = "alTop"
            self.btnLoadConfiguration.Caption = 'Load Configurations for Left and Top'
            self.btnLoadConfiguration.TabOrder = 3
            # Create control: btnClearConf = Button(self)
            self.btnClearConf = Button(self)
            self.btnClearConf.Name = "btnClearConf"
            self.btnClearConf.Parent = self.grpFormApis
            self.btnClearConf.Left = 2
            self.btnClearConf.Top = 117
            self.btnClearConf.Width = 260
            self.btnClearConf.Height = 25
            self.btnClearConf.Cursor = crArrow
            self.btnClearConf.Align = "alTop"
            self.btnClearConf.Caption = 'Clear Configurations'
            self.btnClearConf.TabOrder = 4
            # Create control: btnSetConfiguration = Button(self)
            self.btnSetConfiguration = Button(self)
            self.btnSetConfiguration.Name = "btnSetConfiguration"
            self.btnSetConfiguration.Parent = self.grpFormApis
            self.btnSetConfiguration.Left = 2
            self.btnSetConfiguration.Top = 142
            self.btnSetConfiguration.Width = 260
            self.btnSetConfiguration.Height = 25
            self.btnSetConfiguration.Cursor = crArrow
            self.btnSetConfiguration.Align = "alTop"
            self.btnSetConfiguration.Caption = 'Set Configuration "x = 123"'
            self.btnSetConfiguration.TabOrder = 5
            # Create control: btnGetConfiguration = Button(self)
            self.btnGetConfiguration = Button(self)
            self.btnGetConfiguration.Name = "btnGetConfiguration"
            self.btnGetConfiguration.Parent = self.grpFormApis
            self.btnGetConfiguration.Left = 2
            self.btnGetConfiguration.Top = 167
            self.btnGetConfiguration.Width = 260
            self.btnGetConfiguration.Height = 25
            self.btnGetConfiguration.Cursor = crArrow
            self.btnGetConfiguration.Align = "alTop"
            self.btnGetConfiguration.Caption = 'Get Configuration "x"'
            self.btnGetConfiguration.TabOrder = 6
            # Create control: btnIsConfLoaded = Button(self)
            self.btnIsConfLoaded = Button(self)
            self.btnIsConfLoaded.Name = "btnIsConfLoaded"
            self.btnIsConfLoaded.Parent = self.grpFormApis
            self.btnIsConfLoaded.Left = 2
            self.btnIsConfLoaded.Top = 192
            self.btnIsConfLoaded.Width = 260
            self.btnIsConfLoaded.Height = 25
            self.btnIsConfLoaded.Cursor = crArrow
            self.btnIsConfLoaded.Align = "alTop"
            self.btnIsConfLoaded.Caption = 'Is Configuration Loaded ?'
            self.btnIsConfLoaded.TabOrder = 7
            # Create control: btnRegOnSysVarChange = Button(self)
            self.btnRegOnSysVarChange = Button(self)
            self.btnRegOnSysVarChange.Name = "btnRegOnSysVarChange"
            self.btnRegOnSysVarChange.Parent = self.grpFormApis
            self.btnRegOnSysVarChange.Left = 2
            self.btnRegOnSysVarChange.Top = 217
            self.btnRegOnSysVarChange.Width = 260
            self.btnRegOnSysVarChange.Height = 25
            self.btnRegOnSysVarChange.Cursor = crArrow
            self.btnRegOnSysVarChange.Align = "alTop"
            self.btnRegOnSysVarChange.Caption = 'Register On System Var Change Event'
            self.btnRegOnSysVarChange.TabOrder = 8
            # Create control: btnImageList = Button(self)
            self.btnImageList = Button(self)
            self.btnImageList.Name = "btnImageList"
            self.btnImageList.Parent = self.grpFormApis
            self.btnImageList.Left = 2
            self.btnImageList.Top = 242
            self.btnImageList.Width = 260
            self.btnImageList.Height = 24
            self.btnImageList.Cursor = crArrow
            self.btnImageList.Align = "alTop"
            self.btnImageList.Caption = 'Custom Image List Usage'
            self.btnImageList.TabOrder = 9
            # Create control: grpTools = GroupBox(self)
            self.grpTools = GroupBox(self)
            self.grpTools.Name = "grpTools"
            self.grpTools.Parent = self.shtForm
            self.grpTools.Left = 528
            self.grpTools.Top = 0
            self.grpTools.Width = 264
            self.grpTools.Height = 308
            self.grpTools.Cursor = crArrow
            self.grpTools.Align = "alLeft"
            self.grpTools.Caption = 'Tools'
            self.grpTools.TabOrder = 2
            # Create control: btnPopup = Button(self)
            self.btnPopup = Button(self)
            self.btnPopup.Name = "btnPopup"
            self.btnPopup.Parent = self.grpTools
            self.btnPopup.Left = 2
            self.btnPopup.Top = 17
            self.btnPopup.Width = 260
            self.btnPopup.Height = 25
            self.btnPopup.Cursor = crArrow
            self.btnPopup.Align = "alTop"
            self.btnPopup.Caption = 'Popup Menu...'
            self.btnPopup.TabOrder = 0
            # Create control: btnCreateForm = Button(self)
            self.btnCreateForm = Button(self)
            self.btnCreateForm.Name = "btnCreateForm"
            self.btnCreateForm.Parent = self.grpTools
            self.btnCreateForm.Left = 2
            self.btnCreateForm.Top = 42
            self.btnCreateForm.Width = 260
            self.btnCreateForm.Height = 25
            self.btnCreateForm.Cursor = crArrow
            self.btnCreateForm.Align = "alTop"
            self.btnCreateForm.Caption = 'Dynamic Create a Config Form'
            self.btnCreateForm.TabOrder = 1
            # Create control: btnListControls = Button(self)
            self.btnListControls = Button(self)
            self.btnListControls.Name = "btnListControls"
            self.btnListControls.Parent = self.grpTools
            self.btnListControls.Left = 2
            self.btnListControls.Top = 67
            self.btnListControls.Width = 260
            self.btnListControls.Height = 25
            self.btnListControls.Cursor = crArrow
            self.btnListControls.Align = "alTop"
            self.btnListControls.Caption = 'List Controls'
            self.btnListControls.TabOrder = 2
            # Create control: shtLabel = TabSheet(self)
            self.shtLabel = TabSheet(self)
            self.shtLabel.Name = "shtLabel"
            self.shtLabel.PageControl = self.pgFeatures
            self.shtLabel.Cursor = crArrow
            self.shtLabel.Caption = 'Label'
            # Create control: lblLabel = Label(self)
            self.lblLabel = Label(self)
            self.lblLabel.Name = "lblLabel"
            self.lblLabel.Parent = self.shtLabel
            self.lblLabel.Left = 48
            self.lblLabel.Top = 32
            self.lblLabel.Width = 103
            self.lblLabel.Height = 15
            self.lblLabel.Cursor = crArrow
            self.lblLabel.Caption = 'This is a demo label'
            # Create control: grpLabel = GroupBox(self)
            self.grpLabel = GroupBox(self)
            self.grpLabel.Name = "grpLabel"
            self.grpLabel.Parent = self.shtLabel
            self.grpLabel.Left = 1123
            self.grpLabel.Top = 0
            self.grpLabel.Width = 264
            self.grpLabel.Height = 308
            self.grpLabel.Cursor = crArrow
            self.grpLabel.Align = "alRight"
            self.grpLabel.Caption = 'Control Usages'
            self.grpLabel.TabOrder = 0
            # Create control: btnSetLabelBounds = Button(self)
            self.btnSetLabelBounds = Button(self)
            self.btnSetLabelBounds.Name = "btnSetLabelBounds"
            self.btnSetLabelBounds.Parent = self.grpLabel
            self.btnSetLabelBounds.Left = 2
            self.btnSetLabelBounds.Top = 92
            self.btnSetLabelBounds.Width = 260
            self.btnSetLabelBounds.Height = 25
            self.btnSetLabelBounds.Cursor = crArrow
            self.btnSetLabelBounds.Align = "alTop"
            self.btnSetLabelBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnSetLabelBounds.TabOrder = 0
            # Create control: btnSetLabelTransparency = Button(self)
            self.btnSetLabelTransparency = Button(self)
            self.btnSetLabelTransparency.Name = "btnSetLabelTransparency"
            self.btnSetLabelTransparency.Parent = self.grpLabel
            self.btnSetLabelTransparency.Left = 2
            self.btnSetLabelTransparency.Top = 42
            self.btnSetLabelTransparency.Width = 260
            self.btnSetLabelTransparency.Height = 25
            self.btnSetLabelTransparency.Cursor = crArrow
            self.btnSetLabelTransparency.Align = "alTop"
            self.btnSetLabelTransparency.Caption = 'Toggle Label Transparency'
            self.btnSetLabelTransparency.TabOrder = 1
            # Create control: btnSetLabelCaption = Button(self)
            self.btnSetLabelCaption = Button(self)
            self.btnSetLabelCaption.Name = "btnSetLabelCaption"
            self.btnSetLabelCaption.Parent = self.grpLabel
            self.btnSetLabelCaption.Left = 2
            self.btnSetLabelCaption.Top = 67
            self.btnSetLabelCaption.Width = 260
            self.btnSetLabelCaption.Height = 25
            self.btnSetLabelCaption.Cursor = crArrow
            self.btnSetLabelCaption.Align = "alTop"
            self.btnSetLabelCaption.Caption = 'Set Label Caption'
            self.btnSetLabelCaption.TabOrder = 2
            # Create control: btnSetLabelBackColor = Button(self)
            self.btnSetLabelBackColor = Button(self)
            self.btnSetLabelBackColor.Name = "btnSetLabelBackColor"
            self.btnSetLabelBackColor.Parent = self.grpLabel
            self.btnSetLabelBackColor.Left = 2
            self.btnSetLabelBackColor.Top = 17
            self.btnSetLabelBackColor.Width = 260
            self.btnSetLabelBackColor.Height = 25
            self.btnSetLabelBackColor.Cursor = crArrow
            self.btnSetLabelBackColor.Align = "alTop"
            self.btnSetLabelBackColor.Caption = 'Set Label Background Color'
            self.btnSetLabelBackColor.TabOrder = 3
            # Create control: btnToggleLabelAutoSize = Button(self)
            self.btnToggleLabelAutoSize = Button(self)
            self.btnToggleLabelAutoSize.Name = "btnToggleLabelAutoSize"
            self.btnToggleLabelAutoSize.Parent = self.grpLabel
            self.btnToggleLabelAutoSize.Left = 2
            self.btnToggleLabelAutoSize.Top = 117
            self.btnToggleLabelAutoSize.Width = 260
            self.btnToggleLabelAutoSize.Height = 25
            self.btnToggleLabelAutoSize.Cursor = crArrow
            self.btnToggleLabelAutoSize.Align = "alTop"
            self.btnToggleLabelAutoSize.Caption = 'Toggle Label Auto Size'
            self.btnToggleLabelAutoSize.TabOrder = 4
            # Create control: btnSetLabelFont = Button(self)
            self.btnSetLabelFont = Button(self)
            self.btnSetLabelFont.Name = "btnSetLabelFont"
            self.btnSetLabelFont.Parent = self.grpLabel
            self.btnSetLabelFont.Left = 2
            self.btnSetLabelFont.Top = 142
            self.btnSetLabelFont.Width = 260
            self.btnSetLabelFont.Height = 25
            self.btnSetLabelFont.Cursor = crArrow
            self.btnSetLabelFont.Align = "alTop"
            self.btnSetLabelFont.Caption = 'Set Label Font'
            self.btnSetLabelFont.TabOrder = 5
            # Create control: btnToggleLabelEnabled = Button(self)
            self.btnToggleLabelEnabled = Button(self)
            self.btnToggleLabelEnabled.Name = "btnToggleLabelEnabled"
            self.btnToggleLabelEnabled.Parent = self.grpLabel
            self.btnToggleLabelEnabled.Left = 2
            self.btnToggleLabelEnabled.Top = 167
            self.btnToggleLabelEnabled.Width = 260
            self.btnToggleLabelEnabled.Height = 25
            self.btnToggleLabelEnabled.Cursor = crArrow
            self.btnToggleLabelEnabled.Align = "alTop"
            self.btnToggleLabelEnabled.Caption = 'Toggle Label Enabled'
            self.btnToggleLabelEnabled.TabOrder = 6
            # Create control: btnToggleLabelVisible = Button(self)
            self.btnToggleLabelVisible = Button(self)
            self.btnToggleLabelVisible.Name = "btnToggleLabelVisible"
            self.btnToggleLabelVisible.Parent = self.grpLabel
            self.btnToggleLabelVisible.Left = 2
            self.btnToggleLabelVisible.Top = 192
            self.btnToggleLabelVisible.Width = 260
            self.btnToggleLabelVisible.Height = 25
            self.btnToggleLabelVisible.Cursor = crArrow
            self.btnToggleLabelVisible.Align = "alTop"
            self.btnToggleLabelVisible.Caption = 'Toggle Label Visible'
            self.btnToggleLabelVisible.TabOrder = 7
            # Create control: btnSetLabelAlign = Button(self)
            self.btnSetLabelAlign = Button(self)
            self.btnSetLabelAlign.Name = "btnSetLabelAlign"
            self.btnSetLabelAlign.Parent = self.grpLabel
            self.btnSetLabelAlign.Left = 2
            self.btnSetLabelAlign.Top = 217
            self.btnSetLabelAlign.Width = 260
            self.btnSetLabelAlign.Height = 25
            self.btnSetLabelAlign.Cursor = crArrow
            self.btnSetLabelAlign.Align = "alTop"
            self.btnSetLabelAlign.Caption = 'Set Label Align'
            self.btnSetLabelAlign.TabOrder = 8
            # Create control: btnSetLabelAlignment = Button(self)
            self.btnSetLabelAlignment = Button(self)
            self.btnSetLabelAlignment.Name = "btnSetLabelAlignment"
            self.btnSetLabelAlignment.Parent = self.grpLabel
            self.btnSetLabelAlignment.Left = 2
            self.btnSetLabelAlignment.Top = 242
            self.btnSetLabelAlignment.Width = 260
            self.btnSetLabelAlignment.Height = 25
            self.btnSetLabelAlignment.Cursor = crArrow
            self.btnSetLabelAlignment.Align = "alTop"
            self.btnSetLabelAlignment.Caption = 'Set Label Text Alignment'
            self.btnSetLabelAlignment.TabOrder = 9
            # Create control: btnSetLabelMargins = Button(self)
            self.btnSetLabelMargins = Button(self)
            self.btnSetLabelMargins.Name = "btnSetLabelMargins"
            self.btnSetLabelMargins.Parent = self.grpLabel
            self.btnSetLabelMargins.Left = 2
            self.btnSetLabelMargins.Top = 267
            self.btnSetLabelMargins.Width = 260
            self.btnSetLabelMargins.Height = 25
            self.btnSetLabelMargins.Cursor = crArrow
            self.btnSetLabelMargins.Align = "alTop"
            self.btnSetLabelMargins.Caption = 'Set Label Margins'
            self.btnSetLabelMargins.TabOrder = 10
            # Create control: btnSetLabelOnClickEvent = Button(self)
            self.btnSetLabelOnClickEvent = Button(self)
            self.btnSetLabelOnClickEvent.Name = "btnSetLabelOnClickEvent"
            self.btnSetLabelOnClickEvent.Parent = self.grpLabel
            self.btnSetLabelOnClickEvent.Left = 2
            self.btnSetLabelOnClickEvent.Top = 292
            self.btnSetLabelOnClickEvent.Width = 260
            self.btnSetLabelOnClickEvent.Height = 25
            self.btnSetLabelOnClickEvent.Cursor = crArrow
            self.btnSetLabelOnClickEvent.Align = "alTop"
            self.btnSetLabelOnClickEvent.Caption = 'Set Label On Click Event'
            self.btnSetLabelOnClickEvent.TabOrder = 11
            # Create control: shtButton = TabSheet(self)
            self.shtButton = TabSheet(self)
            self.shtButton.Name = "shtButton"
            self.shtButton.PageControl = self.pgFeatures
            self.shtButton.Cursor = crArrow
            self.shtButton.Caption = 'Button'
            # Create control: grpButton = GroupBox(self)
            self.grpButton = GroupBox(self)
            self.grpButton.Name = "grpButton"
            self.grpButton.Parent = self.shtButton
            self.grpButton.Left = 1123
            self.grpButton.Top = 0
            self.grpButton.Width = 264
            self.grpButton.Height = 308
            self.grpButton.Cursor = crArrow
            self.grpButton.Align = "alRight"
            self.grpButton.Caption = 'Control Usages'
            self.grpButton.TabOrder = 0
            # Create control: btnSetButtonBounds = Button(self)
            self.btnSetButtonBounds = Button(self)
            self.btnSetButtonBounds.Name = "btnSetButtonBounds"
            self.btnSetButtonBounds.Parent = self.grpButton
            self.btnSetButtonBounds.Left = 2
            self.btnSetButtonBounds.Top = 42
            self.btnSetButtonBounds.Width = 260
            self.btnSetButtonBounds.Height = 25
            self.btnSetButtonBounds.Cursor = crArrow
            self.btnSetButtonBounds.Align = "alTop"
            self.btnSetButtonBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnSetButtonBounds.TabOrder = 0
            # Create control: btnSetButtonCaption = Button(self)
            self.btnSetButtonCaption = Button(self)
            self.btnSetButtonCaption.Name = "btnSetButtonCaption"
            self.btnSetButtonCaption.Parent = self.grpButton
            self.btnSetButtonCaption.Left = 2
            self.btnSetButtonCaption.Top = 17
            self.btnSetButtonCaption.Width = 260
            self.btnSetButtonCaption.Height = 25
            self.btnSetButtonCaption.Cursor = crArrow
            self.btnSetButtonCaption.Align = "alTop"
            self.btnSetButtonCaption.Caption = 'Set Button Caption'
            self.btnSetButtonCaption.TabOrder = 1
            # Create control: btnSetButtonFont = Button(self)
            self.btnSetButtonFont = Button(self)
            self.btnSetButtonFont.Name = "btnSetButtonFont"
            self.btnSetButtonFont.Parent = self.grpButton
            self.btnSetButtonFont.Left = 2
            self.btnSetButtonFont.Top = 67
            self.btnSetButtonFont.Width = 260
            self.btnSetButtonFont.Height = 25
            self.btnSetButtonFont.Cursor = crArrow
            self.btnSetButtonFont.Align = "alTop"
            self.btnSetButtonFont.Caption = 'Set Button Font'
            self.btnSetButtonFont.TabOrder = 2
            # Create control: btnToggleButtonEnabled = Button(self)
            self.btnToggleButtonEnabled = Button(self)
            self.btnToggleButtonEnabled.Name = "btnToggleButtonEnabled"
            self.btnToggleButtonEnabled.Parent = self.grpButton
            self.btnToggleButtonEnabled.Left = 2
            self.btnToggleButtonEnabled.Top = 92
            self.btnToggleButtonEnabled.Width = 260
            self.btnToggleButtonEnabled.Height = 25
            self.btnToggleButtonEnabled.Cursor = crArrow
            self.btnToggleButtonEnabled.Align = "alTop"
            self.btnToggleButtonEnabled.Caption = 'Toggle Button Enabled'
            self.btnToggleButtonEnabled.TabOrder = 3
            # Create control: btnToggleButtonVisible = Button(self)
            self.btnToggleButtonVisible = Button(self)
            self.btnToggleButtonVisible.Name = "btnToggleButtonVisible"
            self.btnToggleButtonVisible.Parent = self.grpButton
            self.btnToggleButtonVisible.Left = 2
            self.btnToggleButtonVisible.Top = 117
            self.btnToggleButtonVisible.Width = 260
            self.btnToggleButtonVisible.Height = 25
            self.btnToggleButtonVisible.Cursor = crArrow
            self.btnToggleButtonVisible.Align = "alTop"
            self.btnToggleButtonVisible.Caption = 'Toggle Button Visible'
            self.btnToggleButtonVisible.TabOrder = 4
            # Create control: btnSetButtonAlign = Button(self)
            self.btnSetButtonAlign = Button(self)
            self.btnSetButtonAlign.Name = "btnSetButtonAlign"
            self.btnSetButtonAlign.Parent = self.grpButton
            self.btnSetButtonAlign.Left = 2
            self.btnSetButtonAlign.Top = 142
            self.btnSetButtonAlign.Width = 260
            self.btnSetButtonAlign.Height = 25
            self.btnSetButtonAlign.Cursor = crArrow
            self.btnSetButtonAlign.Align = "alTop"
            self.btnSetButtonAlign.Caption = 'Set Button Align'
            self.btnSetButtonAlign.TabOrder = 5
            # Create control: btnSetButtonMargins = Button(self)
            self.btnSetButtonMargins = Button(self)
            self.btnSetButtonMargins.Name = "btnSetButtonMargins"
            self.btnSetButtonMargins.Parent = self.grpButton
            self.btnSetButtonMargins.Left = 2
            self.btnSetButtonMargins.Top = 167
            self.btnSetButtonMargins.Width = 260
            self.btnSetButtonMargins.Height = 25
            self.btnSetButtonMargins.Cursor = crArrow
            self.btnSetButtonMargins.Align = "alTop"
            self.btnSetButtonMargins.Caption = 'Set Button Margins'
            self.btnSetButtonMargins.TabOrder = 6
            # Create control: btnSetButtonOnClickEvent = Button(self)
            self.btnSetButtonOnClickEvent = Button(self)
            self.btnSetButtonOnClickEvent.Name = "btnSetButtonOnClickEvent"
            self.btnSetButtonOnClickEvent.Parent = self.grpButton
            self.btnSetButtonOnClickEvent.Left = 2
            self.btnSetButtonOnClickEvent.Top = 192
            self.btnSetButtonOnClickEvent.Width = 260
            self.btnSetButtonOnClickEvent.Height = 25
            self.btnSetButtonOnClickEvent.Cursor = crArrow
            self.btnSetButtonOnClickEvent.Align = "alTop"
            self.btnSetButtonOnClickEvent.Caption = 'Set Button On Click Event'
            self.btnSetButtonOnClickEvent.TabOrder = 7
            # Create control: btnSetButtonImage = Button(self)
            self.btnSetButtonImage = Button(self)
            self.btnSetButtonImage.Name = "btnSetButtonImage"
            self.btnSetButtonImage.Parent = self.grpButton
            self.btnSetButtonImage.Left = 2
            self.btnSetButtonImage.Top = 217
            self.btnSetButtonImage.Width = 260
            self.btnSetButtonImage.Height = 25
            self.btnSetButtonImage.Cursor = crArrow
            self.btnSetButtonImage.Align = "alTop"
            self.btnSetButtonImage.Caption = 'Set Button Image'
            self.btnSetButtonImage.TabOrder = 8
            # Create control: btnButton = Button(self)
            self.btnButton = Button(self)
            self.btnButton.Name = "btnButton"
            self.btnButton.Parent = self.shtButton
            self.btnButton.Left = 64
            self.btnButton.Top = 64
            self.btnButton.Width = 96
            self.btnButton.Height = 25
            self.btnButton.Cursor = crArrow
            self.btnButton.Caption = 'Demo Button'
            self.btnButton.TabOrder = 1
            # Create control: shtEdit = TabSheet(self)
            self.shtEdit = TabSheet(self)
            self.shtEdit.Name = "shtEdit"
            self.shtEdit.PageControl = self.pgFeatures
            self.shtEdit.Cursor = crArrow
            self.shtEdit.Caption = 'Edit'
            # Create control: grpEdit = GroupBox(self)
            self.grpEdit = GroupBox(self)
            self.grpEdit.Name = "grpEdit"
            self.grpEdit.Parent = self.shtEdit
            self.grpEdit.Left = 1123
            self.grpEdit.Top = 0
            self.grpEdit.Width = 264
            self.grpEdit.Height = 308
            self.grpEdit.Cursor = crArrow
            self.grpEdit.Align = "alRight"
            self.grpEdit.Caption = 'Control Usages'
            self.grpEdit.TabOrder = 0
            # Create control: btnSetEditBounds = Button(self)
            self.btnSetEditBounds = Button(self)
            self.btnSetEditBounds.Name = "btnSetEditBounds"
            self.btnSetEditBounds.Parent = self.grpEdit
            self.btnSetEditBounds.Left = 2
            self.btnSetEditBounds.Top = 42
            self.btnSetEditBounds.Width = 260
            self.btnSetEditBounds.Height = 25
            self.btnSetEditBounds.Cursor = crArrow
            self.btnSetEditBounds.Align = "alTop"
            self.btnSetEditBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnSetEditBounds.TabOrder = 0
            # Create control: btnSetEditText = Button(self)
            self.btnSetEditText = Button(self)
            self.btnSetEditText.Name = "btnSetEditText"
            self.btnSetEditText.Parent = self.grpEdit
            self.btnSetEditText.Left = 2
            self.btnSetEditText.Top = 17
            self.btnSetEditText.Width = 260
            self.btnSetEditText.Height = 25
            self.btnSetEditText.Cursor = crArrow
            self.btnSetEditText.Align = "alTop"
            self.btnSetEditText.Caption = 'Set Edit Text'
            self.btnSetEditText.TabOrder = 1
            # Create control: btnSetEditFont = Button(self)
            self.btnSetEditFont = Button(self)
            self.btnSetEditFont.Name = "btnSetEditFont"
            self.btnSetEditFont.Parent = self.grpEdit
            self.btnSetEditFont.Left = 2
            self.btnSetEditFont.Top = 67
            self.btnSetEditFont.Width = 260
            self.btnSetEditFont.Height = 25
            self.btnSetEditFont.Cursor = crArrow
            self.btnSetEditFont.Align = "alTop"
            self.btnSetEditFont.Caption = 'Set Edit Font'
            self.btnSetEditFont.TabOrder = 2
            # Create control: btnToggleEditEnabled = Button(self)
            self.btnToggleEditEnabled = Button(self)
            self.btnToggleEditEnabled.Name = "btnToggleEditEnabled"
            self.btnToggleEditEnabled.Parent = self.grpEdit
            self.btnToggleEditEnabled.Left = 2
            self.btnToggleEditEnabled.Top = 92
            self.btnToggleEditEnabled.Width = 260
            self.btnToggleEditEnabled.Height = 25
            self.btnToggleEditEnabled.Cursor = crArrow
            self.btnToggleEditEnabled.Align = "alTop"
            self.btnToggleEditEnabled.Caption = 'Toggle Edit Enabled'
            self.btnToggleEditEnabled.TabOrder = 3
            # Create control: btnToggleEditVisible = Button(self)
            self.btnToggleEditVisible = Button(self)
            self.btnToggleEditVisible.Name = "btnToggleEditVisible"
            self.btnToggleEditVisible.Parent = self.grpEdit
            self.btnToggleEditVisible.Left = 2
            self.btnToggleEditVisible.Top = 117
            self.btnToggleEditVisible.Width = 260
            self.btnToggleEditVisible.Height = 25
            self.btnToggleEditVisible.Cursor = crArrow
            self.btnToggleEditVisible.Align = "alTop"
            self.btnToggleEditVisible.Caption = 'Toggle Edit Visible'
            self.btnToggleEditVisible.TabOrder = 4
            # Create control: btnSetEditAlign = Button(self)
            self.btnSetEditAlign = Button(self)
            self.btnSetEditAlign.Name = "btnSetEditAlign"
            self.btnSetEditAlign.Parent = self.grpEdit
            self.btnSetEditAlign.Left = 2
            self.btnSetEditAlign.Top = 167
            self.btnSetEditAlign.Width = 260
            self.btnSetEditAlign.Height = 25
            self.btnSetEditAlign.Cursor = crArrow
            self.btnSetEditAlign.Align = "alTop"
            self.btnSetEditAlign.Caption = 'Set Edit Align'
            self.btnSetEditAlign.TabOrder = 5
            # Create control: btnSetEditMargins = Button(self)
            self.btnSetEditMargins = Button(self)
            self.btnSetEditMargins.Name = "btnSetEditMargins"
            self.btnSetEditMargins.Parent = self.grpEdit
            self.btnSetEditMargins.Left = 2
            self.btnSetEditMargins.Top = 192
            self.btnSetEditMargins.Width = 260
            self.btnSetEditMargins.Height = 25
            self.btnSetEditMargins.Cursor = crArrow
            self.btnSetEditMargins.Align = "alTop"
            self.btnSetEditMargins.Caption = 'Set Edit Margins'
            self.btnSetEditMargins.TabOrder = 6
            # Create control: btnSetEditClickEvent = Button(self)
            self.btnSetEditClickEvent = Button(self)
            self.btnSetEditClickEvent.Name = "btnSetEditClickEvent"
            self.btnSetEditClickEvent.Parent = self.grpEdit
            self.btnSetEditClickEvent.Left = 2
            self.btnSetEditClickEvent.Top = 217
            self.btnSetEditClickEvent.Width = 260
            self.btnSetEditClickEvent.Height = 25
            self.btnSetEditClickEvent.Cursor = crArrow
            self.btnSetEditClickEvent.Align = "alTop"
            self.btnSetEditClickEvent.Caption = 'Set Edit On Click Event'
            self.btnSetEditClickEvent.TabOrder = 7
            # Create control: btnSetEditReadOnly = Button(self)
            self.btnSetEditReadOnly = Button(self)
            self.btnSetEditReadOnly.Name = "btnSetEditReadOnly"
            self.btnSetEditReadOnly.Parent = self.grpEdit
            self.btnSetEditReadOnly.Left = 2
            self.btnSetEditReadOnly.Top = 317
            self.btnSetEditReadOnly.Width = 260
            self.btnSetEditReadOnly.Height = 25
            self.btnSetEditReadOnly.Cursor = crArrow
            self.btnSetEditReadOnly.Align = "alTop"
            self.btnSetEditReadOnly.Caption = 'Set Edit Read Only'
            self.btnSetEditReadOnly.TabOrder = 8
            # Create control: btnSetEditTextAlignment = Button(self)
            self.btnSetEditTextAlignment = Button(self)
            self.btnSetEditTextAlignment.Name = "btnSetEditTextAlignment"
            self.btnSetEditTextAlignment.Parent = self.grpEdit
            self.btnSetEditTextAlignment.Left = 2
            self.btnSetEditTextAlignment.Top = 142
            self.btnSetEditTextAlignment.Width = 260
            self.btnSetEditTextAlignment.Height = 25
            self.btnSetEditTextAlignment.Cursor = crArrow
            self.btnSetEditTextAlignment.Align = "alTop"
            self.btnSetEditTextAlignment.Caption = 'Set Edit Text Alignment'
            self.btnSetEditTextAlignment.TabOrder = 9
            # Create control: btnSetEditTextHint = Button(self)
            self.btnSetEditTextHint = Button(self)
            self.btnSetEditTextHint.Name = "btnSetEditTextHint"
            self.btnSetEditTextHint.Parent = self.grpEdit
            self.btnSetEditTextHint.Left = 2
            self.btnSetEditTextHint.Top = 267
            self.btnSetEditTextHint.Width = 260
            self.btnSetEditTextHint.Height = 25
            self.btnSetEditTextHint.Cursor = crArrow
            self.btnSetEditTextHint.Align = "alTop"
            self.btnSetEditTextHint.Caption = 'Set Edit Text Hint'
            self.btnSetEditTextHint.TabOrder = 10
            # Create control: btnSetEditNumbersOnly = Button(self)
            self.btnSetEditNumbersOnly = Button(self)
            self.btnSetEditNumbersOnly.Name = "btnSetEditNumbersOnly"
            self.btnSetEditNumbersOnly.Parent = self.grpEdit
            self.btnSetEditNumbersOnly.Left = 2
            self.btnSetEditNumbersOnly.Top = 292
            self.btnSetEditNumbersOnly.Width = 260
            self.btnSetEditNumbersOnly.Height = 25
            self.btnSetEditNumbersOnly.Cursor = crArrow
            self.btnSetEditNumbersOnly.Align = "alTop"
            self.btnSetEditNumbersOnly.Caption = 'Set Edit Numbers Only'
            self.btnSetEditNumbersOnly.TabOrder = 11
            # Create control: btnSetOnEditChangeEvent = Button(self)
            self.btnSetOnEditChangeEvent = Button(self)
            self.btnSetOnEditChangeEvent.Name = "btnSetOnEditChangeEvent"
            self.btnSetOnEditChangeEvent.Parent = self.grpEdit
            self.btnSetOnEditChangeEvent.Left = 2
            self.btnSetOnEditChangeEvent.Top = 242
            self.btnSetOnEditChangeEvent.Width = 260
            self.btnSetOnEditChangeEvent.Height = 25
            self.btnSetOnEditChangeEvent.Cursor = crArrow
            self.btnSetOnEditChangeEvent.Align = "alTop"
            self.btnSetOnEditChangeEvent.Caption = 'Set Edit On Change Event'
            self.btnSetOnEditChangeEvent.TabOrder = 12
            # Create control: edtEdit = Edit(self)
            self.edtEdit = Edit(self)
            self.edtEdit.Name = "edtEdit"
            self.edtEdit.Parent = self.shtEdit
            self.edtEdit.Left = 80
            self.edtEdit.Top = 48
            self.edtEdit.Width = 121
            self.edtEdit.Height = 23
            self.edtEdit.Cursor = crArrow
            self.edtEdit.TabOrder = 1
            self.edtEdit.Text = 'Edit'
            # Create control: shtCheckBox = TabSheet(self)
            self.shtCheckBox = TabSheet(self)
            self.shtCheckBox.Name = "shtCheckBox"
            self.shtCheckBox.PageControl = self.pgFeatures
            self.shtCheckBox.Cursor = crArrow
            self.shtCheckBox.Caption = 'Check Box'
            # Create control: grpCheckbox = GroupBox(self)
            self.grpCheckbox = GroupBox(self)
            self.grpCheckbox.Name = "grpCheckbox"
            self.grpCheckbox.Parent = self.shtCheckBox
            self.grpCheckbox.Left = 1123
            self.grpCheckbox.Top = 0
            self.grpCheckbox.Width = 264
            self.grpCheckbox.Height = 308
            self.grpCheckbox.Cursor = crArrow
            self.grpCheckbox.Align = "alRight"
            self.grpCheckbox.Caption = 'Control Usages'
            self.grpCheckbox.TabOrder = 0
            # Create control: btnSetCheckboxBounds = Button(self)
            self.btnSetCheckboxBounds = Button(self)
            self.btnSetCheckboxBounds.Name = "btnSetCheckboxBounds"
            self.btnSetCheckboxBounds.Parent = self.grpCheckbox
            self.btnSetCheckboxBounds.Left = 2
            self.btnSetCheckboxBounds.Top = 42
            self.btnSetCheckboxBounds.Width = 260
            self.btnSetCheckboxBounds.Height = 25
            self.btnSetCheckboxBounds.Cursor = crArrow
            self.btnSetCheckboxBounds.Align = "alTop"
            self.btnSetCheckboxBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnSetCheckboxBounds.TabOrder = 0
            # Create control: btnSetCheckboxText = Button(self)
            self.btnSetCheckboxText = Button(self)
            self.btnSetCheckboxText.Name = "btnSetCheckboxText"
            self.btnSetCheckboxText.Parent = self.grpCheckbox
            self.btnSetCheckboxText.Left = 2
            self.btnSetCheckboxText.Top = 17
            self.btnSetCheckboxText.Width = 260
            self.btnSetCheckboxText.Height = 25
            self.btnSetCheckboxText.Cursor = crArrow
            self.btnSetCheckboxText.Align = "alTop"
            self.btnSetCheckboxText.Caption = 'Set Checkbox Text'
            self.btnSetCheckboxText.TabOrder = 1
            # Create control: btnSetCheckboxFont = Button(self)
            self.btnSetCheckboxFont = Button(self)
            self.btnSetCheckboxFont.Name = "btnSetCheckboxFont"
            self.btnSetCheckboxFont.Parent = self.grpCheckbox
            self.btnSetCheckboxFont.Left = 2
            self.btnSetCheckboxFont.Top = 67
            self.btnSetCheckboxFont.Width = 260
            self.btnSetCheckboxFont.Height = 25
            self.btnSetCheckboxFont.Cursor = crArrow
            self.btnSetCheckboxFont.Align = "alTop"
            self.btnSetCheckboxFont.Caption = 'Set Checkbox Font'
            self.btnSetCheckboxFont.TabOrder = 2
            # Create control: btnToggleCheckboxEnabled = Button(self)
            self.btnToggleCheckboxEnabled = Button(self)
            self.btnToggleCheckboxEnabled.Name = "btnToggleCheckboxEnabled"
            self.btnToggleCheckboxEnabled.Parent = self.grpCheckbox
            self.btnToggleCheckboxEnabled.Left = 2
            self.btnToggleCheckboxEnabled.Top = 92
            self.btnToggleCheckboxEnabled.Width = 260
            self.btnToggleCheckboxEnabled.Height = 25
            self.btnToggleCheckboxEnabled.Cursor = crArrow
            self.btnToggleCheckboxEnabled.Align = "alTop"
            self.btnToggleCheckboxEnabled.Caption = 'Toggle Checkbox Enabled'
            self.btnToggleCheckboxEnabled.TabOrder = 3
            # Create control: btnToggleCheckboxVisible = Button(self)
            self.btnToggleCheckboxVisible = Button(self)
            self.btnToggleCheckboxVisible.Name = "btnToggleCheckboxVisible"
            self.btnToggleCheckboxVisible.Parent = self.grpCheckbox
            self.btnToggleCheckboxVisible.Left = 2
            self.btnToggleCheckboxVisible.Top = 117
            self.btnToggleCheckboxVisible.Width = 260
            self.btnToggleCheckboxVisible.Height = 25
            self.btnToggleCheckboxVisible.Cursor = crArrow
            self.btnToggleCheckboxVisible.Align = "alTop"
            self.btnToggleCheckboxVisible.Caption = 'Toggle Checkbox Visible'
            self.btnToggleCheckboxVisible.TabOrder = 4
            # Create control: btnSetCheckboxAlign = Button(self)
            self.btnSetCheckboxAlign = Button(self)
            self.btnSetCheckboxAlign.Name = "btnSetCheckboxAlign"
            self.btnSetCheckboxAlign.Parent = self.grpCheckbox
            self.btnSetCheckboxAlign.Left = 2
            self.btnSetCheckboxAlign.Top = 142
            self.btnSetCheckboxAlign.Width = 260
            self.btnSetCheckboxAlign.Height = 25
            self.btnSetCheckboxAlign.Cursor = crArrow
            self.btnSetCheckboxAlign.Align = "alTop"
            self.btnSetCheckboxAlign.Caption = 'Set Checkbox Align'
            self.btnSetCheckboxAlign.TabOrder = 5
            # Create control: btnSetCheckboxMargins = Button(self)
            self.btnSetCheckboxMargins = Button(self)
            self.btnSetCheckboxMargins.Name = "btnSetCheckboxMargins"
            self.btnSetCheckboxMargins.Parent = self.grpCheckbox
            self.btnSetCheckboxMargins.Left = 2
            self.btnSetCheckboxMargins.Top = 167
            self.btnSetCheckboxMargins.Width = 260
            self.btnSetCheckboxMargins.Height = 25
            self.btnSetCheckboxMargins.Cursor = crArrow
            self.btnSetCheckboxMargins.Align = "alTop"
            self.btnSetCheckboxMargins.Caption = 'Set Checkbox Margins'
            self.btnSetCheckboxMargins.TabOrder = 6
            # Create control: btnSetCheckboxOnClickEvent = Button(self)
            self.btnSetCheckboxOnClickEvent = Button(self)
            self.btnSetCheckboxOnClickEvent.Name = "btnSetCheckboxOnClickEvent"
            self.btnSetCheckboxOnClickEvent.Parent = self.grpCheckbox
            self.btnSetCheckboxOnClickEvent.Left = 2
            self.btnSetCheckboxOnClickEvent.Top = 192
            self.btnSetCheckboxOnClickEvent.Width = 260
            self.btnSetCheckboxOnClickEvent.Height = 25
            self.btnSetCheckboxOnClickEvent.Cursor = crArrow
            self.btnSetCheckboxOnClickEvent.Align = "alTop"
            self.btnSetCheckboxOnClickEvent.Caption = 'Set On Click Event'
            self.btnSetCheckboxOnClickEvent.TabOrder = 7
            # Create control: btnToggleCheckboxChecked = Button(self)
            self.btnToggleCheckboxChecked = Button(self)
            self.btnToggleCheckboxChecked.Name = "btnToggleCheckboxChecked"
            self.btnToggleCheckboxChecked.Parent = self.grpCheckbox
            self.btnToggleCheckboxChecked.Left = 2
            self.btnToggleCheckboxChecked.Top = 217
            self.btnToggleCheckboxChecked.Width = 260
            self.btnToggleCheckboxChecked.Height = 25
            self.btnToggleCheckboxChecked.Cursor = crArrow
            self.btnToggleCheckboxChecked.Align = "alTop"
            self.btnToggleCheckboxChecked.Caption = 'Toggle Checked State'
            self.btnToggleCheckboxChecked.TabOrder = 8
            # Create control: chkCheckbox = CheckBox(self)
            self.chkCheckbox = CheckBox(self)
            self.chkCheckbox.Name = "chkCheckbox"
            self.chkCheckbox.Parent = self.shtCheckBox
            self.chkCheckbox.Left = 88
            self.chkCheckbox.Top = 48
            self.chkCheckbox.Width = 232
            self.chkCheckbox.Height = 17
            self.chkCheckbox.Cursor = crArrow
            self.chkCheckbox.Caption = 'Checkbox'
            self.chkCheckbox.TabOrder = 1
            # Create control: shtRadioButton = TabSheet(self)
            self.shtRadioButton = TabSheet(self)
            self.shtRadioButton.Name = "shtRadioButton"
            self.shtRadioButton.PageControl = self.pgFeatures
            self.shtRadioButton.Cursor = crArrow
            self.shtRadioButton.Caption = 'Radio Button'
            # Create control: grpRadioButton = GroupBox(self)
            self.grpRadioButton = GroupBox(self)
            self.grpRadioButton.Name = "grpRadioButton"
            self.grpRadioButton.Parent = self.shtRadioButton
            self.grpRadioButton.Left = 1123
            self.grpRadioButton.Top = 0
            self.grpRadioButton.Width = 264
            self.grpRadioButton.Height = 308
            self.grpRadioButton.Cursor = crArrow
            self.grpRadioButton.Align = "alRight"
            self.grpRadioButton.Caption = 'Control Usages'
            self.grpRadioButton.TabOrder = 0
            # Create control: btnSetRadioButtonBounds = Button(self)
            self.btnSetRadioButtonBounds = Button(self)
            self.btnSetRadioButtonBounds.Name = "btnSetRadioButtonBounds"
            self.btnSetRadioButtonBounds.Parent = self.grpRadioButton
            self.btnSetRadioButtonBounds.Left = 2
            self.btnSetRadioButtonBounds.Top = 42
            self.btnSetRadioButtonBounds.Width = 260
            self.btnSetRadioButtonBounds.Height = 25
            self.btnSetRadioButtonBounds.Cursor = crArrow
            self.btnSetRadioButtonBounds.Align = "alTop"
            self.btnSetRadioButtonBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnSetRadioButtonBounds.TabOrder = 0
            # Create control: btnSetRadioButtonText = Button(self)
            self.btnSetRadioButtonText = Button(self)
            self.btnSetRadioButtonText.Name = "btnSetRadioButtonText"
            self.btnSetRadioButtonText.Parent = self.grpRadioButton
            self.btnSetRadioButtonText.Left = 2
            self.btnSetRadioButtonText.Top = 17
            self.btnSetRadioButtonText.Width = 260
            self.btnSetRadioButtonText.Height = 25
            self.btnSetRadioButtonText.Cursor = crArrow
            self.btnSetRadioButtonText.Align = "alTop"
            self.btnSetRadioButtonText.Caption = 'Set Text'
            self.btnSetRadioButtonText.TabOrder = 1
            # Create control: btnSetRadioButtonFont = Button(self)
            self.btnSetRadioButtonFont = Button(self)
            self.btnSetRadioButtonFont.Name = "btnSetRadioButtonFont"
            self.btnSetRadioButtonFont.Parent = self.grpRadioButton
            self.btnSetRadioButtonFont.Left = 2
            self.btnSetRadioButtonFont.Top = 67
            self.btnSetRadioButtonFont.Width = 260
            self.btnSetRadioButtonFont.Height = 25
            self.btnSetRadioButtonFont.Cursor = crArrow
            self.btnSetRadioButtonFont.Align = "alTop"
            self.btnSetRadioButtonFont.Caption = 'Set Font'
            self.btnSetRadioButtonFont.TabOrder = 2
            # Create control: btnToggleRadioButtonEnabled = Button(self)
            self.btnToggleRadioButtonEnabled = Button(self)
            self.btnToggleRadioButtonEnabled.Name = "btnToggleRadioButtonEnabled"
            self.btnToggleRadioButtonEnabled.Parent = self.grpRadioButton
            self.btnToggleRadioButtonEnabled.Left = 2
            self.btnToggleRadioButtonEnabled.Top = 92
            self.btnToggleRadioButtonEnabled.Width = 260
            self.btnToggleRadioButtonEnabled.Height = 25
            self.btnToggleRadioButtonEnabled.Cursor = crArrow
            self.btnToggleRadioButtonEnabled.Align = "alTop"
            self.btnToggleRadioButtonEnabled.Caption = 'Toggle Enabled'
            self.btnToggleRadioButtonEnabled.TabOrder = 3
            # Create control: btnToggleRadioButtonVisible = Button(self)
            self.btnToggleRadioButtonVisible = Button(self)
            self.btnToggleRadioButtonVisible.Name = "btnToggleRadioButtonVisible"
            self.btnToggleRadioButtonVisible.Parent = self.grpRadioButton
            self.btnToggleRadioButtonVisible.Left = 2
            self.btnToggleRadioButtonVisible.Top = 117
            self.btnToggleRadioButtonVisible.Width = 260
            self.btnToggleRadioButtonVisible.Height = 25
            self.btnToggleRadioButtonVisible.Cursor = crArrow
            self.btnToggleRadioButtonVisible.Align = "alTop"
            self.btnToggleRadioButtonVisible.Caption = 'Toggle Visible'
            self.btnToggleRadioButtonVisible.TabOrder = 4
            # Create control: btnSetRadioButtonAlign = Button(self)
            self.btnSetRadioButtonAlign = Button(self)
            self.btnSetRadioButtonAlign.Name = "btnSetRadioButtonAlign"
            self.btnSetRadioButtonAlign.Parent = self.grpRadioButton
            self.btnSetRadioButtonAlign.Left = 2
            self.btnSetRadioButtonAlign.Top = 142
            self.btnSetRadioButtonAlign.Width = 260
            self.btnSetRadioButtonAlign.Height = 25
            self.btnSetRadioButtonAlign.Cursor = crArrow
            self.btnSetRadioButtonAlign.Align = "alTop"
            self.btnSetRadioButtonAlign.Caption = 'Set Align'
            self.btnSetRadioButtonAlign.TabOrder = 5
            # Create control: btnSetRadioButtonMargins = Button(self)
            self.btnSetRadioButtonMargins = Button(self)
            self.btnSetRadioButtonMargins.Name = "btnSetRadioButtonMargins"
            self.btnSetRadioButtonMargins.Parent = self.grpRadioButton
            self.btnSetRadioButtonMargins.Left = 2
            self.btnSetRadioButtonMargins.Top = 167
            self.btnSetRadioButtonMargins.Width = 260
            self.btnSetRadioButtonMargins.Height = 25
            self.btnSetRadioButtonMargins.Cursor = crArrow
            self.btnSetRadioButtonMargins.Align = "alTop"
            self.btnSetRadioButtonMargins.Caption = 'Set Margins'
            self.btnSetRadioButtonMargins.TabOrder = 6
            # Create control: btnSetRadioButtonOnChangeEvent = Button(self)
            self.btnSetRadioButtonOnChangeEvent = Button(self)
            self.btnSetRadioButtonOnChangeEvent.Name = "btnSetRadioButtonOnChangeEvent"
            self.btnSetRadioButtonOnChangeEvent.Parent = self.grpRadioButton
            self.btnSetRadioButtonOnChangeEvent.Left = 2
            self.btnSetRadioButtonOnChangeEvent.Top = 192
            self.btnSetRadioButtonOnChangeEvent.Width = 260
            self.btnSetRadioButtonOnChangeEvent.Height = 25
            self.btnSetRadioButtonOnChangeEvent.Cursor = crArrow
            self.btnSetRadioButtonOnChangeEvent.Align = "alTop"
            self.btnSetRadioButtonOnChangeEvent.Caption = 'Set On Change Event'
            self.btnSetRadioButtonOnChangeEvent.TabOrder = 7
            # Create control: btnToggleRadioButtonCheckedState = Button(self)
            self.btnToggleRadioButtonCheckedState = Button(self)
            self.btnToggleRadioButtonCheckedState.Name = "btnToggleRadioButtonCheckedState"
            self.btnToggleRadioButtonCheckedState.Parent = self.grpRadioButton
            self.btnToggleRadioButtonCheckedState.Left = 2
            self.btnToggleRadioButtonCheckedState.Top = 217
            self.btnToggleRadioButtonCheckedState.Width = 260
            self.btnToggleRadioButtonCheckedState.Height = 25
            self.btnToggleRadioButtonCheckedState.Cursor = crArrow
            self.btnToggleRadioButtonCheckedState.Align = "alTop"
            self.btnToggleRadioButtonCheckedState.Caption = 'Toggle Checked State'
            self.btnToggleRadioButtonCheckedState.TabOrder = 8
            # Create control: rb1 = RadioButton(self)
            self.rb1 = RadioButton(self)
            self.rb1.Name = "rb1"
            self.rb1.Parent = self.shtRadioButton
            self.rb1.Left = 56
            self.rb1.Top = 48
            self.rb1.Width = 200
            self.rb1.Height = 17
            self.rb1.Cursor = crArrow
            self.rb1.Caption = 'Radio Button 1'
            self.rb1.TabOrder = 1
            # Create control: rb2 = RadioButton(self)
            self.rb2 = RadioButton(self)
            self.rb2.Name = "rb2"
            self.rb2.Parent = self.shtRadioButton
            self.rb2.Left = 56
            self.rb2.Top = 72
            self.rb2.Width = 200
            self.rb2.Height = 17
            self.rb2.Cursor = crArrow
            self.rb2.Caption = 'Radio Button 2'
            self.rb2.TabOrder = 2
            # Create control: shtMemo = TabSheet(self)
            self.shtMemo = TabSheet(self)
            self.shtMemo.Name = "shtMemo"
            self.shtMemo.PageControl = self.pgFeatures
            self.shtMemo.Cursor = crArrow
            self.shtMemo.Caption = 'Memo'
            # Create control: grpMemo = GroupBox(self)
            self.grpMemo = GroupBox(self)
            self.grpMemo.Name = "grpMemo"
            self.grpMemo.Parent = self.shtMemo
            self.grpMemo.Left = 1123
            self.grpMemo.Top = 0
            self.grpMemo.Width = 264
            self.grpMemo.Height = 308
            self.grpMemo.Cursor = crArrow
            self.grpMemo.Align = "alRight"
            self.grpMemo.Caption = 'Control Usages'
            self.grpMemo.TabOrder = 0
            # Create control: btnSetMemoBounds = Button(self)
            self.btnSetMemoBounds = Button(self)
            self.btnSetMemoBounds.Name = "btnSetMemoBounds"
            self.btnSetMemoBounds.Parent = self.grpMemo
            self.btnSetMemoBounds.Left = 2
            self.btnSetMemoBounds.Top = 42
            self.btnSetMemoBounds.Width = 260
            self.btnSetMemoBounds.Height = 25
            self.btnSetMemoBounds.Cursor = crArrow
            self.btnSetMemoBounds.Align = "alTop"
            self.btnSetMemoBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnSetMemoBounds.TabOrder = 0
            # Create control: btnSetMemoText = Button(self)
            self.btnSetMemoText = Button(self)
            self.btnSetMemoText.Name = "btnSetMemoText"
            self.btnSetMemoText.Parent = self.grpMemo
            self.btnSetMemoText.Left = 2
            self.btnSetMemoText.Top = 17
            self.btnSetMemoText.Width = 260
            self.btnSetMemoText.Height = 25
            self.btnSetMemoText.Cursor = crArrow
            self.btnSetMemoText.Align = "alTop"
            self.btnSetMemoText.Caption = 'Set Text'
            self.btnSetMemoText.TabOrder = 1
            # Create control: btnSetMemoFont = Button(self)
            self.btnSetMemoFont = Button(self)
            self.btnSetMemoFont.Name = "btnSetMemoFont"
            self.btnSetMemoFont.Parent = self.grpMemo
            self.btnSetMemoFont.Left = 2
            self.btnSetMemoFont.Top = 67
            self.btnSetMemoFont.Width = 260
            self.btnSetMemoFont.Height = 25
            self.btnSetMemoFont.Cursor = crArrow
            self.btnSetMemoFont.Align = "alTop"
            self.btnSetMemoFont.Caption = 'Set Font'
            self.btnSetMemoFont.TabOrder = 2
            # Create control: btnToggleMemoEnabled = Button(self)
            self.btnToggleMemoEnabled = Button(self)
            self.btnToggleMemoEnabled.Name = "btnToggleMemoEnabled"
            self.btnToggleMemoEnabled.Parent = self.grpMemo
            self.btnToggleMemoEnabled.Left = 2
            self.btnToggleMemoEnabled.Top = 92
            self.btnToggleMemoEnabled.Width = 260
            self.btnToggleMemoEnabled.Height = 25
            self.btnToggleMemoEnabled.Cursor = crArrow
            self.btnToggleMemoEnabled.Align = "alTop"
            self.btnToggleMemoEnabled.Caption = 'Toggle Enabled'
            self.btnToggleMemoEnabled.TabOrder = 3
            # Create control: btnToggleMemoVisible = Button(self)
            self.btnToggleMemoVisible = Button(self)
            self.btnToggleMemoVisible.Name = "btnToggleMemoVisible"
            self.btnToggleMemoVisible.Parent = self.grpMemo
            self.btnToggleMemoVisible.Left = 2
            self.btnToggleMemoVisible.Top = 117
            self.btnToggleMemoVisible.Width = 260
            self.btnToggleMemoVisible.Height = 25
            self.btnToggleMemoVisible.Cursor = crArrow
            self.btnToggleMemoVisible.Align = "alTop"
            self.btnToggleMemoVisible.Caption = 'Toggle Visible'
            self.btnToggleMemoVisible.TabOrder = 4
            # Create control: btnSetMemoAlign = Button(self)
            self.btnSetMemoAlign = Button(self)
            self.btnSetMemoAlign.Name = "btnSetMemoAlign"
            self.btnSetMemoAlign.Parent = self.grpMemo
            self.btnSetMemoAlign.Left = 2
            self.btnSetMemoAlign.Top = 142
            self.btnSetMemoAlign.Width = 260
            self.btnSetMemoAlign.Height = 25
            self.btnSetMemoAlign.Cursor = crArrow
            self.btnSetMemoAlign.Align = "alTop"
            self.btnSetMemoAlign.Caption = 'Set Align'
            self.btnSetMemoAlign.TabOrder = 5
            # Create control: btnSetMemoMargins = Button(self)
            self.btnSetMemoMargins = Button(self)
            self.btnSetMemoMargins.Name = "btnSetMemoMargins"
            self.btnSetMemoMargins.Parent = self.grpMemo
            self.btnSetMemoMargins.Left = 2
            self.btnSetMemoMargins.Top = 167
            self.btnSetMemoMargins.Width = 260
            self.btnSetMemoMargins.Height = 25
            self.btnSetMemoMargins.Cursor = crArrow
            self.btnSetMemoMargins.Align = "alTop"
            self.btnSetMemoMargins.Caption = 'Set Margins'
            self.btnSetMemoMargins.TabOrder = 6
            # Create control: btnSetMemoOnChangeEvent = Button(self)
            self.btnSetMemoOnChangeEvent = Button(self)
            self.btnSetMemoOnChangeEvent.Name = "btnSetMemoOnChangeEvent"
            self.btnSetMemoOnChangeEvent.Parent = self.grpMemo
            self.btnSetMemoOnChangeEvent.Left = 2
            self.btnSetMemoOnChangeEvent.Top = 192
            self.btnSetMemoOnChangeEvent.Width = 260
            self.btnSetMemoOnChangeEvent.Height = 25
            self.btnSetMemoOnChangeEvent.Cursor = crArrow
            self.btnSetMemoOnChangeEvent.Align = "alTop"
            self.btnSetMemoOnChangeEvent.Caption = 'Set On Change Event'
            self.btnSetMemoOnChangeEvent.TabOrder = 7
            # Create control: mmMemo = Memo(self)
            self.mmMemo = Memo(self)
            self.mmMemo.Name = "mmMemo"
            self.mmMemo.Parent = self.shtMemo
            self.mmMemo.Left = 48
            self.mmMemo.Top = 64
            self.mmMemo.Width = 304
            self.mmMemo.Height = 192
            self.mmMemo.Cursor = crArrow
            self.mmMemo.Lines.Assign(['Memo'])
            self.mmMemo.TabOrder = 1
            # Create control: shtComboBox = TabSheet(self)
            self.shtComboBox = TabSheet(self)
            self.shtComboBox.Name = "shtComboBox"
            self.shtComboBox.PageControl = self.pgFeatures
            self.shtComboBox.Cursor = crArrow
            self.shtComboBox.Caption = 'Combo Box'
            # Create control: grpComboBox = GroupBox(self)
            self.grpComboBox = GroupBox(self)
            self.grpComboBox.Name = "grpComboBox"
            self.grpComboBox.Parent = self.shtComboBox
            self.grpComboBox.Left = 1123
            self.grpComboBox.Top = 0
            self.grpComboBox.Width = 264
            self.grpComboBox.Height = 308
            self.grpComboBox.Cursor = crArrow
            self.grpComboBox.Align = "alRight"
            self.grpComboBox.Caption = 'Control Usages'
            self.grpComboBox.TabOrder = 0
            # Create control: btnComboSetBounds = Button(self)
            self.btnComboSetBounds = Button(self)
            self.btnComboSetBounds.Name = "btnComboSetBounds"
            self.btnComboSetBounds.Parent = self.grpComboBox
            self.btnComboSetBounds.Left = 2
            self.btnComboSetBounds.Top = 92
            self.btnComboSetBounds.Width = 260
            self.btnComboSetBounds.Height = 25
            self.btnComboSetBounds.Cursor = crArrow
            self.btnComboSetBounds.Align = "alTop"
            self.btnComboSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnComboSetBounds.TabOrder = 0
            # Create control: btnComboSetText = Button(self)
            self.btnComboSetText = Button(self)
            self.btnComboSetText.Name = "btnComboSetText"
            self.btnComboSetText.Parent = self.grpComboBox
            self.btnComboSetText.Left = 2
            self.btnComboSetText.Top = 17
            self.btnComboSetText.Width = 260
            self.btnComboSetText.Height = 25
            self.btnComboSetText.Cursor = crArrow
            self.btnComboSetText.Align = "alTop"
            self.btnComboSetText.Caption = 'Set Items'
            self.btnComboSetText.TabOrder = 1
            # Create control: btnComboSetFont = Button(self)
            self.btnComboSetFont = Button(self)
            self.btnComboSetFont.Name = "btnComboSetFont"
            self.btnComboSetFont.Parent = self.grpComboBox
            self.btnComboSetFont.Left = 2
            self.btnComboSetFont.Top = 117
            self.btnComboSetFont.Width = 260
            self.btnComboSetFont.Height = 25
            self.btnComboSetFont.Cursor = crArrow
            self.btnComboSetFont.Align = "alTop"
            self.btnComboSetFont.Caption = 'Set Font'
            self.btnComboSetFont.TabOrder = 2
            # Create control: btnComboToggleEnabled = Button(self)
            self.btnComboToggleEnabled = Button(self)
            self.btnComboToggleEnabled.Name = "btnComboToggleEnabled"
            self.btnComboToggleEnabled.Parent = self.grpComboBox
            self.btnComboToggleEnabled.Left = 2
            self.btnComboToggleEnabled.Top = 142
            self.btnComboToggleEnabled.Width = 260
            self.btnComboToggleEnabled.Height = 25
            self.btnComboToggleEnabled.Cursor = crArrow
            self.btnComboToggleEnabled.Align = "alTop"
            self.btnComboToggleEnabled.Caption = 'Toggle Enabled'
            self.btnComboToggleEnabled.TabOrder = 3
            # Create control: btnComboToggleVisible = Button(self)
            self.btnComboToggleVisible = Button(self)
            self.btnComboToggleVisible.Name = "btnComboToggleVisible"
            self.btnComboToggleVisible.Parent = self.grpComboBox
            self.btnComboToggleVisible.Left = 2
            self.btnComboToggleVisible.Top = 167
            self.btnComboToggleVisible.Width = 260
            self.btnComboToggleVisible.Height = 25
            self.btnComboToggleVisible.Cursor = crArrow
            self.btnComboToggleVisible.Align = "alTop"
            self.btnComboToggleVisible.Caption = 'Toggle Visible'
            self.btnComboToggleVisible.TabOrder = 4
            # Create control: btnComboSetAlign = Button(self)
            self.btnComboSetAlign = Button(self)
            self.btnComboSetAlign.Name = "btnComboSetAlign"
            self.btnComboSetAlign.Parent = self.grpComboBox
            self.btnComboSetAlign.Left = 2
            self.btnComboSetAlign.Top = 192
            self.btnComboSetAlign.Width = 260
            self.btnComboSetAlign.Height = 25
            self.btnComboSetAlign.Cursor = crArrow
            self.btnComboSetAlign.Align = "alTop"
            self.btnComboSetAlign.Caption = 'Set Align'
            self.btnComboSetAlign.TabOrder = 5
            # Create control: btnComboSetMargins = Button(self)
            self.btnComboSetMargins = Button(self)
            self.btnComboSetMargins.Name = "btnComboSetMargins"
            self.btnComboSetMargins.Parent = self.grpComboBox
            self.btnComboSetMargins.Left = 2
            self.btnComboSetMargins.Top = 217
            self.btnComboSetMargins.Width = 260
            self.btnComboSetMargins.Height = 25
            self.btnComboSetMargins.Cursor = crArrow
            self.btnComboSetMargins.Align = "alTop"
            self.btnComboSetMargins.Caption = 'Set Margins'
            self.btnComboSetMargins.TabOrder = 6
            # Create control: btnComboSetOnChangeEvent = Button(self)
            self.btnComboSetOnChangeEvent = Button(self)
            self.btnComboSetOnChangeEvent.Name = "btnComboSetOnChangeEvent"
            self.btnComboSetOnChangeEvent.Parent = self.grpComboBox
            self.btnComboSetOnChangeEvent.Left = 2
            self.btnComboSetOnChangeEvent.Top = 242
            self.btnComboSetOnChangeEvent.Width = 260
            self.btnComboSetOnChangeEvent.Height = 25
            self.btnComboSetOnChangeEvent.Cursor = crArrow
            self.btnComboSetOnChangeEvent.Align = "alTop"
            self.btnComboSetOnChangeEvent.Caption = 'Set On Change Event'
            self.btnComboSetOnChangeEvent.TabOrder = 7
            # Create control: btnComboSetItemIndex = Button(self)
            self.btnComboSetItemIndex = Button(self)
            self.btnComboSetItemIndex.Name = "btnComboSetItemIndex"
            self.btnComboSetItemIndex.Parent = self.grpComboBox
            self.btnComboSetItemIndex.Left = 2
            self.btnComboSetItemIndex.Top = 67
            self.btnComboSetItemIndex.Width = 260
            self.btnComboSetItemIndex.Height = 25
            self.btnComboSetItemIndex.Cursor = crArrow
            self.btnComboSetItemIndex.Align = "alTop"
            self.btnComboSetItemIndex.Caption = 'Set Item Index'
            self.btnComboSetItemIndex.TabOrder = 8
            # Create control: btnComboGetItemIndex = Button(self)
            self.btnComboGetItemIndex = Button(self)
            self.btnComboGetItemIndex.Name = "btnComboGetItemIndex"
            self.btnComboGetItemIndex.Parent = self.grpComboBox
            self.btnComboGetItemIndex.Left = 2
            self.btnComboGetItemIndex.Top = 42
            self.btnComboGetItemIndex.Width = 260
            self.btnComboGetItemIndex.Height = 25
            self.btnComboGetItemIndex.Cursor = crArrow
            self.btnComboGetItemIndex.Align = "alTop"
            self.btnComboGetItemIndex.Caption = 'Get Item Index'
            self.btnComboGetItemIndex.TabOrder = 9
            # Create control: cbCombo = ComboBox(self)
            self.cbCombo = ComboBox(self)
            self.cbCombo.Name = "cbCombo"
            self.cbCombo.Parent = self.shtComboBox
            self.cbCombo.Left = 128
            self.cbCombo.Top = 88
            self.cbCombo.Width = 145
            self.cbCombo.Height = 23
            self.cbCombo.Cursor = crArrow
            self.cbCombo.Style = "csDropDownList"
            self.cbCombo.ItemIndex = 0
            self.cbCombo.TabOrder = 1
            self.cbCombo.Text = 'sel 1'
            self.cbCombo.Items.Assign(['sel 1','sel 2','sel 3'])
            # Create control: shtListBox = TabSheet(self)
            self.shtListBox = TabSheet(self)
            self.shtListBox.Name = "shtListBox"
            self.shtListBox.PageControl = self.pgFeatures
            self.shtListBox.Cursor = crArrow
            self.shtListBox.Caption = 'List Box'
            # Create control: grpListBox = GroupBox(self)
            self.grpListBox = GroupBox(self)
            self.grpListBox.Name = "grpListBox"
            self.grpListBox.Parent = self.shtListBox
            self.grpListBox.Left = 1123
            self.grpListBox.Top = 0
            self.grpListBox.Width = 264
            self.grpListBox.Height = 308
            self.grpListBox.Cursor = crArrow
            self.grpListBox.Align = "alRight"
            self.grpListBox.Caption = 'Control Usages'
            self.grpListBox.TabOrder = 0
            # Create control: btnListBoxSetBounds = Button(self)
            self.btnListBoxSetBounds = Button(self)
            self.btnListBoxSetBounds.Name = "btnListBoxSetBounds"
            self.btnListBoxSetBounds.Parent = self.grpListBox
            self.btnListBoxSetBounds.Left = 2
            self.btnListBoxSetBounds.Top = 92
            self.btnListBoxSetBounds.Width = 260
            self.btnListBoxSetBounds.Height = 25
            self.btnListBoxSetBounds.Cursor = crArrow
            self.btnListBoxSetBounds.Align = "alTop"
            self.btnListBoxSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnListBoxSetBounds.TabOrder = 0
            # Create control: btnListBoxSetItems = Button(self)
            self.btnListBoxSetItems = Button(self)
            self.btnListBoxSetItems.Name = "btnListBoxSetItems"
            self.btnListBoxSetItems.Parent = self.grpListBox
            self.btnListBoxSetItems.Left = 2
            self.btnListBoxSetItems.Top = 17
            self.btnListBoxSetItems.Width = 260
            self.btnListBoxSetItems.Height = 25
            self.btnListBoxSetItems.Cursor = crArrow
            self.btnListBoxSetItems.Align = "alTop"
            self.btnListBoxSetItems.Caption = 'Set Items'
            self.btnListBoxSetItems.TabOrder = 1
            # Create control: btnListBoxSetFont = Button(self)
            self.btnListBoxSetFont = Button(self)
            self.btnListBoxSetFont.Name = "btnListBoxSetFont"
            self.btnListBoxSetFont.Parent = self.grpListBox
            self.btnListBoxSetFont.Left = 2
            self.btnListBoxSetFont.Top = 117
            self.btnListBoxSetFont.Width = 260
            self.btnListBoxSetFont.Height = 25
            self.btnListBoxSetFont.Cursor = crArrow
            self.btnListBoxSetFont.Align = "alTop"
            self.btnListBoxSetFont.Caption = 'Set Font'
            self.btnListBoxSetFont.TabOrder = 2
            # Create control: btnListBoxToggleEnabled = Button(self)
            self.btnListBoxToggleEnabled = Button(self)
            self.btnListBoxToggleEnabled.Name = "btnListBoxToggleEnabled"
            self.btnListBoxToggleEnabled.Parent = self.grpListBox
            self.btnListBoxToggleEnabled.Left = 2
            self.btnListBoxToggleEnabled.Top = 142
            self.btnListBoxToggleEnabled.Width = 260
            self.btnListBoxToggleEnabled.Height = 25
            self.btnListBoxToggleEnabled.Cursor = crArrow
            self.btnListBoxToggleEnabled.Align = "alTop"
            self.btnListBoxToggleEnabled.Caption = 'Toggle Enabled'
            self.btnListBoxToggleEnabled.TabOrder = 3
            # Create control: btnListBoxToggleVisible = Button(self)
            self.btnListBoxToggleVisible = Button(self)
            self.btnListBoxToggleVisible.Name = "btnListBoxToggleVisible"
            self.btnListBoxToggleVisible.Parent = self.grpListBox
            self.btnListBoxToggleVisible.Left = 2
            self.btnListBoxToggleVisible.Top = 167
            self.btnListBoxToggleVisible.Width = 260
            self.btnListBoxToggleVisible.Height = 25
            self.btnListBoxToggleVisible.Cursor = crArrow
            self.btnListBoxToggleVisible.Align = "alTop"
            self.btnListBoxToggleVisible.Caption = 'Toggle Visible'
            self.btnListBoxToggleVisible.TabOrder = 4
            # Create control: btnListBoxSetAlign = Button(self)
            self.btnListBoxSetAlign = Button(self)
            self.btnListBoxSetAlign.Name = "btnListBoxSetAlign"
            self.btnListBoxSetAlign.Parent = self.grpListBox
            self.btnListBoxSetAlign.Left = 2
            self.btnListBoxSetAlign.Top = 192
            self.btnListBoxSetAlign.Width = 260
            self.btnListBoxSetAlign.Height = 25
            self.btnListBoxSetAlign.Cursor = crArrow
            self.btnListBoxSetAlign.Align = "alTop"
            self.btnListBoxSetAlign.Caption = 'Set Align'
            self.btnListBoxSetAlign.TabOrder = 5
            # Create control: btnListBoxSetMargins = Button(self)
            self.btnListBoxSetMargins = Button(self)
            self.btnListBoxSetMargins.Name = "btnListBoxSetMargins"
            self.btnListBoxSetMargins.Parent = self.grpListBox
            self.btnListBoxSetMargins.Left = 2
            self.btnListBoxSetMargins.Top = 217
            self.btnListBoxSetMargins.Width = 260
            self.btnListBoxSetMargins.Height = 25
            self.btnListBoxSetMargins.Cursor = crArrow
            self.btnListBoxSetMargins.Align = "alTop"
            self.btnListBoxSetMargins.Caption = 'Set Margins'
            self.btnListBoxSetMargins.TabOrder = 6
            # Create control: btnListBoxSetOnChangeEvent = Button(self)
            self.btnListBoxSetOnChangeEvent = Button(self)
            self.btnListBoxSetOnChangeEvent.Name = "btnListBoxSetOnChangeEvent"
            self.btnListBoxSetOnChangeEvent.Parent = self.grpListBox
            self.btnListBoxSetOnChangeEvent.Left = 2
            self.btnListBoxSetOnChangeEvent.Top = 242
            self.btnListBoxSetOnChangeEvent.Width = 260
            self.btnListBoxSetOnChangeEvent.Height = 25
            self.btnListBoxSetOnChangeEvent.Cursor = crArrow
            self.btnListBoxSetOnChangeEvent.Align = "alTop"
            self.btnListBoxSetOnChangeEvent.Caption = 'Set On Change Event'
            self.btnListBoxSetOnChangeEvent.TabOrder = 7
            # Create control: btnListBoxSetItemIndex = Button(self)
            self.btnListBoxSetItemIndex = Button(self)
            self.btnListBoxSetItemIndex.Name = "btnListBoxSetItemIndex"
            self.btnListBoxSetItemIndex.Parent = self.grpListBox
            self.btnListBoxSetItemIndex.Left = 2
            self.btnListBoxSetItemIndex.Top = 67
            self.btnListBoxSetItemIndex.Width = 260
            self.btnListBoxSetItemIndex.Height = 25
            self.btnListBoxSetItemIndex.Cursor = crArrow
            self.btnListBoxSetItemIndex.Align = "alTop"
            self.btnListBoxSetItemIndex.Caption = 'Set Item Index'
            self.btnListBoxSetItemIndex.TabOrder = 8
            # Create control: btnListBoxGetItemIndex = Button(self)
            self.btnListBoxGetItemIndex = Button(self)
            self.btnListBoxGetItemIndex.Name = "btnListBoxGetItemIndex"
            self.btnListBoxGetItemIndex.Parent = self.grpListBox
            self.btnListBoxGetItemIndex.Left = 2
            self.btnListBoxGetItemIndex.Top = 42
            self.btnListBoxGetItemIndex.Width = 260
            self.btnListBoxGetItemIndex.Height = 25
            self.btnListBoxGetItemIndex.Cursor = crArrow
            self.btnListBoxGetItemIndex.Align = "alTop"
            self.btnListBoxGetItemIndex.Caption = 'Get Item Index'
            self.btnListBoxGetItemIndex.TabOrder = 9
            # Create control: lstListBox = ListBox(self)
            self.lstListBox = ListBox(self)
            self.lstListBox.Name = "lstListBox"
            self.lstListBox.Parent = self.shtListBox
            self.lstListBox.Left = 72
            self.lstListBox.Top = 64
            self.lstListBox.Width = 121
            self.lstListBox.Height = 97
            self.lstListBox.Cursor = crArrow
            self.lstListBox.ItemHeight = 15
            self.lstListBox.Items.Assign(['str 1','str 2','str 3'])
            self.lstListBox.TabOrder = 1
            # Create control: shtStaticText = TabSheet(self)
            self.shtStaticText = TabSheet(self)
            self.shtStaticText.Name = "shtStaticText"
            self.shtStaticText.PageControl = self.pgFeatures
            self.shtStaticText.Cursor = crArrow
            self.shtStaticText.Caption = 'Static Text'
            # Create control: stStaticText = StaticText(self)
            self.stStaticText = StaticText(self)
            self.stStaticText.Name = "stStaticText"
            self.stStaticText.Parent = self.shtStaticText
            self.stStaticText.Left = 88
            self.stStaticText.Top = 96
            self.stStaticText.Width = 64
            self.stStaticText.Height = 19
            self.stStaticText.Cursor = crArrow
            self.stStaticText.Caption = 'stStaticText'
            self.stStaticText.TabOrder = 0
            # Create control: grpStaticText = GroupBox(self)
            self.grpStaticText = GroupBox(self)
            self.grpStaticText.Name = "grpStaticText"
            self.grpStaticText.Parent = self.shtStaticText
            self.grpStaticText.Left = 1123
            self.grpStaticText.Top = 0
            self.grpStaticText.Width = 264
            self.grpStaticText.Height = 308
            self.grpStaticText.Cursor = crArrow
            self.grpStaticText.Align = "alRight"
            self.grpStaticText.Caption = 'Control Usages'
            self.grpStaticText.TabOrder = 1
            # Create control: btnStaticTextSetBounds = Button(self)
            self.btnStaticTextSetBounds = Button(self)
            self.btnStaticTextSetBounds.Name = "btnStaticTextSetBounds"
            self.btnStaticTextSetBounds.Parent = self.grpStaticText
            self.btnStaticTextSetBounds.Left = 2
            self.btnStaticTextSetBounds.Top = 117
            self.btnStaticTextSetBounds.Width = 260
            self.btnStaticTextSetBounds.Height = 25
            self.btnStaticTextSetBounds.Cursor = crArrow
            self.btnStaticTextSetBounds.Align = "alTop"
            self.btnStaticTextSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnStaticTextSetBounds.TabOrder = 0
            # Create control: btnStaticTextToggleTransparency = Button(self)
            self.btnStaticTextToggleTransparency = Button(self)
            self.btnStaticTextToggleTransparency.Name = "btnStaticTextToggleTransparency"
            self.btnStaticTextToggleTransparency.Parent = self.grpStaticText
            self.btnStaticTextToggleTransparency.Left = 2
            self.btnStaticTextToggleTransparency.Top = 67
            self.btnStaticTextToggleTransparency.Width = 260
            self.btnStaticTextToggleTransparency.Height = 25
            self.btnStaticTextToggleTransparency.Cursor = crArrow
            self.btnStaticTextToggleTransparency.Align = "alTop"
            self.btnStaticTextToggleTransparency.Caption = 'Toggle Transparency'
            self.btnStaticTextToggleTransparency.TabOrder = 1
            # Create control: btnStaticTextSetCaption = Button(self)
            self.btnStaticTextSetCaption = Button(self)
            self.btnStaticTextSetCaption.Name = "btnStaticTextSetCaption"
            self.btnStaticTextSetCaption.Parent = self.grpStaticText
            self.btnStaticTextSetCaption.Left = 2
            self.btnStaticTextSetCaption.Top = 92
            self.btnStaticTextSetCaption.Width = 260
            self.btnStaticTextSetCaption.Height = 25
            self.btnStaticTextSetCaption.Cursor = crArrow
            self.btnStaticTextSetCaption.Align = "alTop"
            self.btnStaticTextSetCaption.Caption = 'Set Caption'
            self.btnStaticTextSetCaption.TabOrder = 2
            # Create control: btnStaticTextSetBorderStyle = Button(self)
            self.btnStaticTextSetBorderStyle = Button(self)
            self.btnStaticTextSetBorderStyle.Name = "btnStaticTextSetBorderStyle"
            self.btnStaticTextSetBorderStyle.Parent = self.grpStaticText
            self.btnStaticTextSetBorderStyle.Left = 2
            self.btnStaticTextSetBorderStyle.Top = 42
            self.btnStaticTextSetBorderStyle.Width = 260
            self.btnStaticTextSetBorderStyle.Height = 25
            self.btnStaticTextSetBorderStyle.Cursor = crArrow
            self.btnStaticTextSetBorderStyle.Align = "alTop"
            self.btnStaticTextSetBorderStyle.Caption = 'Set Border Style'
            self.btnStaticTextSetBorderStyle.TabOrder = 3
            # Create control: btnStaticTextToggleAutoSize = Button(self)
            self.btnStaticTextToggleAutoSize = Button(self)
            self.btnStaticTextToggleAutoSize.Name = "btnStaticTextToggleAutoSize"
            self.btnStaticTextToggleAutoSize.Parent = self.grpStaticText
            self.btnStaticTextToggleAutoSize.Left = 2
            self.btnStaticTextToggleAutoSize.Top = 142
            self.btnStaticTextToggleAutoSize.Width = 260
            self.btnStaticTextToggleAutoSize.Height = 25
            self.btnStaticTextToggleAutoSize.Cursor = crArrow
            self.btnStaticTextToggleAutoSize.Align = "alTop"
            self.btnStaticTextToggleAutoSize.Caption = 'Toggle Auto Size'
            self.btnStaticTextToggleAutoSize.TabOrder = 4
            # Create control: btnStaticTextSetFont = Button(self)
            self.btnStaticTextSetFont = Button(self)
            self.btnStaticTextSetFont.Name = "btnStaticTextSetFont"
            self.btnStaticTextSetFont.Parent = self.grpStaticText
            self.btnStaticTextSetFont.Left = 2
            self.btnStaticTextSetFont.Top = 167
            self.btnStaticTextSetFont.Width = 260
            self.btnStaticTextSetFont.Height = 25
            self.btnStaticTextSetFont.Cursor = crArrow
            self.btnStaticTextSetFont.Align = "alTop"
            self.btnStaticTextSetFont.Caption = 'Set Font'
            self.btnStaticTextSetFont.TabOrder = 5
            # Create control: btnStaticTextToggleEnabled = Button(self)
            self.btnStaticTextToggleEnabled = Button(self)
            self.btnStaticTextToggleEnabled.Name = "btnStaticTextToggleEnabled"
            self.btnStaticTextToggleEnabled.Parent = self.grpStaticText
            self.btnStaticTextToggleEnabled.Left = 2
            self.btnStaticTextToggleEnabled.Top = 192
            self.btnStaticTextToggleEnabled.Width = 260
            self.btnStaticTextToggleEnabled.Height = 25
            self.btnStaticTextToggleEnabled.Cursor = crArrow
            self.btnStaticTextToggleEnabled.Align = "alTop"
            self.btnStaticTextToggleEnabled.Caption = 'Toggle Enabled'
            self.btnStaticTextToggleEnabled.TabOrder = 6
            # Create control: btnStaticTextToggleVisible = Button(self)
            self.btnStaticTextToggleVisible = Button(self)
            self.btnStaticTextToggleVisible.Name = "btnStaticTextToggleVisible"
            self.btnStaticTextToggleVisible.Parent = self.grpStaticText
            self.btnStaticTextToggleVisible.Left = 2
            self.btnStaticTextToggleVisible.Top = 217
            self.btnStaticTextToggleVisible.Width = 260
            self.btnStaticTextToggleVisible.Height = 25
            self.btnStaticTextToggleVisible.Cursor = crArrow
            self.btnStaticTextToggleVisible.Align = "alTop"
            self.btnStaticTextToggleVisible.Caption = 'Toggle Visible'
            self.btnStaticTextToggleVisible.TabOrder = 7
            # Create control: btnStaticTextSetAlign = Button(self)
            self.btnStaticTextSetAlign = Button(self)
            self.btnStaticTextSetAlign.Name = "btnStaticTextSetAlign"
            self.btnStaticTextSetAlign.Parent = self.grpStaticText
            self.btnStaticTextSetAlign.Left = 2
            self.btnStaticTextSetAlign.Top = 242
            self.btnStaticTextSetAlign.Width = 260
            self.btnStaticTextSetAlign.Height = 25
            self.btnStaticTextSetAlign.Cursor = crArrow
            self.btnStaticTextSetAlign.Align = "alTop"
            self.btnStaticTextSetAlign.Caption = 'Set Align'
            self.btnStaticTextSetAlign.TabOrder = 8
            # Create control: btnStaticTextSetAlignment = Button(self)
            self.btnStaticTextSetAlignment = Button(self)
            self.btnStaticTextSetAlignment.Name = "btnStaticTextSetAlignment"
            self.btnStaticTextSetAlignment.Parent = self.grpStaticText
            self.btnStaticTextSetAlignment.Left = 2
            self.btnStaticTextSetAlignment.Top = 267
            self.btnStaticTextSetAlignment.Width = 260
            self.btnStaticTextSetAlignment.Height = 25
            self.btnStaticTextSetAlignment.Cursor = crArrow
            self.btnStaticTextSetAlignment.Align = "alTop"
            self.btnStaticTextSetAlignment.Caption = 'Set Text Alignment'
            self.btnStaticTextSetAlignment.TabOrder = 9
            # Create control: btnStaticTextSetMargins = Button(self)
            self.btnStaticTextSetMargins = Button(self)
            self.btnStaticTextSetMargins.Name = "btnStaticTextSetMargins"
            self.btnStaticTextSetMargins.Parent = self.grpStaticText
            self.btnStaticTextSetMargins.Left = 2
            self.btnStaticTextSetMargins.Top = 292
            self.btnStaticTextSetMargins.Width = 260
            self.btnStaticTextSetMargins.Height = 25
            self.btnStaticTextSetMargins.Cursor = crArrow
            self.btnStaticTextSetMargins.Align = "alTop"
            self.btnStaticTextSetMargins.Caption = 'Set Margins'
            self.btnStaticTextSetMargins.TabOrder = 10
            # Create control: btnStaticTextSetClickEvent = Button(self)
            self.btnStaticTextSetClickEvent = Button(self)
            self.btnStaticTextSetClickEvent.Name = "btnStaticTextSetClickEvent"
            self.btnStaticTextSetClickEvent.Parent = self.grpStaticText
            self.btnStaticTextSetClickEvent.Left = 2
            self.btnStaticTextSetClickEvent.Top = 317
            self.btnStaticTextSetClickEvent.Width = 260
            self.btnStaticTextSetClickEvent.Height = 25
            self.btnStaticTextSetClickEvent.Cursor = crArrow
            self.btnStaticTextSetClickEvent.Align = "alTop"
            self.btnStaticTextSetClickEvent.Caption = 'Set On Click Event'
            self.btnStaticTextSetClickEvent.TabOrder = 11
            # Create control: btnStaticTextSetBkgdColor = Button(self)
            self.btnStaticTextSetBkgdColor = Button(self)
            self.btnStaticTextSetBkgdColor.Name = "btnStaticTextSetBkgdColor"
            self.btnStaticTextSetBkgdColor.Parent = self.grpStaticText
            self.btnStaticTextSetBkgdColor.Left = 2
            self.btnStaticTextSetBkgdColor.Top = 17
            self.btnStaticTextSetBkgdColor.Width = 260
            self.btnStaticTextSetBkgdColor.Height = 25
            self.btnStaticTextSetBkgdColor.Cursor = crArrow
            self.btnStaticTextSetBkgdColor.Align = "alTop"
            self.btnStaticTextSetBkgdColor.Caption = 'Set Background Color'
            self.btnStaticTextSetBkgdColor.TabOrder = 12
            # Create control: shtGroupBox = TabSheet(self)
            self.shtGroupBox = TabSheet(self)
            self.shtGroupBox.Name = "shtGroupBox"
            self.shtGroupBox.PageControl = self.pgFeatures
            self.shtGroupBox.Cursor = crArrow
            self.shtGroupBox.Caption = 'Group Box'
            # Create control: grpGroupBox2 = GroupBox(self)
            self.grpGroupBox2 = GroupBox(self)
            self.grpGroupBox2.Name = "grpGroupBox2"
            self.grpGroupBox2.Parent = self.shtGroupBox
            self.grpGroupBox2.Left = 1123
            self.grpGroupBox2.Top = 0
            self.grpGroupBox2.Width = 264
            self.grpGroupBox2.Height = 308
            self.grpGroupBox2.Cursor = crArrow
            self.grpGroupBox2.Align = "alRight"
            self.grpGroupBox2.Caption = 'Control Usages'
            self.grpGroupBox2.TabOrder = 0
            # Create control: btnGroupBoxSetBounds = Button(self)
            self.btnGroupBoxSetBounds = Button(self)
            self.btnGroupBoxSetBounds.Name = "btnGroupBoxSetBounds"
            self.btnGroupBoxSetBounds.Parent = self.grpGroupBox2
            self.btnGroupBoxSetBounds.Left = 2
            self.btnGroupBoxSetBounds.Top = 42
            self.btnGroupBoxSetBounds.Width = 260
            self.btnGroupBoxSetBounds.Height = 25
            self.btnGroupBoxSetBounds.Cursor = crArrow
            self.btnGroupBoxSetBounds.Align = "alTop"
            self.btnGroupBoxSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnGroupBoxSetBounds.TabOrder = 0
            # Create control: btnGroupBoxSetCaption = Button(self)
            self.btnGroupBoxSetCaption = Button(self)
            self.btnGroupBoxSetCaption.Name = "btnGroupBoxSetCaption"
            self.btnGroupBoxSetCaption.Parent = self.grpGroupBox2
            self.btnGroupBoxSetCaption.Left = 2
            self.btnGroupBoxSetCaption.Top = 17
            self.btnGroupBoxSetCaption.Width = 260
            self.btnGroupBoxSetCaption.Height = 25
            self.btnGroupBoxSetCaption.Cursor = crArrow
            self.btnGroupBoxSetCaption.Align = "alTop"
            self.btnGroupBoxSetCaption.Caption = 'Set Caption'
            self.btnGroupBoxSetCaption.TabOrder = 1
            # Create control: btnGroupBoxSetFont = Button(self)
            self.btnGroupBoxSetFont = Button(self)
            self.btnGroupBoxSetFont.Name = "btnGroupBoxSetFont"
            self.btnGroupBoxSetFont.Parent = self.grpGroupBox2
            self.btnGroupBoxSetFont.Left = 2
            self.btnGroupBoxSetFont.Top = 67
            self.btnGroupBoxSetFont.Width = 260
            self.btnGroupBoxSetFont.Height = 25
            self.btnGroupBoxSetFont.Cursor = crArrow
            self.btnGroupBoxSetFont.Align = "alTop"
            self.btnGroupBoxSetFont.Caption = 'Set Font'
            self.btnGroupBoxSetFont.TabOrder = 2
            # Create control: btnGroupBoxToggleEnabled = Button(self)
            self.btnGroupBoxToggleEnabled = Button(self)
            self.btnGroupBoxToggleEnabled.Name = "btnGroupBoxToggleEnabled"
            self.btnGroupBoxToggleEnabled.Parent = self.grpGroupBox2
            self.btnGroupBoxToggleEnabled.Left = 2
            self.btnGroupBoxToggleEnabled.Top = 92
            self.btnGroupBoxToggleEnabled.Width = 260
            self.btnGroupBoxToggleEnabled.Height = 25
            self.btnGroupBoxToggleEnabled.Cursor = crArrow
            self.btnGroupBoxToggleEnabled.Align = "alTop"
            self.btnGroupBoxToggleEnabled.Caption = 'Toggle Enabled'
            self.btnGroupBoxToggleEnabled.TabOrder = 3
            # Create control: btnGroupBoxToggleVisible = Button(self)
            self.btnGroupBoxToggleVisible = Button(self)
            self.btnGroupBoxToggleVisible.Name = "btnGroupBoxToggleVisible"
            self.btnGroupBoxToggleVisible.Parent = self.grpGroupBox2
            self.btnGroupBoxToggleVisible.Left = 2
            self.btnGroupBoxToggleVisible.Top = 117
            self.btnGroupBoxToggleVisible.Width = 260
            self.btnGroupBoxToggleVisible.Height = 25
            self.btnGroupBoxToggleVisible.Cursor = crArrow
            self.btnGroupBoxToggleVisible.Align = "alTop"
            self.btnGroupBoxToggleVisible.Caption = 'Toggle Visible'
            self.btnGroupBoxToggleVisible.TabOrder = 4
            # Create control: btnGroupBoxSetAlign = Button(self)
            self.btnGroupBoxSetAlign = Button(self)
            self.btnGroupBoxSetAlign.Name = "btnGroupBoxSetAlign"
            self.btnGroupBoxSetAlign.Parent = self.grpGroupBox2
            self.btnGroupBoxSetAlign.Left = 2
            self.btnGroupBoxSetAlign.Top = 167
            self.btnGroupBoxSetAlign.Width = 260
            self.btnGroupBoxSetAlign.Height = 25
            self.btnGroupBoxSetAlign.Cursor = crArrow
            self.btnGroupBoxSetAlign.Align = "alTop"
            self.btnGroupBoxSetAlign.Caption = 'Set Align'
            self.btnGroupBoxSetAlign.TabOrder = 5
            # Create control: btnGroupBoxSetMargins = Button(self)
            self.btnGroupBoxSetMargins = Button(self)
            self.btnGroupBoxSetMargins.Name = "btnGroupBoxSetMargins"
            self.btnGroupBoxSetMargins.Parent = self.grpGroupBox2
            self.btnGroupBoxSetMargins.Left = 2
            self.btnGroupBoxSetMargins.Top = 192
            self.btnGroupBoxSetMargins.Width = 260
            self.btnGroupBoxSetMargins.Height = 25
            self.btnGroupBoxSetMargins.Cursor = crArrow
            self.btnGroupBoxSetMargins.Align = "alTop"
            self.btnGroupBoxSetMargins.Caption = 'Set Margins'
            self.btnGroupBoxSetMargins.TabOrder = 6
            # Create control: btnGroupBoxToggleFrame = Button(self)
            self.btnGroupBoxToggleFrame = Button(self)
            self.btnGroupBoxToggleFrame.Name = "btnGroupBoxToggleFrame"
            self.btnGroupBoxToggleFrame.Parent = self.grpGroupBox2
            self.btnGroupBoxToggleFrame.Left = 2
            self.btnGroupBoxToggleFrame.Top = 142
            self.btnGroupBoxToggleFrame.Width = 260
            self.btnGroupBoxToggleFrame.Height = 25
            self.btnGroupBoxToggleFrame.Cursor = crArrow
            self.btnGroupBoxToggleFrame.Align = "alTop"
            self.btnGroupBoxToggleFrame.Caption = 'Toggle Show Frame'
            self.btnGroupBoxToggleFrame.TabOrder = 7
            # Create control: grpGroupBox = GroupBox(self)
            self.grpGroupBox = GroupBox(self)
            self.grpGroupBox.Name = "grpGroupBox"
            self.grpGroupBox.Parent = self.shtGroupBox
            self.grpGroupBox.Left = 64
            self.grpGroupBox.Top = 48
            self.grpGroupBox.Width = 192
            self.grpGroupBox.Height = 120
            self.grpGroupBox.Cursor = crArrow
            self.grpGroupBox.Caption = 'Group Box as a container'
            self.grpGroupBox.TabOrder = 1
            # Create control: shtPanel = TabSheet(self)
            self.shtPanel = TabSheet(self)
            self.shtPanel.Name = "shtPanel"
            self.shtPanel.PageControl = self.pgFeatures
            self.shtPanel.Cursor = crArrow
            self.shtPanel.Caption = 'Panel'
            # Create control: pnlPanel = Panel(self)
            self.pnlPanel = Panel(self)
            self.pnlPanel.Name = "pnlPanel"
            self.pnlPanel.Parent = self.shtPanel
            self.pnlPanel.Left = 72
            self.pnlPanel.Top = 48
            self.pnlPanel.Width = 272
            self.pnlPanel.Height = 176
            self.pnlPanel.Cursor = crArrow
            self.pnlPanel.Caption = 'Panel as a container'
            self.pnlPanel.TabOrder = 0
            # Create control: grpPanel = GroupBox(self)
            self.grpPanel = GroupBox(self)
            self.grpPanel.Name = "grpPanel"
            self.grpPanel.Parent = self.shtPanel
            self.grpPanel.Left = 1123
            self.grpPanel.Top = 0
            self.grpPanel.Width = 264
            self.grpPanel.Height = 308
            self.grpPanel.Cursor = crArrow
            self.grpPanel.Align = "alRight"
            self.grpPanel.Caption = 'Control Usages'
            self.grpPanel.TabOrder = 1
            # Create control: btnPanelSetBounds = Button(self)
            self.btnPanelSetBounds = Button(self)
            self.btnPanelSetBounds.Name = "btnPanelSetBounds"
            self.btnPanelSetBounds.Parent = self.grpPanel
            self.btnPanelSetBounds.Left = 2
            self.btnPanelSetBounds.Top = 42
            self.btnPanelSetBounds.Width = 260
            self.btnPanelSetBounds.Height = 25
            self.btnPanelSetBounds.Cursor = crArrow
            self.btnPanelSetBounds.Align = "alTop"
            self.btnPanelSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnPanelSetBounds.TabOrder = 0
            # Create control: btnPanelSetCaption = Button(self)
            self.btnPanelSetCaption = Button(self)
            self.btnPanelSetCaption.Name = "btnPanelSetCaption"
            self.btnPanelSetCaption.Parent = self.grpPanel
            self.btnPanelSetCaption.Left = 2
            self.btnPanelSetCaption.Top = 17
            self.btnPanelSetCaption.Width = 260
            self.btnPanelSetCaption.Height = 25
            self.btnPanelSetCaption.Cursor = crArrow
            self.btnPanelSetCaption.Align = "alTop"
            self.btnPanelSetCaption.Caption = 'Set Caption'
            self.btnPanelSetCaption.TabOrder = 1
            # Create control: btnPanelSetFont = Button(self)
            self.btnPanelSetFont = Button(self)
            self.btnPanelSetFont.Name = "btnPanelSetFont"
            self.btnPanelSetFont.Parent = self.grpPanel
            self.btnPanelSetFont.Left = 2
            self.btnPanelSetFont.Top = 67
            self.btnPanelSetFont.Width = 260
            self.btnPanelSetFont.Height = 25
            self.btnPanelSetFont.Cursor = crArrow
            self.btnPanelSetFont.Align = "alTop"
            self.btnPanelSetFont.Caption = 'Set Font'
            self.btnPanelSetFont.TabOrder = 2
            # Create control: btnPanelToggleEnabled = Button(self)
            self.btnPanelToggleEnabled = Button(self)
            self.btnPanelToggleEnabled.Name = "btnPanelToggleEnabled"
            self.btnPanelToggleEnabled.Parent = self.grpPanel
            self.btnPanelToggleEnabled.Left = 2
            self.btnPanelToggleEnabled.Top = 142
            self.btnPanelToggleEnabled.Width = 260
            self.btnPanelToggleEnabled.Height = 25
            self.btnPanelToggleEnabled.Cursor = crArrow
            self.btnPanelToggleEnabled.Align = "alTop"
            self.btnPanelToggleEnabled.Caption = 'Toggle Enabled'
            self.btnPanelToggleEnabled.TabOrder = 3
            # Create control: btnPanelToggleVisible = Button(self)
            self.btnPanelToggleVisible = Button(self)
            self.btnPanelToggleVisible.Name = "btnPanelToggleVisible"
            self.btnPanelToggleVisible.Parent = self.grpPanel
            self.btnPanelToggleVisible.Left = 2
            self.btnPanelToggleVisible.Top = 167
            self.btnPanelToggleVisible.Width = 260
            self.btnPanelToggleVisible.Height = 25
            self.btnPanelToggleVisible.Cursor = crArrow
            self.btnPanelToggleVisible.Align = "alTop"
            self.btnPanelToggleVisible.Caption = 'Toggle Visible'
            self.btnPanelToggleVisible.TabOrder = 4
            # Create control: btnPanelSetAlign = Button(self)
            self.btnPanelSetAlign = Button(self)
            self.btnPanelSetAlign.Name = "btnPanelSetAlign"
            self.btnPanelSetAlign.Parent = self.grpPanel
            self.btnPanelSetAlign.Left = 2
            self.btnPanelSetAlign.Top = 192
            self.btnPanelSetAlign.Width = 260
            self.btnPanelSetAlign.Height = 25
            self.btnPanelSetAlign.Cursor = crArrow
            self.btnPanelSetAlign.Align = "alTop"
            self.btnPanelSetAlign.Caption = 'Set Align'
            self.btnPanelSetAlign.TabOrder = 5
            # Create control: btnPanelSetMargins = Button(self)
            self.btnPanelSetMargins = Button(self)
            self.btnPanelSetMargins.Name = "btnPanelSetMargins"
            self.btnPanelSetMargins.Parent = self.grpPanel
            self.btnPanelSetMargins.Left = 2
            self.btnPanelSetMargins.Top = 217
            self.btnPanelSetMargins.Width = 260
            self.btnPanelSetMargins.Height = 25
            self.btnPanelSetMargins.Cursor = crArrow
            self.btnPanelSetMargins.Align = "alTop"
            self.btnPanelSetMargins.Caption = 'Set Margins'
            self.btnPanelSetMargins.TabOrder = 6
            # Create control: btnPanelSetBevel = Button(self)
            self.btnPanelSetBevel = Button(self)
            self.btnPanelSetBevel.Name = "btnPanelSetBevel"
            self.btnPanelSetBevel.Parent = self.grpPanel
            self.btnPanelSetBevel.Left = 2
            self.btnPanelSetBevel.Top = 117
            self.btnPanelSetBevel.Width = 260
            self.btnPanelSetBevel.Height = 25
            self.btnPanelSetBevel.Cursor = crArrow
            self.btnPanelSetBevel.Align = "alTop"
            self.btnPanelSetBevel.Caption = 'Set Bevel'
            self.btnPanelSetBevel.TabOrder = 7
            # Create control: btnPanelSetBorderStyle = Button(self)
            self.btnPanelSetBorderStyle = Button(self)
            self.btnPanelSetBorderStyle.Name = "btnPanelSetBorderStyle"
            self.btnPanelSetBorderStyle.Parent = self.grpPanel
            self.btnPanelSetBorderStyle.Left = 2
            self.btnPanelSetBorderStyle.Top = 92
            self.btnPanelSetBorderStyle.Width = 260
            self.btnPanelSetBorderStyle.Height = 25
            self.btnPanelSetBorderStyle.Cursor = crArrow
            self.btnPanelSetBorderStyle.Align = "alTop"
            self.btnPanelSetBorderStyle.Caption = 'Set Border Style'
            self.btnPanelSetBorderStyle.TabOrder = 8
            # Create control: shtRadioGroup = TabSheet(self)
            self.shtRadioGroup = TabSheet(self)
            self.shtRadioGroup.Name = "shtRadioGroup"
            self.shtRadioGroup.PageControl = self.pgFeatures
            self.shtRadioGroup.Cursor = crArrow
            self.shtRadioGroup.Caption = 'Radio Group'
            # Create control: grpRadioGroup = GroupBox(self)
            self.grpRadioGroup = GroupBox(self)
            self.grpRadioGroup.Name = "grpRadioGroup"
            self.grpRadioGroup.Parent = self.shtRadioGroup
            self.grpRadioGroup.Left = 1123
            self.grpRadioGroup.Top = 0
            self.grpRadioGroup.Width = 264
            self.grpRadioGroup.Height = 308
            self.grpRadioGroup.Cursor = crArrow
            self.grpRadioGroup.Align = "alRight"
            self.grpRadioGroup.Caption = 'Control Usages'
            self.grpRadioGroup.TabOrder = 0
            # Create control: btnRadioGroupSetBounds = Button(self)
            self.btnRadioGroupSetBounds = Button(self)
            self.btnRadioGroupSetBounds.Name = "btnRadioGroupSetBounds"
            self.btnRadioGroupSetBounds.Parent = self.grpRadioGroup
            self.btnRadioGroupSetBounds.Left = 2
            self.btnRadioGroupSetBounds.Top = 92
            self.btnRadioGroupSetBounds.Width = 260
            self.btnRadioGroupSetBounds.Height = 25
            self.btnRadioGroupSetBounds.Cursor = crArrow
            self.btnRadioGroupSetBounds.Align = "alTop"
            self.btnRadioGroupSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnRadioGroupSetBounds.TabOrder = 0
            # Create control: btnRadioGroupSetCaption = Button(self)
            self.btnRadioGroupSetCaption = Button(self)
            self.btnRadioGroupSetCaption.Name = "btnRadioGroupSetCaption"
            self.btnRadioGroupSetCaption.Parent = self.grpRadioGroup
            self.btnRadioGroupSetCaption.Left = 2
            self.btnRadioGroupSetCaption.Top = 17
            self.btnRadioGroupSetCaption.Width = 260
            self.btnRadioGroupSetCaption.Height = 25
            self.btnRadioGroupSetCaption.Cursor = crArrow
            self.btnRadioGroupSetCaption.Align = "alTop"
            self.btnRadioGroupSetCaption.Caption = 'Set Caption'
            self.btnRadioGroupSetCaption.TabOrder = 1
            # Create control: btnRadioGroupSetFont = Button(self)
            self.btnRadioGroupSetFont = Button(self)
            self.btnRadioGroupSetFont.Name = "btnRadioGroupSetFont"
            self.btnRadioGroupSetFont.Parent = self.grpRadioGroup
            self.btnRadioGroupSetFont.Left = 2
            self.btnRadioGroupSetFont.Top = 117
            self.btnRadioGroupSetFont.Width = 260
            self.btnRadioGroupSetFont.Height = 25
            self.btnRadioGroupSetFont.Cursor = crArrow
            self.btnRadioGroupSetFont.Align = "alTop"
            self.btnRadioGroupSetFont.Caption = 'Set Font'
            self.btnRadioGroupSetFont.TabOrder = 2
            # Create control: btnRadioGroupToggleEnabled = Button(self)
            self.btnRadioGroupToggleEnabled = Button(self)
            self.btnRadioGroupToggleEnabled.Name = "btnRadioGroupToggleEnabled"
            self.btnRadioGroupToggleEnabled.Parent = self.grpRadioGroup
            self.btnRadioGroupToggleEnabled.Left = 2
            self.btnRadioGroupToggleEnabled.Top = 142
            self.btnRadioGroupToggleEnabled.Width = 260
            self.btnRadioGroupToggleEnabled.Height = 25
            self.btnRadioGroupToggleEnabled.Cursor = crArrow
            self.btnRadioGroupToggleEnabled.Align = "alTop"
            self.btnRadioGroupToggleEnabled.Caption = 'Toggle Enabled'
            self.btnRadioGroupToggleEnabled.TabOrder = 3
            # Create control: btnRadioGroupToggleVisible = Button(self)
            self.btnRadioGroupToggleVisible = Button(self)
            self.btnRadioGroupToggleVisible.Name = "btnRadioGroupToggleVisible"
            self.btnRadioGroupToggleVisible.Parent = self.grpRadioGroup
            self.btnRadioGroupToggleVisible.Left = 2
            self.btnRadioGroupToggleVisible.Top = 167
            self.btnRadioGroupToggleVisible.Width = 260
            self.btnRadioGroupToggleVisible.Height = 25
            self.btnRadioGroupToggleVisible.Cursor = crArrow
            self.btnRadioGroupToggleVisible.Align = "alTop"
            self.btnRadioGroupToggleVisible.Caption = 'Toggle Visible'
            self.btnRadioGroupToggleVisible.TabOrder = 4
            # Create control: btnRadioGroupSetAlign = Button(self)
            self.btnRadioGroupSetAlign = Button(self)
            self.btnRadioGroupSetAlign.Name = "btnRadioGroupSetAlign"
            self.btnRadioGroupSetAlign.Parent = self.grpRadioGroup
            self.btnRadioGroupSetAlign.Left = 2
            self.btnRadioGroupSetAlign.Top = 192
            self.btnRadioGroupSetAlign.Width = 260
            self.btnRadioGroupSetAlign.Height = 25
            self.btnRadioGroupSetAlign.Cursor = crArrow
            self.btnRadioGroupSetAlign.Align = "alTop"
            self.btnRadioGroupSetAlign.Caption = 'Set Align'
            self.btnRadioGroupSetAlign.TabOrder = 5
            # Create control: btnRadioGroupSetMargins = Button(self)
            self.btnRadioGroupSetMargins = Button(self)
            self.btnRadioGroupSetMargins.Name = "btnRadioGroupSetMargins"
            self.btnRadioGroupSetMargins.Parent = self.grpRadioGroup
            self.btnRadioGroupSetMargins.Left = 2
            self.btnRadioGroupSetMargins.Top = 217
            self.btnRadioGroupSetMargins.Width = 260
            self.btnRadioGroupSetMargins.Height = 25
            self.btnRadioGroupSetMargins.Cursor = crArrow
            self.btnRadioGroupSetMargins.Align = "alTop"
            self.btnRadioGroupSetMargins.Caption = 'Set Margins'
            self.btnRadioGroupSetMargins.TabOrder = 6
            # Create control: btnRadioGroupSetItems = Button(self)
            self.btnRadioGroupSetItems = Button(self)
            self.btnRadioGroupSetItems.Name = "btnRadioGroupSetItems"
            self.btnRadioGroupSetItems.Parent = self.grpRadioGroup
            self.btnRadioGroupSetItems.Left = 2
            self.btnRadioGroupSetItems.Top = 42
            self.btnRadioGroupSetItems.Width = 260
            self.btnRadioGroupSetItems.Height = 25
            self.btnRadioGroupSetItems.Cursor = crArrow
            self.btnRadioGroupSetItems.Align = "alTop"
            self.btnRadioGroupSetItems.Caption = 'Set Items'
            self.btnRadioGroupSetItems.TabOrder = 7
            # Create control: btnRadioGroupSetItemIndex = Button(self)
            self.btnRadioGroupSetItemIndex = Button(self)
            self.btnRadioGroupSetItemIndex.Name = "btnRadioGroupSetItemIndex"
            self.btnRadioGroupSetItemIndex.Parent = self.grpRadioGroup
            self.btnRadioGroupSetItemIndex.Left = 2
            self.btnRadioGroupSetItemIndex.Top = 67
            self.btnRadioGroupSetItemIndex.Width = 260
            self.btnRadioGroupSetItemIndex.Height = 25
            self.btnRadioGroupSetItemIndex.Cursor = crArrow
            self.btnRadioGroupSetItemIndex.Align = "alTop"
            self.btnRadioGroupSetItemIndex.Caption = 'Set Item Index'
            self.btnRadioGroupSetItemIndex.TabOrder = 8
            # Create control: btnSetRadioGroupOnClick = Button(self)
            self.btnSetRadioGroupOnClick = Button(self)
            self.btnSetRadioGroupOnClick.Name = "btnSetRadioGroupOnClick"
            self.btnSetRadioGroupOnClick.Parent = self.grpRadioGroup
            self.btnSetRadioGroupOnClick.Left = 2
            self.btnSetRadioGroupOnClick.Top = 242
            self.btnSetRadioGroupOnClick.Width = 260
            self.btnSetRadioGroupOnClick.Height = 25
            self.btnSetRadioGroupOnClick.Cursor = crArrow
            self.btnSetRadioGroupOnClick.Align = "alTop"
            self.btnSetRadioGroupOnClick.Caption = 'Set On Click Event'
            self.btnSetRadioGroupOnClick.TabOrder = 9
            # Create control: rgRadioGroup = RadioGroup(self)
            self.rgRadioGroup = RadioGroup(self)
            self.rgRadioGroup.Name = "rgRadioGroup"
            self.rgRadioGroup.Parent = self.shtRadioGroup
            self.rgRadioGroup.Left = 56
            self.rgRadioGroup.Top = 56
            self.rgRadioGroup.Width = 312
            self.rgRadioGroup.Height = 184
            self.rgRadioGroup.Cursor = crArrow
            self.rgRadioGroup.Caption = 'Radio Group contains radio buttons'
            self.rgRadioGroup.ItemIndex = 0
            self.rgRadioGroup.Items.Assign(['radio button 1','radio button 2'])
            self.rgRadioGroup.TabOrder = 1
            # Create control: shtShape = TabSheet(self)
            self.shtShape = TabSheet(self)
            self.shtShape.Name = "shtShape"
            self.shtShape.PageControl = self.pgFeatures
            self.shtShape.Cursor = crArrow
            self.shtShape.Caption = 'Shape'
            # Create control: spShape = Shape(self)
            self.spShape = Shape(self)
            self.spShape.Name = "spShape"
            self.spShape.Parent = self.shtShape
            self.spShape.Left = 120
            self.spShape.Top = 88
            self.spShape.Width = 65
            self.spShape.Height = 65
            self.spShape.Cursor = crArrow
            # Create control: grpShape = GroupBox(self)
            self.grpShape = GroupBox(self)
            self.grpShape.Name = "grpShape"
            self.grpShape.Parent = self.shtShape
            self.grpShape.Left = 1123
            self.grpShape.Top = 0
            self.grpShape.Width = 264
            self.grpShape.Height = 308
            self.grpShape.Cursor = crArrow
            self.grpShape.Align = "alRight"
            self.grpShape.Caption = 'Control Usages'
            self.grpShape.TabOrder = 0
            # Create control: btnShapeSetBounds = Button(self)
            self.btnShapeSetBounds = Button(self)
            self.btnShapeSetBounds.Name = "btnShapeSetBounds"
            self.btnShapeSetBounds.Parent = self.grpShape
            self.btnShapeSetBounds.Left = 2
            self.btnShapeSetBounds.Top = 42
            self.btnShapeSetBounds.Width = 260
            self.btnShapeSetBounds.Height = 25
            self.btnShapeSetBounds.Cursor = crArrow
            self.btnShapeSetBounds.Align = "alTop"
            self.btnShapeSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnShapeSetBounds.TabOrder = 0
            # Create control: btnShapeToggleEnabled = Button(self)
            self.btnShapeToggleEnabled = Button(self)
            self.btnShapeToggleEnabled.Name = "btnShapeToggleEnabled"
            self.btnShapeToggleEnabled.Parent = self.grpShape
            self.btnShapeToggleEnabled.Left = 2
            self.btnShapeToggleEnabled.Top = 67
            self.btnShapeToggleEnabled.Width = 260
            self.btnShapeToggleEnabled.Height = 25
            self.btnShapeToggleEnabled.Cursor = crArrow
            self.btnShapeToggleEnabled.Align = "alTop"
            self.btnShapeToggleEnabled.Caption = 'Toggle Enabled'
            self.btnShapeToggleEnabled.TabOrder = 1
            # Create control: btnShapeToggleVisible = Button(self)
            self.btnShapeToggleVisible = Button(self)
            self.btnShapeToggleVisible.Name = "btnShapeToggleVisible"
            self.btnShapeToggleVisible.Parent = self.grpShape
            self.btnShapeToggleVisible.Left = 2
            self.btnShapeToggleVisible.Top = 92
            self.btnShapeToggleVisible.Width = 260
            self.btnShapeToggleVisible.Height = 25
            self.btnShapeToggleVisible.Cursor = crArrow
            self.btnShapeToggleVisible.Align = "alTop"
            self.btnShapeToggleVisible.Caption = 'Toggle Visible'
            self.btnShapeToggleVisible.TabOrder = 2
            # Create control: btnShapeSetAlign = Button(self)
            self.btnShapeSetAlign = Button(self)
            self.btnShapeSetAlign.Name = "btnShapeSetAlign"
            self.btnShapeSetAlign.Parent = self.grpShape
            self.btnShapeSetAlign.Left = 2
            self.btnShapeSetAlign.Top = 117
            self.btnShapeSetAlign.Width = 260
            self.btnShapeSetAlign.Height = 25
            self.btnShapeSetAlign.Cursor = crArrow
            self.btnShapeSetAlign.Align = "alTop"
            self.btnShapeSetAlign.Caption = 'Set Align'
            self.btnShapeSetAlign.TabOrder = 3
            # Create control: btnShapeSetMargins = Button(self)
            self.btnShapeSetMargins = Button(self)
            self.btnShapeSetMargins.Name = "btnShapeSetMargins"
            self.btnShapeSetMargins.Parent = self.grpShape
            self.btnShapeSetMargins.Left = 2
            self.btnShapeSetMargins.Top = 142
            self.btnShapeSetMargins.Width = 260
            self.btnShapeSetMargins.Height = 25
            self.btnShapeSetMargins.Cursor = crArrow
            self.btnShapeSetMargins.Align = "alTop"
            self.btnShapeSetMargins.Caption = 'Set Margins'
            self.btnShapeSetMargins.TabOrder = 4
            # Create control: btnShapeSetShape = Button(self)
            self.btnShapeSetShape = Button(self)
            self.btnShapeSetShape.Name = "btnShapeSetShape"
            self.btnShapeSetShape.Parent = self.grpShape
            self.btnShapeSetShape.Left = 2
            self.btnShapeSetShape.Top = 17
            self.btnShapeSetShape.Width = 260
            self.btnShapeSetShape.Height = 25
            self.btnShapeSetShape.Cursor = crArrow
            self.btnShapeSetShape.Align = "alTop"
            self.btnShapeSetShape.Caption = 'Set Shape'
            self.btnShapeSetShape.TabOrder = 5
            # Create control: shtScrollBar = TabSheet(self)
            self.shtScrollBar = TabSheet(self)
            self.shtScrollBar.Name = "shtScrollBar"
            self.shtScrollBar.PageControl = self.pgFeatures
            self.shtScrollBar.Cursor = crArrow
            self.shtScrollBar.Caption = 'Scroll Bar'
            # Create control: grpScrollBar = GroupBox(self)
            self.grpScrollBar = GroupBox(self)
            self.grpScrollBar.Name = "grpScrollBar"
            self.grpScrollBar.Parent = self.shtScrollBar
            self.grpScrollBar.Left = 1123
            self.grpScrollBar.Top = 0
            self.grpScrollBar.Width = 264
            self.grpScrollBar.Height = 308
            self.grpScrollBar.Cursor = crArrow
            self.grpScrollBar.Align = "alRight"
            self.grpScrollBar.Caption = 'Control Usages'
            self.grpScrollBar.TabOrder = 0
            # Create control: btnScrollBarSetBounds = Button(self)
            self.btnScrollBarSetBounds = Button(self)
            self.btnScrollBarSetBounds.Name = "btnScrollBarSetBounds"
            self.btnScrollBarSetBounds.Parent = self.grpScrollBar
            self.btnScrollBarSetBounds.Left = 2
            self.btnScrollBarSetBounds.Top = 117
            self.btnScrollBarSetBounds.Width = 260
            self.btnScrollBarSetBounds.Height = 25
            self.btnScrollBarSetBounds.Cursor = crArrow
            self.btnScrollBarSetBounds.Align = "alTop"
            self.btnScrollBarSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnScrollBarSetBounds.TabOrder = 0
            # Create control: btnScrollBarToggleEnabled = Button(self)
            self.btnScrollBarToggleEnabled = Button(self)
            self.btnScrollBarToggleEnabled.Name = "btnScrollBarToggleEnabled"
            self.btnScrollBarToggleEnabled.Parent = self.grpScrollBar
            self.btnScrollBarToggleEnabled.Left = 2
            self.btnScrollBarToggleEnabled.Top = 142
            self.btnScrollBarToggleEnabled.Width = 260
            self.btnScrollBarToggleEnabled.Height = 25
            self.btnScrollBarToggleEnabled.Cursor = crArrow
            self.btnScrollBarToggleEnabled.Align = "alTop"
            self.btnScrollBarToggleEnabled.Caption = 'Toggle Enabled'
            self.btnScrollBarToggleEnabled.TabOrder = 1
            # Create control: btnScrollBarToggleVisible = Button(self)
            self.btnScrollBarToggleVisible = Button(self)
            self.btnScrollBarToggleVisible.Name = "btnScrollBarToggleVisible"
            self.btnScrollBarToggleVisible.Parent = self.grpScrollBar
            self.btnScrollBarToggleVisible.Left = 2
            self.btnScrollBarToggleVisible.Top = 167
            self.btnScrollBarToggleVisible.Width = 260
            self.btnScrollBarToggleVisible.Height = 25
            self.btnScrollBarToggleVisible.Cursor = crArrow
            self.btnScrollBarToggleVisible.Align = "alTop"
            self.btnScrollBarToggleVisible.Caption = 'Toggle Visible'
            self.btnScrollBarToggleVisible.TabOrder = 2
            # Create control: btnScrollBarSetAlign = Button(self)
            self.btnScrollBarSetAlign = Button(self)
            self.btnScrollBarSetAlign.Name = "btnScrollBarSetAlign"
            self.btnScrollBarSetAlign.Parent = self.grpScrollBar
            self.btnScrollBarSetAlign.Left = 2
            self.btnScrollBarSetAlign.Top = 192
            self.btnScrollBarSetAlign.Width = 260
            self.btnScrollBarSetAlign.Height = 25
            self.btnScrollBarSetAlign.Cursor = crArrow
            self.btnScrollBarSetAlign.Align = "alTop"
            self.btnScrollBarSetAlign.Caption = 'Set Align'
            self.btnScrollBarSetAlign.TabOrder = 3
            # Create control: btnScrollBarSetMargins = Button(self)
            self.btnScrollBarSetMargins = Button(self)
            self.btnScrollBarSetMargins.Name = "btnScrollBarSetMargins"
            self.btnScrollBarSetMargins.Parent = self.grpScrollBar
            self.btnScrollBarSetMargins.Left = 2
            self.btnScrollBarSetMargins.Top = 217
            self.btnScrollBarSetMargins.Width = 260
            self.btnScrollBarSetMargins.Height = 25
            self.btnScrollBarSetMargins.Cursor = crArrow
            self.btnScrollBarSetMargins.Align = "alTop"
            self.btnScrollBarSetMargins.Caption = 'Set Margins'
            self.btnScrollBarSetMargins.TabOrder = 4
            # Create control: btnScrollBarSetMinMax = Button(self)
            self.btnScrollBarSetMinMax = Button(self)
            self.btnScrollBarSetMinMax.Name = "btnScrollBarSetMinMax"
            self.btnScrollBarSetMinMax.Parent = self.grpScrollBar
            self.btnScrollBarSetMinMax.Left = 2
            self.btnScrollBarSetMinMax.Top = 42
            self.btnScrollBarSetMinMax.Width = 260
            self.btnScrollBarSetMinMax.Height = 25
            self.btnScrollBarSetMinMax.Cursor = crArrow
            self.btnScrollBarSetMinMax.Align = "alTop"
            self.btnScrollBarSetMinMax.Caption = 'Set Min Max'
            self.btnScrollBarSetMinMax.TabOrder = 5
            # Create control: btnScrollBarSetChange = Button(self)
            self.btnScrollBarSetChange = Button(self)
            self.btnScrollBarSetChange.Name = "btnScrollBarSetChange"
            self.btnScrollBarSetChange.Parent = self.grpScrollBar
            self.btnScrollBarSetChange.Left = 2
            self.btnScrollBarSetChange.Top = 67
            self.btnScrollBarSetChange.Width = 260
            self.btnScrollBarSetChange.Height = 25
            self.btnScrollBarSetChange.Cursor = crArrow
            self.btnScrollBarSetChange.Align = "alTop"
            self.btnScrollBarSetChange.Caption = 'Set Small and Large Change'
            self.btnScrollBarSetChange.TabOrder = 6
            # Create control: btnScrollBarSetPosition = Button(self)
            self.btnScrollBarSetPosition = Button(self)
            self.btnScrollBarSetPosition.Name = "btnScrollBarSetPosition"
            self.btnScrollBarSetPosition.Parent = self.grpScrollBar
            self.btnScrollBarSetPosition.Left = 2
            self.btnScrollBarSetPosition.Top = 92
            self.btnScrollBarSetPosition.Width = 260
            self.btnScrollBarSetPosition.Height = 25
            self.btnScrollBarSetPosition.Cursor = crArrow
            self.btnScrollBarSetPosition.Align = "alTop"
            self.btnScrollBarSetPosition.Caption = 'Set Position'
            self.btnScrollBarSetPosition.TabOrder = 7
            # Create control: btnScrollBarSetOnChangeEvent = Button(self)
            self.btnScrollBarSetOnChangeEvent = Button(self)
            self.btnScrollBarSetOnChangeEvent.Name = "btnScrollBarSetOnChangeEvent"
            self.btnScrollBarSetOnChangeEvent.Parent = self.grpScrollBar
            self.btnScrollBarSetOnChangeEvent.Left = 2
            self.btnScrollBarSetOnChangeEvent.Top = 242
            self.btnScrollBarSetOnChangeEvent.Width = 260
            self.btnScrollBarSetOnChangeEvent.Height = 25
            self.btnScrollBarSetOnChangeEvent.Cursor = crArrow
            self.btnScrollBarSetOnChangeEvent.Align = "alTop"
            self.btnScrollBarSetOnChangeEvent.Caption = 'Set On Change Event'
            self.btnScrollBarSetOnChangeEvent.TabOrder = 8
            # Create control: btnScrollBarSetDirection = Button(self)
            self.btnScrollBarSetDirection = Button(self)
            self.btnScrollBarSetDirection.Name = "btnScrollBarSetDirection"
            self.btnScrollBarSetDirection.Parent = self.grpScrollBar
            self.btnScrollBarSetDirection.Left = 2
            self.btnScrollBarSetDirection.Top = 17
            self.btnScrollBarSetDirection.Width = 260
            self.btnScrollBarSetDirection.Height = 25
            self.btnScrollBarSetDirection.Cursor = crArrow
            self.btnScrollBarSetDirection.Align = "alTop"
            self.btnScrollBarSetDirection.Caption = 'Set Direction'
            self.btnScrollBarSetDirection.TabOrder = 9
            # Create control: sbScrollBar = ScrollBar(self)
            self.sbScrollBar = ScrollBar(self)
            self.sbScrollBar.Name = "sbScrollBar"
            self.sbScrollBar.Parent = self.shtScrollBar
            self.sbScrollBar.Left = 48
            self.sbScrollBar.Top = 56
            self.sbScrollBar.Width = 192
            self.sbScrollBar.Height = 24
            self.sbScrollBar.Cursor = crArrow
            self.sbScrollBar.PageSize = 0
            self.sbScrollBar.TabOrder = 1
            # Create control: shtDateTimePicker = TabSheet(self)
            self.shtDateTimePicker = TabSheet(self)
            self.shtDateTimePicker.Name = "shtDateTimePicker"
            self.shtDateTimePicker.PageControl = self.pgFeatures
            self.shtDateTimePicker.Cursor = crArrow
            self.shtDateTimePicker.Caption = 'Date Time Picker'
            # Create control: grpDateTimePicker = GroupBox(self)
            self.grpDateTimePicker = GroupBox(self)
            self.grpDateTimePicker.Name = "grpDateTimePicker"
            self.grpDateTimePicker.Parent = self.shtDateTimePicker
            self.grpDateTimePicker.Left = 1123
            self.grpDateTimePicker.Top = 0
            self.grpDateTimePicker.Width = 264
            self.grpDateTimePicker.Height = 308
            self.grpDateTimePicker.Cursor = crArrow
            self.grpDateTimePicker.Align = "alRight"
            self.grpDateTimePicker.Caption = 'Control Usages'
            self.grpDateTimePicker.TabOrder = 0
            # Create control: btnDateTimePickerSetBounds = Button(self)
            self.btnDateTimePickerSetBounds = Button(self)
            self.btnDateTimePickerSetBounds.Name = "btnDateTimePickerSetBounds"
            self.btnDateTimePickerSetBounds.Parent = self.grpDateTimePicker
            self.btnDateTimePickerSetBounds.Left = 2
            self.btnDateTimePickerSetBounds.Top = 117
            self.btnDateTimePickerSetBounds.Width = 260
            self.btnDateTimePickerSetBounds.Height = 25
            self.btnDateTimePickerSetBounds.Cursor = crArrow
            self.btnDateTimePickerSetBounds.Align = "alTop"
            self.btnDateTimePickerSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnDateTimePickerSetBounds.TabOrder = 0
            # Create control: btnDateTimePickerToggleEnabled = Button(self)
            self.btnDateTimePickerToggleEnabled = Button(self)
            self.btnDateTimePickerToggleEnabled.Name = "btnDateTimePickerToggleEnabled"
            self.btnDateTimePickerToggleEnabled.Parent = self.grpDateTimePicker
            self.btnDateTimePickerToggleEnabled.Left = 2
            self.btnDateTimePickerToggleEnabled.Top = 142
            self.btnDateTimePickerToggleEnabled.Width = 260
            self.btnDateTimePickerToggleEnabled.Height = 25
            self.btnDateTimePickerToggleEnabled.Cursor = crArrow
            self.btnDateTimePickerToggleEnabled.Align = "alTop"
            self.btnDateTimePickerToggleEnabled.Caption = 'Toggle Enabled'
            self.btnDateTimePickerToggleEnabled.TabOrder = 1
            # Create control: btnDateTimePickerToggleVisible = Button(self)
            self.btnDateTimePickerToggleVisible = Button(self)
            self.btnDateTimePickerToggleVisible.Name = "btnDateTimePickerToggleVisible"
            self.btnDateTimePickerToggleVisible.Parent = self.grpDateTimePicker
            self.btnDateTimePickerToggleVisible.Left = 2
            self.btnDateTimePickerToggleVisible.Top = 167
            self.btnDateTimePickerToggleVisible.Width = 260
            self.btnDateTimePickerToggleVisible.Height = 25
            self.btnDateTimePickerToggleVisible.Cursor = crArrow
            self.btnDateTimePickerToggleVisible.Align = "alTop"
            self.btnDateTimePickerToggleVisible.Caption = 'Toggle Visible'
            self.btnDateTimePickerToggleVisible.TabOrder = 2
            # Create control: btnDateTimePickerSetAlign = Button(self)
            self.btnDateTimePickerSetAlign = Button(self)
            self.btnDateTimePickerSetAlign.Name = "btnDateTimePickerSetAlign"
            self.btnDateTimePickerSetAlign.Parent = self.grpDateTimePicker
            self.btnDateTimePickerSetAlign.Left = 2
            self.btnDateTimePickerSetAlign.Top = 192
            self.btnDateTimePickerSetAlign.Width = 260
            self.btnDateTimePickerSetAlign.Height = 25
            self.btnDateTimePickerSetAlign.Cursor = crArrow
            self.btnDateTimePickerSetAlign.Align = "alTop"
            self.btnDateTimePickerSetAlign.Caption = 'Set Align'
            self.btnDateTimePickerSetAlign.TabOrder = 3
            # Create control: btnDateTimePickerSetMargins = Button(self)
            self.btnDateTimePickerSetMargins = Button(self)
            self.btnDateTimePickerSetMargins.Name = "btnDateTimePickerSetMargins"
            self.btnDateTimePickerSetMargins.Parent = self.grpDateTimePicker
            self.btnDateTimePickerSetMargins.Left = 2
            self.btnDateTimePickerSetMargins.Top = 217
            self.btnDateTimePickerSetMargins.Width = 260
            self.btnDateTimePickerSetMargins.Height = 25
            self.btnDateTimePickerSetMargins.Cursor = crArrow
            self.btnDateTimePickerSetMargins.Align = "alTop"
            self.btnDateTimePickerSetMargins.Caption = 'Set Margins'
            self.btnDateTimePickerSetMargins.TabOrder = 4
            # Create control: btnDateTimePickerSetDate = Button(self)
            self.btnDateTimePickerSetDate = Button(self)
            self.btnDateTimePickerSetDate.Name = "btnDateTimePickerSetDate"
            self.btnDateTimePickerSetDate.Parent = self.grpDateTimePicker
            self.btnDateTimePickerSetDate.Left = 2
            self.btnDateTimePickerSetDate.Top = 67
            self.btnDateTimePickerSetDate.Width = 260
            self.btnDateTimePickerSetDate.Height = 25
            self.btnDateTimePickerSetDate.Cursor = crArrow
            self.btnDateTimePickerSetDate.Align = "alTop"
            self.btnDateTimePickerSetDate.Caption = 'Set Date'
            self.btnDateTimePickerSetDate.TabOrder = 5
            # Create control: btnDateTimePickerSetDateFormat = Button(self)
            self.btnDateTimePickerSetDateFormat = Button(self)
            self.btnDateTimePickerSetDateFormat.Name = "btnDateTimePickerSetDateFormat"
            self.btnDateTimePickerSetDateFormat.Parent = self.grpDateTimePicker
            self.btnDateTimePickerSetDateFormat.Left = 2
            self.btnDateTimePickerSetDateFormat.Top = 17
            self.btnDateTimePickerSetDateFormat.Width = 260
            self.btnDateTimePickerSetDateFormat.Height = 25
            self.btnDateTimePickerSetDateFormat.Cursor = crArrow
            self.btnDateTimePickerSetDateFormat.Align = "alTop"
            self.btnDateTimePickerSetDateFormat.Caption = 'Set Date Format'
            self.btnDateTimePickerSetDateFormat.TabOrder = 6
            # Create control: btnDateTimePickerSetKind = Button(self)
            self.btnDateTimePickerSetKind = Button(self)
            self.btnDateTimePickerSetKind.Name = "btnDateTimePickerSetKind"
            self.btnDateTimePickerSetKind.Parent = self.grpDateTimePicker
            self.btnDateTimePickerSetKind.Left = 2
            self.btnDateTimePickerSetKind.Top = 42
            self.btnDateTimePickerSetKind.Width = 260
            self.btnDateTimePickerSetKind.Height = 25
            self.btnDateTimePickerSetKind.Cursor = crArrow
            self.btnDateTimePickerSetKind.Align = "alTop"
            self.btnDateTimePickerSetKind.Caption = 'Set Kind'
            self.btnDateTimePickerSetKind.TabOrder = 7
            # Create control: btnDateTimePickerSetTime = Button(self)
            self.btnDateTimePickerSetTime = Button(self)
            self.btnDateTimePickerSetTime.Name = "btnDateTimePickerSetTime"
            self.btnDateTimePickerSetTime.Parent = self.grpDateTimePicker
            self.btnDateTimePickerSetTime.Left = 2
            self.btnDateTimePickerSetTime.Top = 92
            self.btnDateTimePickerSetTime.Width = 260
            self.btnDateTimePickerSetTime.Height = 25
            self.btnDateTimePickerSetTime.Cursor = crArrow
            self.btnDateTimePickerSetTime.Align = "alTop"
            self.btnDateTimePickerSetTime.Caption = 'Set Time'
            self.btnDateTimePickerSetTime.TabOrder = 8
            # Create control: dtpDateTimePicker = DateTimePicker(self)
            self.dtpDateTimePicker = DateTimePicker(self)
            self.dtpDateTimePicker.Name = "dtpDateTimePicker"
            self.dtpDateTimePicker.Parent = self.shtDateTimePicker
            self.dtpDateTimePicker.Left = 48
            self.dtpDateTimePicker.Top = 56
            self.dtpDateTimePicker.Width = 186
            self.dtpDateTimePicker.Height = 23
            self.dtpDateTimePicker.Cursor = crArrow
            self.dtpDateTimePicker.Date = 44992.00000000000000000
            self.dtpDateTimePicker.Time = 0.71205076389014720
            self.dtpDateTimePicker.TabOrder = 1
            # Create control: shtPageControl = TabSheet(self)
            self.shtPageControl = TabSheet(self)
            self.shtPageControl.Name = "shtPageControl"
            self.shtPageControl.PageControl = self.pgFeatures
            self.shtPageControl.Cursor = crArrow
            self.shtPageControl.Margins.Left = 4
            self.shtPageControl.Margins.Top = 4
            self.shtPageControl.Margins.Right = 4
            self.shtPageControl.Margins.Bottom = 4
            self.shtPageControl.Caption = 'Page Control'
            # Create control: pcPageControl = PageControl(self)
            self.pcPageControl = PageControl(self)
            self.pcPageControl.Name = "pcPageControl"
            self.pcPageControl.Parent = self.shtPageControl
            self.pcPageControl.Left = 136
            self.pcPageControl.Top = 64
            self.pcPageControl.Width = 289
            self.pcPageControl.Height = 193
            self.pcPageControl.Cursor = crArrow
            self.pcPageControl.Margins.Left = 4
            self.pcPageControl.Margins.Top = 4
            self.pcPageControl.Margins.Right = 4
            self.pcPageControl.Margins.Bottom = 4
            self.pcPageControl.Images = app.get_system_imagelist_16px()
            self.pcPageControl.TabOrder = 0
            # Create control: TabSheet41 = TabSheet(self)
            self.TabSheet41 = TabSheet(self)
            self.TabSheet41.Name = "TabSheet41"
            self.TabSheet41.PageControl = self.pcPageControl
            self.TabSheet41.Cursor = crArrow
            self.TabSheet41.Margins.Left = 4
            self.TabSheet41.Margins.Top = 4
            self.TabSheet41.Margins.Right = 4
            self.TabSheet41.Margins.Bottom = 4
            self.TabSheet41.Caption = 'Sheet 1'
            # Create control: TabSheet42 = TabSheet(self)
            self.TabSheet42 = TabSheet(self)
            self.TabSheet42.Name = "TabSheet42"
            self.TabSheet42.PageControl = self.pcPageControl
            self.TabSheet42.Cursor = crArrow
            self.TabSheet42.Margins.Left = 4
            self.TabSheet42.Margins.Top = 4
            self.TabSheet42.Margins.Right = 4
            self.TabSheet42.Margins.Bottom = 4
            self.TabSheet42.Caption = 'Sheet 2'
            # Create control: grpPageControl = GroupBox(self)
            self.grpPageControl = GroupBox(self)
            self.grpPageControl.Name = "grpPageControl"
            self.grpPageControl.Parent = self.shtPageControl
            self.grpPageControl.Left = 1123
            self.grpPageControl.Top = 0
            self.grpPageControl.Width = 264
            self.grpPageControl.Height = 308
            self.grpPageControl.Cursor = crArrow
            self.grpPageControl.Margins.Left = 4
            self.grpPageControl.Margins.Top = 4
            self.grpPageControl.Margins.Right = 4
            self.grpPageControl.Margins.Bottom = 4
            self.grpPageControl.Align = "alRight"
            self.grpPageControl.Caption = 'Control Usages'
            self.grpPageControl.TabOrder = 1
            # Create control: btnPageControlToggleEnabled = Button(self)
            self.btnPageControlToggleEnabled = Button(self)
            self.btnPageControlToggleEnabled.Name = "btnPageControlToggleEnabled"
            self.btnPageControlToggleEnabled.Parent = self.grpPageControl
            self.btnPageControlToggleEnabled.Left = 2
            self.btnPageControlToggleEnabled.Top = 117
            self.btnPageControlToggleEnabled.Width = 260
            self.btnPageControlToggleEnabled.Height = 25
            self.btnPageControlToggleEnabled.Cursor = crArrow
            self.btnPageControlToggleEnabled.Align = "alTop"
            self.btnPageControlToggleEnabled.Caption = 'Toggle Enabled'
            self.btnPageControlToggleEnabled.TabOrder = 0
            # Create control: btnPageControlToggleVisible = Button(self)
            self.btnPageControlToggleVisible = Button(self)
            self.btnPageControlToggleVisible.Name = "btnPageControlToggleVisible"
            self.btnPageControlToggleVisible.Parent = self.grpPageControl
            self.btnPageControlToggleVisible.Left = 2
            self.btnPageControlToggleVisible.Top = 142
            self.btnPageControlToggleVisible.Width = 260
            self.btnPageControlToggleVisible.Height = 25
            self.btnPageControlToggleVisible.Cursor = crArrow
            self.btnPageControlToggleVisible.Align = "alTop"
            self.btnPageControlToggleVisible.Caption = 'Toggle Visible'
            self.btnPageControlToggleVisible.TabOrder = 1
            # Create control: btnPageControlSetAlign = Button(self)
            self.btnPageControlSetAlign = Button(self)
            self.btnPageControlSetAlign.Name = "btnPageControlSetAlign"
            self.btnPageControlSetAlign.Parent = self.grpPageControl
            self.btnPageControlSetAlign.Left = 2
            self.btnPageControlSetAlign.Top = 167
            self.btnPageControlSetAlign.Width = 260
            self.btnPageControlSetAlign.Height = 25
            self.btnPageControlSetAlign.Cursor = crArrow
            self.btnPageControlSetAlign.Align = "alTop"
            self.btnPageControlSetAlign.Caption = 'Set Align'
            self.btnPageControlSetAlign.TabOrder = 2
            # Create control: btnPageControlSetMargins = Button(self)
            self.btnPageControlSetMargins = Button(self)
            self.btnPageControlSetMargins.Name = "btnPageControlSetMargins"
            self.btnPageControlSetMargins.Parent = self.grpPageControl
            self.btnPageControlSetMargins.Left = 2
            self.btnPageControlSetMargins.Top = 192
            self.btnPageControlSetMargins.Width = 260
            self.btnPageControlSetMargins.Height = 25
            self.btnPageControlSetMargins.Cursor = crArrow
            self.btnPageControlSetMargins.Align = "alTop"
            self.btnPageControlSetMargins.Caption = 'Set Margins'
            self.btnPageControlSetMargins.TabOrder = 3
            # Create control: btnPageControlSetTabPosition = Button(self)
            self.btnPageControlSetTabPosition = Button(self)
            self.btnPageControlSetTabPosition.Name = "btnPageControlSetTabPosition"
            self.btnPageControlSetTabPosition.Parent = self.grpPageControl
            self.btnPageControlSetTabPosition.Left = 2
            self.btnPageControlSetTabPosition.Top = 67
            self.btnPageControlSetTabPosition.Width = 260
            self.btnPageControlSetTabPosition.Height = 25
            self.btnPageControlSetTabPosition.Cursor = crArrow
            self.btnPageControlSetTabPosition.Align = "alTop"
            self.btnPageControlSetTabPosition.Caption = 'Set TabPosition'
            self.btnPageControlSetTabPosition.TabOrder = 4
            # Create control: btnPageControlSetOwnerDraw = Button(self)
            self.btnPageControlSetOwnerDraw = Button(self)
            self.btnPageControlSetOwnerDraw.Name = "btnPageControlSetOwnerDraw"
            self.btnPageControlSetOwnerDraw.Parent = self.grpPageControl
            self.btnPageControlSetOwnerDraw.Left = 2
            self.btnPageControlSetOwnerDraw.Top = 17
            self.btnPageControlSetOwnerDraw.Width = 260
            self.btnPageControlSetOwnerDraw.Height = 25
            self.btnPageControlSetOwnerDraw.Cursor = crArrow
            self.btnPageControlSetOwnerDraw.Align = "alTop"
            self.btnPageControlSetOwnerDraw.Caption = 'Set OwnerDraw'
            self.btnPageControlSetOwnerDraw.TabOrder = 5
            # Create control: btnPageControlSetStyle = Button(self)
            self.btnPageControlSetStyle = Button(self)
            self.btnPageControlSetStyle.Name = "btnPageControlSetStyle"
            self.btnPageControlSetStyle.Parent = self.grpPageControl
            self.btnPageControlSetStyle.Left = 2
            self.btnPageControlSetStyle.Top = 42
            self.btnPageControlSetStyle.Width = 260
            self.btnPageControlSetStyle.Height = 25
            self.btnPageControlSetStyle.Cursor = crArrow
            self.btnPageControlSetStyle.Align = "alTop"
            self.btnPageControlSetStyle.Caption = 'Set Style'
            self.btnPageControlSetStyle.TabOrder = 6
            # Create control: btnPageControlSetBounds = Button(self)
            self.btnPageControlSetBounds = Button(self)
            self.btnPageControlSetBounds.Name = "btnPageControlSetBounds"
            self.btnPageControlSetBounds.Parent = self.grpPageControl
            self.btnPageControlSetBounds.Left = 2
            self.btnPageControlSetBounds.Top = 92
            self.btnPageControlSetBounds.Width = 260
            self.btnPageControlSetBounds.Height = 25
            self.btnPageControlSetBounds.Cursor = crArrow
            self.btnPageControlSetBounds.Align = "alTop"
            self.btnPageControlSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnPageControlSetBounds.TabOrder = 7
            # Create control: shtTrackBar = TabSheet(self)
            self.shtTrackBar = TabSheet(self)
            self.shtTrackBar.Name = "shtTrackBar"
            self.shtTrackBar.PageControl = self.pgFeatures
            self.shtTrackBar.Cursor = crArrow
            self.shtTrackBar.Margins.Left = 4
            self.shtTrackBar.Margins.Top = 4
            self.shtTrackBar.Margins.Right = 4
            self.shtTrackBar.Margins.Bottom = 4
            self.shtTrackBar.Caption = 'Track Bar'
            # Create control: tbTrackBar = TrackBar(self)
            self.tbTrackBar = TrackBar(self)
            self.tbTrackBar.Name = "tbTrackBar"
            self.tbTrackBar.Parent = self.shtTrackBar
            self.tbTrackBar.Left = 136
            self.tbTrackBar.Top = 120
            self.tbTrackBar.Width = 150
            self.tbTrackBar.Height = 45
            self.tbTrackBar.Cursor = crArrow
            self.tbTrackBar.Margins.Left = 4
            self.tbTrackBar.Margins.Top = 4
            self.tbTrackBar.Margins.Right = 4
            self.tbTrackBar.Margins.Bottom = 4
            self.tbTrackBar.TabOrder = 0
            self.tbTrackBar.ThumbLength = 25
            # Create control: grpTrackBar = GroupBox(self)
            self.grpTrackBar = GroupBox(self)
            self.grpTrackBar.Name = "grpTrackBar"
            self.grpTrackBar.Parent = self.shtTrackBar
            self.grpTrackBar.Left = 1123
            self.grpTrackBar.Top = 0
            self.grpTrackBar.Width = 264
            self.grpTrackBar.Height = 308
            self.grpTrackBar.Cursor = crArrow
            self.grpTrackBar.Margins.Left = 4
            self.grpTrackBar.Margins.Top = 4
            self.grpTrackBar.Margins.Right = 4
            self.grpTrackBar.Margins.Bottom = 4
            self.grpTrackBar.Align = "alRight"
            self.grpTrackBar.Caption = 'Control Usages'
            self.grpTrackBar.TabOrder = 1
            # Create control: btnTrackBarSetBounds = Button(self)
            self.btnTrackBarSetBounds = Button(self)
            self.btnTrackBarSetBounds.Name = "btnTrackBarSetBounds"
            self.btnTrackBarSetBounds.Parent = self.grpTrackBar
            self.btnTrackBarSetBounds.Left = 2
            self.btnTrackBarSetBounds.Top = 142
            self.btnTrackBarSetBounds.Width = 260
            self.btnTrackBarSetBounds.Height = 25
            self.btnTrackBarSetBounds.Cursor = crArrow
            self.btnTrackBarSetBounds.Align = "alTop"
            self.btnTrackBarSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnTrackBarSetBounds.TabOrder = 0
            # Create control: btnTrackBarToggleEnabled = Button(self)
            self.btnTrackBarToggleEnabled = Button(self)
            self.btnTrackBarToggleEnabled.Name = "btnTrackBarToggleEnabled"
            self.btnTrackBarToggleEnabled.Parent = self.grpTrackBar
            self.btnTrackBarToggleEnabled.Left = 2
            self.btnTrackBarToggleEnabled.Top = 167
            self.btnTrackBarToggleEnabled.Width = 260
            self.btnTrackBarToggleEnabled.Height = 25
            self.btnTrackBarToggleEnabled.Cursor = crArrow
            self.btnTrackBarToggleEnabled.Align = "alTop"
            self.btnTrackBarToggleEnabled.Caption = 'Toggle Enabled'
            self.btnTrackBarToggleEnabled.TabOrder = 1
            # Create control: btnTrackBarToggleVisible = Button(self)
            self.btnTrackBarToggleVisible = Button(self)
            self.btnTrackBarToggleVisible.Name = "btnTrackBarToggleVisible"
            self.btnTrackBarToggleVisible.Parent = self.grpTrackBar
            self.btnTrackBarToggleVisible.Left = 2
            self.btnTrackBarToggleVisible.Top = 192
            self.btnTrackBarToggleVisible.Width = 260
            self.btnTrackBarToggleVisible.Height = 25
            self.btnTrackBarToggleVisible.Cursor = crArrow
            self.btnTrackBarToggleVisible.Align = "alTop"
            self.btnTrackBarToggleVisible.Caption = 'Toggle Visible'
            self.btnTrackBarToggleVisible.TabOrder = 2
            # Create control: btnTrackBarSetAlign = Button(self)
            self.btnTrackBarSetAlign = Button(self)
            self.btnTrackBarSetAlign.Name = "btnTrackBarSetAlign"
            self.btnTrackBarSetAlign.Parent = self.grpTrackBar
            self.btnTrackBarSetAlign.Left = 2
            self.btnTrackBarSetAlign.Top = 217
            self.btnTrackBarSetAlign.Width = 260
            self.btnTrackBarSetAlign.Height = 25
            self.btnTrackBarSetAlign.Cursor = crArrow
            self.btnTrackBarSetAlign.Align = "alTop"
            self.btnTrackBarSetAlign.Caption = 'Set Align'
            self.btnTrackBarSetAlign.TabOrder = 3
            # Create control: btnTrackBarSetMargins = Button(self)
            self.btnTrackBarSetMargins = Button(self)
            self.btnTrackBarSetMargins.Name = "btnTrackBarSetMargins"
            self.btnTrackBarSetMargins.Parent = self.grpTrackBar
            self.btnTrackBarSetMargins.Left = 2
            self.btnTrackBarSetMargins.Top = 242
            self.btnTrackBarSetMargins.Width = 260
            self.btnTrackBarSetMargins.Height = 25
            self.btnTrackBarSetMargins.Cursor = crArrow
            self.btnTrackBarSetMargins.Align = "alTop"
            self.btnTrackBarSetMargins.Caption = 'Set Margins'
            self.btnTrackBarSetMargins.TabOrder = 4
            # Create control: btnTrackBarSetSliderVisible = Button(self)
            self.btnTrackBarSetSliderVisible = Button(self)
            self.btnTrackBarSetSliderVisible.Name = "btnTrackBarSetSliderVisible"
            self.btnTrackBarSetSliderVisible.Parent = self.grpTrackBar
            self.btnTrackBarSetSliderVisible.Left = 2
            self.btnTrackBarSetSliderVisible.Top = 67
            self.btnTrackBarSetSliderVisible.Width = 260
            self.btnTrackBarSetSliderVisible.Height = 25
            self.btnTrackBarSetSliderVisible.Cursor = crArrow
            self.btnTrackBarSetSliderVisible.Align = "alTop"
            self.btnTrackBarSetSliderVisible.Caption = 'Set SliderVisible'
            self.btnTrackBarSetSliderVisible.TabOrder = 5
            # Create control: btnTrackBarSetOrientation = Button(self)
            self.btnTrackBarSetOrientation = Button(self)
            self.btnTrackBarSetOrientation.Name = "btnTrackBarSetOrientation"
            self.btnTrackBarSetOrientation.Parent = self.grpTrackBar
            self.btnTrackBarSetOrientation.Left = 2
            self.btnTrackBarSetOrientation.Top = 17
            self.btnTrackBarSetOrientation.Width = 260
            self.btnTrackBarSetOrientation.Height = 25
            self.btnTrackBarSetOrientation.Cursor = crArrow
            self.btnTrackBarSetOrientation.Align = "alTop"
            self.btnTrackBarSetOrientation.Caption = 'Set Orientation'
            self.btnTrackBarSetOrientation.TabOrder = 6
            # Create control: btnTrackBarSetShowSelRange = Button(self)
            self.btnTrackBarSetShowSelRange = Button(self)
            self.btnTrackBarSetShowSelRange.Name = "btnTrackBarSetShowSelRange"
            self.btnTrackBarSetShowSelRange.Parent = self.grpTrackBar
            self.btnTrackBarSetShowSelRange.Left = 2
            self.btnTrackBarSetShowSelRange.Top = 42
            self.btnTrackBarSetShowSelRange.Width = 260
            self.btnTrackBarSetShowSelRange.Height = 25
            self.btnTrackBarSetShowSelRange.Cursor = crArrow
            self.btnTrackBarSetShowSelRange.Align = "alTop"
            self.btnTrackBarSetShowSelRange.Caption = 'Set ShowSelRange'
            self.btnTrackBarSetShowSelRange.TabOrder = 7
            # Create control: btnTrackBarSetTickStyle = Button(self)
            self.btnTrackBarSetTickStyle = Button(self)
            self.btnTrackBarSetTickStyle.Name = "btnTrackBarSetTickStyle"
            self.btnTrackBarSetTickStyle.Parent = self.grpTrackBar
            self.btnTrackBarSetTickStyle.Left = 2
            self.btnTrackBarSetTickStyle.Top = 117
            self.btnTrackBarSetTickStyle.Width = 260
            self.btnTrackBarSetTickStyle.Height = 25
            self.btnTrackBarSetTickStyle.Cursor = crArrow
            self.btnTrackBarSetTickStyle.Align = "alTop"
            self.btnTrackBarSetTickStyle.Caption = 'Set TickStyle'
            self.btnTrackBarSetTickStyle.TabOrder = 8
            # Create control: btnTrackBarSetTickMarks = Button(self)
            self.btnTrackBarSetTickMarks = Button(self)
            self.btnTrackBarSetTickMarks.Name = "btnTrackBarSetTickMarks"
            self.btnTrackBarSetTickMarks.Parent = self.grpTrackBar
            self.btnTrackBarSetTickMarks.Left = 2
            self.btnTrackBarSetTickMarks.Top = 92
            self.btnTrackBarSetTickMarks.Width = 260
            self.btnTrackBarSetTickMarks.Height = 25
            self.btnTrackBarSetTickMarks.Cursor = crArrow
            self.btnTrackBarSetTickMarks.Margins.Left = 4
            self.btnTrackBarSetTickMarks.Margins.Top = 4
            self.btnTrackBarSetTickMarks.Margins.Right = 4
            self.btnTrackBarSetTickMarks.Margins.Bottom = 4
            self.btnTrackBarSetTickMarks.Align = "alTop"
            self.btnTrackBarSetTickMarks.Caption = 'Set TickMarks'
            self.btnTrackBarSetTickMarks.TabOrder = 9
            # Create control: shtStatusBar = TabSheet(self)
            self.shtStatusBar = TabSheet(self)
            self.shtStatusBar.Name = "shtStatusBar"
            self.shtStatusBar.PageControl = self.pgFeatures
            self.shtStatusBar.Cursor = crArrow
            self.shtStatusBar.Margins.Left = 4
            self.shtStatusBar.Margins.Top = 4
            self.shtStatusBar.Margins.Right = 4
            self.shtStatusBar.Margins.Bottom = 4
            self.shtStatusBar.Caption = 'Status Bar'
            # Create control: sbStatusBar = StatusBar(self)
            self.sbStatusBar = StatusBar(self)
            self.sbStatusBar.Name = "sbStatusBar"
            self.sbStatusBar.Parent = self.shtStatusBar
            self.sbStatusBar.Left = 0
            self.sbStatusBar.Top = 0
            self.sbStatusBar.Width = 328
            self.sbStatusBar.Height = 308
            self.sbStatusBar.Cursor = crArrow
            self.sbStatusBar.Margins.Left = 4
            self.sbStatusBar.Margins.Top = 4
            self.sbStatusBar.Margins.Right = 4
            self.sbStatusBar.Margins.Bottom = 4
            self.sbStatusBar.Align = "alLeft"
            # Create control: grpStatusBar = GroupBox(self)
            self.grpStatusBar = GroupBox(self)
            self.grpStatusBar.Name = "grpStatusBar"
            self.grpStatusBar.Parent = self.shtStatusBar
            self.grpStatusBar.Left = 1123
            self.grpStatusBar.Top = 0
            self.grpStatusBar.Width = 264
            self.grpStatusBar.Height = 308
            self.grpStatusBar.Cursor = crArrow
            self.grpStatusBar.Margins.Left = 4
            self.grpStatusBar.Margins.Top = 4
            self.grpStatusBar.Margins.Right = 4
            self.grpStatusBar.Margins.Bottom = 4
            self.grpStatusBar.Align = "alRight"
            self.grpStatusBar.Caption = 'Control Usages'
            self.grpStatusBar.TabOrder = 1
            # Create control: btnStatusBarSetBounds = Button(self)
            self.btnStatusBarSetBounds = Button(self)
            self.btnStatusBarSetBounds.Name = "btnStatusBarSetBounds"
            self.btnStatusBarSetBounds.Parent = self.grpStatusBar
            self.btnStatusBarSetBounds.Left = 2
            self.btnStatusBarSetBounds.Top = 117
            self.btnStatusBarSetBounds.Width = 260
            self.btnStatusBarSetBounds.Height = 25
            self.btnStatusBarSetBounds.Cursor = crArrow
            self.btnStatusBarSetBounds.Align = "alTop"
            self.btnStatusBarSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnStatusBarSetBounds.TabOrder = 0
            # Create control: btnStatusBarToggleEnabled = Button(self)
            self.btnStatusBarToggleEnabled = Button(self)
            self.btnStatusBarToggleEnabled.Name = "btnStatusBarToggleEnabled"
            self.btnStatusBarToggleEnabled.Parent = self.grpStatusBar
            self.btnStatusBarToggleEnabled.Left = 2
            self.btnStatusBarToggleEnabled.Top = 142
            self.btnStatusBarToggleEnabled.Width = 260
            self.btnStatusBarToggleEnabled.Height = 25
            self.btnStatusBarToggleEnabled.Cursor = crArrow
            self.btnStatusBarToggleEnabled.Align = "alTop"
            self.btnStatusBarToggleEnabled.Caption = 'Toggle Enabled'
            self.btnStatusBarToggleEnabled.TabOrder = 1
            # Create control: btnStatusBarToggleVisible = Button(self)
            self.btnStatusBarToggleVisible = Button(self)
            self.btnStatusBarToggleVisible.Name = "btnStatusBarToggleVisible"
            self.btnStatusBarToggleVisible.Parent = self.grpStatusBar
            self.btnStatusBarToggleVisible.Left = 2
            self.btnStatusBarToggleVisible.Top = 167
            self.btnStatusBarToggleVisible.Width = 260
            self.btnStatusBarToggleVisible.Height = 25
            self.btnStatusBarToggleVisible.Cursor = crArrow
            self.btnStatusBarToggleVisible.Align = "alTop"
            self.btnStatusBarToggleVisible.Caption = 'Toggle Visible'
            self.btnStatusBarToggleVisible.TabOrder = 2
            # Create control: btnStatusBarSetAlign = Button(self)
            self.btnStatusBarSetAlign = Button(self)
            self.btnStatusBarSetAlign.Name = "btnStatusBarSetAlign"
            self.btnStatusBarSetAlign.Parent = self.grpStatusBar
            self.btnStatusBarSetAlign.Left = 2
            self.btnStatusBarSetAlign.Top = 192
            self.btnStatusBarSetAlign.Width = 260
            self.btnStatusBarSetAlign.Height = 25
            self.btnStatusBarSetAlign.Cursor = crArrow
            self.btnStatusBarSetAlign.Align = "alTop"
            self.btnStatusBarSetAlign.Caption = 'Set Align'
            self.btnStatusBarSetAlign.TabOrder = 3
            # Create control: btnStatusBarSetMargins = Button(self)
            self.btnStatusBarSetMargins = Button(self)
            self.btnStatusBarSetMargins.Name = "btnStatusBarSetMargins"
            self.btnStatusBarSetMargins.Parent = self.grpStatusBar
            self.btnStatusBarSetMargins.Left = 2
            self.btnStatusBarSetMargins.Top = 217
            self.btnStatusBarSetMargins.Width = 260
            self.btnStatusBarSetMargins.Height = 25
            self.btnStatusBarSetMargins.Cursor = crArrow
            self.btnStatusBarSetMargins.Align = "alTop"
            self.btnStatusBarSetMargins.Caption = 'Set Margins'
            self.btnStatusBarSetMargins.TabOrder = 4
            # Create control: btnStatusBarSetSimplePanel = Button(self)
            self.btnStatusBarSetSimplePanel = Button(self)
            self.btnStatusBarSetSimplePanel.Name = "btnStatusBarSetSimplePanel"
            self.btnStatusBarSetSimplePanel.Parent = self.grpStatusBar
            self.btnStatusBarSetSimplePanel.Left = 2
            self.btnStatusBarSetSimplePanel.Top = 67
            self.btnStatusBarSetSimplePanel.Width = 260
            self.btnStatusBarSetSimplePanel.Height = 25
            self.btnStatusBarSetSimplePanel.Cursor = crArrow
            self.btnStatusBarSetSimplePanel.Align = "alTop"
            self.btnStatusBarSetSimplePanel.Caption = 'Set SimplePanel'
            self.btnStatusBarSetSimplePanel.TabOrder = 5
            # Create control: btnStatusBarSetBorderWidth = Button(self)
            self.btnStatusBarSetBorderWidth = Button(self)
            self.btnStatusBarSetBorderWidth.Name = "btnStatusBarSetBorderWidth"
            self.btnStatusBarSetBorderWidth.Parent = self.grpStatusBar
            self.btnStatusBarSetBorderWidth.Left = 2
            self.btnStatusBarSetBorderWidth.Top = 17
            self.btnStatusBarSetBorderWidth.Width = 260
            self.btnStatusBarSetBorderWidth.Height = 25
            self.btnStatusBarSetBorderWidth.Cursor = crArrow
            self.btnStatusBarSetBorderWidth.Align = "alTop"
            self.btnStatusBarSetBorderWidth.Caption = 'Set BorderWidth'
            self.btnStatusBarSetBorderWidth.TabOrder = 6
            # Create control: btnStatusBarSetcolor = Button(self)
            self.btnStatusBarSetcolor = Button(self)
            self.btnStatusBarSetcolor.Name = "btnStatusBarSetcolor"
            self.btnStatusBarSetcolor.Parent = self.grpStatusBar
            self.btnStatusBarSetcolor.Left = 2
            self.btnStatusBarSetcolor.Top = 42
            self.btnStatusBarSetcolor.Width = 260
            self.btnStatusBarSetcolor.Height = 25
            self.btnStatusBarSetcolor.Cursor = crArrow
            self.btnStatusBarSetcolor.Align = "alTop"
            self.btnStatusBarSetcolor.Caption = 'Set color'
            self.btnStatusBarSetcolor.TabOrder = 7
            # Create control: btnStatusBarSetSimpleText = Button(self)
            self.btnStatusBarSetSimpleText = Button(self)
            self.btnStatusBarSetSimpleText.Name = "btnStatusBarSetSimpleText"
            self.btnStatusBarSetSimpleText.Parent = self.grpStatusBar
            self.btnStatusBarSetSimpleText.Left = 2
            self.btnStatusBarSetSimpleText.Top = 92
            self.btnStatusBarSetSimpleText.Width = 260
            self.btnStatusBarSetSimpleText.Height = 25
            self.btnStatusBarSetSimpleText.Cursor = crArrow
            self.btnStatusBarSetSimpleText.Align = "alTop"
            self.btnStatusBarSetSimpleText.Caption = 'Set SimpleText'
            self.btnStatusBarSetSimpleText.TabOrder = 8
            # Create control: shtPaintBox = TabSheet(self)
            self.shtPaintBox = TabSheet(self)
            self.shtPaintBox.Name = "shtPaintBox"
            self.shtPaintBox.PageControl = self.pgFeatures
            self.shtPaintBox.Cursor = crArrow
            self.shtPaintBox.Margins.Left = 4
            self.shtPaintBox.Margins.Top = 4
            self.shtPaintBox.Margins.Right = 4
            self.shtPaintBox.Margins.Bottom = 4
            self.shtPaintBox.Caption = 'Paint Box'
            # Create control: PaintBox = PaintBox(self)
            self.PaintBox = PaintBox(self)
            self.PaintBox.Name = "PaintBox"
            self.PaintBox.Parent = self.shtPaintBox
            self.PaintBox.Left = 168
            self.PaintBox.Top = 88
            self.PaintBox.Width = 105
            self.PaintBox.Height = 105
            self.PaintBox.Cursor = crArrow
            self.PaintBox.Margins.Left = 4
            self.PaintBox.Margins.Top = 4
            self.PaintBox.Margins.Right = 4
            self.PaintBox.Margins.Bottom = 4
            # Create control: grpPaintBox = GroupBox(self)
            self.grpPaintBox = GroupBox(self)
            self.grpPaintBox.Name = "grpPaintBox"
            self.grpPaintBox.Parent = self.shtPaintBox
            self.grpPaintBox.Left = 1123
            self.grpPaintBox.Top = 0
            self.grpPaintBox.Width = 264
            self.grpPaintBox.Height = 308
            self.grpPaintBox.Cursor = crArrow
            self.grpPaintBox.Margins.Left = 4
            self.grpPaintBox.Margins.Top = 4
            self.grpPaintBox.Margins.Right = 4
            self.grpPaintBox.Margins.Bottom = 4
            self.grpPaintBox.Align = "alRight"
            self.grpPaintBox.Caption = 'Control Usages'
            self.grpPaintBox.TabOrder = 0
            # Create control: btnPaintBoxSetBounds = Button(self)
            self.btnPaintBoxSetBounds = Button(self)
            self.btnPaintBoxSetBounds.Name = "btnPaintBoxSetBounds"
            self.btnPaintBoxSetBounds.Parent = self.grpPaintBox
            self.btnPaintBoxSetBounds.Left = 2
            self.btnPaintBoxSetBounds.Top = 17
            self.btnPaintBoxSetBounds.Width = 260
            self.btnPaintBoxSetBounds.Height = 25
            self.btnPaintBoxSetBounds.Cursor = crArrow
            self.btnPaintBoxSetBounds.Align = "alTop"
            self.btnPaintBoxSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnPaintBoxSetBounds.TabOrder = 0
            # Create control: btnPaintBoxToggleEnabled = Button(self)
            self.btnPaintBoxToggleEnabled = Button(self)
            self.btnPaintBoxToggleEnabled.Name = "btnPaintBoxToggleEnabled"
            self.btnPaintBoxToggleEnabled.Parent = self.grpPaintBox
            self.btnPaintBoxToggleEnabled.Left = 2
            self.btnPaintBoxToggleEnabled.Top = 42
            self.btnPaintBoxToggleEnabled.Width = 260
            self.btnPaintBoxToggleEnabled.Height = 25
            self.btnPaintBoxToggleEnabled.Cursor = crArrow
            self.btnPaintBoxToggleEnabled.Align = "alTop"
            self.btnPaintBoxToggleEnabled.Caption = 'Toggle Enabled'
            self.btnPaintBoxToggleEnabled.TabOrder = 1
            # Create control: btnPaintBoxToggleVisible = Button(self)
            self.btnPaintBoxToggleVisible = Button(self)
            self.btnPaintBoxToggleVisible.Name = "btnPaintBoxToggleVisible"
            self.btnPaintBoxToggleVisible.Parent = self.grpPaintBox
            self.btnPaintBoxToggleVisible.Left = 2
            self.btnPaintBoxToggleVisible.Top = 67
            self.btnPaintBoxToggleVisible.Width = 260
            self.btnPaintBoxToggleVisible.Height = 25
            self.btnPaintBoxToggleVisible.Cursor = crArrow
            self.btnPaintBoxToggleVisible.Align = "alTop"
            self.btnPaintBoxToggleVisible.Caption = 'Toggle Visible'
            self.btnPaintBoxToggleVisible.TabOrder = 2
            # Create control: btnPaintBoxSetAlign = Button(self)
            self.btnPaintBoxSetAlign = Button(self)
            self.btnPaintBoxSetAlign.Name = "btnPaintBoxSetAlign"
            self.btnPaintBoxSetAlign.Parent = self.grpPaintBox
            self.btnPaintBoxSetAlign.Left = 2
            self.btnPaintBoxSetAlign.Top = 92
            self.btnPaintBoxSetAlign.Width = 260
            self.btnPaintBoxSetAlign.Height = 25
            self.btnPaintBoxSetAlign.Cursor = crArrow
            self.btnPaintBoxSetAlign.Align = "alTop"
            self.btnPaintBoxSetAlign.Caption = 'Set Align'
            self.btnPaintBoxSetAlign.TabOrder = 3
            # Create control: btnPaintBoxSetMargins = Button(self)
            self.btnPaintBoxSetMargins = Button(self)
            self.btnPaintBoxSetMargins.Name = "btnPaintBoxSetMargins"
            self.btnPaintBoxSetMargins.Parent = self.grpPaintBox
            self.btnPaintBoxSetMargins.Left = 2
            self.btnPaintBoxSetMargins.Top = 117
            self.btnPaintBoxSetMargins.Width = 260
            self.btnPaintBoxSetMargins.Height = 25
            self.btnPaintBoxSetMargins.Cursor = crArrow
            self.btnPaintBoxSetMargins.Align = "alTop"
            self.btnPaintBoxSetMargins.Caption = 'Set Margins'
            self.btnPaintBoxSetMargins.TabOrder = 4
            # Create control: shtImage = TabSheet(self)
            self.shtImage = TabSheet(self)
            self.shtImage.Name = "shtImage"
            self.shtImage.PageControl = self.pgFeatures
            self.shtImage.Cursor = crArrow
            self.shtImage.Margins.Left = 4
            self.shtImage.Margins.Top = 4
            self.shtImage.Margins.Right = 4
            self.shtImage.Margins.Bottom = 4
            self.shtImage.Caption = 'Image'
            # Create control: iImage = Image(self)
            self.iImage = Image(self)
            self.iImage.Name = "iImage"
            self.iImage.Parent = self.shtImage
            self.iImage.Left = 136
            self.iImage.Top = 80
            self.iImage.Width = 105
            self.iImage.Height = 105
            self.iImage.Cursor = crArrow
            self.iImage.Margins.Left = 4
            self.iImage.Margins.Top = 4
            self.iImage.Margins.Right = 4
            self.iImage.Margins.Bottom = 4
            # Create control: grpImage = GroupBox(self)
            self.grpImage = GroupBox(self)
            self.grpImage.Name = "grpImage"
            self.grpImage.Parent = self.shtImage
            self.grpImage.Left = 1123
            self.grpImage.Top = 0
            self.grpImage.Width = 264
            self.grpImage.Height = 308
            self.grpImage.Cursor = crArrow
            self.grpImage.Margins.Left = 4
            self.grpImage.Margins.Top = 4
            self.grpImage.Margins.Right = 4
            self.grpImage.Margins.Bottom = 4
            self.grpImage.Align = "alRight"
            self.grpImage.Caption = 'Control Usages'
            self.grpImage.TabOrder = 0
            # Create control: btnImageToggleEnabled = Button(self)
            self.btnImageToggleEnabled = Button(self)
            self.btnImageToggleEnabled.Name = "btnImageToggleEnabled"
            self.btnImageToggleEnabled.Parent = self.grpImage
            self.btnImageToggleEnabled.Left = 2
            self.btnImageToggleEnabled.Top = 67
            self.btnImageToggleEnabled.Width = 260
            self.btnImageToggleEnabled.Height = 25
            self.btnImageToggleEnabled.Cursor = crArrow
            self.btnImageToggleEnabled.Align = "alTop"
            self.btnImageToggleEnabled.Caption = 'Toggle Enabled'
            self.btnImageToggleEnabled.TabOrder = 0
            # Create control: btnImageToggleVisible = Button(self)
            self.btnImageToggleVisible = Button(self)
            self.btnImageToggleVisible.Name = "btnImageToggleVisible"
            self.btnImageToggleVisible.Parent = self.grpImage
            self.btnImageToggleVisible.Left = 2
            self.btnImageToggleVisible.Top = 92
            self.btnImageToggleVisible.Width = 260
            self.btnImageToggleVisible.Height = 25
            self.btnImageToggleVisible.Cursor = crArrow
            self.btnImageToggleVisible.Align = "alTop"
            self.btnImageToggleVisible.Caption = 'Toggle Visible'
            self.btnImageToggleVisible.TabOrder = 1
            # Create control: btnImageSetAlign = Button(self)
            self.btnImageSetAlign = Button(self)
            self.btnImageSetAlign.Name = "btnImageSetAlign"
            self.btnImageSetAlign.Parent = self.grpImage
            self.btnImageSetAlign.Left = 2
            self.btnImageSetAlign.Top = 117
            self.btnImageSetAlign.Width = 260
            self.btnImageSetAlign.Height = 25
            self.btnImageSetAlign.Cursor = crArrow
            self.btnImageSetAlign.Align = "alTop"
            self.btnImageSetAlign.Caption = 'Set Align'
            self.btnImageSetAlign.TabOrder = 2
            # Create control: btnImageSetMargins = Button(self)
            self.btnImageSetMargins = Button(self)
            self.btnImageSetMargins.Name = "btnImageSetMargins"
            self.btnImageSetMargins.Parent = self.grpImage
            self.btnImageSetMargins.Left = 2
            self.btnImageSetMargins.Top = 142
            self.btnImageSetMargins.Width = 260
            self.btnImageSetMargins.Height = 25
            self.btnImageSetMargins.Cursor = crArrow
            self.btnImageSetMargins.Align = "alTop"
            self.btnImageSetMargins.Caption = 'Set Margins'
            self.btnImageSetMargins.TabOrder = 3
            # Create control: btnImageSetPicture = Button(self)
            self.btnImageSetPicture = Button(self)
            self.btnImageSetPicture.Name = "btnImageSetPicture"
            self.btnImageSetPicture.Parent = self.grpImage
            self.btnImageSetPicture.Left = 2
            self.btnImageSetPicture.Top = 17
            self.btnImageSetPicture.Width = 260
            self.btnImageSetPicture.Height = 25
            self.btnImageSetPicture.Cursor = crArrow
            self.btnImageSetPicture.Align = "alTop"
            self.btnImageSetPicture.Caption = 'Set Picture'
            self.btnImageSetPicture.TabOrder = 4
            # Create control: btnImageSetBounds = Button(self)
            self.btnImageSetBounds = Button(self)
            self.btnImageSetBounds.Name = "btnImageSetBounds"
            self.btnImageSetBounds.Parent = self.grpImage
            self.btnImageSetBounds.Left = 2
            self.btnImageSetBounds.Top = 42
            self.btnImageSetBounds.Width = 260
            self.btnImageSetBounds.Height = 25
            self.btnImageSetBounds.Cursor = crArrow
            self.btnImageSetBounds.Margins.Left = 4
            self.btnImageSetBounds.Margins.Top = 4
            self.btnImageSetBounds.Margins.Right = 4
            self.btnImageSetBounds.Margins.Bottom = 4
            self.btnImageSetBounds.Align = "alTop"
            self.btnImageSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnImageSetBounds.TabOrder = 5
            # Create control: shtBevel = TabSheet(self)
            self.shtBevel = TabSheet(self)
            self.shtBevel.Name = "shtBevel"
            self.shtBevel.PageControl = self.pgFeatures
            self.shtBevel.Cursor = crArrow
            self.shtBevel.Margins.Left = 4
            self.shtBevel.Margins.Top = 4
            self.shtBevel.Margins.Right = 4
            self.shtBevel.Margins.Bottom = 4
            self.shtBevel.Caption = 'Bevel'
            # Create control: bBevel = Bevel(self)
            self.bBevel = Bevel(self)
            self.bBevel.Name = "bBevel"
            self.bBevel.Parent = self.shtBevel
            self.bBevel.Left = 184
            self.bBevel.Top = 88
            self.bBevel.Width = 50
            self.bBevel.Height = 50
            self.bBevel.Cursor = crArrow
            self.bBevel.Margins.Left = 4
            self.bBevel.Margins.Top = 4
            self.bBevel.Margins.Right = 4
            self.bBevel.Margins.Bottom = 4
            # Create control: grpBevel = GroupBox(self)
            self.grpBevel = GroupBox(self)
            self.grpBevel.Name = "grpBevel"
            self.grpBevel.Parent = self.shtBevel
            self.grpBevel.Left = 1123
            self.grpBevel.Top = 0
            self.grpBevel.Width = 264
            self.grpBevel.Height = 308
            self.grpBevel.Cursor = crArrow
            self.grpBevel.Margins.Left = 4
            self.grpBevel.Margins.Top = 4
            self.grpBevel.Margins.Right = 4
            self.grpBevel.Margins.Bottom = 4
            self.grpBevel.Align = "alRight"
            self.grpBevel.Caption = 'Control Usages'
            self.grpBevel.TabOrder = 0
            # Create control: btnBevelSetBounds = Button(self)
            self.btnBevelSetBounds = Button(self)
            self.btnBevelSetBounds.Name = "btnBevelSetBounds"
            self.btnBevelSetBounds.Parent = self.grpBevel
            self.btnBevelSetBounds.Left = 2
            self.btnBevelSetBounds.Top = 67
            self.btnBevelSetBounds.Width = 260
            self.btnBevelSetBounds.Height = 25
            self.btnBevelSetBounds.Cursor = crArrow
            self.btnBevelSetBounds.Align = "alTop"
            self.btnBevelSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnBevelSetBounds.TabOrder = 0
            # Create control: btnBevelToggleEnabled = Button(self)
            self.btnBevelToggleEnabled = Button(self)
            self.btnBevelToggleEnabled.Name = "btnBevelToggleEnabled"
            self.btnBevelToggleEnabled.Parent = self.grpBevel
            self.btnBevelToggleEnabled.Left = 2
            self.btnBevelToggleEnabled.Top = 92
            self.btnBevelToggleEnabled.Width = 260
            self.btnBevelToggleEnabled.Height = 25
            self.btnBevelToggleEnabled.Cursor = crArrow
            self.btnBevelToggleEnabled.Align = "alTop"
            self.btnBevelToggleEnabled.Caption = 'Toggle Enabled'
            self.btnBevelToggleEnabled.TabOrder = 1
            # Create control: btnBevelToggleVisible = Button(self)
            self.btnBevelToggleVisible = Button(self)
            self.btnBevelToggleVisible.Name = "btnBevelToggleVisible"
            self.btnBevelToggleVisible.Parent = self.grpBevel
            self.btnBevelToggleVisible.Left = 2
            self.btnBevelToggleVisible.Top = 117
            self.btnBevelToggleVisible.Width = 260
            self.btnBevelToggleVisible.Height = 25
            self.btnBevelToggleVisible.Cursor = crArrow
            self.btnBevelToggleVisible.Align = "alTop"
            self.btnBevelToggleVisible.Caption = 'Toggle Visible'
            self.btnBevelToggleVisible.TabOrder = 2
            # Create control: btnBevelSetAlign = Button(self)
            self.btnBevelSetAlign = Button(self)
            self.btnBevelSetAlign.Name = "btnBevelSetAlign"
            self.btnBevelSetAlign.Parent = self.grpBevel
            self.btnBevelSetAlign.Left = 2
            self.btnBevelSetAlign.Top = 142
            self.btnBevelSetAlign.Width = 260
            self.btnBevelSetAlign.Height = 25
            self.btnBevelSetAlign.Cursor = crArrow
            self.btnBevelSetAlign.Align = "alTop"
            self.btnBevelSetAlign.Caption = 'Set Align'
            self.btnBevelSetAlign.TabOrder = 3
            # Create control: btnBevelSetMargins = Button(self)
            self.btnBevelSetMargins = Button(self)
            self.btnBevelSetMargins.Name = "btnBevelSetMargins"
            self.btnBevelSetMargins.Parent = self.grpBevel
            self.btnBevelSetMargins.Left = 2
            self.btnBevelSetMargins.Top = 167
            self.btnBevelSetMargins.Width = 260
            self.btnBevelSetMargins.Height = 25
            self.btnBevelSetMargins.Cursor = crArrow
            self.btnBevelSetMargins.Align = "alTop"
            self.btnBevelSetMargins.Caption = 'Set Margins'
            self.btnBevelSetMargins.TabOrder = 4
            # Create control: btnBevelSetStyle = Button(self)
            self.btnBevelSetStyle = Button(self)
            self.btnBevelSetStyle.Name = "btnBevelSetStyle"
            self.btnBevelSetStyle.Parent = self.grpBevel
            self.btnBevelSetStyle.Left = 2
            self.btnBevelSetStyle.Top = 17
            self.btnBevelSetStyle.Width = 260
            self.btnBevelSetStyle.Height = 25
            self.btnBevelSetStyle.Cursor = crArrow
            self.btnBevelSetStyle.Align = "alTop"
            self.btnBevelSetStyle.Caption = 'Set Style'
            self.btnBevelSetStyle.TabOrder = 5
            # Create control: btnBevelSetShape = Button(self)
            self.btnBevelSetShape = Button(self)
            self.btnBevelSetShape.Name = "btnBevelSetShape"
            self.btnBevelSetShape.Parent = self.grpBevel
            self.btnBevelSetShape.Left = 2
            self.btnBevelSetShape.Top = 42
            self.btnBevelSetShape.Width = 260
            self.btnBevelSetShape.Height = 25
            self.btnBevelSetShape.Cursor = crArrow
            self.btnBevelSetShape.Align = "alTop"
            self.btnBevelSetShape.Caption = 'Set Shape'
            self.btnBevelSetShape.TabOrder = 6
            # Create control: shtTabControl = TabSheet(self)
            self.shtTabControl = TabSheet(self)
            self.shtTabControl.Name = "shtTabControl"
            self.shtTabControl.PageControl = self.pgFeatures
            self.shtTabControl.Cursor = crArrow
            self.shtTabControl.Margins.Left = 4
            self.shtTabControl.Margins.Top = 4
            self.shtTabControl.Margins.Right = 4
            self.shtTabControl.Margins.Bottom = 4
            self.shtTabControl.Caption = 'Tab Control'
            # Create control: tcTabControl = TabControl(self)
            self.tcTabControl = TabControl(self)
            self.tcTabControl.Name = "tcTabControl"
            self.tcTabControl.Parent = self.shtTabControl
            self.tcTabControl.Left = 160
            self.tcTabControl.Top = 88
            self.tcTabControl.Width = 289
            self.tcTabControl.Height = 193
            self.tcTabControl.Cursor = crArrow
            self.tcTabControl.Margins.Left = 4
            self.tcTabControl.Margins.Top = 4
            self.tcTabControl.Margins.Right = 4
            self.tcTabControl.Margins.Bottom = 4
            self.tcTabControl.TabOrder = 0
            # Create control: grpTabControl = GroupBox(self)
            self.grpTabControl = GroupBox(self)
            self.grpTabControl.Name = "grpTabControl"
            self.grpTabControl.Parent = self.shtTabControl
            self.grpTabControl.Left = 1123
            self.grpTabControl.Top = 0
            self.grpTabControl.Width = 264
            self.grpTabControl.Height = 308
            self.grpTabControl.Cursor = crArrow
            self.grpTabControl.Margins.Left = 4
            self.grpTabControl.Margins.Top = 4
            self.grpTabControl.Margins.Right = 4
            self.grpTabControl.Margins.Bottom = 4
            self.grpTabControl.Align = "alRight"
            self.grpTabControl.Caption = 'Control Usages'
            self.grpTabControl.TabOrder = 1
            # Create control: btnTabControlSetBounds = Button(self)
            self.btnTabControlSetBounds = Button(self)
            self.btnTabControlSetBounds.Name = "btnTabControlSetBounds"
            self.btnTabControlSetBounds.Parent = self.grpTabControl
            self.btnTabControlSetBounds.Left = 2
            self.btnTabControlSetBounds.Top = 67
            self.btnTabControlSetBounds.Width = 260
            self.btnTabControlSetBounds.Height = 25
            self.btnTabControlSetBounds.Cursor = crArrow
            self.btnTabControlSetBounds.Align = "alTop"
            self.btnTabControlSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnTabControlSetBounds.TabOrder = 0
            # Create control: btnTabControlToggleEnabled = Button(self)
            self.btnTabControlToggleEnabled = Button(self)
            self.btnTabControlToggleEnabled.Name = "btnTabControlToggleEnabled"
            self.btnTabControlToggleEnabled.Parent = self.grpTabControl
            self.btnTabControlToggleEnabled.Left = 2
            self.btnTabControlToggleEnabled.Top = 92
            self.btnTabControlToggleEnabled.Width = 260
            self.btnTabControlToggleEnabled.Height = 25
            self.btnTabControlToggleEnabled.Cursor = crArrow
            self.btnTabControlToggleEnabled.Align = "alTop"
            self.btnTabControlToggleEnabled.Caption = 'Toggle Enabled'
            self.btnTabControlToggleEnabled.TabOrder = 1
            # Create control: btnTabControlToggleVisible = Button(self)
            self.btnTabControlToggleVisible = Button(self)
            self.btnTabControlToggleVisible.Name = "btnTabControlToggleVisible"
            self.btnTabControlToggleVisible.Parent = self.grpTabControl
            self.btnTabControlToggleVisible.Left = 2
            self.btnTabControlToggleVisible.Top = 117
            self.btnTabControlToggleVisible.Width = 260
            self.btnTabControlToggleVisible.Height = 25
            self.btnTabControlToggleVisible.Cursor = crArrow
            self.btnTabControlToggleVisible.Align = "alTop"
            self.btnTabControlToggleVisible.Caption = 'Toggle Visible'
            self.btnTabControlToggleVisible.TabOrder = 2
            # Create control: btnTabControlSetAlign = Button(self)
            self.btnTabControlSetAlign = Button(self)
            self.btnTabControlSetAlign.Name = "btnTabControlSetAlign"
            self.btnTabControlSetAlign.Parent = self.grpTabControl
            self.btnTabControlSetAlign.Left = 2
            self.btnTabControlSetAlign.Top = 142
            self.btnTabControlSetAlign.Width = 260
            self.btnTabControlSetAlign.Height = 25
            self.btnTabControlSetAlign.Cursor = crArrow
            self.btnTabControlSetAlign.Align = "alTop"
            self.btnTabControlSetAlign.Caption = 'Set Align'
            self.btnTabControlSetAlign.TabOrder = 3
            # Create control: btnTabControlSetMargins = Button(self)
            self.btnTabControlSetMargins = Button(self)
            self.btnTabControlSetMargins.Name = "btnTabControlSetMargins"
            self.btnTabControlSetMargins.Parent = self.grpTabControl
            self.btnTabControlSetMargins.Left = 2
            self.btnTabControlSetMargins.Top = 167
            self.btnTabControlSetMargins.Width = 260
            self.btnTabControlSetMargins.Height = 25
            self.btnTabControlSetMargins.Cursor = crArrow
            self.btnTabControlSetMargins.Align = "alTop"
            self.btnTabControlSetMargins.Caption = 'Set Margins'
            self.btnTabControlSetMargins.TabOrder = 4
            # Create control: btnTabControlSetOwnerDraw = Button(self)
            self.btnTabControlSetOwnerDraw = Button(self)
            self.btnTabControlSetOwnerDraw.Name = "btnTabControlSetOwnerDraw"
            self.btnTabControlSetOwnerDraw.Parent = self.grpTabControl
            self.btnTabControlSetOwnerDraw.Left = 2
            self.btnTabControlSetOwnerDraw.Top = 17
            self.btnTabControlSetOwnerDraw.Width = 260
            self.btnTabControlSetOwnerDraw.Height = 25
            self.btnTabControlSetOwnerDraw.Cursor = crArrow
            self.btnTabControlSetOwnerDraw.Align = "alTop"
            self.btnTabControlSetOwnerDraw.Caption = 'Set OwnerDraw'
            self.btnTabControlSetOwnerDraw.TabOrder = 5
            # Create control: btnTabControlSetStyle = Button(self)
            self.btnTabControlSetStyle = Button(self)
            self.btnTabControlSetStyle.Name = "btnTabControlSetStyle"
            self.btnTabControlSetStyle.Parent = self.grpTabControl
            self.btnTabControlSetStyle.Left = 2
            self.btnTabControlSetStyle.Top = 42
            self.btnTabControlSetStyle.Width = 260
            self.btnTabControlSetStyle.Height = 25
            self.btnTabControlSetStyle.Cursor = crArrow
            self.btnTabControlSetStyle.Align = "alTop"
            self.btnTabControlSetStyle.Caption = 'Set Style'
            self.btnTabControlSetStyle.TabOrder = 6
            # Create control: shtProgressBar = TabSheet(self)
            self.shtProgressBar = TabSheet(self)
            self.shtProgressBar.Name = "shtProgressBar"
            self.shtProgressBar.PageControl = self.pgFeatures
            self.shtProgressBar.Cursor = crArrow
            self.shtProgressBar.Margins.Left = 4
            self.shtProgressBar.Margins.Top = 4
            self.shtProgressBar.Margins.Right = 4
            self.shtProgressBar.Margins.Bottom = 4
            self.shtProgressBar.Caption = 'Progress Bar'
            # Create control: pbProgressBar = ProgressBar(self)
            self.pbProgressBar = ProgressBar(self)
            self.pbProgressBar.Name = "pbProgressBar"
            self.pbProgressBar.Parent = self.shtProgressBar
            self.pbProgressBar.Left = 176
            self.pbProgressBar.Top = 72
            self.pbProgressBar.Width = 150
            self.pbProgressBar.Height = 21
            self.pbProgressBar.Cursor = crArrow
            self.pbProgressBar.Margins.Left = 4
            self.pbProgressBar.Margins.Top = 4
            self.pbProgressBar.Margins.Right = 4
            self.pbProgressBar.Margins.Bottom = 4
            self.pbProgressBar.TabOrder = 0
            # Create control: grpProgressBar = GroupBox(self)
            self.grpProgressBar = GroupBox(self)
            self.grpProgressBar.Name = "grpProgressBar"
            self.grpProgressBar.Parent = self.shtProgressBar
            self.grpProgressBar.Left = 1123
            self.grpProgressBar.Top = 0
            self.grpProgressBar.Width = 264
            self.grpProgressBar.Height = 308
            self.grpProgressBar.Cursor = crArrow
            self.grpProgressBar.Margins.Left = 4
            self.grpProgressBar.Margins.Top = 4
            self.grpProgressBar.Margins.Right = 4
            self.grpProgressBar.Margins.Bottom = 4
            self.grpProgressBar.Align = "alRight"
            self.grpProgressBar.Caption = 'Control Usages'
            self.grpProgressBar.TabOrder = 1
            # Create control: btnProgressBarToggleEnabled = Button(self)
            self.btnProgressBarToggleEnabled = Button(self)
            self.btnProgressBarToggleEnabled.Name = "btnProgressBarToggleEnabled"
            self.btnProgressBarToggleEnabled.Parent = self.grpProgressBar
            self.btnProgressBarToggleEnabled.Left = 2
            self.btnProgressBarToggleEnabled.Top = 117
            self.btnProgressBarToggleEnabled.Width = 260
            self.btnProgressBarToggleEnabled.Height = 25
            self.btnProgressBarToggleEnabled.Cursor = crArrow
            self.btnProgressBarToggleEnabled.Align = "alTop"
            self.btnProgressBarToggleEnabled.Caption = 'Toggle Enabled'
            self.btnProgressBarToggleEnabled.TabOrder = 0
            # Create control: btnProgressBarToggleVisible = Button(self)
            self.btnProgressBarToggleVisible = Button(self)
            self.btnProgressBarToggleVisible.Name = "btnProgressBarToggleVisible"
            self.btnProgressBarToggleVisible.Parent = self.grpProgressBar
            self.btnProgressBarToggleVisible.Left = 2
            self.btnProgressBarToggleVisible.Top = 142
            self.btnProgressBarToggleVisible.Width = 260
            self.btnProgressBarToggleVisible.Height = 25
            self.btnProgressBarToggleVisible.Cursor = crArrow
            self.btnProgressBarToggleVisible.Align = "alTop"
            self.btnProgressBarToggleVisible.Caption = 'Toggle Visible'
            self.btnProgressBarToggleVisible.TabOrder = 1
            # Create control: btnProgressBarSetAlign = Button(self)
            self.btnProgressBarSetAlign = Button(self)
            self.btnProgressBarSetAlign.Name = "btnProgressBarSetAlign"
            self.btnProgressBarSetAlign.Parent = self.grpProgressBar
            self.btnProgressBarSetAlign.Left = 2
            self.btnProgressBarSetAlign.Top = 167
            self.btnProgressBarSetAlign.Width = 260
            self.btnProgressBarSetAlign.Height = 25
            self.btnProgressBarSetAlign.Cursor = crArrow
            self.btnProgressBarSetAlign.Align = "alTop"
            self.btnProgressBarSetAlign.Caption = 'Set Align'
            self.btnProgressBarSetAlign.TabOrder = 2
            # Create control: btnProgressBarSetMargins = Button(self)
            self.btnProgressBarSetMargins = Button(self)
            self.btnProgressBarSetMargins.Name = "btnProgressBarSetMargins"
            self.btnProgressBarSetMargins.Parent = self.grpProgressBar
            self.btnProgressBarSetMargins.Left = 2
            self.btnProgressBarSetMargins.Top = 192
            self.btnProgressBarSetMargins.Width = 260
            self.btnProgressBarSetMargins.Height = 25
            self.btnProgressBarSetMargins.Cursor = crArrow
            self.btnProgressBarSetMargins.Align = "alTop"
            self.btnProgressBarSetMargins.Caption = 'Set Margins'
            self.btnProgressBarSetMargins.TabOrder = 3
            # Create control: btnProgressBarSetState = Button(self)
            self.btnProgressBarSetState = Button(self)
            self.btnProgressBarSetState.Name = "btnProgressBarSetState"
            self.btnProgressBarSetState.Parent = self.grpProgressBar
            self.btnProgressBarSetState.Left = 2
            self.btnProgressBarSetState.Top = 67
            self.btnProgressBarSetState.Width = 260
            self.btnProgressBarSetState.Height = 25
            self.btnProgressBarSetState.Cursor = crArrow
            self.btnProgressBarSetState.Align = "alTop"
            self.btnProgressBarSetState.Caption = 'Set State'
            self.btnProgressBarSetState.TabOrder = 4
            # Create control: btnProgressBarSetBorderWidth = Button(self)
            self.btnProgressBarSetBorderWidth = Button(self)
            self.btnProgressBarSetBorderWidth.Name = "btnProgressBarSetBorderWidth"
            self.btnProgressBarSetBorderWidth.Parent = self.grpProgressBar
            self.btnProgressBarSetBorderWidth.Left = 2
            self.btnProgressBarSetBorderWidth.Top = 17
            self.btnProgressBarSetBorderWidth.Width = 260
            self.btnProgressBarSetBorderWidth.Height = 25
            self.btnProgressBarSetBorderWidth.Cursor = crArrow
            self.btnProgressBarSetBorderWidth.Align = "alTop"
            self.btnProgressBarSetBorderWidth.Caption = 'Set BorderWidth'
            self.btnProgressBarSetBorderWidth.TabOrder = 5
            # Create control: btnProgressBarSetStyle = Button(self)
            self.btnProgressBarSetStyle = Button(self)
            self.btnProgressBarSetStyle.Name = "btnProgressBarSetStyle"
            self.btnProgressBarSetStyle.Parent = self.grpProgressBar
            self.btnProgressBarSetStyle.Left = 2
            self.btnProgressBarSetStyle.Top = 42
            self.btnProgressBarSetStyle.Width = 260
            self.btnProgressBarSetStyle.Height = 25
            self.btnProgressBarSetStyle.Cursor = crArrow
            self.btnProgressBarSetStyle.Align = "alTop"
            self.btnProgressBarSetStyle.Caption = 'Set Style'
            self.btnProgressBarSetStyle.TabOrder = 6
            # Create control: btnProgressBarSetBounds = Button(self)
            self.btnProgressBarSetBounds = Button(self)
            self.btnProgressBarSetBounds.Name = "btnProgressBarSetBounds"
            self.btnProgressBarSetBounds.Parent = self.grpProgressBar
            self.btnProgressBarSetBounds.Left = 2
            self.btnProgressBarSetBounds.Top = 92
            self.btnProgressBarSetBounds.Width = 260
            self.btnProgressBarSetBounds.Height = 25
            self.btnProgressBarSetBounds.Cursor = crArrow
            self.btnProgressBarSetBounds.Align = "alTop"
            self.btnProgressBarSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnProgressBarSetBounds.TabOrder = 7
            # Create control: shtHeader = TabSheet(self)
            self.shtHeader = TabSheet(self)
            self.shtHeader.Name = "shtHeader"
            self.shtHeader.PageControl = self.pgFeatures
            self.shtHeader.Cursor = crArrow
            self.shtHeader.Margins.Left = 4
            self.shtHeader.Margins.Top = 4
            self.shtHeader.Margins.Right = 4
            self.shtHeader.Margins.Bottom = 4
            self.shtHeader.Caption = 'Header'
            # Create control: hHeader = Header(self)
            self.hHeader = Header(self)
            self.hHeader.Name = "hHeader"
            self.hHeader.Parent = self.shtHeader
            self.hHeader.Left = 192
            self.hHeader.Top = 96
            self.hHeader.Width = 250
            self.hHeader.Height = 25
            self.hHeader.Cursor = crArrow
            self.hHeader.Margins.Left = 4
            self.hHeader.Margins.Top = 4
            self.hHeader.Margins.Right = 4
            self.hHeader.Margins.Bottom = 4
            self.hHeader.TabOrder = 0
            # Create control: grpHeader = GroupBox(self)
            self.grpHeader = GroupBox(self)
            self.grpHeader.Name = "grpHeader"
            self.grpHeader.Parent = self.shtHeader
            self.grpHeader.Left = 1123
            self.grpHeader.Top = 0
            self.grpHeader.Width = 264
            self.grpHeader.Height = 308
            self.grpHeader.Cursor = crArrow
            self.grpHeader.Margins.Left = 4
            self.grpHeader.Margins.Top = 4
            self.grpHeader.Margins.Right = 4
            self.grpHeader.Margins.Bottom = 4
            self.grpHeader.Align = "alRight"
            self.grpHeader.Caption = 'Control Usages'
            self.grpHeader.TabOrder = 1
            # Create control: btnHeaderSetBounds = Button(self)
            self.btnHeaderSetBounds = Button(self)
            self.btnHeaderSetBounds.Name = "btnHeaderSetBounds"
            self.btnHeaderSetBounds.Parent = self.grpHeader
            self.btnHeaderSetBounds.Left = 2
            self.btnHeaderSetBounds.Top = 67
            self.btnHeaderSetBounds.Width = 260
            self.btnHeaderSetBounds.Height = 25
            self.btnHeaderSetBounds.Cursor = crArrow
            self.btnHeaderSetBounds.Align = "alTop"
            self.btnHeaderSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnHeaderSetBounds.TabOrder = 0
            # Create control: btnHeaderToggleEnabled = Button(self)
            self.btnHeaderToggleEnabled = Button(self)
            self.btnHeaderToggleEnabled.Name = "btnHeaderToggleEnabled"
            self.btnHeaderToggleEnabled.Parent = self.grpHeader
            self.btnHeaderToggleEnabled.Left = 2
            self.btnHeaderToggleEnabled.Top = 92
            self.btnHeaderToggleEnabled.Width = 260
            self.btnHeaderToggleEnabled.Height = 25
            self.btnHeaderToggleEnabled.Cursor = crArrow
            self.btnHeaderToggleEnabled.Align = "alTop"
            self.btnHeaderToggleEnabled.Caption = 'Toggle Enabled'
            self.btnHeaderToggleEnabled.TabOrder = 1
            # Create control: btnHeaderToggleVisible = Button(self)
            self.btnHeaderToggleVisible = Button(self)
            self.btnHeaderToggleVisible.Name = "btnHeaderToggleVisible"
            self.btnHeaderToggleVisible.Parent = self.grpHeader
            self.btnHeaderToggleVisible.Left = 2
            self.btnHeaderToggleVisible.Top = 117
            self.btnHeaderToggleVisible.Width = 260
            self.btnHeaderToggleVisible.Height = 25
            self.btnHeaderToggleVisible.Cursor = crArrow
            self.btnHeaderToggleVisible.Align = "alTop"
            self.btnHeaderToggleVisible.Caption = 'Toggle Visible'
            self.btnHeaderToggleVisible.TabOrder = 2
            # Create control: btnHeaderSetAlign = Button(self)
            self.btnHeaderSetAlign = Button(self)
            self.btnHeaderSetAlign.Name = "btnHeaderSetAlign"
            self.btnHeaderSetAlign.Parent = self.grpHeader
            self.btnHeaderSetAlign.Left = 2
            self.btnHeaderSetAlign.Top = 142
            self.btnHeaderSetAlign.Width = 260
            self.btnHeaderSetAlign.Height = 25
            self.btnHeaderSetAlign.Cursor = crArrow
            self.btnHeaderSetAlign.Align = "alTop"
            self.btnHeaderSetAlign.Caption = 'Set Align'
            self.btnHeaderSetAlign.TabOrder = 3
            # Create control: btnHeaderSetMargins = Button(self)
            self.btnHeaderSetMargins = Button(self)
            self.btnHeaderSetMargins.Name = "btnHeaderSetMargins"
            self.btnHeaderSetMargins.Parent = self.grpHeader
            self.btnHeaderSetMargins.Left = 2
            self.btnHeaderSetMargins.Top = 167
            self.btnHeaderSetMargins.Width = 260
            self.btnHeaderSetMargins.Height = 25
            self.btnHeaderSetMargins.Cursor = crArrow
            self.btnHeaderSetMargins.Align = "alTop"
            self.btnHeaderSetMargins.Caption = 'Set Margins'
            self.btnHeaderSetMargins.TabOrder = 4
            # Create control: btnHeaderSetBorderStyle = Button(self)
            self.btnHeaderSetBorderStyle = Button(self)
            self.btnHeaderSetBorderStyle.Name = "btnHeaderSetBorderStyle"
            self.btnHeaderSetBorderStyle.Parent = self.grpHeader
            self.btnHeaderSetBorderStyle.Left = 2
            self.btnHeaderSetBorderStyle.Top = 17
            self.btnHeaderSetBorderStyle.Width = 260
            self.btnHeaderSetBorderStyle.Height = 25
            self.btnHeaderSetBorderStyle.Cursor = crArrow
            self.btnHeaderSetBorderStyle.Align = "alTop"
            self.btnHeaderSetBorderStyle.Caption = 'Set BorderStyle'
            self.btnHeaderSetBorderStyle.TabOrder = 5
            # Create control: btnHeaderSetSections = Button(self)
            self.btnHeaderSetSections = Button(self)
            self.btnHeaderSetSections.Name = "btnHeaderSetSections"
            self.btnHeaderSetSections.Parent = self.grpHeader
            self.btnHeaderSetSections.Left = 2
            self.btnHeaderSetSections.Top = 42
            self.btnHeaderSetSections.Width = 260
            self.btnHeaderSetSections.Height = 25
            self.btnHeaderSetSections.Cursor = crArrow
            self.btnHeaderSetSections.Align = "alTop"
            self.btnHeaderSetSections.Caption = 'Set Sections'
            self.btnHeaderSetSections.TabOrder = 6
            # Create control: shtSplitter = TabSheet(self)
            self.shtSplitter = TabSheet(self)
            self.shtSplitter.Name = "shtSplitter"
            self.shtSplitter.PageControl = self.pgFeatures
            self.shtSplitter.Cursor = crArrow
            self.shtSplitter.Margins.Left = 4
            self.shtSplitter.Margins.Top = 4
            self.shtSplitter.Margins.Right = 4
            self.shtSplitter.Margins.Bottom = 4
            self.shtSplitter.Caption = 'Splitter'
            # Create control: sSplitter = Splitter(self)
            self.sSplitter = Splitter(self)
            self.sSplitter.Name = "sSplitter"
            self.sSplitter.Parent = self.shtSplitter
            self.sSplitter.Left = 0
            self.sSplitter.Top = 0
            self.sSplitter.Cursor = crArrow
            self.sSplitter.Margins.Left = 4
            self.sSplitter.Margins.Top = 4
            self.sSplitter.Margins.Right = 4
            self.sSplitter.Margins.Bottom = 4
            # Create control: grpSplitter = GroupBox(self)
            self.grpSplitter = GroupBox(self)
            self.grpSplitter.Name = "grpSplitter"
            self.grpSplitter.Parent = self.shtSplitter
            self.grpSplitter.Left = 1123
            self.grpSplitter.Top = 0
            self.grpSplitter.Width = 264
            self.grpSplitter.Height = 308
            self.grpSplitter.Cursor = crArrow
            self.grpSplitter.Margins.Left = 4
            self.grpSplitter.Margins.Top = 4
            self.grpSplitter.Margins.Right = 4
            self.grpSplitter.Margins.Bottom = 4
            self.grpSplitter.Align = "alRight"
            self.grpSplitter.Caption = 'Control Usages'
            self.grpSplitter.TabOrder = 0
            # Create control: btnSplitterSetBounds = Button(self)
            self.btnSplitterSetBounds = Button(self)
            self.btnSplitterSetBounds.Name = "btnSplitterSetBounds"
            self.btnSplitterSetBounds.Parent = self.grpSplitter
            self.btnSplitterSetBounds.Left = 2
            self.btnSplitterSetBounds.Top = 67
            self.btnSplitterSetBounds.Width = 260
            self.btnSplitterSetBounds.Height = 25
            self.btnSplitterSetBounds.Cursor = crArrow
            self.btnSplitterSetBounds.Align = "alTop"
            self.btnSplitterSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnSplitterSetBounds.TabOrder = 0
            # Create control: btnSplitterToggleEnabled = Button(self)
            self.btnSplitterToggleEnabled = Button(self)
            self.btnSplitterToggleEnabled.Name = "btnSplitterToggleEnabled"
            self.btnSplitterToggleEnabled.Parent = self.grpSplitter
            self.btnSplitterToggleEnabled.Left = 2
            self.btnSplitterToggleEnabled.Top = 92
            self.btnSplitterToggleEnabled.Width = 260
            self.btnSplitterToggleEnabled.Height = 25
            self.btnSplitterToggleEnabled.Cursor = crArrow
            self.btnSplitterToggleEnabled.Align = "alTop"
            self.btnSplitterToggleEnabled.Caption = 'Toggle Enabled'
            self.btnSplitterToggleEnabled.TabOrder = 1
            # Create control: btnSplitterToggleVisible = Button(self)
            self.btnSplitterToggleVisible = Button(self)
            self.btnSplitterToggleVisible.Name = "btnSplitterToggleVisible"
            self.btnSplitterToggleVisible.Parent = self.grpSplitter
            self.btnSplitterToggleVisible.Left = 2
            self.btnSplitterToggleVisible.Top = 117
            self.btnSplitterToggleVisible.Width = 260
            self.btnSplitterToggleVisible.Height = 25
            self.btnSplitterToggleVisible.Cursor = crArrow
            self.btnSplitterToggleVisible.Align = "alTop"
            self.btnSplitterToggleVisible.Caption = 'Toggle Visible'
            self.btnSplitterToggleVisible.TabOrder = 2
            # Create control: btnSplitterSetAlign = Button(self)
            self.btnSplitterSetAlign = Button(self)
            self.btnSplitterSetAlign.Name = "btnSplitterSetAlign"
            self.btnSplitterSetAlign.Parent = self.grpSplitter
            self.btnSplitterSetAlign.Left = 2
            self.btnSplitterSetAlign.Top = 142
            self.btnSplitterSetAlign.Width = 260
            self.btnSplitterSetAlign.Height = 25
            self.btnSplitterSetAlign.Cursor = crArrow
            self.btnSplitterSetAlign.Align = "alTop"
            self.btnSplitterSetAlign.Caption = 'Set Align'
            self.btnSplitterSetAlign.TabOrder = 3
            # Create control: btnSplitterSetMargins = Button(self)
            self.btnSplitterSetMargins = Button(self)
            self.btnSplitterSetMargins.Name = "btnSplitterSetMargins"
            self.btnSplitterSetMargins.Parent = self.grpSplitter
            self.btnSplitterSetMargins.Left = 2
            self.btnSplitterSetMargins.Top = 167
            self.btnSplitterSetMargins.Width = 260
            self.btnSplitterSetMargins.Height = 25
            self.btnSplitterSetMargins.Cursor = crArrow
            self.btnSplitterSetMargins.Align = "alTop"
            self.btnSplitterSetMargins.Caption = 'Set Margins'
            self.btnSplitterSetMargins.TabOrder = 4
            # Create control: btnSplitterSetBeveled = Button(self)
            self.btnSplitterSetBeveled = Button(self)
            self.btnSplitterSetBeveled.Name = "btnSplitterSetBeveled"
            self.btnSplitterSetBeveled.Parent = self.grpSplitter
            self.btnSplitterSetBeveled.Left = 2
            self.btnSplitterSetBeveled.Top = 17
            self.btnSplitterSetBeveled.Width = 260
            self.btnSplitterSetBeveled.Height = 25
            self.btnSplitterSetBeveled.Cursor = crArrow
            self.btnSplitterSetBeveled.Align = "alTop"
            self.btnSplitterSetBeveled.Caption = 'Set Beveled'
            self.btnSplitterSetBeveled.TabOrder = 5
            # Create control: btnSplitterSetColor = Button(self)
            self.btnSplitterSetColor = Button(self)
            self.btnSplitterSetColor.Name = "btnSplitterSetColor"
            self.btnSplitterSetColor.Parent = self.grpSplitter
            self.btnSplitterSetColor.Left = 2
            self.btnSplitterSetColor.Top = 42
            self.btnSplitterSetColor.Width = 260
            self.btnSplitterSetColor.Height = 25
            self.btnSplitterSetColor.Cursor = crArrow
            self.btnSplitterSetColor.Align = "alTop"
            self.btnSplitterSetColor.Caption = 'Set Color'
            self.btnSplitterSetColor.TabOrder = 6
            # Create control: shtControlBar = TabSheet(self)
            self.shtControlBar = TabSheet(self)
            self.shtControlBar.Name = "shtControlBar"
            self.shtControlBar.PageControl = self.pgFeatures
            self.shtControlBar.Cursor = crArrow
            self.shtControlBar.Margins.Left = 4
            self.shtControlBar.Margins.Top = 4
            self.shtControlBar.Margins.Right = 4
            self.shtControlBar.Margins.Bottom = 4
            self.shtControlBar.Caption = 'Control Bar'
            # Create control: cbControlBar = ControlBar(self)
            self.cbControlBar = ControlBar(self)
            self.cbControlBar.Name = "cbControlBar"
            self.cbControlBar.Parent = self.shtControlBar
            self.cbControlBar.Left = 224
            self.cbControlBar.Top = 72
            self.cbControlBar.Width = 100
            self.cbControlBar.Height = 50
            self.cbControlBar.Cursor = crArrow
            self.cbControlBar.Margins.Left = 4
            self.cbControlBar.Margins.Top = 4
            self.cbControlBar.Margins.Right = 4
            self.cbControlBar.Margins.Bottom = 4
            self.cbControlBar.RowSize = 33
            self.cbControlBar.TabOrder = 0
            # Create control: grpControlBar = GroupBox(self)
            self.grpControlBar = GroupBox(self)
            self.grpControlBar.Name = "grpControlBar"
            self.grpControlBar.Parent = self.shtControlBar
            self.grpControlBar.Left = 1123
            self.grpControlBar.Top = 0
            self.grpControlBar.Width = 264
            self.grpControlBar.Height = 308
            self.grpControlBar.Cursor = crArrow
            self.grpControlBar.Margins.Left = 4
            self.grpControlBar.Margins.Top = 4
            self.grpControlBar.Margins.Right = 4
            self.grpControlBar.Margins.Bottom = 4
            self.grpControlBar.Align = "alRight"
            self.grpControlBar.Caption = 'Control Usages'
            self.grpControlBar.TabOrder = 1
            # Create control: btnControlBarSetBounds = Button(self)
            self.btnControlBarSetBounds = Button(self)
            self.btnControlBarSetBounds.Name = "btnControlBarSetBounds"
            self.btnControlBarSetBounds.Parent = self.grpControlBar
            self.btnControlBarSetBounds.Left = 2
            self.btnControlBarSetBounds.Top = 192
            self.btnControlBarSetBounds.Width = 260
            self.btnControlBarSetBounds.Height = 25
            self.btnControlBarSetBounds.Cursor = crArrow
            self.btnControlBarSetBounds.Align = "alTop"
            self.btnControlBarSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnControlBarSetBounds.TabOrder = 0
            # Create control: btnControlBarToggleEnabled = Button(self)
            self.btnControlBarToggleEnabled = Button(self)
            self.btnControlBarToggleEnabled.Name = "btnControlBarToggleEnabled"
            self.btnControlBarToggleEnabled.Parent = self.grpControlBar
            self.btnControlBarToggleEnabled.Left = 2
            self.btnControlBarToggleEnabled.Top = 242
            self.btnControlBarToggleEnabled.Width = 260
            self.btnControlBarToggleEnabled.Height = 25
            self.btnControlBarToggleEnabled.Cursor = crArrow
            self.btnControlBarToggleEnabled.Align = "alTop"
            self.btnControlBarToggleEnabled.Caption = 'Toggle Enabled'
            self.btnControlBarToggleEnabled.TabOrder = 1
            # Create control: btnControlBarToggleVisible = Button(self)
            self.btnControlBarToggleVisible = Button(self)
            self.btnControlBarToggleVisible.Name = "btnControlBarToggleVisible"
            self.btnControlBarToggleVisible.Parent = self.grpControlBar
            self.btnControlBarToggleVisible.Left = 2
            self.btnControlBarToggleVisible.Top = 267
            self.btnControlBarToggleVisible.Width = 260
            self.btnControlBarToggleVisible.Height = 25
            self.btnControlBarToggleVisible.Cursor = crArrow
            self.btnControlBarToggleVisible.Align = "alTop"
            self.btnControlBarToggleVisible.Caption = 'Toggle Visible'
            self.btnControlBarToggleVisible.TabOrder = 2
            # Create control: btnControlBarSetAlign = Button(self)
            self.btnControlBarSetAlign = Button(self)
            self.btnControlBarSetAlign.Name = "btnControlBarSetAlign"
            self.btnControlBarSetAlign.Parent = self.grpControlBar
            self.btnControlBarSetAlign.Left = 2
            self.btnControlBarSetAlign.Top = 217
            self.btnControlBarSetAlign.Width = 260
            self.btnControlBarSetAlign.Height = 25
            self.btnControlBarSetAlign.Cursor = crArrow
            self.btnControlBarSetAlign.Align = "alTop"
            self.btnControlBarSetAlign.Caption = 'Set Align'
            self.btnControlBarSetAlign.TabOrder = 3
            # Create control: btnControlBarSetMargins = Button(self)
            self.btnControlBarSetMargins = Button(self)
            self.btnControlBarSetMargins.Name = "btnControlBarSetMargins"
            self.btnControlBarSetMargins.Parent = self.grpControlBar
            self.btnControlBarSetMargins.Left = 2
            self.btnControlBarSetMargins.Top = 292
            self.btnControlBarSetMargins.Width = 260
            self.btnControlBarSetMargins.Height = 25
            self.btnControlBarSetMargins.Cursor = crArrow
            self.btnControlBarSetMargins.Align = "alTop"
            self.btnControlBarSetMargins.Caption = 'Set Margins'
            self.btnControlBarSetMargins.TabOrder = 4
            # Create control: btnControlBarSetBevelKind = Button(self)
            self.btnControlBarSetBevelKind = Button(self)
            self.btnControlBarSetBevelKind.Name = "btnControlBarSetBevelKind"
            self.btnControlBarSetBevelKind.Parent = self.grpControlBar
            self.btnControlBarSetBevelKind.Left = 2
            self.btnControlBarSetBevelKind.Top = 67
            self.btnControlBarSetBevelKind.Width = 260
            self.btnControlBarSetBevelKind.Height = 25
            self.btnControlBarSetBevelKind.Cursor = crArrow
            self.btnControlBarSetBevelKind.Align = "alTop"
            self.btnControlBarSetBevelKind.Caption = 'Set BevelKind'
            self.btnControlBarSetBevelKind.TabOrder = 5
            # Create control: btnControlBarSetPicture = Button(self)
            self.btnControlBarSetPicture = Button(self)
            self.btnControlBarSetPicture.Name = "btnControlBarSetPicture"
            self.btnControlBarSetPicture.Parent = self.grpControlBar
            self.btnControlBarSetPicture.Left = 2
            self.btnControlBarSetPicture.Top = 17
            self.btnControlBarSetPicture.Width = 260
            self.btnControlBarSetPicture.Height = 25
            self.btnControlBarSetPicture.Cursor = crArrow
            self.btnControlBarSetPicture.Align = "alTop"
            self.btnControlBarSetPicture.Caption = 'Set Picture'
            self.btnControlBarSetPicture.TabOrder = 6
            # Create control: btnControlBarSetBevelInner = Button(self)
            self.btnControlBarSetBevelInner = Button(self)
            self.btnControlBarSetBevelInner.Name = "btnControlBarSetBevelInner"
            self.btnControlBarSetBevelInner.Parent = self.grpControlBar
            self.btnControlBarSetBevelInner.Left = 2
            self.btnControlBarSetBevelInner.Top = 42
            self.btnControlBarSetBevelInner.Width = 260
            self.btnControlBarSetBevelInner.Height = 25
            self.btnControlBarSetBevelInner.Cursor = crArrow
            self.btnControlBarSetBevelInner.Align = "alTop"
            self.btnControlBarSetBevelInner.Caption = 'Set BevelInner'
            self.btnControlBarSetBevelInner.TabOrder = 7
            # Create control: btnControlBarSetAutoSize = Button(self)
            self.btnControlBarSetAutoSize = Button(self)
            self.btnControlBarSetAutoSize.Name = "btnControlBarSetAutoSize"
            self.btnControlBarSetAutoSize.Parent = self.grpControlBar
            self.btnControlBarSetAutoSize.Left = 2
            self.btnControlBarSetAutoSize.Top = 167
            self.btnControlBarSetAutoSize.Width = 260
            self.btnControlBarSetAutoSize.Height = 25
            self.btnControlBarSetAutoSize.Cursor = crArrow
            self.btnControlBarSetAutoSize.Align = "alTop"
            self.btnControlBarSetAutoSize.Caption = 'Set AutoSize'
            self.btnControlBarSetAutoSize.TabOrder = 8
            # Create control: btnControlBarSetColor = Button(self)
            self.btnControlBarSetColor = Button(self)
            self.btnControlBarSetColor.Name = "btnControlBarSetColor"
            self.btnControlBarSetColor.Parent = self.grpControlBar
            self.btnControlBarSetColor.Left = 2
            self.btnControlBarSetColor.Top = 142
            self.btnControlBarSetColor.Width = 260
            self.btnControlBarSetColor.Height = 25
            self.btnControlBarSetColor.Cursor = crArrow
            self.btnControlBarSetColor.Margins.Left = 4
            self.btnControlBarSetColor.Margins.Top = 4
            self.btnControlBarSetColor.Margins.Right = 4
            self.btnControlBarSetColor.Margins.Bottom = 4
            self.btnControlBarSetColor.Align = "alTop"
            self.btnControlBarSetColor.Caption = 'Set Color'
            self.btnControlBarSetColor.TabOrder = 9
            # Create control: btnControlBarSetBorderWidth = Button(self)
            self.btnControlBarSetBorderWidth = Button(self)
            self.btnControlBarSetBorderWidth.Name = "btnControlBarSetBorderWidth"
            self.btnControlBarSetBorderWidth.Parent = self.grpControlBar
            self.btnControlBarSetBorderWidth.Left = 2
            self.btnControlBarSetBorderWidth.Top = 117
            self.btnControlBarSetBorderWidth.Width = 260
            self.btnControlBarSetBorderWidth.Height = 25
            self.btnControlBarSetBorderWidth.Cursor = crArrow
            self.btnControlBarSetBorderWidth.Margins.Left = 4
            self.btnControlBarSetBorderWidth.Margins.Top = 4
            self.btnControlBarSetBorderWidth.Margins.Right = 4
            self.btnControlBarSetBorderWidth.Margins.Bottom = 4
            self.btnControlBarSetBorderWidth.Align = "alTop"
            self.btnControlBarSetBorderWidth.Caption = 'Set BorderWidth'
            self.btnControlBarSetBorderWidth.TabOrder = 10
            # Create control: btnControlBarSetBevelOuter = Button(self)
            self.btnControlBarSetBevelOuter = Button(self)
            self.btnControlBarSetBevelOuter.Name = "btnControlBarSetBevelOuter"
            self.btnControlBarSetBevelOuter.Parent = self.grpControlBar
            self.btnControlBarSetBevelOuter.Left = 2
            self.btnControlBarSetBevelOuter.Top = 92
            self.btnControlBarSetBevelOuter.Width = 260
            self.btnControlBarSetBevelOuter.Height = 25
            self.btnControlBarSetBevelOuter.Cursor = crArrow
            self.btnControlBarSetBevelOuter.Margins.Left = 4
            self.btnControlBarSetBevelOuter.Margins.Top = 4
            self.btnControlBarSetBevelOuter.Margins.Right = 4
            self.btnControlBarSetBevelOuter.Margins.Bottom = 4
            self.btnControlBarSetBevelOuter.Align = "alTop"
            self.btnControlBarSetBevelOuter.Caption = 'Set BevelOuter'
            self.btnControlBarSetBevelOuter.TabOrder = 11
            # Create control: shtBoundLabel = TabSheet(self)
            self.shtBoundLabel = TabSheet(self)
            self.shtBoundLabel.Name = "shtBoundLabel"
            self.shtBoundLabel.PageControl = self.pgFeatures
            self.shtBoundLabel.Cursor = crArrow
            self.shtBoundLabel.Margins.Left = 4
            self.shtBoundLabel.Margins.Top = 4
            self.shtBoundLabel.Margins.Right = 4
            self.shtBoundLabel.Margins.Bottom = 4
            self.shtBoundLabel.Caption = 'Bound Label'
            # Create control: grpBoundLabel = GroupBox(self)
            self.grpBoundLabel = GroupBox(self)
            self.grpBoundLabel.Name = "grpBoundLabel"
            self.grpBoundLabel.Parent = self.shtBoundLabel
            self.grpBoundLabel.Left = 1123
            self.grpBoundLabel.Top = 0
            self.grpBoundLabel.Width = 264
            self.grpBoundLabel.Height = 308
            self.grpBoundLabel.Cursor = crArrow
            self.grpBoundLabel.Margins.Left = 4
            self.grpBoundLabel.Margins.Top = 4
            self.grpBoundLabel.Margins.Right = 4
            self.grpBoundLabel.Margins.Bottom = 4
            self.grpBoundLabel.Align = "alRight"
            self.grpBoundLabel.Caption = 'Control Usages'
            self.grpBoundLabel.TabOrder = 0
            # Create control: btnBoundLabelSetBounds = Button(self)
            self.btnBoundLabelSetBounds = Button(self)
            self.btnBoundLabelSetBounds.Name = "btnBoundLabelSetBounds"
            self.btnBoundLabelSetBounds.Parent = self.grpBoundLabel
            self.btnBoundLabelSetBounds.Left = 2
            self.btnBoundLabelSetBounds.Top = 92
            self.btnBoundLabelSetBounds.Width = 260
            self.btnBoundLabelSetBounds.Height = 25
            self.btnBoundLabelSetBounds.Cursor = crArrow
            self.btnBoundLabelSetBounds.Align = "alTop"
            self.btnBoundLabelSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnBoundLabelSetBounds.TabOrder = 0
            # Create control: Button271 = Button(self)
            self.Button271 = Button(self)
            self.Button271.Name = "Button271"
            self.Button271.Parent = self.grpBoundLabel
            self.Button271.Left = 2
            self.Button271.Top = 117
            self.Button271.Width = 260
            self.Button271.Height = 25
            self.Button271.Cursor = crArrow
            self.Button271.Align = "alTop"
            self.Button271.Caption = 'Toggle Enabled'
            self.Button271.TabOrder = 1
            # Create control: btnBoundLabelSetMargins = Button(self)
            self.btnBoundLabelSetMargins = Button(self)
            self.btnBoundLabelSetMargins.Name = "btnBoundLabelSetMargins"
            self.btnBoundLabelSetMargins.Parent = self.grpBoundLabel
            self.btnBoundLabelSetMargins.Left = 2
            self.btnBoundLabelSetMargins.Top = 142
            self.btnBoundLabelSetMargins.Width = 260
            self.btnBoundLabelSetMargins.Height = 25
            self.btnBoundLabelSetMargins.Cursor = crArrow
            self.btnBoundLabelSetMargins.Align = "alTop"
            self.btnBoundLabelSetMargins.Caption = 'Set Margins'
            self.btnBoundLabelSetMargins.TabOrder = 2
            # Create control: btnBoundLabelSetColor = Button(self)
            self.btnBoundLabelSetColor = Button(self)
            self.btnBoundLabelSetColor.Name = "btnBoundLabelSetColor"
            self.btnBoundLabelSetColor.Parent = self.grpBoundLabel
            self.btnBoundLabelSetColor.Left = 2
            self.btnBoundLabelSetColor.Top = 67
            self.btnBoundLabelSetColor.Width = 260
            self.btnBoundLabelSetColor.Height = 25
            self.btnBoundLabelSetColor.Cursor = crArrow
            self.btnBoundLabelSetColor.Align = "alTop"
            self.btnBoundLabelSetColor.Caption = 'Set Color'
            self.btnBoundLabelSetColor.TabOrder = 3
            # Create control: btnBoundLabelSetLayout = Button(self)
            self.btnBoundLabelSetLayout = Button(self)
            self.btnBoundLabelSetLayout.Name = "btnBoundLabelSetLayout"
            self.btnBoundLabelSetLayout.Parent = self.grpBoundLabel
            self.btnBoundLabelSetLayout.Left = 2
            self.btnBoundLabelSetLayout.Top = 17
            self.btnBoundLabelSetLayout.Width = 260
            self.btnBoundLabelSetLayout.Height = 25
            self.btnBoundLabelSetLayout.Cursor = crArrow
            self.btnBoundLabelSetLayout.Align = "alTop"
            self.btnBoundLabelSetLayout.Caption = 'Set Layout'
            self.btnBoundLabelSetLayout.TabOrder = 4
            # Create control: btnBoundLabelSetTransparent = Button(self)
            self.btnBoundLabelSetTransparent = Button(self)
            self.btnBoundLabelSetTransparent.Name = "btnBoundLabelSetTransparent"
            self.btnBoundLabelSetTransparent.Parent = self.grpBoundLabel
            self.btnBoundLabelSetTransparent.Left = 2
            self.btnBoundLabelSetTransparent.Top = 42
            self.btnBoundLabelSetTransparent.Width = 260
            self.btnBoundLabelSetTransparent.Height = 25
            self.btnBoundLabelSetTransparent.Cursor = crArrow
            self.btnBoundLabelSetTransparent.Align = "alTop"
            self.btnBoundLabelSetTransparent.Caption = 'Set Transparent'
            self.btnBoundLabelSetTransparent.TabOrder = 5
            # Create control: shtLabeledEdit = TabSheet(self)
            self.shtLabeledEdit = TabSheet(self)
            self.shtLabeledEdit.Name = "shtLabeledEdit"
            self.shtLabeledEdit.PageControl = self.pgFeatures
            self.shtLabeledEdit.Cursor = crArrow
            self.shtLabeledEdit.Margins.Left = 4
            self.shtLabeledEdit.Margins.Top = 4
            self.shtLabeledEdit.Margins.Right = 4
            self.shtLabeledEdit.Margins.Bottom = 4
            self.shtLabeledEdit.Caption = 'Labeled Edit'
            # Create control: leLabeledEdit = LabeledEdit(self)
            self.leLabeledEdit = LabeledEdit(self)
            self.leLabeledEdit.Name = "leLabeledEdit"
            self.leLabeledEdit.Parent = self.shtLabeledEdit
            self.leLabeledEdit.Left = 160
            self.leLabeledEdit.Top = 96
            self.leLabeledEdit.Width = 121
            self.leLabeledEdit.Height = 23
            self.leLabeledEdit.Cursor = crArrow
            self.leLabeledEdit.Margins.Left = 4
            self.leLabeledEdit.Margins.Top = 4
            self.leLabeledEdit.Margins.Right = 4
            self.leLabeledEdit.Margins.Bottom = 4
            self.leLabeledEdit.EditLabel.Width = 3
            self.leLabeledEdit.EditLabel.Height = 15
            self.leLabeledEdit.EditLabel.Margins.Left = 4
            self.leLabeledEdit.EditLabel.Margins.Top = 4
            self.leLabeledEdit.EditLabel.Margins.Right = 4
            self.leLabeledEdit.EditLabel.Margins.Bottom = 4
            self.leLabeledEdit.TabOrder = 0
            self.leLabeledEdit.Text = 'leLabeledEdit'
            # Create control: grpLabeledEdit = GroupBox(self)
            self.grpLabeledEdit = GroupBox(self)
            self.grpLabeledEdit.Name = "grpLabeledEdit"
            self.grpLabeledEdit.Parent = self.shtLabeledEdit
            self.grpLabeledEdit.Left = 1123
            self.grpLabeledEdit.Top = 0
            self.grpLabeledEdit.Width = 264
            self.grpLabeledEdit.Height = 308
            self.grpLabeledEdit.Cursor = crArrow
            self.grpLabeledEdit.Margins.Left = 4
            self.grpLabeledEdit.Margins.Top = 4
            self.grpLabeledEdit.Margins.Right = 4
            self.grpLabeledEdit.Margins.Bottom = 4
            self.grpLabeledEdit.Align = "alRight"
            self.grpLabeledEdit.Caption = 'Control Usages'
            self.grpLabeledEdit.TabOrder = 1
            # Create control: btnLabeledEditSetBounds = Button(self)
            self.btnLabeledEditSetBounds = Button(self)
            self.btnLabeledEditSetBounds.Name = "btnLabeledEditSetBounds"
            self.btnLabeledEditSetBounds.Parent = self.grpLabeledEdit
            self.btnLabeledEditSetBounds.Left = 2
            self.btnLabeledEditSetBounds.Top = 167
            self.btnLabeledEditSetBounds.Width = 260
            self.btnLabeledEditSetBounds.Height = 25
            self.btnLabeledEditSetBounds.Cursor = crArrow
            self.btnLabeledEditSetBounds.Align = "alTop"
            self.btnLabeledEditSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnLabeledEditSetBounds.TabOrder = 0
            # Create control: btnLabeledEditToggleEnabled = Button(self)
            self.btnLabeledEditToggleEnabled = Button(self)
            self.btnLabeledEditToggleEnabled.Name = "btnLabeledEditToggleEnabled"
            self.btnLabeledEditToggleEnabled.Parent = self.grpLabeledEdit
            self.btnLabeledEditToggleEnabled.Left = 2
            self.btnLabeledEditToggleEnabled.Top = 192
            self.btnLabeledEditToggleEnabled.Width = 260
            self.btnLabeledEditToggleEnabled.Height = 25
            self.btnLabeledEditToggleEnabled.Cursor = crArrow
            self.btnLabeledEditToggleEnabled.Align = "alTop"
            self.btnLabeledEditToggleEnabled.Caption = 'Toggle Enabled'
            self.btnLabeledEditToggleEnabled.TabOrder = 1
            # Create control: btnLabeledEditToggleVisible = Button(self)
            self.btnLabeledEditToggleVisible = Button(self)
            self.btnLabeledEditToggleVisible.Name = "btnLabeledEditToggleVisible"
            self.btnLabeledEditToggleVisible.Parent = self.grpLabeledEdit
            self.btnLabeledEditToggleVisible.Left = 2
            self.btnLabeledEditToggleVisible.Top = 217
            self.btnLabeledEditToggleVisible.Width = 260
            self.btnLabeledEditToggleVisible.Height = 25
            self.btnLabeledEditToggleVisible.Cursor = crArrow
            self.btnLabeledEditToggleVisible.Align = "alTop"
            self.btnLabeledEditToggleVisible.Caption = 'Toggle Visible'
            self.btnLabeledEditToggleVisible.TabOrder = 2
            # Create control: btnLabeledEditSetAlign = Button(self)
            self.btnLabeledEditSetAlign = Button(self)
            self.btnLabeledEditSetAlign.Name = "btnLabeledEditSetAlign"
            self.btnLabeledEditSetAlign.Parent = self.grpLabeledEdit
            self.btnLabeledEditSetAlign.Left = 2
            self.btnLabeledEditSetAlign.Top = 242
            self.btnLabeledEditSetAlign.Width = 260
            self.btnLabeledEditSetAlign.Height = 25
            self.btnLabeledEditSetAlign.Cursor = crArrow
            self.btnLabeledEditSetAlign.Align = "alTop"
            self.btnLabeledEditSetAlign.Caption = 'Set Align'
            self.btnLabeledEditSetAlign.TabOrder = 3
            # Create control: btnLabeledEditSetMargins = Button(self)
            self.btnLabeledEditSetMargins = Button(self)
            self.btnLabeledEditSetMargins.Name = "btnLabeledEditSetMargins"
            self.btnLabeledEditSetMargins.Parent = self.grpLabeledEdit
            self.btnLabeledEditSetMargins.Left = 2
            self.btnLabeledEditSetMargins.Top = 267
            self.btnLabeledEditSetMargins.Width = 260
            self.btnLabeledEditSetMargins.Height = 25
            self.btnLabeledEditSetMargins.Cursor = crArrow
            self.btnLabeledEditSetMargins.Align = "alTop"
            self.btnLabeledEditSetMargins.Caption = 'Set Margins'
            self.btnLabeledEditSetMargins.TabOrder = 4
            # Create control: btnLabeledEditSetColor = Button(self)
            self.btnLabeledEditSetColor = Button(self)
            self.btnLabeledEditSetColor.Name = "btnLabeledEditSetColor"
            self.btnLabeledEditSetColor.Parent = self.grpLabeledEdit
            self.btnLabeledEditSetColor.Left = 2
            self.btnLabeledEditSetColor.Top = 117
            self.btnLabeledEditSetColor.Width = 260
            self.btnLabeledEditSetColor.Height = 25
            self.btnLabeledEditSetColor.Cursor = crArrow
            self.btnLabeledEditSetColor.Align = "alTop"
            self.btnLabeledEditSetColor.Caption = 'Set Color'
            self.btnLabeledEditSetColor.TabOrder = 5
            # Create control: btnLabeledEditSetBorderStyle = Button(self)
            self.btnLabeledEditSetBorderStyle = Button(self)
            self.btnLabeledEditSetBorderStyle.Name = "btnLabeledEditSetBorderStyle"
            self.btnLabeledEditSetBorderStyle.Parent = self.grpLabeledEdit
            self.btnLabeledEditSetBorderStyle.Left = 2
            self.btnLabeledEditSetBorderStyle.Top = 67
            self.btnLabeledEditSetBorderStyle.Width = 260
            self.btnLabeledEditSetBorderStyle.Height = 25
            self.btnLabeledEditSetBorderStyle.Cursor = crArrow
            self.btnLabeledEditSetBorderStyle.Align = "alTop"
            self.btnLabeledEditSetBorderStyle.Caption = 'Set BorderStyle'
            self.btnLabeledEditSetBorderStyle.TabOrder = 6
            # Create control: btnLabeledEditSetCharCase = Button(self)
            self.btnLabeledEditSetCharCase = Button(self)
            self.btnLabeledEditSetCharCase.Name = "btnLabeledEditSetCharCase"
            self.btnLabeledEditSetCharCase.Parent = self.grpLabeledEdit
            self.btnLabeledEditSetCharCase.Left = 2
            self.btnLabeledEditSetCharCase.Top = 92
            self.btnLabeledEditSetCharCase.Width = 260
            self.btnLabeledEditSetCharCase.Height = 25
            self.btnLabeledEditSetCharCase.Cursor = crArrow
            self.btnLabeledEditSetCharCase.Align = "alTop"
            self.btnLabeledEditSetCharCase.Caption = 'Set CharCase'
            self.btnLabeledEditSetCharCase.TabOrder = 7
            # Create control: btnLabeledEditSetText = Button(self)
            self.btnLabeledEditSetText = Button(self)
            self.btnLabeledEditSetText.Name = "btnLabeledEditSetText"
            self.btnLabeledEditSetText.Parent = self.grpLabeledEdit
            self.btnLabeledEditSetText.Left = 2
            self.btnLabeledEditSetText.Top = 142
            self.btnLabeledEditSetText.Width = 260
            self.btnLabeledEditSetText.Height = 25
            self.btnLabeledEditSetText.Cursor = crArrow
            self.btnLabeledEditSetText.Align = "alTop"
            self.btnLabeledEditSetText.Caption = 'Set Text'
            self.btnLabeledEditSetText.TabOrder = 8
            # Create control: btnLabeledEditSetBevelKind = Button(self)
            self.btnLabeledEditSetBevelKind = Button(self)
            self.btnLabeledEditSetBevelKind.Name = "btnLabeledEditSetBevelKind"
            self.btnLabeledEditSetBevelKind.Parent = self.grpLabeledEdit
            self.btnLabeledEditSetBevelKind.Left = 2
            self.btnLabeledEditSetBevelKind.Top = 42
            self.btnLabeledEditSetBevelKind.Width = 260
            self.btnLabeledEditSetBevelKind.Height = 25
            self.btnLabeledEditSetBevelKind.Cursor = crArrow
            self.btnLabeledEditSetBevelKind.Margins.Left = 4
            self.btnLabeledEditSetBevelKind.Margins.Top = 4
            self.btnLabeledEditSetBevelKind.Margins.Right = 4
            self.btnLabeledEditSetBevelKind.Margins.Bottom = 4
            self.btnLabeledEditSetBevelKind.Align = "alTop"
            self.btnLabeledEditSetBevelKind.Caption = 'Set BevelKind'
            self.btnLabeledEditSetBevelKind.TabOrder = 9
            # Create control: btnLabeledEditSetAlignment = Button(self)
            self.btnLabeledEditSetAlignment = Button(self)
            self.btnLabeledEditSetAlignment.Name = "btnLabeledEditSetAlignment"
            self.btnLabeledEditSetAlignment.Parent = self.grpLabeledEdit
            self.btnLabeledEditSetAlignment.Left = 2
            self.btnLabeledEditSetAlignment.Top = 17
            self.btnLabeledEditSetAlignment.Width = 260
            self.btnLabeledEditSetAlignment.Height = 25
            self.btnLabeledEditSetAlignment.Cursor = crArrow
            self.btnLabeledEditSetAlignment.Margins.Left = 4
            self.btnLabeledEditSetAlignment.Margins.Top = 4
            self.btnLabeledEditSetAlignment.Margins.Right = 4
            self.btnLabeledEditSetAlignment.Margins.Bottom = 4
            self.btnLabeledEditSetAlignment.Align = "alTop"
            self.btnLabeledEditSetAlignment.Caption = 'Set Alignment'
            self.btnLabeledEditSetAlignment.TabOrder = 10
            # Create control: shtColorBox = TabSheet(self)
            self.shtColorBox = TabSheet(self)
            self.shtColorBox.Name = "shtColorBox"
            self.shtColorBox.PageControl = self.pgFeatures
            self.shtColorBox.Cursor = crArrow
            self.shtColorBox.Margins.Left = 4
            self.shtColorBox.Margins.Top = 4
            self.shtColorBox.Margins.Right = 4
            self.shtColorBox.Margins.Bottom = 4
            self.shtColorBox.Caption = 'Color Box'
            # Create control: ColorBox = ColorBox(self)
            self.ColorBox = ColorBox(self)
            self.ColorBox.Name = "ColorBox"
            self.ColorBox.Parent = self.shtColorBox
            self.ColorBox.Left = 144
            self.ColorBox.Top = 96
            self.ColorBox.Width = 145
            self.ColorBox.Height = 36
            self.ColorBox.Cursor = crArrow
            self.ColorBox.Margins.Left = 4
            self.ColorBox.Margins.Top = 4
            self.ColorBox.Margins.Right = 4
            self.ColorBox.Margins.Bottom = 4
            self.ColorBox.ItemHeight = 20
            self.ColorBox.TabOrder = 0
            # Create control: grpColorBox = GroupBox(self)
            self.grpColorBox = GroupBox(self)
            self.grpColorBox.Name = "grpColorBox"
            self.grpColorBox.Parent = self.shtColorBox
            self.grpColorBox.Left = 1123
            self.grpColorBox.Top = 0
            self.grpColorBox.Width = 264
            self.grpColorBox.Height = 308
            self.grpColorBox.Cursor = crArrow
            self.grpColorBox.Margins.Left = 4
            self.grpColorBox.Margins.Top = 4
            self.grpColorBox.Margins.Right = 4
            self.grpColorBox.Margins.Bottom = 4
            self.grpColorBox.Align = "alRight"
            self.grpColorBox.Caption = 'Control Usages'
            self.grpColorBox.TabOrder = 1
            # Create control: btnColorBoxSetBounds = Button(self)
            self.btnColorBoxSetBounds = Button(self)
            self.btnColorBoxSetBounds.Name = "btnColorBoxSetBounds"
            self.btnColorBoxSetBounds.Parent = self.grpColorBox
            self.btnColorBoxSetBounds.Left = 2
            self.btnColorBoxSetBounds.Top = 117
            self.btnColorBoxSetBounds.Width = 260
            self.btnColorBoxSetBounds.Height = 25
            self.btnColorBoxSetBounds.Cursor = crArrow
            self.btnColorBoxSetBounds.Align = "alTop"
            self.btnColorBoxSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnColorBoxSetBounds.TabOrder = 0
            # Create control: btnColorBoxToggleEnabled = Button(self)
            self.btnColorBoxToggleEnabled = Button(self)
            self.btnColorBoxToggleEnabled.Name = "btnColorBoxToggleEnabled"
            self.btnColorBoxToggleEnabled.Parent = self.grpColorBox
            self.btnColorBoxToggleEnabled.Left = 2
            self.btnColorBoxToggleEnabled.Top = 142
            self.btnColorBoxToggleEnabled.Width = 260
            self.btnColorBoxToggleEnabled.Height = 25
            self.btnColorBoxToggleEnabled.Cursor = crArrow
            self.btnColorBoxToggleEnabled.Align = "alTop"
            self.btnColorBoxToggleEnabled.Caption = 'Toggle Enabled'
            self.btnColorBoxToggleEnabled.TabOrder = 1
            # Create control: btnColorBoxToggleVisible = Button(self)
            self.btnColorBoxToggleVisible = Button(self)
            self.btnColorBoxToggleVisible.Name = "btnColorBoxToggleVisible"
            self.btnColorBoxToggleVisible.Parent = self.grpColorBox
            self.btnColorBoxToggleVisible.Left = 2
            self.btnColorBoxToggleVisible.Top = 167
            self.btnColorBoxToggleVisible.Width = 260
            self.btnColorBoxToggleVisible.Height = 25
            self.btnColorBoxToggleVisible.Cursor = crArrow
            self.btnColorBoxToggleVisible.Align = "alTop"
            self.btnColorBoxToggleVisible.Caption = 'Toggle Visible'
            self.btnColorBoxToggleVisible.TabOrder = 2
            # Create control: btnColorBoxSetAlign = Button(self)
            self.btnColorBoxSetAlign = Button(self)
            self.btnColorBoxSetAlign.Name = "btnColorBoxSetAlign"
            self.btnColorBoxSetAlign.Parent = self.grpColorBox
            self.btnColorBoxSetAlign.Left = 2
            self.btnColorBoxSetAlign.Top = 192
            self.btnColorBoxSetAlign.Width = 260
            self.btnColorBoxSetAlign.Height = 25
            self.btnColorBoxSetAlign.Cursor = crArrow
            self.btnColorBoxSetAlign.Align = "alTop"
            self.btnColorBoxSetAlign.Caption = 'Set Align'
            self.btnColorBoxSetAlign.TabOrder = 3
            # Create control: btnColorBoxSetMargins = Button(self)
            self.btnColorBoxSetMargins = Button(self)
            self.btnColorBoxSetMargins.Name = "btnColorBoxSetMargins"
            self.btnColorBoxSetMargins.Parent = self.grpColorBox
            self.btnColorBoxSetMargins.Left = 2
            self.btnColorBoxSetMargins.Top = 217
            self.btnColorBoxSetMargins.Width = 260
            self.btnColorBoxSetMargins.Height = 25
            self.btnColorBoxSetMargins.Cursor = crArrow
            self.btnColorBoxSetMargins.Align = "alTop"
            self.btnColorBoxSetMargins.Caption = 'Set Margins'
            self.btnColorBoxSetMargins.TabOrder = 4
            # Create control: btnColorBoxSetColor = Button(self)
            self.btnColorBoxSetColor = Button(self)
            self.btnColorBoxSetColor.Name = "btnColorBoxSetColor"
            self.btnColorBoxSetColor.Parent = self.grpColorBox
            self.btnColorBoxSetColor.Left = 2
            self.btnColorBoxSetColor.Top = 67
            self.btnColorBoxSetColor.Width = 260
            self.btnColorBoxSetColor.Height = 25
            self.btnColorBoxSetColor.Cursor = crArrow
            self.btnColorBoxSetColor.Align = "alTop"
            self.btnColorBoxSetColor.Caption = 'Set Color'
            self.btnColorBoxSetColor.TabOrder = 5
            # Create control: btnColorBoxSetBevelKind = Button(self)
            self.btnColorBoxSetBevelKind = Button(self)
            self.btnColorBoxSetBevelKind.Name = "btnColorBoxSetBevelKind"
            self.btnColorBoxSetBevelKind.Parent = self.grpColorBox
            self.btnColorBoxSetBevelKind.Left = 2
            self.btnColorBoxSetBevelKind.Top = 17
            self.btnColorBoxSetBevelKind.Width = 260
            self.btnColorBoxSetBevelKind.Height = 25
            self.btnColorBoxSetBevelKind.Cursor = crArrow
            self.btnColorBoxSetBevelKind.Align = "alTop"
            self.btnColorBoxSetBevelKind.Caption = 'Set BevelKind'
            self.btnColorBoxSetBevelKind.TabOrder = 6
            # Create control: btnColorBoxSetBiDiMode = Button(self)
            self.btnColorBoxSetBiDiMode = Button(self)
            self.btnColorBoxSetBiDiMode.Name = "btnColorBoxSetBiDiMode"
            self.btnColorBoxSetBiDiMode.Parent = self.grpColorBox
            self.btnColorBoxSetBiDiMode.Left = 2
            self.btnColorBoxSetBiDiMode.Top = 42
            self.btnColorBoxSetBiDiMode.Width = 260
            self.btnColorBoxSetBiDiMode.Height = 25
            self.btnColorBoxSetBiDiMode.Cursor = crArrow
            self.btnColorBoxSetBiDiMode.Align = "alTop"
            self.btnColorBoxSetBiDiMode.Caption = 'Set BiDiMode'
            self.btnColorBoxSetBiDiMode.TabOrder = 7
            # Create control: btnColorBoxSetSelected = Button(self)
            self.btnColorBoxSetSelected = Button(self)
            self.btnColorBoxSetSelected.Name = "btnColorBoxSetSelected"
            self.btnColorBoxSetSelected.Parent = self.grpColorBox
            self.btnColorBoxSetSelected.Left = 2
            self.btnColorBoxSetSelected.Top = 92
            self.btnColorBoxSetSelected.Width = 260
            self.btnColorBoxSetSelected.Height = 25
            self.btnColorBoxSetSelected.Cursor = crArrow
            self.btnColorBoxSetSelected.Align = "alTop"
            self.btnColorBoxSetSelected.Caption = 'Set Selected'
            self.btnColorBoxSetSelected.TabOrder = 8
            # Create control: shtSpeedButton = TabSheet(self)
            self.shtSpeedButton = TabSheet(self)
            self.shtSpeedButton.Name = "shtSpeedButton"
            self.shtSpeedButton.PageControl = self.pgFeatures
            self.shtSpeedButton.Cursor = crArrow
            self.shtSpeedButton.Margins.Left = 4
            self.shtSpeedButton.Margins.Top = 4
            self.shtSpeedButton.Margins.Right = 4
            self.shtSpeedButton.Margins.Bottom = 4
            self.shtSpeedButton.Caption = 'Speed Button'
            # Create control: SpeedButton = TSSpeedButton(self)
            self.SpeedButton = TSSpeedButton(self)
            self.SpeedButton.Name = "SpeedButton"
            self.SpeedButton.Parent = self.shtSpeedButton
            self.SpeedButton.Left = 280
            self.SpeedButton.Top = 128
            self.SpeedButton.Width = 136
            self.SpeedButton.Height = 32
            self.SpeedButton.Cursor = crArrow
            self.SpeedButton.Margins.Left = 4
            self.SpeedButton.Margins.Top = 4
            self.SpeedButton.Margins.Right = 4
            self.SpeedButton.Margins.Bottom = 4
            self.SpeedButton.Caption = 'SpeedButton'
            self.SpeedButton.Images = app.get_system_imagelist_16px()
            # Create control: grpSpeedButton = GroupBox(self)
            self.grpSpeedButton = GroupBox(self)
            self.grpSpeedButton.Name = "grpSpeedButton"
            self.grpSpeedButton.Parent = self.shtSpeedButton
            self.grpSpeedButton.Left = 1123
            self.grpSpeedButton.Top = 0
            self.grpSpeedButton.Width = 264
            self.grpSpeedButton.Height = 308
            self.grpSpeedButton.Cursor = crArrow
            self.grpSpeedButton.Margins.Left = 4
            self.grpSpeedButton.Margins.Top = 4
            self.grpSpeedButton.Margins.Right = 4
            self.grpSpeedButton.Margins.Bottom = 4
            self.grpSpeedButton.Align = "alRight"
            self.grpSpeedButton.Caption = 'Control Usages'
            self.grpSpeedButton.TabOrder = 0
            # Create control: btnSpeedButtonSetBounds = Button(self)
            self.btnSpeedButtonSetBounds = Button(self)
            self.btnSpeedButtonSetBounds.Name = "btnSpeedButtonSetBounds"
            self.btnSpeedButtonSetBounds.Parent = self.grpSpeedButton
            self.btnSpeedButtonSetBounds.Left = 2
            self.btnSpeedButtonSetBounds.Top = 92
            self.btnSpeedButtonSetBounds.Width = 260
            self.btnSpeedButtonSetBounds.Height = 25
            self.btnSpeedButtonSetBounds.Cursor = crArrow
            self.btnSpeedButtonSetBounds.Align = "alTop"
            self.btnSpeedButtonSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnSpeedButtonSetBounds.TabOrder = 0
            # Create control: btnSpeedButtonToggleEnabled = Button(self)
            self.btnSpeedButtonToggleEnabled = Button(self)
            self.btnSpeedButtonToggleEnabled.Name = "btnSpeedButtonToggleEnabled"
            self.btnSpeedButtonToggleEnabled.Parent = self.grpSpeedButton
            self.btnSpeedButtonToggleEnabled.Left = 2
            self.btnSpeedButtonToggleEnabled.Top = 117
            self.btnSpeedButtonToggleEnabled.Width = 260
            self.btnSpeedButtonToggleEnabled.Height = 25
            self.btnSpeedButtonToggleEnabled.Cursor = crArrow
            self.btnSpeedButtonToggleEnabled.Align = "alTop"
            self.btnSpeedButtonToggleEnabled.Caption = 'Toggle Enabled'
            self.btnSpeedButtonToggleEnabled.TabOrder = 1
            # Create control: btnSpeedButtonToggleVisible = Button(self)
            self.btnSpeedButtonToggleVisible = Button(self)
            self.btnSpeedButtonToggleVisible.Name = "btnSpeedButtonToggleVisible"
            self.btnSpeedButtonToggleVisible.Parent = self.grpSpeedButton
            self.btnSpeedButtonToggleVisible.Left = 2
            self.btnSpeedButtonToggleVisible.Top = 142
            self.btnSpeedButtonToggleVisible.Width = 260
            self.btnSpeedButtonToggleVisible.Height = 25
            self.btnSpeedButtonToggleVisible.Cursor = crArrow
            self.btnSpeedButtonToggleVisible.Align = "alTop"
            self.btnSpeedButtonToggleVisible.Caption = 'Toggle Visible'
            self.btnSpeedButtonToggleVisible.TabOrder = 2
            # Create control: btnSpeedButtonSetAlign = Button(self)
            self.btnSpeedButtonSetAlign = Button(self)
            self.btnSpeedButtonSetAlign.Name = "btnSpeedButtonSetAlign"
            self.btnSpeedButtonSetAlign.Parent = self.grpSpeedButton
            self.btnSpeedButtonSetAlign.Left = 2
            self.btnSpeedButtonSetAlign.Top = 167
            self.btnSpeedButtonSetAlign.Width = 260
            self.btnSpeedButtonSetAlign.Height = 25
            self.btnSpeedButtonSetAlign.Cursor = crArrow
            self.btnSpeedButtonSetAlign.Align = "alTop"
            self.btnSpeedButtonSetAlign.Caption = 'Set Align'
            self.btnSpeedButtonSetAlign.TabOrder = 3
            # Create control: btnSpeedButtonSetMargins = Button(self)
            self.btnSpeedButtonSetMargins = Button(self)
            self.btnSpeedButtonSetMargins.Name = "btnSpeedButtonSetMargins"
            self.btnSpeedButtonSetMargins.Parent = self.grpSpeedButton
            self.btnSpeedButtonSetMargins.Left = 2
            self.btnSpeedButtonSetMargins.Top = 192
            self.btnSpeedButtonSetMargins.Width = 260
            self.btnSpeedButtonSetMargins.Height = 25
            self.btnSpeedButtonSetMargins.Cursor = crArrow
            self.btnSpeedButtonSetMargins.Align = "alTop"
            self.btnSpeedButtonSetMargins.Caption = 'Set Margins'
            self.btnSpeedButtonSetMargins.TabOrder = 4
            # Create control: btnSpeedButtonSetLayout = Button(self)
            self.btnSpeedButtonSetLayout = Button(self)
            self.btnSpeedButtonSetLayout.Name = "btnSpeedButtonSetLayout"
            self.btnSpeedButtonSetLayout.Parent = self.grpSpeedButton
            self.btnSpeedButtonSetLayout.Left = 2
            self.btnSpeedButtonSetLayout.Top = 42
            self.btnSpeedButtonSetLayout.Width = 260
            self.btnSpeedButtonSetLayout.Height = 25
            self.btnSpeedButtonSetLayout.Cursor = crArrow
            self.btnSpeedButtonSetLayout.Align = "alTop"
            self.btnSpeedButtonSetLayout.Caption = 'Set Layout'
            self.btnSpeedButtonSetLayout.TabOrder = 5
            # Create control: btnSpeedButtonSetGlyph = Button(self)
            self.btnSpeedButtonSetGlyph = Button(self)
            self.btnSpeedButtonSetGlyph.Name = "btnSpeedButtonSetGlyph"
            self.btnSpeedButtonSetGlyph.Parent = self.grpSpeedButton
            self.btnSpeedButtonSetGlyph.Left = 2
            self.btnSpeedButtonSetGlyph.Top = 17
            self.btnSpeedButtonSetGlyph.Width = 260
            self.btnSpeedButtonSetGlyph.Height = 25
            self.btnSpeedButtonSetGlyph.Cursor = crArrow
            self.btnSpeedButtonSetGlyph.Align = "alTop"
            self.btnSpeedButtonSetGlyph.Caption = 'Set Glyph'
            self.btnSpeedButtonSetGlyph.TabOrder = 6
            # Create control: btnSpeedButtonSetFlat = Button(self)
            self.btnSpeedButtonSetFlat = Button(self)
            self.btnSpeedButtonSetFlat.Name = "btnSpeedButtonSetFlat"
            self.btnSpeedButtonSetFlat.Parent = self.grpSpeedButton
            self.btnSpeedButtonSetFlat.Left = 2
            self.btnSpeedButtonSetFlat.Top = 67
            self.btnSpeedButtonSetFlat.Width = 260
            self.btnSpeedButtonSetFlat.Height = 25
            self.btnSpeedButtonSetFlat.Cursor = crArrow
            self.btnSpeedButtonSetFlat.Align = "alTop"
            self.btnSpeedButtonSetFlat.Caption = 'Set Flat'
            self.btnSpeedButtonSetFlat.TabOrder = 7
            # Create control: shtBitBtn = TabSheet(self)
            self.shtBitBtn = TabSheet(self)
            self.shtBitBtn.Name = "shtBitBtn"
            self.shtBitBtn.PageControl = self.pgFeatures
            self.shtBitBtn.Cursor = crArrow
            self.shtBitBtn.Margins.Left = 4
            self.shtBitBtn.Margins.Top = 4
            self.shtBitBtn.Margins.Right = 4
            self.shtBitBtn.Margins.Bottom = 4
            self.shtBitBtn.Caption = 'Bit Btn'
            # Create control: grpBitBtn = GroupBox(self)
            self.grpBitBtn = GroupBox(self)
            self.grpBitBtn.Name = "grpBitBtn"
            self.grpBitBtn.Parent = self.shtBitBtn
            self.grpBitBtn.Left = 1123
            self.grpBitBtn.Top = 0
            self.grpBitBtn.Width = 264
            self.grpBitBtn.Height = 308
            self.grpBitBtn.Cursor = crArrow
            self.grpBitBtn.Margins.Left = 4
            self.grpBitBtn.Margins.Top = 4
            self.grpBitBtn.Margins.Right = 4
            self.grpBitBtn.Margins.Bottom = 4
            self.grpBitBtn.Align = "alRight"
            self.grpBitBtn.Caption = 'Control Usages'
            self.grpBitBtn.TabOrder = 0
            # Create control: btnBitBtnSetBounds = Button(self)
            self.btnBitBtnSetBounds = Button(self)
            self.btnBitBtnSetBounds.Name = "btnBitBtnSetBounds"
            self.btnBitBtnSetBounds.Parent = self.grpBitBtn
            self.btnBitBtnSetBounds.Left = 2
            self.btnBitBtnSetBounds.Top = 92
            self.btnBitBtnSetBounds.Width = 260
            self.btnBitBtnSetBounds.Height = 25
            self.btnBitBtnSetBounds.Cursor = crArrow
            self.btnBitBtnSetBounds.Align = "alTop"
            self.btnBitBtnSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnBitBtnSetBounds.TabOrder = 0
            # Create control: btnBitBtnToggleEnabled = Button(self)
            self.btnBitBtnToggleEnabled = Button(self)
            self.btnBitBtnToggleEnabled.Name = "btnBitBtnToggleEnabled"
            self.btnBitBtnToggleEnabled.Parent = self.grpBitBtn
            self.btnBitBtnToggleEnabled.Left = 2
            self.btnBitBtnToggleEnabled.Top = 117
            self.btnBitBtnToggleEnabled.Width = 260
            self.btnBitBtnToggleEnabled.Height = 25
            self.btnBitBtnToggleEnabled.Cursor = crArrow
            self.btnBitBtnToggleEnabled.Align = "alTop"
            self.btnBitBtnToggleEnabled.Caption = 'Toggle Enabled'
            self.btnBitBtnToggleEnabled.TabOrder = 1
            # Create control: btnBitBtnToggleVisible = Button(self)
            self.btnBitBtnToggleVisible = Button(self)
            self.btnBitBtnToggleVisible.Name = "btnBitBtnToggleVisible"
            self.btnBitBtnToggleVisible.Parent = self.grpBitBtn
            self.btnBitBtnToggleVisible.Left = 2
            self.btnBitBtnToggleVisible.Top = 142
            self.btnBitBtnToggleVisible.Width = 260
            self.btnBitBtnToggleVisible.Height = 25
            self.btnBitBtnToggleVisible.Cursor = crArrow
            self.btnBitBtnToggleVisible.Align = "alTop"
            self.btnBitBtnToggleVisible.Caption = 'Toggle Visible'
            self.btnBitBtnToggleVisible.TabOrder = 2
            # Create control: btnBitBtnSetAlign = Button(self)
            self.btnBitBtnSetAlign = Button(self)
            self.btnBitBtnSetAlign.Name = "btnBitBtnSetAlign"
            self.btnBitBtnSetAlign.Parent = self.grpBitBtn
            self.btnBitBtnSetAlign.Left = 2
            self.btnBitBtnSetAlign.Top = 167
            self.btnBitBtnSetAlign.Width = 260
            self.btnBitBtnSetAlign.Height = 25
            self.btnBitBtnSetAlign.Cursor = crArrow
            self.btnBitBtnSetAlign.Align = "alTop"
            self.btnBitBtnSetAlign.Caption = 'Set Align'
            self.btnBitBtnSetAlign.TabOrder = 3
            # Create control: btnBitBtnSetMargins = Button(self)
            self.btnBitBtnSetMargins = Button(self)
            self.btnBitBtnSetMargins.Name = "btnBitBtnSetMargins"
            self.btnBitBtnSetMargins.Parent = self.grpBitBtn
            self.btnBitBtnSetMargins.Left = 2
            self.btnBitBtnSetMargins.Top = 192
            self.btnBitBtnSetMargins.Width = 260
            self.btnBitBtnSetMargins.Height = 25
            self.btnBitBtnSetMargins.Cursor = crArrow
            self.btnBitBtnSetMargins.Align = "alTop"
            self.btnBitBtnSetMargins.Caption = 'Set Margins'
            self.btnBitBtnSetMargins.TabOrder = 4
            # Create control: btnBitBtnSetGlyph = Button(self)
            self.btnBitBtnSetGlyph = Button(self)
            self.btnBitBtnSetGlyph.Name = "btnBitBtnSetGlyph"
            self.btnBitBtnSetGlyph.Parent = self.grpBitBtn
            self.btnBitBtnSetGlyph.Left = 2
            self.btnBitBtnSetGlyph.Top = 42
            self.btnBitBtnSetGlyph.Width = 260
            self.btnBitBtnSetGlyph.Height = 25
            self.btnBitBtnSetGlyph.Cursor = crArrow
            self.btnBitBtnSetGlyph.Align = "alTop"
            self.btnBitBtnSetGlyph.Caption = 'Set Glyph'
            self.btnBitBtnSetGlyph.TabOrder = 5
            # Create control: btnBitBtnSetKind = Button(self)
            self.btnBitBtnSetKind = Button(self)
            self.btnBitBtnSetKind.Name = "btnBitBtnSetKind"
            self.btnBitBtnSetKind.Parent = self.grpBitBtn
            self.btnBitBtnSetKind.Left = 2
            self.btnBitBtnSetKind.Top = 67
            self.btnBitBtnSetKind.Width = 260
            self.btnBitBtnSetKind.Height = 25
            self.btnBitBtnSetKind.Cursor = crArrow
            self.btnBitBtnSetKind.Align = "alTop"
            self.btnBitBtnSetKind.Caption = 'Set Kind'
            self.btnBitBtnSetKind.TabOrder = 6
            # Create control: btnBitBtnSetDefault = Button(self)
            self.btnBitBtnSetDefault = Button(self)
            self.btnBitBtnSetDefault.Name = "btnBitBtnSetDefault"
            self.btnBitBtnSetDefault.Parent = self.grpBitBtn
            self.btnBitBtnSetDefault.Left = 2
            self.btnBitBtnSetDefault.Top = 17
            self.btnBitBtnSetDefault.Width = 260
            self.btnBitBtnSetDefault.Height = 25
            self.btnBitBtnSetDefault.Cursor = crArrow
            self.btnBitBtnSetDefault.Margins.Left = 4
            self.btnBitBtnSetDefault.Margins.Top = 4
            self.btnBitBtnSetDefault.Margins.Right = 4
            self.btnBitBtnSetDefault.Margins.Bottom = 4
            self.btnBitBtnSetDefault.Align = "alTop"
            self.btnBitBtnSetDefault.Caption = 'Set Default'
            self.btnBitBtnSetDefault.TabOrder = 7
            # Create control: bbBitBtn = TSBitBtn(self)
            self.bbBitBtn = TSBitBtn(self)
            self.bbBitBtn.Name = "bbBitBtn"
            self.bbBitBtn.Parent = self.shtBitBtn
            self.bbBitBtn.Left = 264
            self.bbBitBtn.Top = 96
            self.bbBitBtn.Width = 136
            self.bbBitBtn.Height = 40
            self.bbBitBtn.Cursor = crArrow
            self.bbBitBtn.Margins.Left = 4
            self.bbBitBtn.Margins.Top = 4
            self.bbBitBtn.Margins.Right = 4
            self.bbBitBtn.Margins.Bottom = 4
            self.bbBitBtn.Caption = 'BitBtn'
            self.bbBitBtn.Images = app.get_system_imagelist_16px()
            self.bbBitBtn.TabOrder = 1
            # Create control: shtDrawGrid = TabSheet(self)
            self.shtDrawGrid = TabSheet(self)
            self.shtDrawGrid.Name = "shtDrawGrid"
            self.shtDrawGrid.PageControl = self.pgFeatures
            self.shtDrawGrid.Cursor = crArrow
            self.shtDrawGrid.Margins.Left = 4
            self.shtDrawGrid.Margins.Top = 4
            self.shtDrawGrid.Margins.Right = 4
            self.shtDrawGrid.Margins.Bottom = 4
            self.shtDrawGrid.Caption = 'Draw Grid'
            # Create control: dgDrawGrid = DrawGrid(self)
            self.dgDrawGrid = DrawGrid(self)
            self.dgDrawGrid.Name = "dgDrawGrid"
            self.dgDrawGrid.Parent = self.shtDrawGrid
            self.dgDrawGrid.Left = 10
            self.dgDrawGrid.Top = 10
            self.dgDrawGrid.Width = 520
            self.dgDrawGrid.Height = 320
            self.dgDrawGrid.Cursor = crArrow
            self.dgDrawGrid.Margins.Left = 4
            self.dgDrawGrid.Margins.Top = 4
            self.dgDrawGrid.Margins.Right = 4
            self.dgDrawGrid.Margins.Bottom = 4
            self.dgDrawGrid.DefaultColWidth = 80
            self.dgDrawGrid.TabOrder = 0
            # Create control: grpDrawGrid = GroupBox(self)
            self.grpDrawGrid = GroupBox(self)
            self.grpDrawGrid.Name = "grpDrawGrid"
            self.grpDrawGrid.Parent = self.shtDrawGrid
            self.grpDrawGrid.Left = 1123
            self.grpDrawGrid.Top = 0
            self.grpDrawGrid.Width = 264
            self.grpDrawGrid.Height = 308
            self.grpDrawGrid.Cursor = crArrow
            self.grpDrawGrid.Margins.Left = 4
            self.grpDrawGrid.Margins.Top = 4
            self.grpDrawGrid.Margins.Right = 4
            self.grpDrawGrid.Margins.Bottom = 4
            self.grpDrawGrid.Align = "alRight"
            self.grpDrawGrid.Caption = 'Control Usages'
            self.grpDrawGrid.TabOrder = 1
            # Create control: btnDrawGridSetBounds = Button(self)
            self.btnDrawGridSetBounds = Button(self)
            self.btnDrawGridSetBounds.Name = "btnDrawGridSetBounds"
            self.btnDrawGridSetBounds.Parent = self.grpDrawGrid
            self.btnDrawGridSetBounds.Left = 2
            self.btnDrawGridSetBounds.Top = 117
            self.btnDrawGridSetBounds.Width = 260
            self.btnDrawGridSetBounds.Height = 25
            self.btnDrawGridSetBounds.Cursor = crArrow
            self.btnDrawGridSetBounds.Align = "alTop"
            self.btnDrawGridSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnDrawGridSetBounds.TabOrder = 0
            # Create control: btnDrawGridToggleEnabled = Button(self)
            self.btnDrawGridToggleEnabled = Button(self)
            self.btnDrawGridToggleEnabled.Name = "btnDrawGridToggleEnabled"
            self.btnDrawGridToggleEnabled.Parent = self.grpDrawGrid
            self.btnDrawGridToggleEnabled.Left = 2
            self.btnDrawGridToggleEnabled.Top = 142
            self.btnDrawGridToggleEnabled.Width = 260
            self.btnDrawGridToggleEnabled.Height = 25
            self.btnDrawGridToggleEnabled.Cursor = crArrow
            self.btnDrawGridToggleEnabled.Align = "alTop"
            self.btnDrawGridToggleEnabled.Caption = 'Toggle Enabled'
            self.btnDrawGridToggleEnabled.TabOrder = 1
            # Create control: btnDrawGridToggleVisible = Button(self)
            self.btnDrawGridToggleVisible = Button(self)
            self.btnDrawGridToggleVisible.Name = "btnDrawGridToggleVisible"
            self.btnDrawGridToggleVisible.Parent = self.grpDrawGrid
            self.btnDrawGridToggleVisible.Left = 2
            self.btnDrawGridToggleVisible.Top = 167
            self.btnDrawGridToggleVisible.Width = 260
            self.btnDrawGridToggleVisible.Height = 25
            self.btnDrawGridToggleVisible.Cursor = crArrow
            self.btnDrawGridToggleVisible.Align = "alTop"
            self.btnDrawGridToggleVisible.Caption = 'Toggle Visible'
            self.btnDrawGridToggleVisible.TabOrder = 2
            # Create control: btnDrawGridSetAlign = Button(self)
            self.btnDrawGridSetAlign = Button(self)
            self.btnDrawGridSetAlign.Name = "btnDrawGridSetAlign"
            self.btnDrawGridSetAlign.Parent = self.grpDrawGrid
            self.btnDrawGridSetAlign.Left = 2
            self.btnDrawGridSetAlign.Top = 192
            self.btnDrawGridSetAlign.Width = 260
            self.btnDrawGridSetAlign.Height = 25
            self.btnDrawGridSetAlign.Cursor = crArrow
            self.btnDrawGridSetAlign.Align = "alTop"
            self.btnDrawGridSetAlign.Caption = 'Set Align'
            self.btnDrawGridSetAlign.TabOrder = 3
            # Create control: btnDrawGridSetMargins = Button(self)
            self.btnDrawGridSetMargins = Button(self)
            self.btnDrawGridSetMargins.Name = "btnDrawGridSetMargins"
            self.btnDrawGridSetMargins.Parent = self.grpDrawGrid
            self.btnDrawGridSetMargins.Left = 2
            self.btnDrawGridSetMargins.Top = 217
            self.btnDrawGridSetMargins.Width = 260
            self.btnDrawGridSetMargins.Height = 25
            self.btnDrawGridSetMargins.Cursor = crArrow
            self.btnDrawGridSetMargins.Align = "alTop"
            self.btnDrawGridSetMargins.Caption = 'Set Margins'
            self.btnDrawGridSetMargins.TabOrder = 4
            # Create control: btnDrawGridSetBorderStyle = Button(self)
            self.btnDrawGridSetBorderStyle = Button(self)
            self.btnDrawGridSetBorderStyle.Name = "btnDrawGridSetBorderStyle"
            self.btnDrawGridSetBorderStyle.Parent = self.grpDrawGrid
            self.btnDrawGridSetBorderStyle.Left = 2
            self.btnDrawGridSetBorderStyle.Top = 67
            self.btnDrawGridSetBorderStyle.Width = 260
            self.btnDrawGridSetBorderStyle.Height = 25
            self.btnDrawGridSetBorderStyle.Cursor = crArrow
            self.btnDrawGridSetBorderStyle.Align = "alTop"
            self.btnDrawGridSetBorderStyle.Caption = 'Set BorderStyle'
            self.btnDrawGridSetBorderStyle.TabOrder = 5
            # Create control: btnDrawGridSetBevelKind = Button(self)
            self.btnDrawGridSetBevelKind = Button(self)
            self.btnDrawGridSetBevelKind.Name = "btnDrawGridSetBevelKind"
            self.btnDrawGridSetBevelKind.Parent = self.grpDrawGrid
            self.btnDrawGridSetBevelKind.Left = 2
            self.btnDrawGridSetBevelKind.Top = 17
            self.btnDrawGridSetBevelKind.Width = 260
            self.btnDrawGridSetBevelKind.Height = 25
            self.btnDrawGridSetBevelKind.Cursor = crArrow
            self.btnDrawGridSetBevelKind.Align = "alTop"
            self.btnDrawGridSetBevelKind.Caption = 'Set BevelKind'
            self.btnDrawGridSetBevelKind.TabOrder = 6
            # Create control: btnDrawGridSetBiDiMode = Button(self)
            self.btnDrawGridSetBiDiMode = Button(self)
            self.btnDrawGridSetBiDiMode.Name = "btnDrawGridSetBiDiMode"
            self.btnDrawGridSetBiDiMode.Parent = self.grpDrawGrid
            self.btnDrawGridSetBiDiMode.Left = 2
            self.btnDrawGridSetBiDiMode.Top = 42
            self.btnDrawGridSetBiDiMode.Width = 260
            self.btnDrawGridSetBiDiMode.Height = 25
            self.btnDrawGridSetBiDiMode.Cursor = crArrow
            self.btnDrawGridSetBiDiMode.Align = "alTop"
            self.btnDrawGridSetBiDiMode.Caption = 'Set BiDiMode'
            self.btnDrawGridSetBiDiMode.TabOrder = 7
            # Create control: btnDrawGridSetScrollBars = Button(self)
            self.btnDrawGridSetScrollBars = Button(self)
            self.btnDrawGridSetScrollBars.Name = "btnDrawGridSetScrollBars"
            self.btnDrawGridSetScrollBars.Parent = self.grpDrawGrid
            self.btnDrawGridSetScrollBars.Left = 2
            self.btnDrawGridSetScrollBars.Top = 92
            self.btnDrawGridSetScrollBars.Width = 260
            self.btnDrawGridSetScrollBars.Height = 25
            self.btnDrawGridSetScrollBars.Cursor = crArrow
            self.btnDrawGridSetScrollBars.Align = "alTop"
            self.btnDrawGridSetScrollBars.Caption = 'Set ScrollBars'
            self.btnDrawGridSetScrollBars.TabOrder = 8
            # Create control: shtStringGrid = TabSheet(self)
            self.shtStringGrid = TabSheet(self)
            self.shtStringGrid.Name = "shtStringGrid"
            self.shtStringGrid.PageControl = self.pgFeatures
            self.shtStringGrid.Cursor = crArrow
            self.shtStringGrid.Margins.Left = 4
            self.shtStringGrid.Margins.Top = 4
            self.shtStringGrid.Margins.Right = 4
            self.shtStringGrid.Margins.Bottom = 4
            self.shtStringGrid.Caption = 'String Grid'
            # Create control: sgStringGrid = StringGrid(self)
            self.sgStringGrid = StringGrid(self)
            self.sgStringGrid.Name = "sgStringGrid"
            self.sgStringGrid.Parent = self.shtStringGrid
            self.sgStringGrid.Left = 160
            self.sgStringGrid.Top = 80
            self.sgStringGrid.Width = 320
            self.sgStringGrid.Height = 120
            self.sgStringGrid.Cursor = crArrow
            self.sgStringGrid.Margins.Left = 4
            self.sgStringGrid.Margins.Top = 4
            self.sgStringGrid.Margins.Right = 4
            self.sgStringGrid.Margins.Bottom = 4
            self.sgStringGrid.DefaultColWidth = 80
            self.sgStringGrid.DefaultRowHeight = 30
            self.sgStringGrid.TabOrder = 0
            # Create control: GroupBox42 = GroupBox(self)
            self.GroupBox42 = GroupBox(self)
            self.GroupBox42.Name = "GroupBox42"
            self.GroupBox42.Parent = self.shtStringGrid
            self.GroupBox42.Left = 1123
            self.GroupBox42.Top = 0
            self.GroupBox42.Width = 264
            self.GroupBox42.Height = 308
            self.GroupBox42.Cursor = crArrow
            self.GroupBox42.Margins.Left = 4
            self.GroupBox42.Margins.Top = 4
            self.GroupBox42.Margins.Right = 4
            self.GroupBox42.Margins.Bottom = 4
            self.GroupBox42.Align = "alRight"
            self.GroupBox42.Caption = 'Control Usages'
            self.GroupBox42.TabOrder = 1
            # Create control: btnStringGridSetBounds = Button(self)
            self.btnStringGridSetBounds = Button(self)
            self.btnStringGridSetBounds.Name = "btnStringGridSetBounds"
            self.btnStringGridSetBounds.Parent = self.GroupBox42
            self.btnStringGridSetBounds.Left = 2
            self.btnStringGridSetBounds.Top = 117
            self.btnStringGridSetBounds.Width = 260
            self.btnStringGridSetBounds.Height = 25
            self.btnStringGridSetBounds.Cursor = crArrow
            self.btnStringGridSetBounds.Align = "alTop"
            self.btnStringGridSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnStringGridSetBounds.TabOrder = 0
            # Create control: btnStringGridToggleEnabled = Button(self)
            self.btnStringGridToggleEnabled = Button(self)
            self.btnStringGridToggleEnabled.Name = "btnStringGridToggleEnabled"
            self.btnStringGridToggleEnabled.Parent = self.GroupBox42
            self.btnStringGridToggleEnabled.Left = 2
            self.btnStringGridToggleEnabled.Top = 142
            self.btnStringGridToggleEnabled.Width = 260
            self.btnStringGridToggleEnabled.Height = 25
            self.btnStringGridToggleEnabled.Cursor = crArrow
            self.btnStringGridToggleEnabled.Align = "alTop"
            self.btnStringGridToggleEnabled.Caption = 'Toggle Enabled'
            self.btnStringGridToggleEnabled.TabOrder = 1
            # Create control: btnStringGridToggleVisible = Button(self)
            self.btnStringGridToggleVisible = Button(self)
            self.btnStringGridToggleVisible.Name = "btnStringGridToggleVisible"
            self.btnStringGridToggleVisible.Parent = self.GroupBox42
            self.btnStringGridToggleVisible.Left = 2
            self.btnStringGridToggleVisible.Top = 167
            self.btnStringGridToggleVisible.Width = 260
            self.btnStringGridToggleVisible.Height = 25
            self.btnStringGridToggleVisible.Cursor = crArrow
            self.btnStringGridToggleVisible.Align = "alTop"
            self.btnStringGridToggleVisible.Caption = 'Toggle Visible'
            self.btnStringGridToggleVisible.TabOrder = 2
            # Create control: btnStringGridSetAlign = Button(self)
            self.btnStringGridSetAlign = Button(self)
            self.btnStringGridSetAlign.Name = "btnStringGridSetAlign"
            self.btnStringGridSetAlign.Parent = self.GroupBox42
            self.btnStringGridSetAlign.Left = 2
            self.btnStringGridSetAlign.Top = 192
            self.btnStringGridSetAlign.Width = 260
            self.btnStringGridSetAlign.Height = 25
            self.btnStringGridSetAlign.Cursor = crArrow
            self.btnStringGridSetAlign.Align = "alTop"
            self.btnStringGridSetAlign.Caption = 'Set Align'
            self.btnStringGridSetAlign.TabOrder = 3
            # Create control: btnStringGridSetMargins = Button(self)
            self.btnStringGridSetMargins = Button(self)
            self.btnStringGridSetMargins.Name = "btnStringGridSetMargins"
            self.btnStringGridSetMargins.Parent = self.GroupBox42
            self.btnStringGridSetMargins.Left = 2
            self.btnStringGridSetMargins.Top = 217
            self.btnStringGridSetMargins.Width = 260
            self.btnStringGridSetMargins.Height = 25
            self.btnStringGridSetMargins.Cursor = crArrow
            self.btnStringGridSetMargins.Align = "alTop"
            self.btnStringGridSetMargins.Caption = 'Set Margins'
            self.btnStringGridSetMargins.TabOrder = 4
            # Create control: btnStringGridSetBorderStyle = Button(self)
            self.btnStringGridSetBorderStyle = Button(self)
            self.btnStringGridSetBorderStyle.Name = "btnStringGridSetBorderStyle"
            self.btnStringGridSetBorderStyle.Parent = self.GroupBox42
            self.btnStringGridSetBorderStyle.Left = 2
            self.btnStringGridSetBorderStyle.Top = 67
            self.btnStringGridSetBorderStyle.Width = 260
            self.btnStringGridSetBorderStyle.Height = 25
            self.btnStringGridSetBorderStyle.Cursor = crArrow
            self.btnStringGridSetBorderStyle.Align = "alTop"
            self.btnStringGridSetBorderStyle.Caption = 'Set BorderStyle'
            self.btnStringGridSetBorderStyle.TabOrder = 5
            # Create control: btnStringGridSetBevelKind = Button(self)
            self.btnStringGridSetBevelKind = Button(self)
            self.btnStringGridSetBevelKind.Name = "btnStringGridSetBevelKind"
            self.btnStringGridSetBevelKind.Parent = self.GroupBox42
            self.btnStringGridSetBevelKind.Left = 2
            self.btnStringGridSetBevelKind.Top = 17
            self.btnStringGridSetBevelKind.Width = 260
            self.btnStringGridSetBevelKind.Height = 25
            self.btnStringGridSetBevelKind.Cursor = crArrow
            self.btnStringGridSetBevelKind.Align = "alTop"
            self.btnStringGridSetBevelKind.Caption = 'Set BevelKind'
            self.btnStringGridSetBevelKind.TabOrder = 6
            # Create control: btnStringGridSetBiDiMode = Button(self)
            self.btnStringGridSetBiDiMode = Button(self)
            self.btnStringGridSetBiDiMode.Name = "btnStringGridSetBiDiMode"
            self.btnStringGridSetBiDiMode.Parent = self.GroupBox42
            self.btnStringGridSetBiDiMode.Left = 2
            self.btnStringGridSetBiDiMode.Top = 42
            self.btnStringGridSetBiDiMode.Width = 260
            self.btnStringGridSetBiDiMode.Height = 25
            self.btnStringGridSetBiDiMode.Cursor = crArrow
            self.btnStringGridSetBiDiMode.Align = "alTop"
            self.btnStringGridSetBiDiMode.Caption = 'Set BiDiMode'
            self.btnStringGridSetBiDiMode.TabOrder = 7
            # Create control: btnStringGridSetScrollBars = Button(self)
            self.btnStringGridSetScrollBars = Button(self)
            self.btnStringGridSetScrollBars.Name = "btnStringGridSetScrollBars"
            self.btnStringGridSetScrollBars.Parent = self.GroupBox42
            self.btnStringGridSetScrollBars.Left = 2
            self.btnStringGridSetScrollBars.Top = 92
            self.btnStringGridSetScrollBars.Width = 260
            self.btnStringGridSetScrollBars.Height = 25
            self.btnStringGridSetScrollBars.Cursor = crArrow
            self.btnStringGridSetScrollBars.Align = "alTop"
            self.btnStringGridSetScrollBars.Caption = 'Set ScrollBars'
            self.btnStringGridSetScrollBars.TabOrder = 8
            # Create control: shtSpinEdit = TabSheet(self)
            self.shtSpinEdit = TabSheet(self)
            self.shtSpinEdit.Name = "shtSpinEdit"
            self.shtSpinEdit.PageControl = self.pgFeatures
            self.shtSpinEdit.Cursor = crArrow
            self.shtSpinEdit.Margins.Left = 4
            self.shtSpinEdit.Margins.Top = 4
            self.shtSpinEdit.Margins.Right = 4
            self.shtSpinEdit.Margins.Bottom = 4
            self.shtSpinEdit.Caption = 'Spin Edit'
            # Create control: seSpinEdit = SpinEdit(self)
            self.seSpinEdit = SpinEdit(self)
            self.seSpinEdit.Name = "seSpinEdit"
            self.seSpinEdit.Parent = self.shtSpinEdit
            self.seSpinEdit.Left = 208
            self.seSpinEdit.Top = 96
            self.seSpinEdit.Width = 121
            self.seSpinEdit.Height = 24
            self.seSpinEdit.Cursor = crArrow
            self.seSpinEdit.Margins.Left = 4
            self.seSpinEdit.Margins.Top = 4
            self.seSpinEdit.Margins.Right = 4
            self.seSpinEdit.Margins.Bottom = 4
            self.seSpinEdit.MaxValue = 0
            self.seSpinEdit.MinValue = 0
            self.seSpinEdit.TabOrder = 0
            self.seSpinEdit.Value = 0
            # Create control: grpSpinEdit = GroupBox(self)
            self.grpSpinEdit = GroupBox(self)
            self.grpSpinEdit.Name = "grpSpinEdit"
            self.grpSpinEdit.Parent = self.shtSpinEdit
            self.grpSpinEdit.Left = 1123
            self.grpSpinEdit.Top = 0
            self.grpSpinEdit.Width = 264
            self.grpSpinEdit.Height = 308
            self.grpSpinEdit.Cursor = crArrow
            self.grpSpinEdit.Margins.Left = 4
            self.grpSpinEdit.Margins.Top = 4
            self.grpSpinEdit.Margins.Right = 4
            self.grpSpinEdit.Margins.Bottom = 4
            self.grpSpinEdit.Align = "alRight"
            self.grpSpinEdit.Caption = 'Control Usages'
            self.grpSpinEdit.TabOrder = 1
            # Create control: btnSpinEditSetBounds = Button(self)
            self.btnSpinEditSetBounds = Button(self)
            self.btnSpinEditSetBounds.Name = "btnSpinEditSetBounds"
            self.btnSpinEditSetBounds.Parent = self.grpSpinEdit
            self.btnSpinEditSetBounds.Left = 2
            self.btnSpinEditSetBounds.Top = 67
            self.btnSpinEditSetBounds.Width = 260
            self.btnSpinEditSetBounds.Height = 25
            self.btnSpinEditSetBounds.Cursor = crArrow
            self.btnSpinEditSetBounds.Align = "alTop"
            self.btnSpinEditSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnSpinEditSetBounds.TabOrder = 0
            # Create control: btnSpinEditToggleEnabled = Button(self)
            self.btnSpinEditToggleEnabled = Button(self)
            self.btnSpinEditToggleEnabled.Name = "btnSpinEditToggleEnabled"
            self.btnSpinEditToggleEnabled.Parent = self.grpSpinEdit
            self.btnSpinEditToggleEnabled.Left = 2
            self.btnSpinEditToggleEnabled.Top = 92
            self.btnSpinEditToggleEnabled.Width = 260
            self.btnSpinEditToggleEnabled.Height = 25
            self.btnSpinEditToggleEnabled.Cursor = crArrow
            self.btnSpinEditToggleEnabled.Align = "alTop"
            self.btnSpinEditToggleEnabled.Caption = 'Toggle Enabled'
            self.btnSpinEditToggleEnabled.TabOrder = 1
            # Create control: btnSpinEditToggleVisible = Button(self)
            self.btnSpinEditToggleVisible = Button(self)
            self.btnSpinEditToggleVisible.Name = "btnSpinEditToggleVisible"
            self.btnSpinEditToggleVisible.Parent = self.grpSpinEdit
            self.btnSpinEditToggleVisible.Left = 2
            self.btnSpinEditToggleVisible.Top = 117
            self.btnSpinEditToggleVisible.Width = 260
            self.btnSpinEditToggleVisible.Height = 25
            self.btnSpinEditToggleVisible.Cursor = crArrow
            self.btnSpinEditToggleVisible.Align = "alTop"
            self.btnSpinEditToggleVisible.Caption = 'Toggle Visible'
            self.btnSpinEditToggleVisible.TabOrder = 2
            # Create control: btnSpinEditSetAlign = Button(self)
            self.btnSpinEditSetAlign = Button(self)
            self.btnSpinEditSetAlign.Name = "btnSpinEditSetAlign"
            self.btnSpinEditSetAlign.Parent = self.grpSpinEdit
            self.btnSpinEditSetAlign.Left = 2
            self.btnSpinEditSetAlign.Top = 142
            self.btnSpinEditSetAlign.Width = 260
            self.btnSpinEditSetAlign.Height = 25
            self.btnSpinEditSetAlign.Cursor = crArrow
            self.btnSpinEditSetAlign.Align = "alTop"
            self.btnSpinEditSetAlign.Caption = 'Set Align'
            self.btnSpinEditSetAlign.TabOrder = 3
            # Create control: btnSpinEditSetMargins = Button(self)
            self.btnSpinEditSetMargins = Button(self)
            self.btnSpinEditSetMargins.Name = "btnSpinEditSetMargins"
            self.btnSpinEditSetMargins.Parent = self.grpSpinEdit
            self.btnSpinEditSetMargins.Left = 2
            self.btnSpinEditSetMargins.Top = 167
            self.btnSpinEditSetMargins.Width = 260
            self.btnSpinEditSetMargins.Height = 25
            self.btnSpinEditSetMargins.Cursor = crArrow
            self.btnSpinEditSetMargins.Align = "alTop"
            self.btnSpinEditSetMargins.Caption = 'Set Margins'
            self.btnSpinEditSetMargins.TabOrder = 4
            # Create control: btnSpinEditSetColor = Button(self)
            self.btnSpinEditSetColor = Button(self)
            self.btnSpinEditSetColor.Name = "btnSpinEditSetColor"
            self.btnSpinEditSetColor.Parent = self.grpSpinEdit
            self.btnSpinEditSetColor.Left = 2
            self.btnSpinEditSetColor.Top = 17
            self.btnSpinEditSetColor.Width = 260
            self.btnSpinEditSetColor.Height = 25
            self.btnSpinEditSetColor.Cursor = crArrow
            self.btnSpinEditSetColor.Align = "alTop"
            self.btnSpinEditSetColor.Caption = 'Set Color'
            self.btnSpinEditSetColor.TabOrder = 5
            # Create control: btnSpinEditSetCtl3D = Button(self)
            self.btnSpinEditSetCtl3D = Button(self)
            self.btnSpinEditSetCtl3D.Name = "btnSpinEditSetCtl3D"
            self.btnSpinEditSetCtl3D.Parent = self.grpSpinEdit
            self.btnSpinEditSetCtl3D.Left = 2
            self.btnSpinEditSetCtl3D.Top = 42
            self.btnSpinEditSetCtl3D.Width = 260
            self.btnSpinEditSetCtl3D.Height = 25
            self.btnSpinEditSetCtl3D.Cursor = crArrow
            self.btnSpinEditSetCtl3D.Align = "alTop"
            self.btnSpinEditSetCtl3D.Caption = 'Set Ctl3D'
            self.btnSpinEditSetCtl3D.TabOrder = 6
            # Create control: shtToggleSwitch = TabSheet(self)
            self.shtToggleSwitch = TabSheet(self)
            self.shtToggleSwitch.Name = "shtToggleSwitch"
            self.shtToggleSwitch.PageControl = self.pgFeatures
            self.shtToggleSwitch.Cursor = crArrow
            self.shtToggleSwitch.Margins.Left = 4
            self.shtToggleSwitch.Margins.Top = 4
            self.shtToggleSwitch.Margins.Right = 4
            self.shtToggleSwitch.Margins.Bottom = 4
            self.shtToggleSwitch.Caption = 'Toggle Switch'
            # Create control: tgToggleSwitch = ToggleSwitch(self)
            self.tgToggleSwitch = ToggleSwitch(self)
            self.tgToggleSwitch.Name = "tgToggleSwitch"
            self.tgToggleSwitch.Parent = self.shtToggleSwitch
            self.tgToggleSwitch.Left = 136
            self.tgToggleSwitch.Top = 80
            self.tgToggleSwitch.Width = 86
            self.tgToggleSwitch.Height = 25
            self.tgToggleSwitch.Cursor = crArrow
            self.tgToggleSwitch.Margins.Left = 4
            self.tgToggleSwitch.Margins.Top = 4
            self.tgToggleSwitch.Margins.Right = 4
            self.tgToggleSwitch.Margins.Bottom = 4
            self.tgToggleSwitch.SwitchHeight = 25
            self.tgToggleSwitch.SwitchWidth = 63
            self.tgToggleSwitch.TabOrder = 0
            self.tgToggleSwitch.ThumbWidth = 19
            # Create control: grpToggleSwitch = GroupBox(self)
            self.grpToggleSwitch = GroupBox(self)
            self.grpToggleSwitch.Name = "grpToggleSwitch"
            self.grpToggleSwitch.Parent = self.shtToggleSwitch
            self.grpToggleSwitch.Left = 1123
            self.grpToggleSwitch.Top = 0
            self.grpToggleSwitch.Width = 264
            self.grpToggleSwitch.Height = 308
            self.grpToggleSwitch.Cursor = crArrow
            self.grpToggleSwitch.Margins.Left = 4
            self.grpToggleSwitch.Margins.Top = 4
            self.grpToggleSwitch.Margins.Right = 4
            self.grpToggleSwitch.Margins.Bottom = 4
            self.grpToggleSwitch.Align = "alRight"
            self.grpToggleSwitch.Caption = 'Control Usages'
            self.grpToggleSwitch.TabOrder = 1
            # Create control: btnToggleSwitchSetBounds = Button(self)
            self.btnToggleSwitchSetBounds = Button(self)
            self.btnToggleSwitchSetBounds.Name = "btnToggleSwitchSetBounds"
            self.btnToggleSwitchSetBounds.Parent = self.grpToggleSwitch
            self.btnToggleSwitchSetBounds.Left = 2
            self.btnToggleSwitchSetBounds.Top = 67
            self.btnToggleSwitchSetBounds.Width = 260
            self.btnToggleSwitchSetBounds.Height = 25
            self.btnToggleSwitchSetBounds.Cursor = crArrow
            self.btnToggleSwitchSetBounds.Align = "alTop"
            self.btnToggleSwitchSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnToggleSwitchSetBounds.TabOrder = 0
            # Create control: btnToggleSwitchToggleEnabled = Button(self)
            self.btnToggleSwitchToggleEnabled = Button(self)
            self.btnToggleSwitchToggleEnabled.Name = "btnToggleSwitchToggleEnabled"
            self.btnToggleSwitchToggleEnabled.Parent = self.grpToggleSwitch
            self.btnToggleSwitchToggleEnabled.Left = 2
            self.btnToggleSwitchToggleEnabled.Top = 92
            self.btnToggleSwitchToggleEnabled.Width = 260
            self.btnToggleSwitchToggleEnabled.Height = 25
            self.btnToggleSwitchToggleEnabled.Cursor = crArrow
            self.btnToggleSwitchToggleEnabled.Align = "alTop"
            self.btnToggleSwitchToggleEnabled.Caption = 'Toggle Enabled'
            self.btnToggleSwitchToggleEnabled.TabOrder = 1
            # Create control: btnToggleSwitchToggleVisible = Button(self)
            self.btnToggleSwitchToggleVisible = Button(self)
            self.btnToggleSwitchToggleVisible.Name = "btnToggleSwitchToggleVisible"
            self.btnToggleSwitchToggleVisible.Parent = self.grpToggleSwitch
            self.btnToggleSwitchToggleVisible.Left = 2
            self.btnToggleSwitchToggleVisible.Top = 117
            self.btnToggleSwitchToggleVisible.Width = 260
            self.btnToggleSwitchToggleVisible.Height = 25
            self.btnToggleSwitchToggleVisible.Cursor = crArrow
            self.btnToggleSwitchToggleVisible.Align = "alTop"
            self.btnToggleSwitchToggleVisible.Caption = 'Toggle Visible'
            self.btnToggleSwitchToggleVisible.TabOrder = 2
            # Create control: btnToggleSwitchSetAlign = Button(self)
            self.btnToggleSwitchSetAlign = Button(self)
            self.btnToggleSwitchSetAlign.Name = "btnToggleSwitchSetAlign"
            self.btnToggleSwitchSetAlign.Parent = self.grpToggleSwitch
            self.btnToggleSwitchSetAlign.Left = 2
            self.btnToggleSwitchSetAlign.Top = 142
            self.btnToggleSwitchSetAlign.Width = 260
            self.btnToggleSwitchSetAlign.Height = 25
            self.btnToggleSwitchSetAlign.Cursor = crArrow
            self.btnToggleSwitchSetAlign.Align = "alTop"
            self.btnToggleSwitchSetAlign.Caption = 'Set Align'
            self.btnToggleSwitchSetAlign.TabOrder = 3
            # Create control: btnToggleSwitchSetMargins = Button(self)
            self.btnToggleSwitchSetMargins = Button(self)
            self.btnToggleSwitchSetMargins.Name = "btnToggleSwitchSetMargins"
            self.btnToggleSwitchSetMargins.Parent = self.grpToggleSwitch
            self.btnToggleSwitchSetMargins.Left = 2
            self.btnToggleSwitchSetMargins.Top = 167
            self.btnToggleSwitchSetMargins.Width = 260
            self.btnToggleSwitchSetMargins.Height = 25
            self.btnToggleSwitchSetMargins.Cursor = crArrow
            self.btnToggleSwitchSetMargins.Align = "alTop"
            self.btnToggleSwitchSetMargins.Caption = 'Set Margins'
            self.btnToggleSwitchSetMargins.TabOrder = 4
            # Create control: btnToggleSwitchSetAlignment = Button(self)
            self.btnToggleSwitchSetAlignment = Button(self)
            self.btnToggleSwitchSetAlignment.Name = "btnToggleSwitchSetAlignment"
            self.btnToggleSwitchSetAlignment.Parent = self.grpToggleSwitch
            self.btnToggleSwitchSetAlignment.Left = 2
            self.btnToggleSwitchSetAlignment.Top = 17
            self.btnToggleSwitchSetAlignment.Width = 260
            self.btnToggleSwitchSetAlignment.Height = 25
            self.btnToggleSwitchSetAlignment.Cursor = crArrow
            self.btnToggleSwitchSetAlignment.Align = "alTop"
            self.btnToggleSwitchSetAlignment.Caption = 'Set Alignment'
            self.btnToggleSwitchSetAlignment.TabOrder = 5
            # Create control: btnToggleSwitchSetColor = Button(self)
            self.btnToggleSwitchSetColor = Button(self)
            self.btnToggleSwitchSetColor.Name = "btnToggleSwitchSetColor"
            self.btnToggleSwitchSetColor.Parent = self.grpToggleSwitch
            self.btnToggleSwitchSetColor.Left = 2
            self.btnToggleSwitchSetColor.Top = 42
            self.btnToggleSwitchSetColor.Width = 260
            self.btnToggleSwitchSetColor.Height = 25
            self.btnToggleSwitchSetColor.Cursor = crArrow
            self.btnToggleSwitchSetColor.Align = "alTop"
            self.btnToggleSwitchSetColor.Caption = 'Set Color'
            self.btnToggleSwitchSetColor.TabOrder = 6
            # Create control: shtNumberBox = TabSheet(self)
            self.shtNumberBox = TabSheet(self)
            self.shtNumberBox.Name = "shtNumberBox"
            self.shtNumberBox.PageControl = self.pgFeatures
            self.shtNumberBox.Cursor = crArrow
            self.shtNumberBox.Margins.Left = 4
            self.shtNumberBox.Margins.Top = 4
            self.shtNumberBox.Margins.Right = 4
            self.shtNumberBox.Margins.Bottom = 4
            self.shtNumberBox.Caption = 'Number Box'
            # Create control: nbNumberBox = NumberBox(self)
            self.nbNumberBox = NumberBox(self)
            self.nbNumberBox.Name = "nbNumberBox"
            self.nbNumberBox.Parent = self.shtNumberBox
            self.nbNumberBox.Left = 168
            self.nbNumberBox.Top = 88
            self.nbNumberBox.Width = 121
            self.nbNumberBox.Height = 23
            self.nbNumberBox.Cursor = crArrow
            self.nbNumberBox.Margins.Left = 4
            self.nbNumberBox.Margins.Top = 4
            self.nbNumberBox.Margins.Right = 4
            self.nbNumberBox.Margins.Bottom = 4
            self.nbNumberBox.TabOrder = 0
            self.nbNumberBox.SpinButtonOptions.ButtonWidth = 21
            # Create control: grpNumberBox = GroupBox(self)
            self.grpNumberBox = GroupBox(self)
            self.grpNumberBox.Name = "grpNumberBox"
            self.grpNumberBox.Parent = self.shtNumberBox
            self.grpNumberBox.Left = 1123
            self.grpNumberBox.Top = 0
            self.grpNumberBox.Width = 264
            self.grpNumberBox.Height = 308
            self.grpNumberBox.Cursor = crArrow
            self.grpNumberBox.Margins.Left = 4
            self.grpNumberBox.Margins.Top = 4
            self.grpNumberBox.Margins.Right = 4
            self.grpNumberBox.Margins.Bottom = 4
            self.grpNumberBox.Align = "alRight"
            self.grpNumberBox.Caption = 'Control Usages'
            self.grpNumberBox.TabOrder = 1
            # Create control: btnNumberBoxSetBounds = Button(self)
            self.btnNumberBoxSetBounds = Button(self)
            self.btnNumberBoxSetBounds.Name = "btnNumberBoxSetBounds"
            self.btnNumberBoxSetBounds.Parent = self.grpNumberBox
            self.btnNumberBoxSetBounds.Left = 2
            self.btnNumberBoxSetBounds.Top = 117
            self.btnNumberBoxSetBounds.Width = 260
            self.btnNumberBoxSetBounds.Height = 25
            self.btnNumberBoxSetBounds.Cursor = crArrow
            self.btnNumberBoxSetBounds.Align = "alTop"
            self.btnNumberBoxSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnNumberBoxSetBounds.TabOrder = 0
            # Create control: btnNumberBoxToggleEnabled = Button(self)
            self.btnNumberBoxToggleEnabled = Button(self)
            self.btnNumberBoxToggleEnabled.Name = "btnNumberBoxToggleEnabled"
            self.btnNumberBoxToggleEnabled.Parent = self.grpNumberBox
            self.btnNumberBoxToggleEnabled.Left = 2
            self.btnNumberBoxToggleEnabled.Top = 142
            self.btnNumberBoxToggleEnabled.Width = 260
            self.btnNumberBoxToggleEnabled.Height = 25
            self.btnNumberBoxToggleEnabled.Cursor = crArrow
            self.btnNumberBoxToggleEnabled.Align = "alTop"
            self.btnNumberBoxToggleEnabled.Caption = 'Toggle Enabled'
            self.btnNumberBoxToggleEnabled.TabOrder = 1
            # Create control: btnNumberBoxToggleVisible = Button(self)
            self.btnNumberBoxToggleVisible = Button(self)
            self.btnNumberBoxToggleVisible.Name = "btnNumberBoxToggleVisible"
            self.btnNumberBoxToggleVisible.Parent = self.grpNumberBox
            self.btnNumberBoxToggleVisible.Left = 2
            self.btnNumberBoxToggleVisible.Top = 167
            self.btnNumberBoxToggleVisible.Width = 260
            self.btnNumberBoxToggleVisible.Height = 25
            self.btnNumberBoxToggleVisible.Cursor = crArrow
            self.btnNumberBoxToggleVisible.Align = "alTop"
            self.btnNumberBoxToggleVisible.Caption = 'Toggle Visible'
            self.btnNumberBoxToggleVisible.TabOrder = 2
            # Create control: btnNumberBoxSetAlign = Button(self)
            self.btnNumberBoxSetAlign = Button(self)
            self.btnNumberBoxSetAlign.Name = "btnNumberBoxSetAlign"
            self.btnNumberBoxSetAlign.Parent = self.grpNumberBox
            self.btnNumberBoxSetAlign.Left = 2
            self.btnNumberBoxSetAlign.Top = 192
            self.btnNumberBoxSetAlign.Width = 260
            self.btnNumberBoxSetAlign.Height = 25
            self.btnNumberBoxSetAlign.Cursor = crArrow
            self.btnNumberBoxSetAlign.Align = "alTop"
            self.btnNumberBoxSetAlign.Caption = 'Set Align'
            self.btnNumberBoxSetAlign.TabOrder = 3
            # Create control: btnNumberBoxSetMargins = Button(self)
            self.btnNumberBoxSetMargins = Button(self)
            self.btnNumberBoxSetMargins.Name = "btnNumberBoxSetMargins"
            self.btnNumberBoxSetMargins.Parent = self.grpNumberBox
            self.btnNumberBoxSetMargins.Left = 2
            self.btnNumberBoxSetMargins.Top = 217
            self.btnNumberBoxSetMargins.Width = 260
            self.btnNumberBoxSetMargins.Height = 25
            self.btnNumberBoxSetMargins.Cursor = crArrow
            self.btnNumberBoxSetMargins.Align = "alTop"
            self.btnNumberBoxSetMargins.Caption = 'Set Margins'
            self.btnNumberBoxSetMargins.TabOrder = 4
            # Create control: btnNumberBoxSetColor = Button(self)
            self.btnNumberBoxSetColor = Button(self)
            self.btnNumberBoxSetColor.Name = "btnNumberBoxSetColor"
            self.btnNumberBoxSetColor.Parent = self.grpNumberBox
            self.btnNumberBoxSetColor.Left = 2
            self.btnNumberBoxSetColor.Top = 67
            self.btnNumberBoxSetColor.Width = 260
            self.btnNumberBoxSetColor.Height = 25
            self.btnNumberBoxSetColor.Cursor = crArrow
            self.btnNumberBoxSetColor.Align = "alTop"
            self.btnNumberBoxSetColor.Caption = 'Set Color'
            self.btnNumberBoxSetColor.TabOrder = 5
            # Create control: btnNumberBoxSetBorderStyle = Button(self)
            self.btnNumberBoxSetBorderStyle = Button(self)
            self.btnNumberBoxSetBorderStyle.Name = "btnNumberBoxSetBorderStyle"
            self.btnNumberBoxSetBorderStyle.Parent = self.grpNumberBox
            self.btnNumberBoxSetBorderStyle.Left = 2
            self.btnNumberBoxSetBorderStyle.Top = 17
            self.btnNumberBoxSetBorderStyle.Width = 260
            self.btnNumberBoxSetBorderStyle.Height = 25
            self.btnNumberBoxSetBorderStyle.Cursor = crArrow
            self.btnNumberBoxSetBorderStyle.Align = "alTop"
            self.btnNumberBoxSetBorderStyle.Caption = 'Set BorderStyle'
            self.btnNumberBoxSetBorderStyle.TabOrder = 6
            # Create control: btnNumberBoxSetBiDiMode = Button(self)
            self.btnNumberBoxSetBiDiMode = Button(self)
            self.btnNumberBoxSetBiDiMode.Name = "btnNumberBoxSetBiDiMode"
            self.btnNumberBoxSetBiDiMode.Parent = self.grpNumberBox
            self.btnNumberBoxSetBiDiMode.Left = 2
            self.btnNumberBoxSetBiDiMode.Top = 42
            self.btnNumberBoxSetBiDiMode.Width = 260
            self.btnNumberBoxSetBiDiMode.Height = 25
            self.btnNumberBoxSetBiDiMode.Cursor = crArrow
            self.btnNumberBoxSetBiDiMode.Align = "alTop"
            self.btnNumberBoxSetBiDiMode.Caption = 'Set BiDiMode'
            self.btnNumberBoxSetBiDiMode.TabOrder = 7
            # Create control: btnNumberBoxSetDisplayFormat = Button(self)
            self.btnNumberBoxSetDisplayFormat = Button(self)
            self.btnNumberBoxSetDisplayFormat.Name = "btnNumberBoxSetDisplayFormat"
            self.btnNumberBoxSetDisplayFormat.Parent = self.grpNumberBox
            self.btnNumberBoxSetDisplayFormat.Left = 2
            self.btnNumberBoxSetDisplayFormat.Top = 92
            self.btnNumberBoxSetDisplayFormat.Width = 260
            self.btnNumberBoxSetDisplayFormat.Height = 25
            self.btnNumberBoxSetDisplayFormat.Cursor = crArrow
            self.btnNumberBoxSetDisplayFormat.Align = "alTop"
            self.btnNumberBoxSetDisplayFormat.Caption = 'Set DisplayFormat'
            self.btnNumberBoxSetDisplayFormat.TabOrder = 8
            # Create control: shtMediaPlayer = TabSheet(self)
            self.shtMediaPlayer = TabSheet(self)
            self.shtMediaPlayer.Name = "shtMediaPlayer"
            self.shtMediaPlayer.PageControl = self.pgFeatures
            self.shtMediaPlayer.Cursor = crArrow
            self.shtMediaPlayer.Margins.Left = 4
            self.shtMediaPlayer.Margins.Top = 4
            self.shtMediaPlayer.Margins.Right = 4
            self.shtMediaPlayer.Margins.Bottom = 4
            self.shtMediaPlayer.Caption = 'Media Player'
            # Create control: mpMediaPlayer = MediaPlayer(self)
            self.mpMediaPlayer = MediaPlayer(self)
            self.mpMediaPlayer.Name = "mpMediaPlayer"
            self.mpMediaPlayer.Parent = self.shtMediaPlayer
            self.mpMediaPlayer.Left = 248
            self.mpMediaPlayer.Top = 112
            self.mpMediaPlayer.Width = 253
            self.mpMediaPlayer.Height = 30
            self.mpMediaPlayer.Cursor = crArrow
            self.mpMediaPlayer.Margins.Left = 4
            self.mpMediaPlayer.Margins.Top = 4
            self.mpMediaPlayer.Margins.Right = 4
            self.mpMediaPlayer.Margins.Bottom = 4
            self.mpMediaPlayer.TabOrder = 0
            # Create control: GroupBox40 = GroupBox(self)
            self.GroupBox40 = GroupBox(self)
            self.GroupBox40.Name = "GroupBox40"
            self.GroupBox40.Parent = self.shtMediaPlayer
            self.GroupBox40.Left = 1123
            self.GroupBox40.Top = 0
            self.GroupBox40.Width = 264
            self.GroupBox40.Height = 308
            self.GroupBox40.Cursor = crArrow
            self.GroupBox40.Margins.Left = 4
            self.GroupBox40.Margins.Top = 4
            self.GroupBox40.Margins.Right = 4
            self.GroupBox40.Margins.Bottom = 4
            self.GroupBox40.Align = "alRight"
            self.GroupBox40.Caption = 'Control Usages'
            self.GroupBox40.TabOrder = 1
            # Create control: btnMediaPlayerSetBounds = Button(self)
            self.btnMediaPlayerSetBounds = Button(self)
            self.btnMediaPlayerSetBounds.Name = "btnMediaPlayerSetBounds"
            self.btnMediaPlayerSetBounds.Parent = self.GroupBox40
            self.btnMediaPlayerSetBounds.Left = 2
            self.btnMediaPlayerSetBounds.Top = 67
            self.btnMediaPlayerSetBounds.Width = 260
            self.btnMediaPlayerSetBounds.Height = 25
            self.btnMediaPlayerSetBounds.Cursor = crArrow
            self.btnMediaPlayerSetBounds.Align = "alTop"
            self.btnMediaPlayerSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnMediaPlayerSetBounds.TabOrder = 0
            # Create control: btnMediaPlayerToggleEnabled = Button(self)
            self.btnMediaPlayerToggleEnabled = Button(self)
            self.btnMediaPlayerToggleEnabled.Name = "btnMediaPlayerToggleEnabled"
            self.btnMediaPlayerToggleEnabled.Parent = self.GroupBox40
            self.btnMediaPlayerToggleEnabled.Left = 2
            self.btnMediaPlayerToggleEnabled.Top = 92
            self.btnMediaPlayerToggleEnabled.Width = 260
            self.btnMediaPlayerToggleEnabled.Height = 25
            self.btnMediaPlayerToggleEnabled.Cursor = crArrow
            self.btnMediaPlayerToggleEnabled.Align = "alTop"
            self.btnMediaPlayerToggleEnabled.Caption = 'Toggle Enabled'
            self.btnMediaPlayerToggleEnabled.TabOrder = 1
            # Create control: btnMediaPlayerToggleVisible = Button(self)
            self.btnMediaPlayerToggleVisible = Button(self)
            self.btnMediaPlayerToggleVisible.Name = "btnMediaPlayerToggleVisible"
            self.btnMediaPlayerToggleVisible.Parent = self.GroupBox40
            self.btnMediaPlayerToggleVisible.Left = 2
            self.btnMediaPlayerToggleVisible.Top = 117
            self.btnMediaPlayerToggleVisible.Width = 260
            self.btnMediaPlayerToggleVisible.Height = 25
            self.btnMediaPlayerToggleVisible.Cursor = crArrow
            self.btnMediaPlayerToggleVisible.Align = "alTop"
            self.btnMediaPlayerToggleVisible.Caption = 'Toggle Visible'
            self.btnMediaPlayerToggleVisible.TabOrder = 2
            # Create control: btnMediaPlayerSetAlign = Button(self)
            self.btnMediaPlayerSetAlign = Button(self)
            self.btnMediaPlayerSetAlign.Name = "btnMediaPlayerSetAlign"
            self.btnMediaPlayerSetAlign.Parent = self.GroupBox40
            self.btnMediaPlayerSetAlign.Left = 2
            self.btnMediaPlayerSetAlign.Top = 142
            self.btnMediaPlayerSetAlign.Width = 260
            self.btnMediaPlayerSetAlign.Height = 25
            self.btnMediaPlayerSetAlign.Cursor = crArrow
            self.btnMediaPlayerSetAlign.Align = "alTop"
            self.btnMediaPlayerSetAlign.Caption = 'Set Align'
            self.btnMediaPlayerSetAlign.TabOrder = 3
            # Create control: btnMediaPlayerSetMargins = Button(self)
            self.btnMediaPlayerSetMargins = Button(self)
            self.btnMediaPlayerSetMargins.Name = "btnMediaPlayerSetMargins"
            self.btnMediaPlayerSetMargins.Parent = self.GroupBox40
            self.btnMediaPlayerSetMargins.Left = 2
            self.btnMediaPlayerSetMargins.Top = 167
            self.btnMediaPlayerSetMargins.Width = 260
            self.btnMediaPlayerSetMargins.Height = 25
            self.btnMediaPlayerSetMargins.Cursor = crArrow
            self.btnMediaPlayerSetMargins.Align = "alTop"
            self.btnMediaPlayerSetMargins.Caption = 'Set Margins'
            self.btnMediaPlayerSetMargins.TabOrder = 4
            # Create control: btnMediaPlayerSetAutoEnable = Button(self)
            self.btnMediaPlayerSetAutoEnable = Button(self)
            self.btnMediaPlayerSetAutoEnable.Name = "btnMediaPlayerSetAutoEnable"
            self.btnMediaPlayerSetAutoEnable.Parent = self.GroupBox40
            self.btnMediaPlayerSetAutoEnable.Left = 2
            self.btnMediaPlayerSetAutoEnable.Top = 17
            self.btnMediaPlayerSetAutoEnable.Width = 260
            self.btnMediaPlayerSetAutoEnable.Height = 25
            self.btnMediaPlayerSetAutoEnable.Cursor = crArrow
            self.btnMediaPlayerSetAutoEnable.Align = "alTop"
            self.btnMediaPlayerSetAutoEnable.Caption = 'Set AutoEnable'
            self.btnMediaPlayerSetAutoEnable.TabOrder = 5
            # Create control: btnMediaPlayerSetFileName = Button(self)
            self.btnMediaPlayerSetFileName = Button(self)
            self.btnMediaPlayerSetFileName.Name = "btnMediaPlayerSetFileName"
            self.btnMediaPlayerSetFileName.Parent = self.GroupBox40
            self.btnMediaPlayerSetFileName.Left = 2
            self.btnMediaPlayerSetFileName.Top = 42
            self.btnMediaPlayerSetFileName.Width = 260
            self.btnMediaPlayerSetFileName.Height = 25
            self.btnMediaPlayerSetFileName.Cursor = crArrow
            self.btnMediaPlayerSetFileName.Align = "alTop"
            self.btnMediaPlayerSetFileName.Caption = 'Set FileName'
            self.btnMediaPlayerSetFileName.TabOrder = 6
            # Create control: shtImageButton = TabSheet(self)
            self.shtImageButton = TabSheet(self)
            self.shtImageButton.Name = "shtImageButton"
            self.shtImageButton.PageControl = self.pgFeatures
            self.shtImageButton.Cursor = crArrow
            self.shtImageButton.Margins.Left = 4
            self.shtImageButton.Margins.Top = 4
            self.shtImageButton.Margins.Right = 4
            self.shtImageButton.Margins.Bottom = 4
            self.shtImageButton.Caption = 'Image Button'
            # Create control: ibImageButton = TSSvgImageButton(self)
            self.ibImageButton = TSSvgImageButton(self)
            self.ibImageButton.Name = "ibImageButton"
            self.ibImageButton.Parent = self.shtImageButton
            self.ibImageButton.Left = 192
            self.ibImageButton.Top = 96
            self.ibImageButton.Width = 185
            self.ibImageButton.Height = 41
            self.ibImageButton.Cursor = crArrow
            self.ibImageButton.Margins.Left = 4
            self.ibImageButton.Margins.Top = 4
            self.ibImageButton.Margins.Right = 4
            self.ibImageButton.Margins.Bottom = 4
            self.ibImageButton.Caption = 'Image Button'
            self.ibImageButton.ShowCaption = "False"
            self.ibImageButton.TabOrder = 0
            self.ibImageButton.ImageIndex = 34
            self.ibImageButton.ImageStretch = False
            self.ibImageButton.ReadOnly = False
            # Create control: grpImageButton = GroupBox(self)
            self.grpImageButton = GroupBox(self)
            self.grpImageButton.Name = "grpImageButton"
            self.grpImageButton.Parent = self.shtImageButton
            self.grpImageButton.Left = 1123
            self.grpImageButton.Top = 0
            self.grpImageButton.Width = 264
            self.grpImageButton.Height = 308
            self.grpImageButton.Cursor = crArrow
            self.grpImageButton.Margins.Left = 4
            self.grpImageButton.Margins.Top = 4
            self.grpImageButton.Margins.Right = 4
            self.grpImageButton.Margins.Bottom = 4
            self.grpImageButton.Align = "alRight"
            self.grpImageButton.Caption = 'Control Usages'
            self.grpImageButton.TabOrder = 1
            # Create control: btnImageButtonSetBevelInner = Button(self)
            self.btnImageButtonSetBevelInner = Button(self)
            self.btnImageButtonSetBevelInner.Name = "btnImageButtonSetBevelInner"
            self.btnImageButtonSetBevelInner.Parent = self.grpImageButton
            self.btnImageButtonSetBevelInner.Left = 2
            self.btnImageButtonSetBevelInner.Top = 17
            self.btnImageButtonSetBevelInner.Width = 260
            self.btnImageButtonSetBevelInner.Height = 25
            self.btnImageButtonSetBevelInner.Cursor = crArrow
            self.btnImageButtonSetBevelInner.Align = "alTop"
            self.btnImageButtonSetBevelInner.Caption = 'Set BevelInner'
            self.btnImageButtonSetBevelInner.TabOrder = 5
            # Create control: btnImageButtonSetBevelKind = Button(self)
            self.btnImageButtonSetBevelKind = Button(self)
            self.btnImageButtonSetBevelKind.Name = "btnImageButtonSetBevelKind"
            self.btnImageButtonSetBevelKind.Parent = self.grpImageButton
            self.btnImageButtonSetBevelKind.Left = 2
            self.btnImageButtonSetBevelKind.Top = 42
            self.btnImageButtonSetBevelKind.Width = 260
            self.btnImageButtonSetBevelKind.Height = 25
            self.btnImageButtonSetBevelKind.Cursor = crArrow
            self.btnImageButtonSetBevelKind.Align = "alTop"
            self.btnImageButtonSetBevelKind.Caption = 'Set BevelKind'
            self.btnImageButtonSetBevelKind.TabOrder = 7
            # Create control: btnImageButtonSetBounds = Button(self)
            self.btnImageButtonSetBounds = Button(self)
            self.btnImageButtonSetBounds.Name = "btnImageButtonSetBounds"
            self.btnImageButtonSetBounds.Parent = self.grpImageButton
            self.btnImageButtonSetBounds.Left = 2
            self.btnImageButtonSetBounds.Top = 67
            self.btnImageButtonSetBounds.Width = 260
            self.btnImageButtonSetBounds.Height = 25
            self.btnImageButtonSetBounds.Cursor = crArrow
            self.btnImageButtonSetBounds.Align = "alTop"
            self.btnImageButtonSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnImageButtonSetBounds.TabOrder = 6
            # Create control: btnImageButtonSetBevelOuter = Button(self)
            self.btnImageButtonSetBevelOuter = Button(self)
            self.btnImageButtonSetBevelOuter.Name = "btnImageButtonSetBevelOuter"
            self.btnImageButtonSetBevelOuter.Parent = self.grpImageButton
            self.btnImageButtonSetBevelOuter.Left = 2
            self.btnImageButtonSetBevelOuter.Top = 92
            self.btnImageButtonSetBevelOuter.Width = 260
            self.btnImageButtonSetBevelOuter.Height = 25
            self.btnImageButtonSetBevelOuter.Cursor = crArrow
            self.btnImageButtonSetBevelOuter.Align = "alTop"
            self.btnImageButtonSetBevelOuter.Caption = 'Set Bevel Outer'
            self.btnImageButtonSetBevelOuter.TabOrder = 8
            # Create control: btnImageButtonToggleEnabled = Button(self)
            self.btnImageButtonToggleEnabled = Button(self)
            self.btnImageButtonToggleEnabled.Name = "btnImageButtonToggleEnabled"
            self.btnImageButtonToggleEnabled.Parent = self.grpImageButton
            self.btnImageButtonToggleEnabled.Left = 2
            self.btnImageButtonToggleEnabled.Top = 117
            self.btnImageButtonToggleEnabled.Width = 260
            self.btnImageButtonToggleEnabled.Height = 25
            self.btnImageButtonToggleEnabled.Cursor = crArrow
            self.btnImageButtonToggleEnabled.Align = "alTop"
            self.btnImageButtonToggleEnabled.Caption = 'Toggle Enabled'
            self.btnImageButtonToggleEnabled.TabOrder = 9
            # Create control: btnImageButtonToggleVisible = Button(self)
            self.btnImageButtonToggleVisible = Button(self)
            self.btnImageButtonToggleVisible.Name = "btnImageButtonToggleVisible"
            self.btnImageButtonToggleVisible.Parent = self.grpImageButton
            self.btnImageButtonToggleVisible.Left = 2
            self.btnImageButtonToggleVisible.Top = 142
            self.btnImageButtonToggleVisible.Width = 260
            self.btnImageButtonToggleVisible.Height = 25
            self.btnImageButtonToggleVisible.Cursor = crArrow
            self.btnImageButtonToggleVisible.Align = "alTop"
            self.btnImageButtonToggleVisible.Caption = 'Toggle Visible'
            self.btnImageButtonToggleVisible.TabOrder = 0
            # Create control: btnImageButtonSetImageStretch = Button(self)
            self.btnImageButtonSetImageStretch = Button(self)
            self.btnImageButtonSetImageStretch.Name = "btnImageButtonSetImageStretch"
            self.btnImageButtonSetImageStretch.Parent = self.grpImageButton
            self.btnImageButtonSetImageStretch.Left = 2
            self.btnImageButtonSetImageStretch.Top = 167
            self.btnImageButtonSetImageStretch.Width = 260
            self.btnImageButtonSetImageStretch.Height = 25
            self.btnImageButtonSetImageStretch.Cursor = crArrow
            self.btnImageButtonSetImageStretch.Align = "alTop"
            self.btnImageButtonSetImageStretch.Caption = 'Set ImageStretch'
            self.btnImageButtonSetImageStretch.TabOrder = 10
            # Create control: btnImageButtonSetAlign = Button(self)
            self.btnImageButtonSetAlign = Button(self)
            self.btnImageButtonSetAlign.Name = "btnImageButtonSetAlign"
            self.btnImageButtonSetAlign.Parent = self.grpImageButton
            self.btnImageButtonSetAlign.Left = 2
            self.btnImageButtonSetAlign.Top = 192
            self.btnImageButtonSetAlign.Width = 260
            self.btnImageButtonSetAlign.Height = 25
            self.btnImageButtonSetAlign.Cursor = crArrow
            self.btnImageButtonSetAlign.Align = "alTop"
            self.btnImageButtonSetAlign.Caption = 'Set Align'
            self.btnImageButtonSetAlign.TabOrder = 1
            # Create control: btnImageButtonSetShowCaption = Button(self)
            self.btnImageButtonSetShowCaption = Button(self)
            self.btnImageButtonSetShowCaption.Name = "btnImageButtonSetShowCaption"
            self.btnImageButtonSetShowCaption.Parent = self.grpImageButton
            self.btnImageButtonSetShowCaption.Left = 2
            self.btnImageButtonSetShowCaption.Top = 217
            self.btnImageButtonSetShowCaption.Width = 260
            self.btnImageButtonSetShowCaption.Height = 25
            self.btnImageButtonSetShowCaption.Cursor = crArrow
            self.btnImageButtonSetShowCaption.Align = "alTop"
            self.btnImageButtonSetShowCaption.Caption = 'Set ShowCaption'
            self.btnImageButtonSetShowCaption.TabOrder = 11
            # Create control: btnImageButtonSetMargins = Button(self)
            self.btnImageButtonSetMargins = Button(self)
            self.btnImageButtonSetMargins.Name = "btnImageButtonSetMargins"
            self.btnImageButtonSetMargins.Parent = self.grpImageButton
            self.btnImageButtonSetMargins.Left = 2
            self.btnImageButtonSetMargins.Top = 242
            self.btnImageButtonSetMargins.Width = 260
            self.btnImageButtonSetMargins.Height = 25
            self.btnImageButtonSetMargins.Cursor = crArrow
            self.btnImageButtonSetMargins.Align = "alTop"
            self.btnImageButtonSetMargins.Caption = 'Set Margins'
            self.btnImageButtonSetMargins.TabOrder = 2
            # Create control: btnImageButtonSetColor = Button(self)
            self.btnImageButtonSetColor = Button(self)
            self.btnImageButtonSetColor.Name = "btnImageButtonSetColor"
            self.btnImageButtonSetColor.Parent = self.grpImageButton
            self.btnImageButtonSetColor.Left = 2
            self.btnImageButtonSetColor.Top = 267
            self.btnImageButtonSetColor.Width = 260
            self.btnImageButtonSetColor.Height = 25
            self.btnImageButtonSetColor.Cursor = crArrow
            self.btnImageButtonSetColor.Align = "alTop"
            self.btnImageButtonSetColor.Caption = 'Set Color'
            self.btnImageButtonSetColor.TabOrder = 3
            # Create control: btnImageButtonSetParentBackground = Button(self)
            self.btnImageButtonSetParentBackground = Button(self)
            self.btnImageButtonSetParentBackground.Name = "btnImageButtonSetParentBackground"
            self.btnImageButtonSetParentBackground.Parent = self.grpImageButton
            self.btnImageButtonSetParentBackground.Left = 2
            self.btnImageButtonSetParentBackground.Top = 292
            self.btnImageButtonSetParentBackground.Width = 260
            self.btnImageButtonSetParentBackground.Height = 25
            self.btnImageButtonSetParentBackground.Cursor = crArrow
            self.btnImageButtonSetParentBackground.Align = "alTop"
            self.btnImageButtonSetParentBackground.Caption = 'Set ParentBackground'
            self.btnImageButtonSetParentBackground.TabOrder = 4
            # Create control: shtActivityIndicator = TabSheet(self)
            self.shtActivityIndicator = TabSheet(self)
            self.shtActivityIndicator.Name = "shtActivityIndicator"
            self.shtActivityIndicator.PageControl = self.pgFeatures
            self.shtActivityIndicator.Cursor = crArrow
            self.shtActivityIndicator.Margins.Left = 4
            self.shtActivityIndicator.Margins.Top = 4
            self.shtActivityIndicator.Margins.Right = 4
            self.shtActivityIndicator.Margins.Bottom = 4
            self.shtActivityIndicator.Caption = 'Activity Indicator'
            # Create control: pcPageControl2 = PageControl(self)
            self.pcPageControl2 = PageControl(self)
            self.pcPageControl2.Name = "pcPageControl2"
            self.pcPageControl2.Parent = self.shtActivityIndicator
            self.pcPageControl2.Left = 384
            self.pcPageControl2.Top = 88
            self.pcPageControl2.Width = 289
            self.pcPageControl2.Height = 193
            self.pcPageControl2.Cursor = crArrow
            self.pcPageControl2.Margins.Left = 4
            self.pcPageControl2.Margins.Top = 4
            self.pcPageControl2.Margins.Right = 4
            self.pcPageControl2.Margins.Bottom = 4
            self.pcPageControl2.Images = app.get_system_imagelist_16px()
            self.pcPageControl2.TabOrder = 0
            # Create control: TabSheet44 = TabSheet(self)
            self.TabSheet44 = TabSheet(self)
            self.TabSheet44.Name = "TabSheet44"
            self.TabSheet44.PageControl = self.pcPageControl2
            self.TabSheet44.Cursor = crArrow
            self.TabSheet44.Margins.Left = 4
            self.TabSheet44.Margins.Top = 4
            self.TabSheet44.Margins.Right = 4
            self.TabSheet44.Margins.Bottom = 4
            self.TabSheet44.Caption = 'Sheet 1'
            # Create control: aiActivityIndicator = ActivityIndicator(self)
            self.aiActivityIndicator = ActivityIndicator(self)
            self.aiActivityIndicator.Name = "aiActivityIndicator"
            self.aiActivityIndicator.Parent = self.TabSheet44
            self.aiActivityIndicator.Left = 96
            self.aiActivityIndicator.Top = 64
            self.aiActivityIndicator.Cursor = crArrow
            self.aiActivityIndicator.Margins.Left = 4
            self.aiActivityIndicator.Margins.Top = 4
            self.aiActivityIndicator.Margins.Right = 4
            self.aiActivityIndicator.Margins.Bottom = 4
            # Create control: TabSheet45 = TabSheet(self)
            self.TabSheet45 = TabSheet(self)
            self.TabSheet45.Name = "TabSheet45"
            self.TabSheet45.PageControl = self.pcPageControl2
            self.TabSheet45.Cursor = crArrow
            self.TabSheet45.Margins.Left = 4
            self.TabSheet45.Margins.Top = 4
            self.TabSheet45.Margins.Right = 4
            self.TabSheet45.Margins.Bottom = 4
            self.TabSheet45.Caption = 'Sheet 2'
            # Create control: grpActivityIndicator = GroupBox(self)
            self.grpActivityIndicator = GroupBox(self)
            self.grpActivityIndicator.Name = "grpActivityIndicator"
            self.grpActivityIndicator.Parent = self.shtActivityIndicator
            self.grpActivityIndicator.Left = 1123
            self.grpActivityIndicator.Top = 0
            self.grpActivityIndicator.Width = 264
            self.grpActivityIndicator.Height = 308
            self.grpActivityIndicator.Cursor = crArrow
            self.grpActivityIndicator.Margins.Left = 4
            self.grpActivityIndicator.Margins.Top = 4
            self.grpActivityIndicator.Margins.Right = 4
            self.grpActivityIndicator.Margins.Bottom = 4
            self.grpActivityIndicator.Align = "alRight"
            self.grpActivityIndicator.Caption = 'Control Usages'
            self.grpActivityIndicator.TabOrder = 1
            # Create control: btnActivityIndicatorSetBounds = Button(self)
            self.btnActivityIndicatorSetBounds = Button(self)
            self.btnActivityIndicatorSetBounds.Name = "btnActivityIndicatorSetBounds"
            self.btnActivityIndicatorSetBounds.Parent = self.grpActivityIndicator
            self.btnActivityIndicatorSetBounds.Left = 2
            self.btnActivityIndicatorSetBounds.Top = 42
            self.btnActivityIndicatorSetBounds.Width = 260
            self.btnActivityIndicatorSetBounds.Height = 25
            self.btnActivityIndicatorSetBounds.Cursor = crArrow
            self.btnActivityIndicatorSetBounds.Align = "alTop"
            self.btnActivityIndicatorSetBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnActivityIndicatorSetBounds.TabOrder = 0
            # Create control: btnActivityIndicatorSetAlign = Button(self)
            self.btnActivityIndicatorSetAlign = Button(self)
            self.btnActivityIndicatorSetAlign.Name = "btnActivityIndicatorSetAlign"
            self.btnActivityIndicatorSetAlign.Parent = self.grpActivityIndicator
            self.btnActivityIndicatorSetAlign.Left = 2
            self.btnActivityIndicatorSetAlign.Top = 67
            self.btnActivityIndicatorSetAlign.Width = 260
            self.btnActivityIndicatorSetAlign.Height = 25
            self.btnActivityIndicatorSetAlign.Cursor = crArrow
            self.btnActivityIndicatorSetAlign.Align = "alTop"
            self.btnActivityIndicatorSetAlign.Caption = 'Set Align'
            self.btnActivityIndicatorSetAlign.TabOrder = 1
            # Create control: btnActivityIndicatorSetMargins = Button(self)
            self.btnActivityIndicatorSetMargins = Button(self)
            self.btnActivityIndicatorSetMargins.Name = "btnActivityIndicatorSetMargins"
            self.btnActivityIndicatorSetMargins.Parent = self.grpActivityIndicator
            self.btnActivityIndicatorSetMargins.Left = 2
            self.btnActivityIndicatorSetMargins.Top = 92
            self.btnActivityIndicatorSetMargins.Width = 260
            self.btnActivityIndicatorSetMargins.Height = 25
            self.btnActivityIndicatorSetMargins.Cursor = crArrow
            self.btnActivityIndicatorSetMargins.Align = "alTop"
            self.btnActivityIndicatorSetMargins.Caption = 'Set Margins'
            self.btnActivityIndicatorSetMargins.TabOrder = 2
            # Create control: btnActivityIndicatorSetIndicatorSize = Button(self)
            self.btnActivityIndicatorSetIndicatorSize = Button(self)
            self.btnActivityIndicatorSetIndicatorSize.Name = "btnActivityIndicatorSetIndicatorSize"
            self.btnActivityIndicatorSetIndicatorSize.Parent = self.grpActivityIndicator
            self.btnActivityIndicatorSetIndicatorSize.Left = 2
            self.btnActivityIndicatorSetIndicatorSize.Top = 17
            self.btnActivityIndicatorSetIndicatorSize.Width = 260
            self.btnActivityIndicatorSetIndicatorSize.Height = 25
            self.btnActivityIndicatorSetIndicatorSize.Cursor = crArrow
            self.btnActivityIndicatorSetIndicatorSize.Align = "alTop"
            self.btnActivityIndicatorSetIndicatorSize.Caption = 'Set IndicatorSize'
            self.btnActivityIndicatorSetIndicatorSize.TabOrder = 3
            # Create control: shtTreeView = TabSheet(self)
            self.shtTreeView = TabSheet(self)
            self.shtTreeView.Name = "shtTreeView"
            self.shtTreeView.PageControl = self.pgFeatures
            self.shtTreeView.Cursor = crArrow
            self.shtTreeView.Caption = 'TreeView'
            # Create control: GroupBox44 = GroupBox(self)
            self.GroupBox44 = GroupBox(self)
            self.GroupBox44.Name = "GroupBox44"
            self.GroupBox44.Parent = self.shtTreeView
            self.GroupBox44.Left = 1123
            self.GroupBox44.Top = 0
            self.GroupBox44.Width = 264
            self.GroupBox44.Height = 308
            self.GroupBox44.Cursor = crArrow
            self.GroupBox44.Margins.Left = 4
            self.GroupBox44.Margins.Top = 4
            self.GroupBox44.Margins.Right = 4
            self.GroupBox44.Margins.Bottom = 4
            self.GroupBox44.Align = "alRight"
            self.GroupBox44.Caption = 'Control Usages'
            self.GroupBox44.TabOrder = 0
            # Create control: btnTreeViewBounds = Button(self)
            self.btnTreeViewBounds = Button(self)
            self.btnTreeViewBounds.Name = "btnTreeViewBounds"
            self.btnTreeViewBounds.Parent = self.GroupBox44
            self.btnTreeViewBounds.Left = 2
            self.btnTreeViewBounds.Top = 17
            self.btnTreeViewBounds.Width = 260
            self.btnTreeViewBounds.Height = 25
            self.btnTreeViewBounds.Cursor = crArrow
            self.btnTreeViewBounds.Align = "alTop"
            self.btnTreeViewBounds.Caption = 'Set Bounds for Left, Top, Width and Height'
            self.btnTreeViewBounds.TabOrder = 5
            # Create control: btnTreeViewEnabled = Button(self)
            self.btnTreeViewEnabled = Button(self)
            self.btnTreeViewEnabled.Name = "btnTreeViewEnabled"
            self.btnTreeViewEnabled.Parent = self.GroupBox44
            self.btnTreeViewEnabled.Left = 2
            self.btnTreeViewEnabled.Top = 42
            self.btnTreeViewEnabled.Width = 260
            self.btnTreeViewEnabled.Height = 25
            self.btnTreeViewEnabled.Cursor = crArrow
            self.btnTreeViewEnabled.Align = "alTop"
            self.btnTreeViewEnabled.Caption = 'Toggle Enabled'
            self.btnTreeViewEnabled.TabOrder = 6
            # Create control: btnTreeViewVisible = Button(self)
            self.btnTreeViewVisible = Button(self)
            self.btnTreeViewVisible.Name = "btnTreeViewVisible"
            self.btnTreeViewVisible.Parent = self.GroupBox44
            self.btnTreeViewVisible.Left = 2
            self.btnTreeViewVisible.Top = 67
            self.btnTreeViewVisible.Width = 260
            self.btnTreeViewVisible.Height = 25
            self.btnTreeViewVisible.Cursor = crArrow
            self.btnTreeViewVisible.Align = "alTop"
            self.btnTreeViewVisible.Caption = 'Toggle Visible'
            self.btnTreeViewVisible.TabOrder = 0
            # Create control: btnTreeViewAlign = Button(self)
            self.btnTreeViewAlign = Button(self)
            self.btnTreeViewAlign.Name = "btnTreeViewAlign"
            self.btnTreeViewAlign.Parent = self.GroupBox44
            self.btnTreeViewAlign.Left = 2
            self.btnTreeViewAlign.Top = 92
            self.btnTreeViewAlign.Width = 260
            self.btnTreeViewAlign.Height = 25
            self.btnTreeViewAlign.Cursor = crArrow
            self.btnTreeViewAlign.Align = "alTop"
            self.btnTreeViewAlign.Caption = 'Set Align'
            self.btnTreeViewAlign.TabOrder = 1
            # Create control: btnTreeViewChecked = Button(self)
            self.btnTreeViewChecked = Button(self)
            self.btnTreeViewChecked.Name = "btnTreeViewChecked"
            self.btnTreeViewChecked.Parent = self.GroupBox44
            self.btnTreeViewChecked.Left = 2
            self.btnTreeViewChecked.Top = 217
            self.btnTreeViewChecked.Width = 260
            self.btnTreeViewChecked.Height = 25
            self.btnTreeViewChecked.Cursor = crArrow
            self.btnTreeViewChecked.Align = "alTop"
            self.btnTreeViewChecked.Caption = 'Toggle Checked'
            self.btnTreeViewChecked.TabOrder = 7
            # Create control: btnTreeViewMargins = Button(self)
            self.btnTreeViewMargins = Button(self)
            self.btnTreeViewMargins.Name = "btnTreeViewMargins"
            self.btnTreeViewMargins.Parent = self.GroupBox44
            self.btnTreeViewMargins.Left = 2
            self.btnTreeViewMargins.Top = 117
            self.btnTreeViewMargins.Width = 260
            self.btnTreeViewMargins.Height = 25
            self.btnTreeViewMargins.Cursor = crArrow
            self.btnTreeViewMargins.Align = "alTop"
            self.btnTreeViewMargins.Caption = 'Set Margins'
            self.btnTreeViewMargins.TabOrder = 2
            # Create control: btnTreeViewColor = Button(self)
            self.btnTreeViewColor = Button(self)
            self.btnTreeViewColor.Name = "btnTreeViewColor"
            self.btnTreeViewColor.Parent = self.GroupBox44
            self.btnTreeViewColor.Left = 2
            self.btnTreeViewColor.Top = 142
            self.btnTreeViewColor.Width = 260
            self.btnTreeViewColor.Height = 25
            self.btnTreeViewColor.Cursor = crArrow
            self.btnTreeViewColor.Align = "alTop"
            self.btnTreeViewColor.Caption = 'Set Color'
            self.btnTreeViewColor.TabOrder = 3
            # Create control: btnTreeViewImageIndex = Button(self)
            self.btnTreeViewImageIndex = Button(self)
            self.btnTreeViewImageIndex.Name = "btnTreeViewImageIndex"
            self.btnTreeViewImageIndex.Parent = self.GroupBox44
            self.btnTreeViewImageIndex.Left = 2
            self.btnTreeViewImageIndex.Top = 167
            self.btnTreeViewImageIndex.Width = 260
            self.btnTreeViewImageIndex.Height = 25
            self.btnTreeViewImageIndex.Cursor = crArrow
            self.btnTreeViewImageIndex.Align = "alTop"
            self.btnTreeViewImageIndex.Caption = 'Toggle ImageIndex'
            self.btnTreeViewImageIndex.TabOrder = 4
            # Create control: btnTreeViewCheckbox = Button(self)
            self.btnTreeViewCheckbox = Button(self)
            self.btnTreeViewCheckbox.Name = "btnTreeViewCheckbox"
            self.btnTreeViewCheckbox.Parent = self.GroupBox44
            self.btnTreeViewCheckbox.Left = 2
            self.btnTreeViewCheckbox.Top = 192
            self.btnTreeViewCheckbox.Width = 260
            self.btnTreeViewCheckbox.Height = 25
            self.btnTreeViewCheckbox.Cursor = crArrow
            self.btnTreeViewCheckbox.Align = "alTop"
            self.btnTreeViewCheckbox.Caption = 'Toggle Checkbox'
            self.btnTreeViewCheckbox.TabOrder = 8
            # Create control: trv = TreeView(self)
            self.trv = TreeView(self)
            self.trv.Name = "trv"
            self.trv.Parent = self.shtTreeView
            self.trv.Left = 48
            self.trv.Top = 24
            self.trv.Width = 328
            self.trv.Height = 248
            self.trv.Cursor = crArrow
            self.trv.Indent = 19
            self.trv.TabOrder = 1
            # Create control: shtTreeList = TabSheet(self)
            self.shtTreeList = TabSheet(self)
            self.shtTreeList.Name = "shtTreeList"
            self.shtTreeList.PageControl = self.pgFeatures
            self.shtTreeList.Cursor = crArrow
            self.shtTreeList.Caption = 'Tree List'
            # Create control: GroupBox45 = GroupBox(self)
            self.GroupBox45 = GroupBox(self)
            self.GroupBox45.Name = "GroupBox45"
            self.GroupBox45.Parent = self.shtTreeList
            self.GroupBox45.Left = 1123
            self.GroupBox45.Top = 0
            self.GroupBox45.Width = 264
            self.GroupBox45.Height = 308
            self.GroupBox45.Cursor = crArrow
            self.GroupBox45.Margins.Left = 4
            self.GroupBox45.Margins.Top = 4
            self.GroupBox45.Margins.Right = 4
            self.GroupBox45.Margins.Bottom = 4
            self.GroupBox45.Align = "alRight"
            self.GroupBox45.Caption = 'Control Usages'
            self.GroupBox45.TabOrder = 0
            # Create control: btnAddNode = Button(self)
            self.btnAddNode = Button(self)
            self.btnAddNode.Name = "btnAddNode"
            self.btnAddNode.Parent = self.GroupBox45
            self.btnAddNode.Left = 2
            self.btnAddNode.Top = 17
            self.btnAddNode.Width = 260
            self.btnAddNode.Height = 25
            self.btnAddNode.Cursor = crArrow
            self.btnAddNode.Margins.Left = 5
            self.btnAddNode.Margins.Top = 5
            self.btnAddNode.Margins.Right = 5
            self.btnAddNode.Margins.Bottom = 5
            self.btnAddNode.Align = "alTop"
            self.btnAddNode.Caption = 'Add Nodes'
            self.btnAddNode.TabOrder = 5
            # Create control: btnAddSubNodes = Button(self)
            self.btnAddSubNodes = Button(self)
            self.btnAddSubNodes.Name = "btnAddSubNodes"
            self.btnAddSubNodes.Parent = self.GroupBox45
            self.btnAddSubNodes.Left = 2
            self.btnAddSubNodes.Top = 42
            self.btnAddSubNodes.Width = 260
            self.btnAddSubNodes.Height = 25
            self.btnAddSubNodes.Cursor = crArrow
            self.btnAddSubNodes.Margins.Left = 5
            self.btnAddSubNodes.Margins.Top = 5
            self.btnAddSubNodes.Margins.Right = 5
            self.btnAddSubNodes.Margins.Bottom = 5
            self.btnAddSubNodes.Align = "alTop"
            self.btnAddSubNodes.Caption = 'Add Sub Nodes'
            self.btnAddSubNodes.TabOrder = 6
            # Create control: btnGetValue = Button(self)
            self.btnGetValue = Button(self)
            self.btnGetValue.Name = "btnGetValue"
            self.btnGetValue.Parent = self.GroupBox45
            self.btnGetValue.Left = 2
            self.btnGetValue.Top = 67
            self.btnGetValue.Width = 260
            self.btnGetValue.Height = 25
            self.btnGetValue.Cursor = crArrow
            self.btnGetValue.Margins.Left = 5
            self.btnGetValue.Margins.Top = 5
            self.btnGetValue.Margins.Right = 5
            self.btnGetValue.Margins.Bottom = 5
            self.btnGetValue.Align = "alTop"
            self.btnGetValue.Caption = 'Get Value'
            self.btnGetValue.TabOrder = 0
            # Create control: btnSetValue = Button(self)
            self.btnSetValue = Button(self)
            self.btnSetValue.Name = "btnSetValue"
            self.btnSetValue.Parent = self.GroupBox45
            self.btnSetValue.Left = 2
            self.btnSetValue.Top = 92
            self.btnSetValue.Width = 260
            self.btnSetValue.Height = 25
            self.btnSetValue.Cursor = crArrow
            self.btnSetValue.Margins.Left = 5
            self.btnSetValue.Margins.Top = 5
            self.btnSetValue.Margins.Right = 5
            self.btnSetValue.Margins.Bottom = 5
            self.btnSetValue.Align = "alTop"
            self.btnSetValue.Caption = 'Set Value'
            self.btnSetValue.TabOrder = 1
            # Create control: btnCollapseAll = Button(self)
            self.btnCollapseAll = Button(self)
            self.btnCollapseAll.Name = "btnCollapseAll"
            self.btnCollapseAll.Parent = self.GroupBox45
            self.btnCollapseAll.Left = 2
            self.btnCollapseAll.Top = 117
            self.btnCollapseAll.Width = 260
            self.btnCollapseAll.Height = 25
            self.btnCollapseAll.Cursor = crArrow
            self.btnCollapseAll.Margins.Left = 5
            self.btnCollapseAll.Margins.Top = 5
            self.btnCollapseAll.Margins.Right = 5
            self.btnCollapseAll.Margins.Bottom = 5
            self.btnCollapseAll.Align = "alTop"
            self.btnCollapseAll.Caption = 'Collapse All'
            self.btnCollapseAll.TabOrder = 2
            # Create control: btnExpandAll = Button(self)
            self.btnExpandAll = Button(self)
            self.btnExpandAll.Name = "btnExpandAll"
            self.btnExpandAll.Parent = self.GroupBox45
            self.btnExpandAll.Left = 2
            self.btnExpandAll.Top = 142
            self.btnExpandAll.Width = 260
            self.btnExpandAll.Height = 25
            self.btnExpandAll.Cursor = crArrow
            self.btnExpandAll.Margins.Left = 5
            self.btnExpandAll.Margins.Top = 5
            self.btnExpandAll.Margins.Right = 5
            self.btnExpandAll.Margins.Bottom = 5
            self.btnExpandAll.Align = "alTop"
            self.btnExpandAll.Caption = 'Expand All'
            self.btnExpandAll.TabOrder = 3
            # Create control: btnChangeImageIdx = Button(self)
            self.btnChangeImageIdx = Button(self)
            self.btnChangeImageIdx.Name = "btnChangeImageIdx"
            self.btnChangeImageIdx.Parent = self.GroupBox45
            self.btnChangeImageIdx.Left = 2
            self.btnChangeImageIdx.Top = 167
            self.btnChangeImageIdx.Width = 260
            self.btnChangeImageIdx.Height = 25
            self.btnChangeImageIdx.Cursor = crArrow
            self.btnChangeImageIdx.Margins.Left = 5
            self.btnChangeImageIdx.Margins.Top = 5
            self.btnChangeImageIdx.Margins.Right = 5
            self.btnChangeImageIdx.Margins.Bottom = 5
            self.btnChangeImageIdx.Align = "alTop"
            self.btnChangeImageIdx.Caption = 'Change ImageIndex'
            self.btnChangeImageIdx.TabOrder = 4
            # Create control: btnSetColumn = Button(self)
            self.btnSetColumn = Button(self)
            self.btnSetColumn.Name = "btnSetColumn"
            self.btnSetColumn.Parent = self.GroupBox45
            self.btnSetColumn.Left = 2
            self.btnSetColumn.Top = 192
            self.btnSetColumn.Width = 260
            self.btnSetColumn.Height = 25
            self.btnSetColumn.Cursor = crArrow
            self.btnSetColumn.Margins.Left = 5
            self.btnSetColumn.Margins.Top = 5
            self.btnSetColumn.Margins.Right = 5
            self.btnSetColumn.Margins.Bottom = 5
            self.btnSetColumn.Align = "alTop"
            self.btnSetColumn.Caption = 'Set Column'
            self.btnSetColumn.TabOrder = 7
            # Create control: TSTreelist1 = TSTreelist(self)
            self.TSTreelist1 = TSTreelist(self)
            self.TSTreelist1.Name = "TSTreelist1"
            self.TSTreelist1.Parent = self.shtTreeList
            self.TSTreelist1.AlignWithMargins = True
            self.TSTreelist1.Left = 3
            self.TSTreelist1.Top = 3
            self.TSTreelist1.Width = 1117
            self.TSTreelist1.Height = 302
            self.TSTreelist1.Cursor = crArrow
            self.TSTreelist1.Align = "alClient"
            self.TSTreelist1.Images = app.get_system_imagelist_16px()
            self.TSTreelist1.OptionsBehavior.CellHints = True
            self.TSTreelist1.OptionsCustomizing.ColumnVertSizing = False
            self.TSTreelist1.OptionsSelection.MultiSelect = True
            self.TSTreelist1.OptionsView.ColumnAutoWidth = True
            self.TSTreelist1.TabOrder = 1
            # Create control: TSTreelist1Column1 = self.TSTreelist1.CreateColumn(None)
            self.TSTreelist1Column1 = self.TSTreelist1.CreateColumn(None)
            self.TSTreelist1Column1.Name = "TSTreelist1Column1"
            self.TSTreelist1Column1.PropertiesClassName = 'TcxImageComboBoxProperties'
            self.TSTreelist1Column1.Caption.AlignHorz = "taCenter"
            self.TSTreelist1Column1.Caption.Text = 'Image Column'
            self.TSTreelist1Column1.MinWidth = 13
            self.TSTreelist1Column1.Options.VertSizing = False
            self.TSTreelist1Column1.Width = 67
            self.TSTreelist1Column1.Position.ColIndex = 0
            self.TSTreelist1Column1.Position.RowIndex = 0
            self.TSTreelist1Column1.Position.BandIndex = 0
            # Create control: TSTreelist1Column2 = self.TSTreelist1.CreateColumn(None)
            self.TSTreelist1Column2 = self.TSTreelist1.CreateColumn(None)
            self.TSTreelist1Column2.Name = "TSTreelist1Column2"
            self.TSTreelist1Column2.PropertiesClassName = 'TcxCheckBoxProperties'
            self.TSTreelist1Column2.Properties.ImmediatePost = True
            self.TSTreelist1Column2.Caption.AlignHorz = "taCenter"
            self.TSTreelist1Column2.Caption.Text = 'Check Box Column'
            self.TSTreelist1Column2.MinWidth = 13
            self.TSTreelist1Column2.Options.VertSizing = False
            self.TSTreelist1Column2.Width = 67
            self.TSTreelist1Column2.Position.ColIndex = 1
            self.TSTreelist1Column2.Position.RowIndex = 0
            self.TSTreelist1Column2.Position.BandIndex = 0
            # Create control: TSTreelist1Column3 = self.TSTreelist1.CreateColumn(None)
            self.TSTreelist1Column3 = self.TSTreelist1.CreateColumn(None)
            self.TSTreelist1Column3.Name = "TSTreelist1Column3"
            self.TSTreelist1Column3.PropertiesClassName = 'TcxTextEditProperties'
            self.TSTreelist1Column3.Properties.UseLeftAlignmentOnEditing = False
            self.TSTreelist1Column3.Caption.AlignHorz = "taCenter"
            self.TSTreelist1Column3.Caption.Text = 'Text Edit Column'
            self.TSTreelist1Column3.MinWidth = 13
            self.TSTreelist1Column3.Options.VertSizing = False
            self.TSTreelist1Column3.Width = 67
            self.TSTreelist1Column3.Position.ColIndex = 2
            self.TSTreelist1Column3.Position.RowIndex = 0
            self.TSTreelist1Column3.Position.BandIndex = 0
        finally:
            # End UI auto creation
            self.EndUIAutoCreation()
        # Auto Generated Python Code, do not modify END [UI] ----------------
        global f
        f = self
        self.FRecvCANCounter = 0
        self.FShowHideCounter = 3
        self.FNeedRefresh = True
        self.btnHide.OnClick = self.btnHideClick
        self.Caption = "This is a simple guide for TSMaster toolbox built with Python"
        self.OnRefreshEvent = self.UIRefreshEvent
        self.OnRawCANEvent = self.RawCANEvent
        self.OnResize = self.OnFormResizeEvent
        # self.OnShow = self.OnFormShowEvent
        self.OnHide = self.OnFormHideEvent
        self.OnMeasurementStartedEvent = self.MeasurementStarted
        self.OnMeasurementStoppedEvent = self.MeasurementStopped
        self.OnMeasurementPreStartEvent = self.MeasurementPreStart
        self.OnMeasurementPreStopEvent = self.MeasurementPreStop
        self.tim1 = Timer(self)
        self.tim1.Interval = 2000
        self.tim1.OnTimer = self.OnShowTimer
        self.tim1.Enabled = False

        def OnFormFinalize():
            global f
            f = None

        self.OnFinalizationEvent = OnFormFinalize
        # form set bounds
        def OnSetFormBoundsClick(sender):
            self.InternalRunScript('f.SetBounds(10, 10, f.Width + 3, f.Height + 3)')
        self.btnSetBounds.OnClick = OnSetFormBoundsClick
        # form move left and right
        def OnMoveLeftEvent(sender):
            self.InternalRunScript('f.Left = f.Left - 10')
        def OnMoveRightEvent(sender):
            self.InternalRunScript('f.Left = f.Left + 10')
        self.btnMoveLeft.OnClick = OnMoveLeftEvent
        self.btnMoveRight.OnClick = OnMoveRightEvent
        # form log
        def OnLogClick(sender):
            self.InternalRunScript(
                'f.log("this is a normal log text")\r\nf.log_ok("this is a green log text (OK)")\r\nf.log_error("this is a red log text (Error)")\r\nf.log_warning("this is a blue log text (Warning)")\r\nf.log_hint("this is a yellow log text (Hint)")')
        self.btnLog.OnClick = OnLogClick
# form caption
        def OnSetCaptionClick(sender):
            self.InternalRunScript('f.Caption = str(app.get_timestamp_us())')
        self.btnSetCaption.OnClick = OnSetCaptionClick
        def OnGetCaptionClick(sender):
            self.InternalRunScript('ShowMessage(f.Caption)')
        self.btnGetCaption.OnClick = OnGetCaptionClick
# form handle
        def OnGetHandleClick(sender):
            self.InternalRunScript('ShowMessage("Form handle = " + str(f.Handle))')
        self.btnGetHandle.OnClick = OnGetHandleClick
# form toolbar buttons
        def OnToolbarRegClick(sender):
            self.InternalRunScript(
                'f.RegisterToolbarButton("Connect", 194, False).OnClick = f.OnConnectClick\r\nf.RegisterToolbarButton("Disconnect", 195, False).OnClick = f.OnDisconnectClick')
        self.btnToolbar.OnClick = OnToolbarRegClick
# form conf saving and loading
        def OnConfSaveClick(sender):
            self.SetConfiguration('left_pos', str(self.Left))
            self.SetConfiguration('top_pos', str(self.Top))
            self.Left = 0
            self.Top = 0
            self.InternalRunScript('f.SaveConfigurations()')
        def OnConfLoadClick(sender):
            self.InternalRunScript('f.LoadConfigurations()')
            self.Left = int(self.GetConfiguration('left_pos', '0'))
            self.Top = int(self.GetConfiguration('top_pos', '0'))
        self.btnSaveConfiguration.OnClick = OnConfSaveClick
        self.btnLoadConfiguration.OnClick = OnConfLoadClick
# form conf clear and get set
        def OnConfClearClick(sender):
            self.ClearConfigurations()
        self.btnClearConf.OnClick = OnConfClearClick
        def OnConfSetClick(sender):
            self.InternalRunScript('f.SetConfiguration("x", "123")')
        def OnConfGetClick(sender):
            self.InternalRunScript('ShowMessage("x = " + f.GetConfiguration("x", "0"))')
        self.btnSetConfiguration.OnClick = OnConfSetClick
        self.btnGetConfiguration.OnClick = OnConfGetClick
        def OnConfLoadedClick(sender):
            self.InternalRunScript('ShowMessage("Is configuration loaded: " + str(f.IsConfigurationLoaded))')
        self.btnIsConfLoaded.OnClick = OnConfLoadedClick
# label
        def OnSetLabelBackColor(sender):
            self.InternalRunScript('f.lblLabel.Transparent = False\r\nf.lblLabel.Color = clGreen')
        self.btnSetLabelBackColor.OnClick = OnSetLabelBackColor
        def OnToggleLabelTransparencyClick(sender):
            self.InternalRunScript('f.lblLabel.Transparent = not f.lblLabel.Transparent')
        self.btnSetLabelTransparency.OnClick = OnToggleLabelTransparencyClick
        def OnSetLabelCaptionClick(sender):
            self.InternalRunScript('f.lblLabel.Caption = "This is a new caption string set by python"')
        self.btnSetLabelCaption.OnClick = OnSetLabelCaptionClick
        def OnSetLabelBoundsClick(sender):
            self.InternalRunScript('f.lblLabel.SetBounds(100, 100, 300, 100)')
        self.btnSetLabelBounds.OnClick = OnSetLabelBoundsClick
        def OnToggleLabelAutoSizeClick(sender):
            self.InternalRunScript('f.lblLabel.Width = 50\r\nf.lblLabel.AutoSize = not f.lblLabel.AutoSize')
        self.btnToggleLabelAutoSize.OnClick = OnToggleLabelAutoSizeClick
        def OnSetLabelFontClick(sender):
            self.InternalRunScript('f.lblLabel.Font.Color = clRed\r\nf.lblLabel.Font.Size = 20\r\nf.lblLabel.Font.Name = "Tahoma"')
        self.btnSetLabelFont.OnClick = OnSetLabelFontClick
        def OnToggleLabelEnabledClick(sender):
            self.InternalRunScript('f.lblLabel.Enabled = not f.lblLabel.Enabled')
        self.btnToggleLabelEnabled.OnClick = OnToggleLabelEnabledClick
        def OnToggleLabelVisibleClick(sender):
            self.InternalRunScript('f.lblLabel.Visible = not f.lblLabel.Visible')
        self.btnToggleLabelVisible.OnClick = OnToggleLabelVisibleClick
        def OnSetLabelAlignClick(sender):
            self.InternalRunScript('f.lblLabel.Align = "alTop"')
        self.btnSetLabelAlign.OnClick = OnSetLabelAlignClick
        def OnSetLabelAlignmentClick(sender):
            self.InternalRunScript('f.lblLabel.Alignment = "taCenter"')
        self.btnSetLabelAlignment.OnClick = OnSetLabelAlignmentClick
        def OnSetLabelMargins(sender):
            self.InternalRunScript(
                'f.lblLabel.AlignWithMargins = True\r\nf.lblLabel.Margins.Left = 100\r\nf.lblLabel.Margins.Top = 10\r\nf.lblLabel.Margins.Right = 100\r\nf.lblLabel.Margins.Bottom = 10')
        self.btnSetLabelMargins.OnClick = OnSetLabelMargins
        def OnSetLabelOnClickEventClick(sender):
            self.InternalRunScript(
                'f.lblLabel.OnClick = f.OnLabelClickEvent\r\n# Please click label to see what happens')
        self.btnSetLabelOnClickEvent.OnClick = OnSetLabelOnClickEventClick
# button
        def OnSetButtonCaptionClick(sender):
            self.InternalRunScript('f.btnButton.Caption = "This is a new caption set for button"')
        self.btnSetButtonCaption.OnClick = OnSetButtonCaptionClick
        def OnSetButtonBoundsClick(sender):
            self.InternalRunScript('f.btnButton.SetBounds(100, 100, 300, 50)')
        self.btnSetButtonBounds.OnClick = OnSetButtonBoundsClick
        def OnSetButtonFontClick(sender):
            self.InternalRunScript('f.btnButton.Font.Size = 14')
        self.btnSetButtonFont.OnClick = OnSetButtonFontClick
        def OnSetButtonEnabledClick(sender):
            self.InternalRunScript('f.btnButton.Enabled = not f.btnButton.Enabled')
        self.btnToggleButtonEnabled.OnClick = OnSetButtonEnabledClick
        def OnToggleButtonVisibleClick(sender):
            self.InternalRunScript('f.btnButton.Visible = not f.btnButton.Visible')
        self.btnToggleButtonVisible.OnClick = OnToggleButtonVisibleClick
        def OnSetButtonAlignClick(sender):
            self.InternalRunScript('f.btnButton.Align = "alLeft"')
        self.btnSetButtonAlign.OnClick = OnSetButtonAlignClick
        def OnSetButtonMarginsClick(sender):
            self.InternalRunScript('f.btnButton.AlignWithMargins = True\r\nf.btnButton.Margins.Left = 12')
        self.btnSetButtonMargins.OnClick = OnSetButtonMarginsClick
        def OnSetButtonClickEventClick(sender):
            self.InternalRunScript('f.btnButton.OnClick = f.OnButtonClickEvent\r\n# Please click button to see what happens')
        self.btnSetButtonOnClickEvent.OnClick = OnSetButtonClickEventClick
        def OnSetButtonImageClick(sender):
            self.InternalRunScript('f.btnButton.Images = app.get_system_imagelist_16px()\r\nf.btnButton.ImageIndex = 12')
        self.btnSetButtonImage.OnClick = OnSetButtonImageClick
# Edit
        def OnSetEditTextClick(sender):
            self.InternalRunScript('f.edtEdit.Text = "a new text"')
        self.btnSetEditText.OnClick = OnSetEditTextClick
        def OnSetEditBoundsClick(sender):
            self.InternalRunScript('f.edtEdit.SetBounds(100, 100, 300, 50)')
        self.btnSetEditBounds.OnClick = OnSetEditBoundsClick
        def OnSetEditFontClick(sender):
            self.InternalRunScript('f.edtEdit.Font.Size = 14')
        self.btnSetEditFont.OnClick = OnSetEditFontClick
        def OnSetEditEnabledClick(sender):
            self.InternalRunScript('f.edtEdit.Enabled = not f.edtEdit.Enabled')
        self.btnToggleEditEnabled.OnClick = OnSetEditEnabledClick
        def OnToggleEditVisibleClick(sender):
            self.InternalRunScript('f.edtEdit.Visible = not f.edtEdit.Visible')
        self.btnToggleEditVisible.OnClick = OnToggleEditVisibleClick
        def OnSetEditAlignmentClick(sender):
            self.InternalRunScript('f.edtEdit.Alignment = "taCenter"')
        self.btnSetEditTextAlignment.OnClick = OnSetEditAlignmentClick
        def OnSetEditAlignClick(sender):
            self.InternalRunScript('f.edtEdit.Align = "alLeft"')
        self.btnSetEditAlign.OnClick = OnSetEditAlignClick
        def OnSetEditMarginsClick(sender):
            self.InternalRunScript('f.edtEdit.AlignWithMargins = True\r\nf.edtEdit.Margins.Left = 12')
        self.btnSetEditMargins.OnClick = OnSetEditMarginsClick
        def OnSetEditClickEventClick(sender):
            self.InternalRunScript('f.edtEdit.OnClick = f.OnEditClickEvent\r\n# Please click edit to see what happens')
        self.btnSetEditClickEvent.OnClick = OnSetEditClickEventClick
        def OnSetEditChangeEventClick(sender):
            self.InternalRunScript('f.edtEdit.OnChange = f.OnEditChangeEvent\r\n# Please modify edit to see what happens')
        self.btnSetOnEditChangeEvent.OnClick = OnSetEditChangeEventClick
        def OnSetEditTextHintClick(sender):
            self.InternalRunScript('f.edtEdit.ShowHint = True\r\nf.edtEdit.TextHint = "this is a text hint"\r\n# Please clear this edit and kill focus to show text hint')
        self.btnSetEditTextHint.OnClick = OnSetEditTextHintClick
        def OnSetEditNumbersOnlyClick(sender):
            self.InternalRunScript('f.edtEdit.NumbersOnly = True')
        self.btnSetEditNumbersOnly.OnClick = OnSetEditNumbersOnlyClick
        def OnSetEditReadOnlyClick(sender):
            self.InternalRunScript('f.edtEdit.ReadOnly = True')
        self.btnSetEditReadOnly.OnClick = OnSetEditReadOnlyClick
# Checkbox
        def OnSetCheckboxTextClick(sender):
            self.InternalRunScript('f.chkCheckbox.Caption = "a new check box caption"')
        self.btnSetCheckboxText.OnClick = OnSetCheckboxTextClick
        def OnSetCheckboxBoundsClick(sender):
            self.InternalRunScript('f.chkCheckbox.SetBounds(100, 100, 300, 50)')
        self.btnSetCheckboxBounds.OnClick = OnSetCheckboxBoundsClick
        def OnSetCheckboxFontClick(sender):
            self.InternalRunScript('f.chkCheckbox.Font.Size = 14')
        self.btnSetCheckboxFont.OnClick = OnSetCheckboxFontClick
        def OnSetCheckboxEnabledClick(sender):
            self.InternalRunScript('f.chkCheckbox.Enabled = not f.chkCheckbox.Enabled')
        self.btnToggleCheckboxEnabled.OnClick = OnSetCheckboxEnabledClick
        def OnToggleCheckboxVisibleClick(sender):
            self.InternalRunScript('f.chkCheckbox.Visible = not f.chkCheckbox.Visible')
        self.btnToggleCheckboxVisible.OnClick = OnToggleCheckboxVisibleClick
        def OnSetCheckboxAlignClick(sender):
            self.InternalRunScript('f.chkCheckbox.Align = "alLeft"')
        self.btnSetCheckboxAlign.OnClick = OnSetCheckboxAlignClick
        def OnSetCheckboxMarginsClick(sender):
            self.InternalRunScript('f.chkCheckbox.AlignWithMargins = True\r\nf.chkCheckbox.Margins.Left = 12')
        self.btnSetCheckboxMargins.OnClick = OnSetCheckboxMarginsClick
        def OnSetCheckboxClickEventClick(sender):
            self.InternalRunScript('f.chkCheckbox.OnClick = f.OnCheckboxClickEvent\r\n# Please click Checkbox to see what happens')
        self.btnSetCheckboxOnClickEvent.OnClick = OnSetCheckboxClickEventClick
        def ONToggleCheckboxCheckedClick(sender):
            self.InternalRunScript('f.chkCheckbox.Checked = not f.chkCheckbox.Checked')
        self.btnToggleCheckboxChecked.OnClick = ONToggleCheckboxCheckedClick
# Radio Button
        def OnSetRadioButtonTextClick(sender):
            self.InternalRunScript('f.rb1.Caption = "a new caption 1"\r\nf.rb2.Caption = "a new caption 2"')
        self.btnSetRadioButtonText.OnClick = OnSetRadioButtonTextClick
        def OnSetRadioButtonBoundsClick(sender):
            self.InternalRunScript('f.rb1.SetBounds(100, 100, 300, 50)\r\nf.rb2.SetBounds(100, 200, 300, 50)')
        self.btnSetRadioButtonBounds.OnClick = OnSetRadioButtonBoundsClick
        def OnSetRadioButtonFontClick(sender):
            self.InternalRunScript('f.rb1.Font.Size = 14\r\nf.rb2.Font.Size = 14')
        self.btnSetRadioButtonFont.OnClick = OnSetRadioButtonFontClick
        def OnSetRadioButtonEnabledClick(sender):
            self.InternalRunScript('f.rb1.Enabled = not f.rb1.Enabled')
        self.btnToggleRadioButtonEnabled.OnClick = OnSetRadioButtonEnabledClick
        def OnToggleRadioButtonVisibleClick(sender):
            self.InternalRunScript('f.rb2.Visible = not f.rb2.Visible')
        self.btnToggleRadioButtonVisible.OnClick = OnToggleRadioButtonVisibleClick
        def OnSetRadioButtonAlignClick(sender):
            self.InternalRunScript('f.rb1.Align = "alTop"\r\nf.rb2.Align = "alTop"')
        self.btnSetRadioButtonAlign.OnClick = OnSetRadioButtonAlignClick
        def OnSetRadioButtonMarginsClick(sender):
            self.InternalRunScript('f.rb1.AlignWithMargins = True\r\nf.rb2.AlignWithMargins = True')
        self.btnSetRadioButtonMargins.OnClick = OnSetRadioButtonMarginsClick
        def OnSetRadioButtonClickEventClick(sender):
            self.InternalRunScript('f.rb1.OnClick = f.OnRadioButtonChangeEvent\r\nf.rb2.OnClick = f.OnRadioButtonChangeEvent\r\n# Please check Radio Button 1 to see what happens')
        self.btnSetRadioButtonOnChangeEvent.OnClick = OnSetRadioButtonClickEventClick
        def ONToggleRadioButtonCheckedClick(sender):
            self.InternalRunScript('f.rb1.Checked = not f.rb1.Checked')
        self.btnToggleRadioButtonCheckedState.OnClick = ONToggleRadioButtonCheckedClick
# Memo
        def OnSetMemoTextClick(sender):
            self.InternalRunScript('f.mmMemo.Text = "a new text"')
        self.btnSetMemoText.OnClick = OnSetMemoTextClick
        def OnSetMemoBoundsClick(sender):
            self.InternalRunScript('f.mmMemo.SetBounds(100, 100, 300, 50)')
        self.btnSetMemoBounds.OnClick = OnSetMemoBoundsClick
        def OnSetMemoFontClick(sender):
            self.InternalRunScript('f.mmMemo.Font.Size = 14')
        self.btnSetMemoFont.OnClick = OnSetMemoFontClick
        def OnSetMemoEnabledClick(sender):
            self.InternalRunScript('f.mmMemo.Enabled = not f.mmMemo.Enabled')
        self.btnToggleMemoEnabled.OnClick = OnSetMemoEnabledClick
        def OnToggleMemoVisibleClick(sender):
            self.InternalRunScript('f.mmMemo.Visible = not f.mmMemo.Visible')
        self.btnToggleMemoVisible.OnClick = OnToggleMemoVisibleClick
        def OnSetMemoAlignClick(sender):
            self.InternalRunScript('f.mmMemo.Align = "alClient"')
        self.btnSetMemoAlign.OnClick = OnSetMemoAlignClick
        def OnSetMemoMarginsClick(sender):
            self.InternalRunScript('f.mmMemo.AlignWithMargins = True')
        self.btnSetMemoMargins.OnClick = OnSetMemoMarginsClick
        def OnSetMemoClickEventClick(sender):
            self.InternalRunScript('f.mmMemo.OnChange = f.OnMemoChangeEvent\r\n# Please modify memo text to see what happens')
        self.btnSetMemoOnChangeEvent.OnClick = OnSetMemoClickEventClick
# Combobox
        def OnSetComboItemsClick(sender):
            self.InternalRunScript('f.cbCombo.Items.StrictDelimiter = True\r\nf.cbCombo.Items.CommaText = "item 1,item 2,item 3,item 4"\r\nf.cbCombo.ItemIndex = 0')
        self.btnComboSetText.OnClick = OnSetComboItemsClick
        def OnGetComboItemsClick(sender):
            self.InternalRunScript('ShowMessage("item index is: " + str(f.cbCombo.ItemIndex))')
        self.btnComboGetItemIndex.OnClick = OnGetComboItemsClick
        def OnSetComboItemIndexClick(sender):
            self.InternalRunScript('f.cbCombo.ItemIndex = 2')
        self.btnComboSetItemIndex.OnClick = OnSetComboItemIndexClick
        def OnSetComboBoundsClick(sender):
            self.InternalRunScript('f.cbCombo.SetBounds(100, 100, 300, 50)')
        self.btnComboSetBounds.OnClick = OnSetComboBoundsClick
        def OnSetComboFontClick(sender):
            self.InternalRunScript('f.cbCombo.Font.Size = 14')
        self.btnComboSetFont.OnClick = OnSetComboFontClick
        def OnSetComboEnabledClick(sender):
            self.InternalRunScript('f.cbCombo.Enabled = not f.cbCombo.Enabled')
        self.btnComboToggleEnabled.OnClick = OnSetComboEnabledClick

        def OnToggleComboVisibleClick(sender):
            self.InternalRunScript('f.cbCombo.Visible = not f.cbCombo.Visible')
        self.btnComboToggleVisible.OnClick = OnToggleComboVisibleClick
        def OnSetComboAlignClick(sender):
            self.InternalRunScript('f.cbCombo.Align = "alLeft"')
        self.btnComboSetAlign.OnClick = OnSetComboAlignClick
        def OnSetComboMarginsClick(sender):
            self.InternalRunScript('f.cbCombo.AlignWithMargins = True')
        self.btnComboSetMargins.OnClick = OnSetComboMarginsClick
        def OnSetComboChangeEventClick(sender):
            self.InternalRunScript('f.cbCombo.OnChange = f.OnComboChangeEvent\r\n# Please modify combo index to see what happens')
        self.btnComboSetOnChangeEvent.OnClick = OnSetComboChangeEventClick
# Listbox
        def OnSetListBoxItemsClick(sender):
            self.InternalRunScript('f.lstListBox.Items.StrictDelimiter = True\r\nf.lstListBox.Items.CommaText = "item 1,item 2,item 3,item 4"\r\nf.lstListBox.ItemIndex = 0')
        self.btnListBoxSetItems.OnClick = OnSetListBoxItemsClick
        def OnGetListBoxItemIndexClick(sender):
            self.InternalRunScript('ShowMessage("item index is: " + str(f.lstListBox.ItemIndex))')
        self.btnListBoxGetItemIndex.OnClick = OnGetListBoxItemIndexClick
        def OnSetListBoxItemIndexClick(sender):
            self.InternalRunScript('f.lstListBox.ItemIndex = 2')
        self.btnListBoxSetItemIndex.OnClick = OnSetListBoxItemIndexClick
        def OnSetListBoxBoundsClick(sender):
            self.InternalRunScript('f.lstListBox.SetBounds(100, 100, 300, 50)')
        self.btnListBoxSetBounds.OnClick = OnSetListBoxBoundsClick
        def OnSetListBoxFontClick(sender):
            self.InternalRunScript('f.lstListBox.Font.Size = 14')
        self.btnListBoxSetFont.OnClick = OnSetListBoxFontClick
        def OnSetListBoxEnabledClick(sender):
            self.InternalRunScript('f.lstListBox.Enabled = not f.lstListBox.Enabled')
        self.btnListBoxToggleEnabled.OnClick = OnSetListBoxEnabledClick
        def OnToggleListBoxVisibleClick(sender):
            self.InternalRunScript('f.lstListBox.Visible = not f.lstListBox.Visible')
        self.btnListBoxToggleVisible.OnClick = OnToggleListBoxVisibleClick
        def OnSetListBoxAlignClick(sender):
            self.InternalRunScript('f.lstListBox.Align = "alLeft"')
        self.btnListBoxSetAlign.OnClick = OnSetListBoxAlignClick
        def OnSetListBoxMarginsClick(sender):
            self.InternalRunScript('f.lstListBox.AlignWithMargins = True')
        self.btnListBoxSetMargins.OnClick = OnSetListBoxMarginsClick
        def OnSetListBoxChangeEventClick(sender):
            self.InternalRunScript('f.lstListBox.OnClick = f.OnListBoxChangeEvent\r\n# Please modify ListBox index to see what happens')
        self.btnListBoxSetOnChangeEvent.OnClick = OnSetListBoxChangeEventClick
# static text
        def OnSetStaticTextBkgdColor(sender):
            self.InternalRunScript('f.stStaticText.Transparent = False\r\nf.stStaticText.Color = clGreen')
        self.btnStaticTextSetBkgdColor.OnClick = OnSetStaticTextBkgdColor
        def OnSetStaticTextBorderStyle(sender):
            self.InternalRunScript('f.stStaticText.BorderStyle = "sbsSunken"')
        self.btnStaticTextSetBorderStyle.OnClick = OnSetStaticTextBorderStyle
        def OnToggleStaticTextTransparencyClick(sender):
            self.InternalRunScript('f.stStaticText.Transparent = not f.stStaticText.Transparent')
        self.btnStaticTextToggleTransparency.OnClick = OnToggleStaticTextTransparencyClick
        def OnSetStaticTextCaptionClick(sender):
            self.InternalRunScript('f.stStaticText.Caption = "This is a new caption string set by python"')
        self.btnStaticTextSetCaption.OnClick = OnSetStaticTextCaptionClick
        def OnSetStaticTextBoundsClick(sender):
            self.InternalRunScript('f.stStaticText.SetBounds(100, 100, 300, 100)')
        self.btnStaticTextSetBounds.OnClick = OnSetStaticTextBoundsClick
        def OnToggleStaticTextAutoSizeClick(sender):
            self.InternalRunScript('f.stStaticText.Width = 50\r\nf.stStaticText.AutoSize = not f.stStaticText.AutoSize')
        self.btnStaticTextToggleAutoSize.OnClick = OnToggleStaticTextAutoSizeClick
        def OnSetStaticTextFontClick(sender):
            self.InternalRunScript('f.stStaticText.Font.Color = clRed\r\nf.stStaticText.Font.Size = 20\r\nf.stStaticText.Font.Name = "Tahoma"')
        self.btnStaticTextSetFont.OnClick = OnSetStaticTextFontClick
        def OnToggleStaticTextEnabledClick(sender):
            self.InternalRunScript('f.stStaticText.Enabled = not f.stStaticText.Enabled')
        self.btnStaticTextToggleEnabled.OnClick = OnToggleStaticTextEnabledClick
        def OnToggleStaticTextVisibleClick(sender):
            self.InternalRunScript('f.stStaticText.Visible = not f.stStaticText.Visible')
        self.btnStaticTextToggleVisible.OnClick = OnToggleStaticTextVisibleClick
        def OnSetStaticTextAlignClick(sender):
            self.InternalRunScript('f.stStaticText.Align = "alTop"')
        self.btnStaticTextSetAlign.OnClick = OnSetStaticTextAlignClick
        def OnSetStaticTextAlignmentClick(sender):
            self.InternalRunScript('f.stStaticText.Alignment = "taCenter"')
        self.btnStaticTextSetAlignment.OnClick = OnSetStaticTextAlignmentClick
        def OnSetStaticTextMargins(sender):
            self.InternalRunScript('f.stStaticText.AlignWithMargins = True\r\nf.stStaticText.Margins.Left = 100\r\nf.stStaticText.Margins.Top = 10\r\nf.stStaticText.Margins.Right = 100\r\nf.stStaticText.Margins.Bottom = 10')
        self.btnStaticTextSetMargins.OnClick = OnSetStaticTextMargins
        def OnSetStaticTextOnClickEventClick(sender):
            self.InternalRunScript('f.stStaticText.OnClick = f.OnStaticTextClickEvent\r\n# Please click Static Text to see what happens')
        self.btnStaticTextSetClickEvent.OnClick = OnSetStaticTextOnClickEventClick
# Group box
        def OnSetGroupBoxCaptionClick(sender):
            self.InternalRunScript('f.grpGroupBox.Caption = "This is a new caption string set by python"')
        self.btnGroupBoxSetCaption.OnClick = OnSetGroupBoxCaptionClick
        def OnSetGroupBoxBoundsClick(sender):
            self.InternalRunScript('f.grpGroupBox.SetBounds(100, 100, 300, 100)')
        self.btnGroupBoxSetBounds.OnClick = OnSetGroupBoxBoundsClick
        def OnSetGroupBoxFontClick(sender):
            self.InternalRunScript('f.grpGroupBox.Font.Color = clRed\r\nf.grpGroupBox.Font.Size = 20\r\nf.grpGroupBox.Font.Name = "Tahoma"')
        self.btnGroupBoxSetFont.OnClick = OnSetGroupBoxFontClick
        def OnToggleGroupBoxEnabledClick(sender):
            self.InternalRunScript('f.grpGroupBox.Enabled = not f.grpGroupBox.Enabled')
        self.btnGroupBoxToggleEnabled.OnClick = OnToggleGroupBoxEnabledClick
        def OnToggleGroupBoxVisibleClick(sender):
            self.InternalRunScript('f.grpGroupBox.Visible = not f.grpGroupBox.Visible')
        self.btnGroupBoxToggleVisible.OnClick = OnToggleGroupBoxVisibleClick
        def OnToggleGroupBoxFrameClick(sender):
            self.InternalRunScript('f.grpGroupBox.ShowFrame = not f.grpGroupBox.ShowFrame')
        self.btnGroupBoxToggleFrame.OnClick = OnToggleGroupBoxFrameClick
        def OnSetGroupBoxAlignClick(sender):
            self.InternalRunScript('f.grpGroupBox.Align = "alTop"')
        self.btnGroupBoxSetAlign.OnClick = OnSetGroupBoxAlignClick
        def OnSetGroupBoxMargins(sender):
            self.InternalRunScript('f.grpGroupBox.AlignWithMargins = True\r\nf.grpGroupBox.Margins.Left = 100\r\nf.grpGroupBox.Margins.Top = 10\r\nf.grpGroupBox.Margins.Right = 100\r\nf.grpGroupBox.Margins.Bottom = 10')
        self.btnGroupBoxSetMargins.OnClick = OnSetGroupBoxMargins
# Panel
        def OnSetPanelCaptionClick(sender):
            self.InternalRunScript('f.pnlPanel.Caption = "This is a new caption string set by python"')
        self.btnPanelSetCaption.OnClick = OnSetPanelCaptionClick
        def OnSetPanelBoundsClick(sender):
            self.InternalRunScript('f.pnlPanel.SetBounds(100, 100, 300, 100)')
        self.btnPanelSetBounds.OnClick = OnSetPanelBoundsClick
        def OnSetPanelFontClick(sender):
            self.InternalRunScript('f.pnlPanel.Font.Color = clRed\r\nf.pnlPanel.Font.Size = 20\r\nf.pnlPanel.Font.Name = "Tahoma"')
        self.btnPanelSetFont.OnClick = OnSetPanelFontClick
        def OnSetPanelBorderStyleClick(sender):
            self.InternalRunScript('if f.pnlPanel.BorderStyle == "bsNone":\r\n  f.pnlPanel.BorderStyle = "bsSingle"\r\nelse:\r\n  f.pnlPanel.BorderStyle = "bsNone"')
        self.btnPanelSetBorderStyle.OnClick = OnSetPanelBorderStyleClick
        def OnSetPanelBevelClick(sender):
            self.InternalRunScript('f.pnlPanel.BevelKind = "bkTile"')
        self.btnPanelSetBevel.OnClick = OnSetPanelBevelClick
        def OnTogglePanelEnabledClick(sender):
            self.InternalRunScript('f.pnlPanel.Enabled = not f.pnlPanel.Enabled')
        self.btnPanelToggleEnabled.OnClick = OnTogglePanelEnabledClick
        def OnTogglePanelVisibleClick(sender):
            self.InternalRunScript('f.pnlPanel.Visible = not f.pnlPanel.Visible')
        self.btnPanelToggleVisible.OnClick = OnTogglePanelVisibleClick
        def OnSetPanelAlignClick(sender):
            self.InternalRunScript('f.pnlPanel.Align = "alTop"')
        self.btnPanelSetAlign.OnClick = OnSetPanelAlignClick
        def OnSetPanelMargins(sender):
            self.InternalRunScript(
                'f.pnlPanel.AlignWithMargins = True\r\nf.pnlPanel.Margins.Left = 100\r\nf.pnlPanel.Margins.Top = 10\r\nf.pnlPanel.Margins.Right = 100\r\nf.pnlPanel.Margins.Bottom = 10')
        self.btnPanelSetMargins.OnClick = OnSetPanelMargins
# Radio Group
        def OnSetRadioGroupCaptionClick(sender):
            self.InternalRunScript('f.rgRadioGroup.Caption = "This is a new caption string set by python"')
        self.btnRadioGroupSetCaption.OnClick = OnSetRadioGroupCaptionClick
        def OnSetRadioGroupItemsClick(sender):
            self.InternalRunScript(
                'f.rgRadioGroup.Items.CommaText = "btn1,btn2,btn3,btn4"\r\nf.rgRadioGroup.ItemIndex = -1')
        self.btnRadioGroupSetItems.OnClick = OnSetRadioGroupItemsClick
        def OnSetRadioGroupItemIndexClick(sender):
            self.InternalRunScript('f.rgRadioGroup.ItemIndex = 2')
        self.btnRadioGroupSetItemIndex.OnClick = OnSetRadioGroupItemIndexClick
        def OnSetRadioGroupBoundsClick(sender):
            self.InternalRunScript('f.rgRadioGroup.SetBounds(100, 100, 300, 100)')
        self.btnRadioGroupSetBounds.OnClick = OnSetRadioGroupBoundsClick
        def OnSetRadioGroupFontClick(sender):
            self.InternalRunScript('f.rgRadioGroup.Font.Color = clRed\r\nf.rgRadioGroup.Font.Size = 20\r\nf.rgRadioGroup.Font.Name = "Tahoma"')
        self.btnRadioGroupSetFont.OnClick = OnSetRadioGroupFontClick
        def OnToggleRadioGroupEnabledClick(sender):
            self.InternalRunScript('f.rgRadioGroup.Enabled = not f.rgRadioGroup.Enabled')
        self.btnRadioGroupToggleEnabled.OnClick = OnToggleRadioGroupEnabledClick
        def OnToggleRadioGroupVisibleClick(sender):
            self.InternalRunScript('f.rgRadioGroup.Visible = not f.rgRadioGroup.Visible')
        self.btnRadioGroupToggleVisible.OnClick = OnToggleRadioGroupVisibleClick
        def OnSetRadioGroupAlignClick(sender):
            self.InternalRunScript('f.rgRadioGroup.Align = "alLeft"')
        self.btnRadioGroupSetAlign.OnClick = OnSetRadioGroupAlignClick
        def OnSetRadioGroupMargins(sender):
            self.InternalRunScript('f.rgRadioGroup.AlignWithMargins = True\r\nf.rgRadioGroup.Margins.Left = 100\r\nf.rgRadioGroup.Margins.Top = 10\r\nf.rgRadioGroup.Margins.Right = 100\r\nf.rgRadioGroup.Margins.Bottom = 10')
        self.btnRadioGroupSetMargins.OnClick = OnSetRadioGroupMargins
        def OnSetRadioGroupOnClickClick(sender):
            self.InternalRunScript('f.rgRadioGroup.OnClick = f.OnRadioGroupClickEvent')
        self.btnSetRadioGroupOnClick.OnClick = OnSetRadioGroupOnClickClick
# Shape
        def OnSetShapeShapeClick(sender):
            self.InternalRunScript('f.spShape.Shape = "stEllipse"')
        self.btnShapeSetShape.OnClick = OnSetShapeShapeClick
        def OnSetShapeBoundsClick(sender):
            self.InternalRunScript('f.spShape.SetBounds(100, 100, 300, 100)')
        self.btnShapeSetBounds.OnClick = OnSetShapeBoundsClick
        def OnToggleShapeEnabledClick(sender):
            self.InternalRunScript('f.spShape.Enabled = not f.spShape.Enabled')
        self.btnShapeToggleEnabled.OnClick = OnToggleShapeEnabledClick
        def OnToggleShapeVisibleClick(sender):
            self.InternalRunScript('f.spShape.Visible = not f.spShape.Visible')
        self.btnShapeToggleVisible.OnClick = OnToggleShapeVisibleClick
        def OnSetShapeAlignClick(sender):
            self.InternalRunScript('f.spShape.Align = "alLeft"')
        self.btnShapeSetAlign.OnClick = OnSetShapeAlignClick
        def OnSetShapeMargins(sender):
            self.InternalRunScript('f.spShape.AlignWithMargins = True\r\nf.spShape.Margins.Left = 100\r\nf.spShape.Margins.Top = 10\r\nf.spShape.Margins.Right = 100\r\nf.spShape.Margins.Bottom = 10')
        self.btnShapeSetMargins.OnClick = OnSetShapeMargins
# Scroll Bar
        def OnSetScrollBarDirectionClick(sender):
            self.InternalRunScript('f.sbScrollBar.Kind = "sbVertical"')
        self.btnScrollBarSetDirection.OnClick = OnSetScrollBarDirectionClick
        def OnSetScrollBarMinMaxClick(sender):
            self.InternalRunScript('f.sbScrollBar.Min = 0\r\nf.sbScrollBar.Max = 1000')
        self.btnScrollBarSetMinMax.OnClick = OnSetScrollBarMinMaxClick
        def OnSetScrollBarChangeClick(sender):
            self.InternalRunScript('f.sbScrollBar.SmallChange = 5\r\nf.sbScrollBar.LargeChange = 100')
        self.btnScrollBarSetChange.OnClick = OnSetScrollBarChangeClick
        def OnSetScrollBarPositionClick(sender):
            self.InternalRunScript('f.sbScrollBar.Position = 500')
        self.btnScrollBarSetPosition.OnClick = OnSetScrollBarPositionClick
        def OnSetScrollBarBoundsClick(sender):
            self.InternalRunScript('f.sbScrollBar.SetBounds(100, 100, 50, 100)')
        self.btnScrollBarSetBounds.OnClick = OnSetScrollBarBoundsClick
        def OnToggleScrollBarEnabledClick(sender):
            self.InternalRunScript('f.sbScrollBar.Enabled = not f.sbScrollBar.Enabled')
        self.btnScrollBarToggleEnabled.OnClick = OnToggleScrollBarEnabledClick
        def OnToggleScrollBarVisibleClick(sender):
            self.InternalRunScript('f.sbScrollBar.Visible = not f.sbScrollBar.Visible')
        self.btnScrollBarToggleVisible.OnClick = OnToggleScrollBarVisibleClick
        def OnSetScrollBarAlignClick(sender):
            self.InternalRunScript('f.sbScrollBar.Align = "alLeft"')
        self.btnScrollBarSetAlign.OnClick = OnSetScrollBarAlignClick
        def OnSetScrollBarMargins(sender):
            self.InternalRunScript('f.sbScrollBar.AlignWithMargins = True\r\nf.sbScrollBar.Margins.Left = 100\r\nf.sbScrollBar.Margins.Top = 10\r\nf.sbScrollBar.Margins.Right = 100\r\nf.sbScrollBar.Margins.Bottom = 10')
        self.btnScrollBarSetMargins.OnClick = OnSetScrollBarMargins
        def OnSetScrollBarChangeEventClick(sender):
            self.InternalRunScript('f.sbScrollBar.OnChange = f.OnScrollBarChangeEvent')
        self.btnScrollBarSetOnChangeEvent.OnClick = OnSetScrollBarChangeEventClick
# Date Time Picker
        def OnSetDateTimePickerDateFormatClick(sender):
            self.InternalRunScript('f.dtpDateTimePicker.DateFormat = "dfLong"')
        self.btnDateTimePickerSetDateFormat.OnClick = OnSetDateTimePickerDateFormatClick
        def OnSetDateTimePickerKindClick(sender):
            self.InternalRunScript('f.dtpDateTimePicker.Kind = "dtkTime"')
        self.btnDateTimePickerSetKind.OnClick = OnSetDateTimePickerKindClick
        def OnSetDateTimePickerSetDateClick(sender):
            self.InternalRunScript('f.dtpDateTimePicker.Date = "2017/06/29"')
        self.btnDateTimePickerSetDate.OnClick = OnSetDateTimePickerSetDateClick
        def OnSetDateTimePickerTimeClick(sender):
            self.InternalRunScript('f.dtpDateTimePicker.Time = "17:06:29"')
        self.btnDateTimePickerSetTime.OnClick = OnSetDateTimePickerTimeClick
        def OnSetDateTimePickerBoundsClick(sender):
            self.InternalRunScript('f.dtpDateTimePicker.SetBounds(114, 135, 447, 57)')
        self.btnDateTimePickerSetBounds.OnClick = OnSetDateTimePickerBoundsClick
        def OnToggleDateTimePickerEnabledClick(sender):
            self.InternalRunScript('f.dtpDateTimePicker.Enabled = not f.dtpDateTimePicker.Enabled')
        self.btnDateTimePickerToggleEnabled.OnClick = OnToggleDateTimePickerEnabledClick
        def OnToggleDateTimePickerVisibleClick(sender):
            self.InternalRunScript('f.dtpDateTimePicker.Visible = not f.dtpDateTimePicker.Visible')
        self.btnDateTimePickerToggleVisible.OnClick = OnToggleDateTimePickerVisibleClick
        def OnSetDateTimePickerAlignClick(sender):
            self.InternalRunScript('f.dtpDateTimePicker.Align = "alLeft"')
        self.btnDateTimePickerSetAlign.OnClick = OnSetDateTimePickerAlignClick
        def OnSetDateTimePickerMargins(sender):
            self.InternalRunScript('f.dtpDateTimePicker.AlignWithMargins = True\r\nf.dtpDateTimePicker.Margins.Left = 100\r\nf.dtpDateTimePicker.Margins.Top = 10\r\nf.dtpDateTimePicker.Margins.Right = 100\r\nf.dtpDateTimePicker.Margins.Bottom = 10')
        self.btnDateTimePickerSetMargins.OnClick = OnSetDateTimePickerMargins
# Page Control
        def OnSetPageControlOwnerDrawClick(sender):
            self.InternalRunScript('f.pcPageControl.OwnerDraw = True')
        self.btnPageControlSetOwnerDraw.OnClick = OnSetPageControlOwnerDrawClick
        def OnSetPageControlStyleClick(sender):
            self.InternalRunScript('f.pcPageControl.Style = "tsFlatButtons"')
        self.btnPageControlSetStyle.OnClick = OnSetPageControlStyleClick
        def OnSetPageControlTabPositionClick(sender):
            self.InternalRunScript('f.pcPageControl.TabPosition = "tpBottom"')
        self.btnPageControlSetTabPosition.OnClick = OnSetPageControlTabPositionClick
        def OnSetPageControlBoundsClick(sender):
            self.InternalRunScript('f.pcPageControl.SetBounds(327, 153, 693, 465)')
        self.btnPageControlSetBounds.OnClick = OnSetPageControlBoundsClick
        def OnTogglePageControlEnabledClick(sender):
            self.InternalRunScript('f.pcPageControl.Enabled = not f.pcPageControl.Enabled')
        self.btnPageControlToggleEnabled.OnClick = OnTogglePageControlEnabledClick
        def OnTogglePageControlVisibleClick(sender):
            self.InternalRunScript('f.pcPageControl.Visible = not f.pcPageControl.Visible')
        self.btnPageControlToggleVisible.OnClick = OnTogglePageControlVisibleClick
        def OnSetPageControlAlignClick(sender):
            self.InternalRunScript('f.pcPageControl.Align = "alLeft"')
        self.btnPageControlSetAlign.OnClick = OnSetPageControlAlignClick
        def OnSetPageControlMargins(sender):
            self.InternalRunScript('f.pcPageControl.AlignWithMargins = True\r\nf.pcPageControl.Margins.Left = 100\r\nf.pcPageControl.Margins.Top = 10\r\nf.pcPageControl.Margins.Right = 100\r\nf.pcPageControl.Margins.Bottom = 10')
        self.btnPageControlSetMargins.OnClick = OnSetPageControlMargins
        def OnDrawTab(Control, TabIndex, Rect, Active):
            DT_CENTER = 1
            DT_SINGLELINE = 32
            DT_VCENTER = 4
            self.pcPageControl.Canvas.Font.Color = clRed
            s = self.pcPageControl.Pages[TabIndex].Caption
            rtl.draw_text(self.pcPageControl.Canvas.Handle, s, Rect.Left, Rect.Top, Rect.Right-Rect.Left, Rect.Bottom-Rect.Top, DT_CENTER + DT_SINGLELINE + DT_VCENTER)
            self.log_hint('On Draw Tab Index: ' + str(TabIndex) + ': ' + s + ', ' + str(self.pcPageControl.Canvas.Handle))
        self.pcPageControl.OnDrawTab = OnDrawTab

# Track Bar
        def OnSetTrackBarOrientationClick(sender):
            self.InternalRunScript('f.tbTrackBar.Orientation = "trVertical"')
        self.btnTrackBarSetOrientation.OnClick = OnSetTrackBarOrientationClick
        def OnSetTrackBarShowSelRangeClick(sender):
            self.InternalRunScript('f.tbTrackBar.ShowSelRange = False')
        self.btnTrackBarSetShowSelRange.OnClick = OnSetTrackBarShowSelRangeClick
        def OnSetTrackBarSliderVisibleClick(sender):
            self.InternalRunScript('f.tbTrackBar.SliderVisible = False')
        self.btnTrackBarSetSliderVisible.OnClick = OnSetTrackBarSliderVisibleClick
        def OnSetTrackBarTickMarksClick(sender):
            self.InternalRunScript('f.tbTrackBar.TickMarks = "tmBoth"')
        self.btnTrackBarSetTickMarks.OnClick = OnSetTrackBarTickMarksClick
        def OnSetTrackBarTickStyleClick(sender):
            self.InternalRunScript('f.tbTrackBar.TickStyle = "tsManual"')
        self.btnTrackBarSetTickStyle.OnClick = OnSetTrackBarTickStyleClick
        def OnSetTrackBarBoundsClick(sender):
            self.InternalRunScript('f.tbTrackBar.SetBounds(327, 288, 360, 108)')
        self.btnTrackBarSetBounds.OnClick = OnSetTrackBarBoundsClick
        def OnToggleTrackBarEnabledClick(sender):
            self.InternalRunScript('f.tbTrackBar.Enabled = not f.tbTrackBar.Enabled')
        self.btnTrackBarToggleEnabled.OnClick = OnToggleTrackBarEnabledClick
        def OnToggleTrackBarVisibleClick(sender):
            self.InternalRunScript('f.tbTrackBar.Visible = not f.tbTrackBar.Visible')
        self.btnTrackBarToggleVisible.OnClick = OnToggleTrackBarVisibleClick
        def OnSetTrackBarAlignClick(sender):
            self.InternalRunScript('f.tbTrackBar.Align = "alLeft"')
        self.btnTrackBarSetAlign.OnClick = OnSetTrackBarAlignClick
        def OnSetTrackBarMargins(sender):
            self.InternalRunScript('f.tbTrackBar.AlignWithMargins = True\r\nf.tbTrackBar.Margins.Left = 100\r\nf.tbTrackBar.Margins.Top = 10\r\nf.tbTrackBar.Margins.Right = 100\r\nf.tbTrackBar.Margins.Bottom = 10')
        self.btnTrackBarSetMargins.OnClick = OnSetTrackBarMargins
# Status Bar
        def OnSetStatusBarBorderWidthClick(sender):
            self.InternalRunScript('f.sbStatusBar.BorderWidth = 10')
        self.btnStatusBarSetBorderWidth.OnClick = OnSetStatusBarBorderWidthClick
        def OnSetStatusBarcolorClick(sender):
            self.InternalRunScript('f.sbStatusBar.color = clBlue')
        self.btnStatusBarSetcolor.OnClick = OnSetStatusBarcolorClick
        def OnSetStatusBarSimplePanelClick(sender):
            self.InternalRunScript('f.sbStatusBar.SimplePanel = True')
        self.btnStatusBarSetSimplePanel.OnClick = OnSetStatusBarSimplePanelClick
        def OnSetStatusBarSimpleTextClick(sender):
            self.InternalRunScript('f.sbStatusBar.SimpleText = "SimpleText Demo"')
        self.btnStatusBarSetSimpleText.OnClick = OnSetStatusBarSimpleTextClick
        def OnSetStatusBarBoundsClick(sender):
            self.InternalRunScript('f.sbStatusBar.SetBounds(0, 0, 608, 318)')
        self.btnStatusBarSetBounds.OnClick = OnSetStatusBarBoundsClick
        def OnToggleStatusBarEnabledClick(sender):
            self.InternalRunScript('f.sbStatusBar.Enabled = not f.sbStatusBar.Enabled')
        self.btnStatusBarToggleEnabled.OnClick = OnToggleStatusBarEnabledClick
        def OnToggleStatusBarVisibleClick(sender):
            self.InternalRunScript('f.sbStatusBar.Visible = not f.sbStatusBar.Visible')
        self.btnStatusBarToggleVisible.OnClick = OnToggleStatusBarVisibleClick
        def OnSetStatusBarAlignClick(sender):
            self.InternalRunScript('f.sbStatusBar.Align = "alLeft"')
        self.btnStatusBarSetAlign.OnClick = OnSetStatusBarAlignClick
        def OnSetStatusBarMargins(sender):
            self.InternalRunScript('f.sbStatusBar.AlignWithMargins = True\r\nf.sbStatusBar.Margins.Left = 100\r\nf.sbStatusBar.Margins.Top = 10\r\nf.sbStatusBar.Margins.Right = 100\r\nf.sbStatusBar.Margins.Bottom = 10')
        self.btnStatusBarSetMargins.OnClick = OnSetStatusBarMargins
# Paint Box
        def OnSetPaintBoxBoundsClick(sender):
            self.InternalRunScript('f.PaintBox.SetBounds(268, 140, 168, 168)')
        self.btnPaintBoxSetBounds.OnClick = OnSetPaintBoxBoundsClick
        def OnTogglePaintBoxEnabledClick(sender):
            self.InternalRunScript('f.PaintBox.Enabled = not f.PaintBox.Enabled')
        self.btnPaintBoxToggleEnabled.OnClick = OnTogglePaintBoxEnabledClick
        def OnTogglePaintBoxVisibleClick(sender):
            self.InternalRunScript('f.PaintBox.Visible = not f.PaintBox.Visible')
        self.btnPaintBoxToggleVisible.OnClick = OnTogglePaintBoxVisibleClick
        def OnSetPaintBoxAlignClick(sender):
            self.InternalRunScript('f.PaintBox.Align = "alLeft"')
        self.btnPaintBoxSetAlign.OnClick = OnSetPaintBoxAlignClick
        def OnSetPaintBoxMargins(sender):
            self.InternalRunScript('f.PaintBox.AlignWithMargins = True\r\nf.PaintBox.Margins.Left = 100\r\nf.PaintBox.Margins.Top = 10\r\nf.PaintBox.Margins.Right = 100\r\nf.PaintBox.Margins.Bottom = 10')
        self.btnPaintBoxSetMargins.OnClick = OnSetPaintBoxMargins
# Image
        def OnSetImagePictureClick(sender):
            self.InternalRunScript('f.iImage.LoadImageFromString("89504E470D0A1A0A0000000D49484452000000970000003B0802000000F9238FBB0000073C494441547801ED5B6F6ADB4A10DF3EDE156259BA426245B16F90D8B131B9408A9360F0E7129A4002F95C7881D752DE6783701AEA0B0413B7716F605791EB2BC85EF5107DAB3FBB5A492B4B4AA34097350549BBB3A399F9CDCCCE8E" \
      "D257BF7EFD02E2F7875BE0AF3F5C7E21BE630181220F7E20501428F260011E7410B12850E4C1023CE8206251A0C8830578D041C4A24091070BF0A083884581220F16E04107118B02451E2CC0830E2216058A3C5880071D442C0A1479B0000F3AFCFDC24A4068035092A46CAF853644845229237936A619A96CF361F27D959198" \
      "222BABADFAA627307C18EA86A341D65FB971D9D9CC4A4CD1E546D1BCFD384AD5ADAC763BBB94E96DF3F6F368B6B4A8170345EB1DEDA952891EF3EEE17CA88F0D2B440D14456B1F1DAA1ED3F9F09FB1671DA97D7EA88659041212A3C06F834FE6D2238BCAE68EB218AE0C631A9621FC9E8427454228E2396859FE6BF1C8DA6B79" \
      "ED6CF2646E14015846ECCB624E191619483718D6B08CFEB5A1548FC3DE677FF9F7FD1D831A581644CE43F862EB50AE12C88125A48CB2B4B00F594BBDBC75598F7ACF5A8601EBA7DD2117942961624CE0749607ECD8FA27A0282B0A6183EDE50C50E34462F82D02A1A2C8801814006B76F3061CFF87D3087CF84C4128D7AA7E66" \
      "5A46E298BCFF4937D66862D6A3119CCC49EB7DC842BC18BCBD992671D1D41DA6BF79F410E509EC64491CD68EE74651ED9C92800008A4EBB11739B5EEE94925F2AAC500CF228C6BDDD727151C017031F874E3E7ABD9CD60FBDA5D6B3F1AD82595E6D53995933B00CE1779769888249147A37FAB12D789CCB11E6D38FFB9F6ED1B" \
      "5254F7101B6B74D30F0D3CF3436E14B3BF1F3E7C25BE19C558DA3C396A2E31C6D3C7C54905ED253F03872C470B20A9E2970CD905584719B8CE3A2A3CF7F35E4F8E338708C56BE0DB78557055DAC7EDB5B1381AB1369D8041CA5D71288602AB15775569B75D1DF767AE7C33D3EC6CAA604346B9DA0BEDD9D7C1F64610BB295A64" \
      "9FD67A5DD0D70DB460AA0F7732A5CAECCC93290DF33BD965185490550930E892868A4331082C45DB623AA2BAAD8199635000E00A0254AF6E6BF29D5FD42DA7FAFB69721D9BA44FFA78E5B057355CEFC99E57374F3E5C9FA4B05E7C4F26B0AC68C99D4CFB9499C25084106F71C96295241C7BCB253A464A40AA9FF656177E80A2" \
      "756E1D8BCE2407CDBD7DB2A726F3CB38A3768E6B33374366CFABE8ACF235696794761ABBFE11282A01F25ECF0C54E9171477D4607461BEE7C250A4C4905987426A3E74AB76AEAFCA439DDE272CE34E3766EDB3F8F120B432C7C366AB2D4F478E7DB3E6551B1D06BCB4117F8D2C2314E3C3C82DEB7B0786E156DDD4B9763E7CE3" \
      "A674A5FDFAB9347A091497A85FC38C249BEC07B28CAB57640DA97E7859DF83F3097DF6B746EF079257CAB20C96734CAABF3E30BC83A99B571B242BA432A20228882AF62AEAE064F4DF469D0069F466145B580DCE5DB1B9C481C2BAE1D256151F2B2DE3073319414886A57274E72C4995C3CBF3B35E5B26B2A35296DCE31B6743" \
      "0DFFEC556A6BC95950DA3F6AFA02A2BC3A0FF3487E42C5F6E5B9FFAF4BC9C65801BFE96EB833A69E7BA8B8582C955155E6D55ED6F87EBE1B3F4DDE1325AB2A3323215BAB41D000B042B0BBE78DD8864A9985AAAACA1BD478EC56DAEDB6CD775E5E1D8D63D3BF39607FF9444ED2672D2AD3007BF2CECFA8C7DD4A4CC23CBB0F11" \
      "B1381481DA682A335F93A9FE51BE38DD270107175FD0A9DF97423E68788D47D480FE012A49950200E410E904FAD86B043A1BDB05EEAF0260DE066CABCC344E54775237C9ABD4E8DADBE5783878C414ABC4022EC8A58A061E27F7788573C5D9C332CCFB68DA905A9D5D9A36E37D812802CAD951A976777D71A7C835943A57704A" \
      "F588D1264FD05D19E3BBD118751DAB9AEAE458688E8CA0465782D8A2CF246E3FD66954C250A3AEDA206C936DE1E4D5196E3E2493053319CF0CA8D8BE92504F5F6A6B669FA49C808D7B67C5BBEDDA4E0795EAB97F45A2E838FBE915F8E8652D47346B49E387069C6E38A3318D908BD60240697629CA4818C58CABF5706F36C524" \
      "21574BA1750466F4B525E681DED9D72BA8710870371833274EAC68B5E8CA68C70AAF49B9168B227AB9036465714FBAA6441EC629B054D6648551F8C9B576837CB4C30C4AFBE767E58749BC77853CA3DBC9D1AE8B3804E6CFBECACD437A83471BB5677838275FBE7C24DC2FA96867DF6A35B642BCECC9547752B1A2A9ADF8BE88" \
      "3EA9E6FF9EFAEA25FF5FBFAF188236650FB7A9EA35C32762EF63B263AACCDF9F4376653E906F64C9DF34A88F018485E29D6BF1A1908C67BFF139645F0040E1B1480B93061EA1CD09467EE7256FFAAD1BAAC8C27CE4D4920A533EE7F54563F139052F9C17F98B0DA76E4CAA38D0DF64047526FA5B0DF4E12589B44881058A455A" \
      "F7A57817D6BB792905C47B9005048A3CB8814051A0C8830578D041C4A24091070BF0A083884581220F16E04107118B02451E2CC0830E2216058A3C5880071D442C0A1479B0000F3A88581428F260011E7410B12850E4C1023CE82062910714FF07590EB657CA47ED1F0000000049454E44AE426082")')
        self.btnImageSetPicture.OnClick = OnSetImagePictureClick
        def OnSetImageBoundsClick(sender):
            self.InternalRunScript('f.iImage.SetBounds(218, 128, 168, 168)')
        self.btnImageSetBounds.OnClick = OnSetImageBoundsClick
        def OnToggleImageEnabledClick(sender):
            self.InternalRunScript('f.iImage.Enabled = not f.iImage.Enabled')
        self.btnImageToggleEnabled.OnClick = OnToggleImageEnabledClick
        def OnToggleImageVisibleClick(sender):
            self.InternalRunScript('f.iImage.Visible = not f.iImage.Visible')
        self.btnImageToggleVisible.OnClick = OnToggleImageVisibleClick
        def OnSetImageAlignClick(sender):
            self.InternalRunScript('f.iImage.Align = "alLeft"')
        self.btnImageSetAlign.OnClick = OnSetImageAlignClick
        def OnSetImageMargins(sender):
            self.InternalRunScript('f.iImage.AlignWithMargins = True\r\nf.iImage.Margins.Left = 100\r\nf.iImage.Margins.Top = 10\r\nf.iImage.Margins.Right = 100\r\nf.iImage.Margins.Bottom = 10')
        self.btnImageSetMargins.OnClick = OnSetImageMargins
# Bevel
        def OnSetBevelStyleClick(sender):
            self.InternalRunScript('f.bBevel.style = "bsRaised"')
        self.btnBevelSetStyle.OnClick = OnSetBevelStyleClick
        def OnSetBevelShapeClick(sender):
            self.InternalRunScript('f.bBevel.Shape = "bsFrame"')
        self.btnBevelSetShape.OnClick = OnSetBevelShapeClick
        def OnSetBevelBoundsClick(sender):
            self.InternalRunScript('f.bBevel.SetBounds(294, 140, 80, 80)')
        self.btnBevelSetBounds.OnClick = OnSetBevelBoundsClick
        def OnToggleBevelEnabledClick(sender):
            self.InternalRunScript('f.bBevel.Enabled = not f.bBevel.Enabled')
        self.btnBevelToggleEnabled.OnClick = OnToggleBevelEnabledClick
        def OnToggleBevelVisibleClick(sender):
            self.InternalRunScript('f.bBevel.Visible = not f.bBevel.Visible')
        self.btnBevelToggleVisible.OnClick = OnToggleBevelVisibleClick
        def OnSetBevelAlignClick(sender):
            self.InternalRunScript('f.bBevel.Align = "alLeft"')
        self.btnBevelSetAlign.OnClick = OnSetBevelAlignClick
        def OnSetBevelMargins(sender):
            self.InternalRunScript('f.bBevel.AlignWithMargins = True\r\nf.bBevel.Margins.Left = 100\r\nf.bBevel.Margins.Top = 10\r\nf.bBevel.Margins.Right = 100\r\nf.bBevel.Margins.Bottom = 10')
        self.btnBevelSetMargins.OnClick = OnSetBevelMargins
# Tab Control
        def OnSetTabControlOwnerDrawClick(sender):
            self.InternalRunScript('f.tcTabControl.OwnerDraw = True')
        self.btnTabControlSetOwnerDraw.OnClick = OnSetTabControlOwnerDrawClick
        def OnSetTabControlStyleClick(sender):
            self.InternalRunScript('f.tcTabControl.Style = "tsButtons"')
        self.btnTabControlSetStyle.OnClick = OnSetTabControlStyleClick
        def OnSetTabControlBoundsClick(sender):
            self.InternalRunScript('f.tcTabControl.SetBounds(256, 140, 461, 310)')
        self.btnTabControlSetBounds.OnClick = OnSetTabControlBoundsClick
        def OnToggleTabControlEnabledClick(sender):
            self.InternalRunScript('f.tcTabControl.Enabled = not f.tcTabControl.Enabled')
        self.btnTabControlToggleEnabled.OnClick = OnToggleTabControlEnabledClick
        def OnToggleTabControlVisibleClick(sender):
            self.InternalRunScript('f.tcTabControl.Visible = not f.tcTabControl.Visible')
        self.btnTabControlToggleVisible.OnClick = OnToggleTabControlVisibleClick
        def OnSetTabControlAlignClick(sender):
            self.InternalRunScript('f.tcTabControl.Align = "alLeft"')
        self.btnTabControlSetAlign.OnClick = OnSetTabControlAlignClick
        def OnSetTabControlMargins(sender):
            self.InternalRunScript('f.tcTabControl.AlignWithMargins = True\r\nf.tcTabControl.Margins.Left = 100\r\nf.tcTabControl.Margins.Top = 10\r\nf.tcTabControl.Margins.Right = 100\r\nf.tcTabControl.Margins.Bottom = 10')
        self.btnTabControlSetMargins.OnClick = OnSetTabControlMargins
# Progress Bar
        def OnSetProgressBarBorderWidthClick(sender):
            self.InternalRunScript('f.pbProgressBar.BorderWidth = 10')
        self.btnProgressBarSetBorderWidth.OnClick = OnSetProgressBarBorderWidthClick
        def OnSetProgressBarStyleClick(sender):
            self.InternalRunScript('f.pbProgressBar.Style = "pbstMarquee"')
        self.btnProgressBarSetStyle.OnClick = OnSetProgressBarStyleClick
        def OnSetProgressBarStateClick(sender):
            self.InternalRunScript('f.pbProgressBar.State = "pbsError"')
        self.btnProgressBarSetState.OnClick = OnSetProgressBarStateClick
        def OnSetProgressBarBoundsClick(sender):
            self.InternalRunScript('f.pbProgressBar.SetBounds(282, 116, 240, 38)')
        self.btnProgressBarSetBounds.OnClick = OnSetProgressBarBoundsClick
        def OnToggleProgressBarEnabledClick(sender):
            self.InternalRunScript('f.pbProgressBar.Enabled = not f.pbProgressBar.Enabled')
        self.btnProgressBarToggleEnabled.OnClick = OnToggleProgressBarEnabledClick
        def OnToggleProgressBarVisibleClick(sender):
            self.InternalRunScript('f.pbProgressBar.Visible = not f.pbProgressBar.Visible')
        self.btnProgressBarToggleVisible.OnClick = OnToggleProgressBarVisibleClick
        def OnSetProgressBarAlignClick(sender):
            self.InternalRunScript('f.pbProgressBar.Align = "alLeft"')
        self.btnProgressBarSetAlign.OnClick = OnSetProgressBarAlignClick
        def OnSetProgressBarMargins(sender):
            self.InternalRunScript('f.pbProgressBar.AlignWithMargins = True\r\nf.pbProgressBar.Margins.Left = 100\r\nf.pbProgressBar.Margins.Top = 10\r\nf.pbProgressBar.Margins.Right = 100\r\nf.pbProgressBar.Margins.Bottom = 10')
        self.btnProgressBarSetMargins.OnClick = OnSetProgressBarMargins
# Header
        def OnSetHeaderBorderStyleClick(sender):
            self.InternalRunScript('f.hHeader.BorderStyle = "bsSingle"')
        self.btnHeaderSetBorderStyle.OnClick = OnSetHeaderBorderStyleClick
        def OnSetHeaderSectionsClick(sender):
            self.InternalRunScript('f.hHeader.Sections.Assign(["text"])')
        self.btnHeaderSetSections.OnClick = OnSetHeaderSectionsClick
        def OnSetHeaderBoundsClick(sender):
            self.InternalRunScript('f.hHeader.SetBounds(308, 154, 400, 40)')
        self.btnHeaderSetBounds.OnClick = OnSetHeaderBoundsClick
        def OnToggleHeaderEnabledClick(sender):
            self.InternalRunScript('f.hHeader.Enabled = not f.hHeader.Enabled')
        self.btnHeaderToggleEnabled.OnClick = OnToggleHeaderEnabledClick
        def OnToggleHeaderVisibleClick(sender):
            self.InternalRunScript('f.hHeader.Visible = not f.hHeader.Visible')
        self.btnHeaderToggleVisible.OnClick = OnToggleHeaderVisibleClick
        def OnSetHeaderAlignClick(sender):
            self.InternalRunScript('f.hHeader.Align = "alLeft"')
        self.btnHeaderSetAlign.OnClick = OnSetHeaderAlignClick
        def OnSetHeaderMargins(sender):
            self.InternalRunScript('f.hHeader.AlignWithMargins = True\r\nf.hHeader.Margins.Left = 100\r\nf.hHeader.Margins.Top = 10\r\nf.hHeader.Margins.Right = 100\r\nf.hHeader.Margins.Bottom = 10')
        self.btnHeaderSetMargins.OnClick = OnSetHeaderMargins
# Splitter
        def OnSetSplitterBeveledClick(sender):
            self.InternalRunScript('f.sSplitter.Beveled = True')
        self.btnSplitterSetBeveled.OnClick = OnSetSplitterBeveledClick
        def OnSetSplitterColorClick(sender):
            self.InternalRunScript('f.sSplitter.Color = clMenuHighlight')
        self.btnSplitterSetColor.OnClick = OnSetSplitterColorClick
        def OnSetSplitterBoundsClick(sender):
            self.InternalRunScript('f.sSplitter.SetBounds(0, 0, 340, 518)')
        self.btnSplitterSetBounds.OnClick = OnSetSplitterBoundsClick
        def OnToggleSplitterEnabledClick(sender):
            self.InternalRunScript('f.sSplitter.Enabled = not f.sSplitter.Enabled')
        self.btnSplitterToggleEnabled.OnClick = OnToggleSplitterEnabledClick
        def OnToggleSplitterVisibleClick(sender):
            self.InternalRunScript('f.sSplitter.Visible = not f.sSplitter.Visible')
        self.btnSplitterToggleVisible.OnClick = OnToggleSplitterVisibleClick
        def OnSetSplitterAlignClick(sender):
            self.InternalRunScript('f.sSplitter.Align = "alLeft"')
        self.btnSplitterSetAlign.OnClick = OnSetSplitterAlignClick
        def OnSetSplitterMargins(sender):
            self.InternalRunScript('f.sSplitter.AlignWithMargins = True\r\nf.sSplitter.Margins.Left = 100\r\nf.sSplitter.Margins.Top = 10\r\nf.sSplitter.Margins.Right = 100\r\nf.sSplitter.Margins.Bottom = 10')
        self.btnSplitterSetMargins.OnClick = OnSetSplitterMargins
# Control Bar
        def OnSetControlBarPictureClick(sender):
            self.InternalRunScript('f.cbControlBar.LoadImageFromString("89504E470D0A1A0A0000000D49484452000000970000003B0802000000F9238FBB0000073C494441547801ED5B6F6ADB4A10DF3EDE156259BA426245B16F90D8B131B9408A9360F0E7129A4002F95C7881D752DE6783701AEA0B0413B7716F605791EB2BC85EF5107DAB3FBB5A492B4B4AA34097350549BBB3A399F9CDCCCE8E" \
            "D257BF7EFD02E2F7875BE0AF3F5C7E21BE630181220F7E20501428F260011E7410B12850E4C1023CE8206251A0C8830578D041C4A24091070BF0A083884581220F16E04107118B02451E2CC0830E2216058A3C5880071D442C0A1479B0000F3AFCFDC24A4068035092A46CAF853644845229237936A619A96CF361F27D959198" \
            "222BABADFAA627307C18EA86A341D65FB971D9D9CC4A4CD1E546D1BCFD384AD5ADAC763BBB94E96DF3F6F368B6B4A8170345EB1DEDA952891EF3EEE17CA88F0D2B440D14456B1F1DAA1ED3F9F09FB1671DA97D7EA88659041212A3C06F834FE6D2238BCAE68EB218AE0C631A9621FC9E8427454228E2396859FE6BF1C8DA6B79" \
            "ED6CF2646E14015846ECCB624E191619483718D6B08CFEB5A1548FC3DE677FF9F7FD1D831A581644CE43F862EB50AE12C88125A48CB2B4B00F594BBDBC75598F7ACF5A8601EBA7DD2117942961624CE0749607ECD8FA27A0282B0A6183EDE50C50E34462F82D02A1A2C8801814006B76F3061CFF87D3087CF84C4128D7AA7E66" \
            "5A46E298BCFF4937D66862D6A3119CCC49EB7DC842BC18BCBD992671D1D41DA6BF79F410E509EC64491CD68EE74651ED9C92800008A4EBB11739B5EEE94925F2AAC500CF228C6BDDD727151C017031F874E3E7ABD9CD60FBDA5D6B3F1AD82595E6D53995933B00CE1779769888249147A37FAB12D789CCB11E6D38FFB9F6ED1B" \
            "5254F7101B6B74D30F0D3CF3436E14B3BF1F3E7C25BE19C558DA3C396A2E31C6D3C7C54905ED253F03872C470B20A9E2970CD905584719B8CE3A2A3CF7F35E4F8E338708C56BE0DB78557055DAC7EDB5B1381AB1369D8041CA5D71288602AB15775569B75D1DF767AE7C33D3EC6CAA604346B9DA0BEDD9D7C1F64610BB295A64" \
            "9FD67A5DD0D70DB460AA0F7732A5CAECCC93290DF33BD965185490550930E892868A4331082C45DB623AA2BAAD8199635000E00A0254AF6E6BF29D5FD42DA7FAFB69721D9BA44FFA78E5B057355CEFC99E57374F3E5C9FA4B05E7C4F26B0AC68C99D4CFB9499C25084106F71C96295241C7BCB253A464A40AA9FF656177E80A2" \
            "756E1D8BCE2407CDBD7DB2A726F3CB38A3768E6B33374366CFABE8ACF235696794761ABBFE11282A01F25ECF0C54E9171477D4607461BEE7C250A4C4905987426A3E74AB76AEAFCA439DDE272CE34E3766EDB3F8F120B432C7C366AB2D4F478E7DB3E6551B1D06BCB4117F8D2C2314E3C3C82DEB7B0786E156DDD4B9763E7CE3" \
            "A674A5FDFAB9347A091497A85FC38C249BEC07B28CAB57640DA97E7859DF83F3097DF6B746EF079257CAB20C96734CAABF3E30BC83A99B571B242BA432A20228882AF62AEAE064F4DF469D0069F466145B580DCE5DB1B9C481C2BAE1D256151F2B2DE3073319414886A57274E72C4995C3CBF3B35E5B26B2A35296DCE31B6743" \
            "0DFFEC556A6BC95950DA3F6AFA02A2BC3A0FF3487E42C5F6E5B9FFAF4BC9C65801BFE96EB833A69E7BA8B8582C955155E6D55ED6F87EBE1B3F4DDE1325AB2A3323215BAB41D000B042B0BBE78DD8864A9985AAAACA1BD478EC56DAEDB6CD775E5E1D8D63D3BF39607FF9444ED2672D2AD3007BF2CECFA8C7DD4A4CC23CBB0F11" \
            "B1381481DA682A335F93A9FE51BE38DD270107175FD0A9DF97423E68788D47D480FE012A49950200E410E904FAD86B043A1BDB05EEAF0260DE066CABCC344E54775237C9ABD4E8DADBE5783878C414ABC4022EC8A58A061E27F7788573C5D9C332CCFB68DA905A9D5D9A36E37D812802CAD951A976777D71A7C835943A57704A" \
            "F588D1264FD05D19E3BBD118751DAB9AEAE458688E8CA0465782D8A2CF246E3FD66954C250A3AEDA206C936DE1E4D5196E3E2493053319CF0CA8D8BE92504F5F6A6B669FA49C808D7B67C5BBEDDA4E0795EAB97F45A2E838FBE915F8E8652D47346B49E387069C6E38A3318D908BD60240697629CA4818C58CABF5706F36C524" \
            "21574BA1750466F4B525E681DED9D72BA8710870371833274EAC68B5E8CA68C70AAF49B9168B227AB9036465714FBAA6441EC629B054D6648551F8C9B576837CB4C30C4AFBE767E58749BC77853CA3DBC9D1AE8B3804E6CFBECACD437A83471BB5677838275FBE7C24DC2FA96867DF6A35B642BCECC9547752B1A2A9ADF8BE88" \
            "3EA9E6FF9EFAEA25FF5FBFAF188236650FB7A9EA35C32762EF63B263AACCDF9F4376653E906F64C9DF34A88F018485E29D6BF1A1908C67BFF139645F0040E1B1480B93061EA1CD09467EE7256FFAAD1BAAC8C27CE4D4920A533EE7F54563F139052F9C17F98B0DA76E4CAA38D0DF64047526FA5B0DF4E12589B44881058A455A" \
            "F7A57817D6BB792905C47B9005048A3CB8814051A0C8830578D041C4A24091070BF0A083884581220F16E04107118B02451E2CC0830E2216058A3C5880071D442C0A1479B0000F3A88581428F260011E7410B12850E4C1023CE82062910714FF07590EB657CA47ED1F0000000049454E44AE426082")')
        self.btnControlBarSetPicture.OnClick = OnSetControlBarPictureClick
        def OnSetControlBarBevelInnerClick(sender):
            self.InternalRunScript('f.cbControlBar.BevelInner = "bvLowered"')
        self.btnControlBarSetBevelInner.OnClick = OnSetControlBarBevelInnerClick
        def OnSetControlBarBevelKindClick(sender):
            self.InternalRunScript('f.cbControlBar.BevelKind = "dkDock"')
        self.btnControlBarSetBevelKind.OnClick = OnSetControlBarBevelKindClick
        def OnSetControlBarBevelOuterClick(sender):
            self.InternalRunScript('f.cbControlBar.BevelOuter = "bvRaised"')
        self.btnControlBarSetBevelOuter.OnClick = OnSetControlBarBevelOuterClick
        def OnSetControlBarBorderWidthClick(sender):
            self.InternalRunScript('f.cbControlBar.BorderWidth = 10')
        self.btnControlBarSetBorderWidth.OnClick = OnSetControlBarBorderWidthClick
        def OnSetControlBarColorClick(sender):
            self.InternalRunScript('f.cbControlBar.Color = clMenuHighlight')
        self.btnControlBarSetColor.OnClick = OnSetControlBarColorClick
        def OnSetControlBarAutoSizeClick(sender):
            self.InternalRunScript('f.cbControlBar.AutoSize = True')
        self.btnControlBarSetAutoSize.OnClick = OnSetControlBarAutoSizeClick
        def OnSetControlBarBoundsClick(sender):
            self.InternalRunScript('f.cbControlBar.SetBounds(358, 116, 160, 80)')
        self.btnControlBarSetBounds.OnClick = OnSetControlBarBoundsClick
        def OnToggleControlBarEnabledClick(sender):
            self.InternalRunScript('f.cbControlBar.Enabled = not f.cbControlBar.Enabled')
        self.btnControlBarToggleEnabled.OnClick = OnToggleControlBarEnabledClick
        def OnToggleControlBarVisibleClick(sender):
            self.InternalRunScript('f.cbControlBar.Visible = not f.cbControlBar.Visible')
        self.btnControlBarToggleVisible.OnClick = OnToggleControlBarVisibleClick
        def OnSetControlBarAlignClick(sender):
            self.InternalRunScript('f.cbControlBar.Align = "alLeft"')
        self.btnControlBarSetAlign.OnClick = OnSetControlBarAlignClick
        def OnSetControlBarMargins(sender):
            self.InternalRunScript('f.cbControlBar.AlignWithMargins = True\r\nf.cbControlBar.Margins.Left = 100\r\nf.cbControlBar.Margins.Top = 10\r\nf.cbControlBar.Margins.Right = 100\r\nf.cbControlBar.Margins.Bottom = 10')
        self.btnControlBarSetMargins.OnClick = OnSetControlBarMargins
# Bound Label
        def OnSetBoundLabelLayoutClick(sender):
            self.InternalRunScript('f.blBoundLabel.Layout = "tlTop"')
        self.btnBoundLabelSetLayout.OnClick = OnSetBoundLabelLayoutClick
        def OnSetBoundLabelTransparentClick(sender):
            self.InternalRunScript('f.blBoundLabel.Transparent = False')
        self.btnBoundLabelSetTransparent.OnClick = OnSetBoundLabelTransparentClick
        def OnSetBoundLabelColorClick(sender):
            self.InternalRunScript('f.blBoundLabel.Color = clHotLight')
        self.btnBoundLabelSetColor.OnClick = OnSetBoundLabelColorClick
        def OnSetBoundLabelBoundsClick(sender):
            self.InternalRunScript('f.blBoundLabel.SetBounds(200, 100, 132, 33)')
        self.btnBoundLabelSetBounds.OnClick = OnSetBoundLabelBoundsClick
        def OnSetBoundLabelMargins(sender):
            self.InternalRunScript('f.blBoundLabel.AlignWithMargins = True\r\nf.blBoundLabel.Margins.Left = 100\r\nf.blBoundLabel.Margins.Top = 10\r\nf.blBoundLabel.Margins.Right = 100\r\nf.blBoundLabel.Margins.Bottom = 10')
        self.btnBoundLabelSetMargins.OnClick = OnSetBoundLabelMargins
# Labeled Edit
        def OnSetLabeledEditAlignmentClick(sender):
            self.InternalRunScript('f.leLabeledEdit.Alignment = "taLeftJustify"')
        self.btnLabeledEditSetAlignment.OnClick = OnSetLabeledEditAlignmentClick
        def OnSetLabeledEditBevelKindClick(sender):
            self.InternalRunScript('f.leLabeledEdit.BevelKind = "bkSoft"')
        self.btnLabeledEditSetBevelKind.OnClick = OnSetLabeledEditBevelKindClick
        def OnSetLabeledEditBorderStyleClick(sender):
            self.InternalRunScript('f.leLabeledEdit.BorderStyle = "bsSingle"')
        self.btnLabeledEditSetBorderStyle.OnClick = OnSetLabeledEditBorderStyleClick
        def OnSetLabeledEditCharCaseClick(sender):
            self.InternalRunScript('f.leLabeledEdit.CharCase = "ecUpperCase"')
        self.btnLabeledEditSetCharCase.OnClick = OnSetLabeledEditCharCaseClick
        def OnSetLabeledEditColorClick(sender):
            self.InternalRunScript('f.leLabeledEdit.Color = clMenuHighlight')
        self.btnLabeledEditSetColor.OnClick = OnSetLabeledEditColorClick
        def OnSetLabeledEditTextClick(sender):
            self.InternalRunScript('f.leLabeledEdit.Text = "lelabelededit_Text"')
        self.btnLabeledEditSetText.OnClick = OnSetLabeledEditTextClick
        def OnSetLabeledEditBoundsClick(sender):
            self.InternalRunScript('f.leLabeledEdit.SetBounds(256, 154, 194, 38)')
        self.btnLabeledEditSetBounds.OnClick = OnSetLabeledEditBoundsClick
        def OnToggleLabeledEditEnabledClick(sender):
            self.InternalRunScript('f.leLabeledEdit.Enabled = not f.leLabeledEdit.Enabled')
        self.btnLabeledEditToggleEnabled.OnClick = OnToggleLabeledEditEnabledClick
        def OnToggleLabeledEditVisibleClick(sender):
            self.InternalRunScript('f.leLabeledEdit.Visible = not f.leLabeledEdit.Visible')
        self.btnLabeledEditToggleVisible.OnClick = OnToggleLabeledEditVisibleClick
        def OnSetLabeledEditAlignClick(sender):
            self.InternalRunScript('f.leLabeledEdit.Align = "alLeft"')
        self.btnLabeledEditSetAlign.OnClick = OnSetLabeledEditAlignClick
        def OnSetLabeledEditMargins(sender):
            self.InternalRunScript('f.leLabeledEdit.AlignWithMargins = True\r\nf.leLabeledEdit.Margins.Left = 100\r\nf.leLabeledEdit.Margins.Top = 10\r\nf.leLabeledEdit.Margins.Right = 100\r\nf.leLabeledEdit.Margins.Bottom = 10')
        self.btnLabeledEditSetMargins.OnClick = OnSetLabeledEditMargins
# Color Box
        def OnSetColorBoxBevelKindClick(sender):
            self.InternalRunScript('f.cbColorBox.BevelKind = "bkFlat"')
        self.btnColorBoxSetBevelKind.OnClick = OnSetColorBoxBevelKindClick
        def OnSetColorBoxBiDiModeClick(sender):
            self.InternalRunScript('f.cbColorBox.BiDiMode = "bdRightToLeft"')
        self.btnColorBoxSetBiDiMode.OnClick = OnSetColorBoxBiDiModeClick
        def OnSetColorBoxColorClick(sender):
            self.InternalRunScript('f.cbColorBox.Color = clMenuHighlight')
        self.btnColorBoxSetColor.OnClick = OnSetColorBoxColorClick
        def OnSetColorBoxSelectedClick(sender):
            self.InternalRunScript('f.cbColorBox.Selected = clNavy')
        self.btnColorBoxSetSelected.OnClick = OnSetColorBoxSelectedClick
        def OnSetColorBoxBoundsClick(sender):
            self.InternalRunScript('f.cbColorBox.SetBounds(230, 154, 232, 44)')
        self.btnColorBoxSetBounds.OnClick = OnSetColorBoxBoundsClick
        def OnToggleColorBoxEnabledClick(sender):
            self.InternalRunScript('f.cbColorBox.Enabled = not f.cbColorBox.Enabled')
        self.btnColorBoxToggleEnabled.OnClick = OnToggleColorBoxEnabledClick
        def OnToggleColorBoxVisibleClick(sender):
            self.InternalRunScript('f.cbColorBox.Visible = not f.cbColorBox.Visible')
        self.btnColorBoxToggleVisible.OnClick = OnToggleColorBoxVisibleClick
        def OnSetColorBoxAlignClick(sender):
            self.InternalRunScript('f.cbColorBox.Align = "alLeft"')
        self.btnColorBoxSetAlign.OnClick = OnSetColorBoxAlignClick
        def OnSetColorBoxMargins(sender):
            self.InternalRunScript('f.cbColorBox.AlignWithMargins = True\r\nf.cbColorBox.Margins.Left = 100\r\nf.cbColorBox.Margins.Top = 10\r\nf.cbColorBox.Margins.Right = 100\r\nf.cbColorBox.Margins.Bottom = 10')
        self.btnColorBoxSetMargins.OnClick = OnSetColorBoxMargins
# Speed Button
        def OnSetSpeedButtonGlyphClick(sender):
            self.InternalRunScript('f.SpeedButton.LoadImageFromString("424D6A8B0000000000003600000028000000970000003B0000000100200000000000348B000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFFA6BBD1FFA6A3A0FFBDA3A0FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFA6BBE8FFA6A3A0FFA6A3A0FFA6A3A0FFD4BBA0FFFFE8E8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFF8F71" \
            "6DFFFFE8B9FFFFFFFFFFA6D2FFFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9E8E8FFE9E8E8FFE9E8E8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFFE9E8E8FFE9E8E8FFE9E8E8FFFFFFE8FFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9E8FFFFE9E8E8FFE9E8E8FFFFE8E8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFA6D2FFFF76716DFF76716DFF76716DFF76716DFF76716DFF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4E8" \
            "E8FF768BA0FF76716DFF76716DFF76716DFF76716DFF76716DFFA68B6DFFE9D2B9FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBD1FF767187FF76716DFF76716DFF76716DFF76716DFF76716DFF8F716DFFD4BBA0FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFFA6BBD1FF767187FF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFFD4A387FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFF" \
            "D1FFA6D2FFFF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE8E8FFFFFFFFFFFFFFFFFFA6D2E8FF767187FF76716DFFD4A36DFFFFFFFFFFFFFFFFFFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFA6D2E8FF76716DFF76716DFFD4BB87FFE9E8E8FFE9E8E8FFE9E8" \
            "E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A3" \
            "87FFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFFA68B87FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3" \
            "A0FFBDA3A0FFFFE8D1FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFBDD2E8FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FF8F8BA0FF76716DFF76716DFFA68B6DFFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFBDA3A0FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF8F8B6DFFA6A3A0FF8F8BA0FF76716DFF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFFA68B87FFD4BBB9FFD4D2" \
            "D1FFA6BBD1FF768B87FF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFFA68B87FF8FA3A0FF767187FF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFA6D2" \
            "E8FFBD8B87FF8FBBD1FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFFFFFFFFFD4E8FFFF768BB9FF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFE9FFFFFFBDBBD1FFFFE8D1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFE9FF" \
            "FFFF768BB9FF76716DFF76716DFFA6716DFFFFE8D1FFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFF" \
            "FFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFFA68B87FFA6A3A0FFA6A3A0FFA6A3A0FF768BA0FF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FF8FBBE8FF76716DFF76716DFFA68B6DFFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FF8F8BA0FF7671" \
            "6DFF76716DFFA68B6DFFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFBDA3A0FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFD4FFFFFF7671A0FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4FF" \
            "FFFF7671A0FF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFFFFD2" \
            "A0FFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFE9FFFFFF768BB9FF76716DFF76716DFFE9D2A0FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFA6D2E8FF76716DFF76716DFFD4BB87FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFFFFF" \
            "E8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFFA6716DFFFFFFD1FFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF8FBBD1FF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF7671" \
            "6DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFBDBBA0FF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671" \
            "A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF7671" \
            "6DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFFA6D2E8FF768B87FF76716DFF76716DFF7671" \
            "6DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFD4A36DFFBDE8" \
            "FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFF8F716DFF8F8B87FF8F8B87FF8F8B87FF767187FF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF7671" \
            "6DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFA6BBE8FF767187FF76716DFF76716DFF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFF" \
            "D1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFF8FBBE8FF76716DFF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA671" \
            "6DFFFFFFD1FFA6D2FFFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8" \
            "FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFF76716DFF76716DFF76716DFFA68B6DFFE9D2B9FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A3" \
            "6DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFD4FFFFFF7671A0FF76716DFF76716DFFFFD2A0FFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFBDE8FFFFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3" \
            "A0FFA6A3A0FFBDA3A0FFFFE8D1FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFA6BBE8FF76716DFF76716DFF8F716DFF8F8B87FF8F8B87FF8F8B87FF767187FF76716DFF76716DFF8F716DFF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FFD4A387FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4FFFFFF7671A0FF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFF8FBBE8FF76716DFF76716DFF7671" \
            "6DFF76716DFFA68B6DFFE9E8D1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FF76A3D1FF7671" \
            "6DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFF" \
            "FFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFA6716DFFFFFFD1FFE9FFFFFF768BB9FF76716DFF76716DFF8F716DFFE9D2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFA6D2D1FF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFF" \
            "D1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFD4FFD1FF7671A0FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFA6716DFFD4FFD1FF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFFA68B87FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3" \
            "A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FF8FA3A0FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFD4A36DFFFFFFFFFFD4FFFFFF7671A0FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFD4FFD1FF7671A0FF76716DFF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFA6716DFFD4FFD1FF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFFD4BB87FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFA6BBD1FF767187FF76716DFFD4A3" \
            "6DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4FFFFFF7671A0FF76716DFF76716DFF8F716DFFE9D2A0FFFFFFFFFFFFFFFFFFFFFFFFFFD4E8FFFF768BA0FF76716DFF76716DFF76716DFFFFD2A0FFFFFF" \
            "FFFFE9FFFFFF768BB9FF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4D2E8FFFFE8D1FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF7671" \
            "87FF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFE9FFD1FFD4D2E8FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFE9D2D1FFD4FF" \
            "E8FF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FA3D1FF8F8B87FF8F8B87FF8F8B87FF768B87FF76716DFF7671" \
            "6DFF76716DFF8F716DFF8F8B87FF8F8B87FF8F8B87FFBDA387FFFFFFE8FFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFF76716DFF8F8B87FF767187FF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF8F716DFFA6A3A0FFA6A3A0FF8FA3" \
            "A0FF767187FF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF7671" \
            "6DFFD4BB87FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFA6BBD1FF767187FF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFF" \
            "FFFFA6D2FFFF767187FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A387FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA671" \
            "6DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFFA68B87FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3" \
            "A0FFA6A3A0FF8FA3A0FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FA3D1FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FFBDA387FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF8FA3D1FF767187FF76716DFF76716DFF76716DFF76716DFFA68B" \
            "6DFFE9E8D1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2E8FF768B87FF76716DFF76716DFF76716DFF76716DFF76716DFFA68B87FFFFE8D1FFFFFFFFFFFFFFFFFFA6D2FFFF8F8B87FF8F8B87FFA68B87FFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FA3D1FF8F8B87FF8F8B" \
            "87FFD4A387FFFFFFFFFFFFFFFFFFBDE8FFFF8F8BA0FF8F8B87FF8F8B87FFBDA387FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF8F8B87FF8F8B87FFA68B87FFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9E8E8FFFFE8E8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFE9E8FFFFE9E8E8FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFFA6BBD1FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFD4BBA0FFFFFF" \
            "E8FFFFFFFFFFFFFFFFFFA6BBE8FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FFD4A387FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")')
        self.btnSpeedButtonSetGlyph.OnClick = OnSetSpeedButtonGlyphClick
        def OnSetSpeedButtonLayoutClick(sender):
            self.InternalRunScript('f.SpeedButton.Layout = "blGlyphBottom"')
        self.btnSpeedButtonSetLayout.OnClick = OnSetSpeedButtonLayoutClick
        def OnSetSpeedButtonFlatClick(sender):
            self.InternalRunScript('f.SpeedButton.Flat = False')
        self.btnSpeedButtonSetFlat.OnClick = OnSetSpeedButtonFlatClick
        def OnSetSpeedButtonBoundsClick(sender):
            self.InternalRunScript('f.SpeedButton.SetBounds(224, 102, 218, 52)')
        self.btnSpeedButtonSetBounds.OnClick = OnSetSpeedButtonBoundsClick
        def OnToggleSpeedButtonEnabledClick(sender):
            self.InternalRunScript('f.SpeedButton.Enabled = not f.SpeedButton.Enabled')
        self.btnSpeedButtonToggleEnabled.OnClick = OnToggleSpeedButtonEnabledClick
        def OnToggleSpeedButtonVisibleClick(sender):
            self.InternalRunScript('f.SpeedButton.Visible = not f.SpeedButton.Visible')
        self.btnSpeedButtonToggleVisible.OnClick = OnToggleSpeedButtonVisibleClick
        def OnSetSpeedButtonAlignClick(sender):
            self.InternalRunScript('f.SpeedButton.Align = "alLeft"')
        self.btnSpeedButtonSetAlign.OnClick = OnSetSpeedButtonAlignClick
        def OnSetSpeedButtonMargins(sender):
            self.InternalRunScript('f.SpeedButton.AlignWithMargins = True\r\nf.SpeedButton.Margins.Left = 100\r\nf.SpeedButton.Margins.Top = 10\r\nf.SpeedButton.Margins.Right = 100\r\nf.SpeedButton.Margins.Bottom = 10')
        self.btnSpeedButtonSetMargins.OnClick = OnSetSpeedButtonMargins
# Bitmap Button
        def OnSetBitBtnDefaultClick(sender):
            self.InternalRunScript('f.bbBitBtn.Default = True')
        self.btnBitBtnSetDefault.OnClick = OnSetBitBtnDefaultClick
        def OnSetBitBtnGlyphClick(sender):
            self.InternalRunScript('f.bbBitBtn.LoadImageFromString("424D6A8B0000000000003600000028000000970000003B0000000100200000000000348B000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFFA6BBD1FFA6A3A0FFBDA3A0FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFA6BBE8FFA6A3A0FFA6A3A0FFA6A3A0FFD4BBA0FFFFE8E8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFF8F71" \
            "6DFFFFE8B9FFFFFFFFFFA6D2FFFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9E8E8FFE9E8E8FFE9E8E8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFFE9E8E8FFE9E8E8FFE9E8E8FFFFFFE8FFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9E8FFFFE9E8E8FFE9E8E8FFFFE8E8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFA6D2FFFF76716DFF76716DFF76716DFF76716DFF76716DFF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4E8" \
            "E8FF768BA0FF76716DFF76716DFF76716DFF76716DFF76716DFFA68B6DFFE9D2B9FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBD1FF767187FF76716DFF76716DFF76716DFF76716DFF76716DFF8F716DFFD4BBA0FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFFA6BBD1FF767187FF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFFD4A387FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFF" \
            "D1FFA6D2FFFF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE8E8FFFFFFFFFFFFFFFFFFA6D2E8FF767187FF76716DFFD4A36DFFFFFFFFFFFFFFFFFFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFA6D2E8FF76716DFF76716DFFD4BB87FFE9E8E8FFE9E8E8FFE9E8" \
            "E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A3" \
            "87FFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFFA68B87FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3" \
            "A0FFBDA3A0FFFFE8D1FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFBDD2E8FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FF8F8BA0FF76716DFF76716DFFA68B6DFFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFBDA3A0FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF8F8B6DFFA6A3A0FF8F8BA0FF76716DFF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFFA68B87FFD4BBB9FFD4D2" \
            "D1FFA6BBD1FF768B87FF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFFA68B87FF8FA3A0FF767187FF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFA6D2" \
            "E8FFBD8B87FF8FBBD1FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFFFFFFFFFD4E8FFFF768BB9FF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFE9FFFFFFBDBBD1FFFFE8D1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFE9FF" \
            "FFFF768BB9FF76716DFF76716DFFA6716DFFFFE8D1FFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFF" \
            "FFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFFA68B87FFA6A3A0FFA6A3A0FFA6A3A0FF768BA0FF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FF8FBBE8FF76716DFF76716DFFA68B6DFFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FF8F8BA0FF7671" \
            "6DFF76716DFFA68B6DFFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFBDA3A0FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFD4FFFFFF7671A0FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4FF" \
            "FFFF7671A0FF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFFFFD2" \
            "A0FFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFE9FFFFFF768BB9FF76716DFF76716DFFE9D2A0FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFA6D2E8FF76716DFF76716DFFD4BB87FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFE9E8E8FFFFFF" \
            "E8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFFA6716DFFFFFFD1FFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF8FBBD1FF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF7671" \
            "6DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFBDBBA0FF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671" \
            "A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF7671" \
            "6DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFFA6D2E8FF768B87FF76716DFF76716DFF7671" \
            "6DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFD4A36DFFBDE8" \
            "FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFF8F716DFF8F8B87FF8F8B87FF8F8B87FF767187FF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF7671" \
            "6DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFA6BBE8FF767187FF76716DFF76716DFF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFF" \
            "D1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFFFFFFFFF8FBBE8FF76716DFF76716DFFA6716DFFFFFFD1FFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA671" \
            "6DFFFFFFD1FFA6D2FFFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF8F716DFFFFE8B9FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8" \
            "FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFF76716DFF76716DFF76716DFFA68B6DFFE9D2B9FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A3" \
            "6DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FFD4FFFFFF7671A0FF76716DFF76716DFFFFD2A0FFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFBDE8FFFFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3" \
            "A0FFA6A3A0FFBDA3A0FFFFE8D1FFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFA6BBE8FF76716DFF76716DFF8F716DFF8F8B87FF8F8B87FF8F8B87FF767187FF76716DFF76716DFF8F716DFF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FFD4A387FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4FFFFFF7671A0FF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFF8FBBE8FF76716DFF76716DFF7671" \
            "6DFF76716DFFA68B6DFFE9E8D1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFFFFFD1FF76A3D1FF7671" \
            "6DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFF" \
            "FFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFA6716DFFFFFFD1FFE9FFFFFF768BB9FF76716DFF76716DFF8F716DFFE9D2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFFA6716DFFA6D2D1FF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFF" \
            "D1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFD4FFD1FF7671A0FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFA6716DFFD4FFD1FF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFFA68B87FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3" \
            "A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FF8FA3A0FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFD4A36DFFFFFFFFFFD4FFFFFF7671A0FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFD4FFD1FF7671A0FF76716DFF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFA6716DFFD4FFD1FF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFFD4BB87FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFA6BBD1FF767187FF76716DFFD4A3" \
            "6DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFFFFD2A0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4FFFFFF7671A0FF76716DFF76716DFF8F716DFFE9D2A0FFFFFFFFFFFFFFFFFFFFFFFFFFD4E8FFFF768BA0FF76716DFF76716DFF76716DFFFFD2A0FFFFFF" \
            "FFFFE9FFFFFF768BB9FF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4D2E8FFFFE8D1FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF7671" \
            "87FF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFE9FFD1FFD4D2E8FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFE9D2D1FFD4FF" \
            "E8FF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FA3D1FF8F8B87FF8F8B87FF8F8B87FF768B87FF76716DFF7671" \
            "6DFF76716DFF8F716DFF8F8B87FF8F8B87FF8F8B87FFBDA387FFFFFFE8FFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFF76716DFF8F8B87FF767187FF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF8F716DFFA6A3A0FFA6A3A0FF8FA3" \
            "A0FF767187FF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFFA6716DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD4FFFFFF7671A0FF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF7671" \
            "6DFFD4BB87FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFD4D2D1FFA6BBD1FF767187FF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFF" \
            "FFFFA6D2FFFF767187FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A387FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF8F716DFFFFE8B9FFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA671" \
            "6DFFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF76A3D1FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFBDE8FFFF767187FF76716DFF76716DFF76716DFFE9BB87FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF76716DFF76716DFFA6716DFFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFFA68B87FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3" \
            "A0FFA6A3A0FF8FA3A0FF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FA3D1FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FFBDA387FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFF8FA3D1FF767187FF76716DFF76716DFF76716DFF76716DFFA68B" \
            "6DFFE9E8D1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2E8FF768B87FF76716DFF76716DFF76716DFF76716DFF76716DFFA68B87FFFFE8D1FFFFFFFFFFFFFFFFFFA6D2FFFF8F8B87FF8F8B87FFA68B87FFFFFFD1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF8FA3D1FF8F8B87FF8F8B" \
            "87FFD4A387FFFFFFFFFFFFFFFFFFBDE8FFFF8F8BA0FF8F8B87FF8F8B87FFBDA387FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA6D2FFFF8F8B87FF8F8B87FFA68B87FFFFFFD1FFFFFFFFFFE9FFFFFF768BB9FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF7671" \
            "6DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFBD8B6DFFFFFFE8FFFFFFFFFFFFFFFFFF8FBBE8FF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFF76716DFFD4A36DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9E8E8FFFFE8E8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFE9E8FFFFE9E8E8FFFFFFE8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9FFFFFFA6BBD1FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFA6A3A0FFD4BBA0FFFFFF" \
            "E8FFFFFFFFFFFFFFFFFFA6BBE8FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FF8F8B87FFD4A387FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" \
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")')
        self.btnBitBtnSetGlyph.OnClick = OnSetBitBtnGlyphClick
        def OnSetBitBtnKindClick(sender):
            self.InternalRunScript('f.bbBitBtn.Kind = "bkOK"')
        self.btnBitBtnSetKind.OnClick = OnSetBitBtnKindClick
        def OnSetBitBtnBoundsClick(sender):
            self.InternalRunScript('f.bbBitBtn.SetBounds(211, 77, 218, 64)')
        self.btnBitBtnSetBounds.OnClick = OnSetBitBtnBoundsClick
        def OnToggleBitBtnEnabledClick(sender):
            self.InternalRunScript('f.bbBitBtn.Enabled = not f.bbBitBtn.Enabled')
        self.btnBitBtnToggleEnabled.OnClick = OnToggleBitBtnEnabledClick
        def OnToggleBitBtnVisibleClick(sender):
            self.InternalRunScript('f.bbBitBtn.Visible = not f.bbBitBtn.Visible')
        self.btnBitBtnToggleVisible.OnClick = OnToggleBitBtnVisibleClick
        def OnSetBitBtnAlignClick(sender):
            self.InternalRunScript('f.bbBitBtn.Align = "alLeft"')
        self.btnBitBtnSetAlign.OnClick = OnSetBitBtnAlignClick
        def OnSetBitBtnMargins(sender):
            self.InternalRunScript('f.bbBitBtn.AlignWithMargins = True\r\nf.bbBitBtn.Margins.Left = 100\r\nf.bbBitBtn.Margins.Top = 10\r\nf.bbBitBtn.Margins.Right = 100\r\nf.bbBitBtn.Margins.Bottom = 10')
        self.btnBitBtnSetMargins.OnClick = OnSetBitBtnMargins
# Draw Grid
        self.edit =Edit(self)
        self.edit.Visible = True
        self.edit.Text = 'edit box'
        self.edit.Parent = self.dgDrawGrid
        self.com = ComboBox(self)
        self.com.Visible = True
        self.com.Parent = self.dgDrawGrid
        self.com.Items.Assign(["1","2","3","4"])
        self.com.Text = '3'
        def on_draw_dg(sender, col, row, rect, state):
            if col == 1 and row == 1:
                self.edit.Left = rect.Left
                self.edit.Top = rect.Top
                self.edit.Width = rect.Right - rect.Left
                self.edit.Height = rect.Bottom - rect.Top
            elif col ==1  and row ==2:
                pass
                self.com.Left = rect.Left
                self.com.Top = rect.Top
                self.com.Width = rect.Right - rect.Left
            else:
                self.dgDrawGrid.Canvas.FillRect(rect)
                self.dgDrawGrid.Canvas.TextOut(rect.Left, rect.Top + 2, str(col) + ',' + str(row))
        self.dgDrawGrid.OnDrawCell = on_draw_dg
        def OnSetDrawGridBevelKindClick(sender):
            self.InternalRunScript('f.dgDrawGrid.BevelKind = "bkFlat"')
        self.btnDrawGridSetBevelKind.OnClick = OnSetDrawGridBevelKindClick
        def OnSetDrawGridBiDiModeClick(sender):
            self.InternalRunScript('f.dgDrawGrid.BiDiMode = "bdRightToLeft"')
        self.btnDrawGridSetBiDiMode.OnClick = OnSetDrawGridBiDiModeClick
        def OnSetDrawGridBorderStyleClick(sender):
            self.InternalRunScript('f.dgDrawGrid.BorderStyle = "bsSingle"')
        self.btnDrawGridSetBorderStyle.OnClick = OnSetDrawGridBorderStyleClick
        def OnSetDrawGridScrollBarsClick(sender):
            self.InternalRunScript('f.dgDrawGrid.ScrollBars = "ssNone"')
        self.btnDrawGridSetScrollBars.OnClick = OnSetDrawGridScrollBarsClick
        def OnSetDrawGridBoundsClick(sender):
            self.InternalRunScript('f.dgDrawGrid.SetBounds(102, 70, 512, 192)')
        self.btnDrawGridSetBounds.OnClick = OnSetDrawGridBoundsClick
        def OnToggleDrawGridEnabledClick(sender):
            self.InternalRunScript('f.dgDrawGrid.Enabled = not f.dgDrawGrid.Enabled')
        self.btnDrawGridToggleEnabled.OnClick = OnToggleDrawGridEnabledClick
        def OnToggleDrawGridVisibleClick(sender):
            self.InternalRunScript('f.dgDrawGrid.Visible = not f.dgDrawGrid.Visible')
        self.btnDrawGridToggleVisible.OnClick = OnToggleDrawGridVisibleClick
        def OnSetDrawGridAlignClick(sender):
            self.InternalRunScript('f.dgDrawGrid.Align = "alLeft"')
        self.btnDrawGridSetAlign.OnClick = OnSetDrawGridAlignClick
        def OnSetDrawGridMargins(sender):
            self.InternalRunScript('f.dgDrawGrid.AlignWithMargins = True\r\nf.dgDrawGrid.Margins.Left = 100\r\nf.dgDrawGrid.Margins.Top = 10\r\nf.dgDrawGrid.Margins.Right = 100\r\nf.dgDrawGrid.Margins.Bottom = 10')
        self.btnDrawGridSetMargins.OnClick = OnSetDrawGridMargins
        self.dgDrawGrid.SetColWidthByIndex(0, self.dgDrawGrid.GetColWidthByIndex(0) + 50)
        self.dgDrawGrid.SetRowHeightByIndex(0, self.dgDrawGrid.GetRowHeightByIndex(0) + 50)

# String Grid
        def OnSetStringGridBevelKindClick(sender):
            self.InternalRunScript('f.sgStringGrid.BevelKind = "bkFlat"')
        self.btnStringGridSetBevelKind.OnClick = OnSetStringGridBevelKindClick
        def OnSetStringGridBiDiModeClick(sender):
            self.InternalRunScript('f.sgStringGrid.BiDiMode = "bdRightToLeft"')
        self.btnStringGridSetBiDiMode.OnClick = OnSetStringGridBiDiModeClick
        def OnSetStringGridBorderStyleClick(sender):
            self.InternalRunScript('f.sgStringGrid.BorderStyle = "bsSingle"')
        self.btnStringGridSetBorderStyle.OnClick = OnSetStringGridBorderStyleClick
        def OnSetStringGridScrollBarsClick(sender):
            self.InternalRunScript('f.sgStringGrid.ScrollBars = "ssNone"')
        self.btnStringGridSetScrollBars.OnClick = OnSetStringGridScrollBarsClick
        def OnSetStringGridBoundsClick(sender):
            self.InternalRunScript('f.sgStringGrid.SetBounds(102, 70, 512, 192)')
        self.btnStringGridSetBounds.OnClick = OnSetStringGridBoundsClick
        def OnToggleStringGridEnabledClick(sender):
            self.InternalRunScript('f.sgStringGrid.Enabled = not f.sgStringGrid.Enabled')
        self.btnStringGridToggleEnabled.OnClick = OnToggleStringGridEnabledClick
        def OnToggleStringGridVisibleClick(sender):
            self.InternalRunScript('f.sgStringGrid.Visible = not f.sgStringGrid.Visible')
        self.btnStringGridToggleVisible.OnClick = OnToggleStringGridVisibleClick
        def OnSetStringGridAlignClick(sender):
            self.InternalRunScript('f.sgStringGrid.Align = "alLeft"')
        self.btnStringGridSetAlign.OnClick = OnSetStringGridAlignClick
        def OnSetStringGridMargins(sender):
            self.InternalRunScript('f.sgStringGrid.AlignWithMargins = True\r\nf.sgStringGrid.Margins.Left = 100\r\nf.sgStringGrid.Margins.Top = 10\r\nf.sgStringGrid.Margins.Right = 100\r\nf.sgStringGrid.Margins.Bottom = 10')
        self.btnStringGridSetMargins.OnClick = OnSetStringGridMargins
        # draw cell
        DFC_BUTTON = 4
        DFCS_BUTTONCHECK = 0
        DFCS_CHECKED = 1024
        grd = self.sgStringGrid
        grd.ColCount = 10
        grd.RowCount = 10        
        grd.DefaultColWidth = 20
        grd.DefaultRowHeight = 20
        grd.FixedCols = 1
        grd.FixedRows = 1
        for i in range(0, grd.ColCount):
            for j in range(0, grd.RowCount):
                if (j < 1) or (i < 1):
                    grd.SetCell(i, j, str(j * grd.ColCount + i))
                else:
                    grd.SetCell(i, j, str(random.randint(0, 1)))
        def OnStringGridSelectCell(sender, acol, arow, CanSelect):
            if acol < 5:
                grd.Options = ["goFixedVertLine", "goFixedHorzLine", "goVertLine", "goHorzLine", "goRangeSelect", "goDrawFocusSelected", "goFixedRowDefAlign"]
                if grd.GetCell(acol, arow) == '1':
                    grd.SetCell(acol, arow, '0')
                else:
                    grd.SetCell(acol, arow, '1')
            else:
                grd.Options = ["goFixedVertLine", "goFixedHorzLine", "goVertLine", "goHorzLine", "goRangeSelect", "goDrawFocusSelected", "goFixedRowDefAlign", "goEditing"]
        grd.OnSelectCell = OnStringGridSelectCell
        
        def OnStringGridDrawCell(Sender, ACol, ARow, ARect, State):
            sg = grd
            rct = Rect(0, 0, 5, 5)            
            if ACol >= sg.FixedCols and ARow >= sg.FixedRows:
                rct.Left = (ARect.Right - ARect.Left - 16) // 2 + ARect.Left
                rct.Top = (ARect.Bottom - ARect.Top - 16) // 2 + ARect.Top
                rct.Right = rct.Left + 16
                rct.Bottom = rct.Top + 16
                if sg.GetCell(ACol, ARow) == '1':
                    rtl.draw_frame_control(sg.Canvas.Handle, rct.Left, rct.Top, 16, 16, DFC_BUTTON, DFCS_BUTTONCHECK | DFCS_CHECKED)
                else:
                    rtl.draw_frame_control(sg.Canvas.Handle, rct.Left, rct.Top, 16, 16, DFC_BUTTON, DFCS_BUTTONCHECK)        
        grd.OnDrawCell = OnStringGridDrawCell

# Spin Edit
        def OnSetSpinEditColorClick(sender):
            self.InternalRunScript('f.seSpinEdit.Color = clMenuHighlight')
        self.btnSpinEditSetColor.OnClick = OnSetSpinEditColorClick
        def OnSetSpinEditCtl3DClick(sender):
            self.InternalRunScript('f.seSpinEdit.Ctl3D = True')
        self.btnSpinEditSetCtl3D.OnClick = OnSetSpinEditCtl3DClick
        def OnSetSpinEditBoundsClick(sender):
            self.InternalRunScript('f.seSpinEdit.SetBounds(166, 77, 194, 38)')
        self.btnSpinEditSetBounds.OnClick = OnSetSpinEditBoundsClick
        def OnToggleSpinEditEnabledClick(sender):
            self.InternalRunScript('f.seSpinEdit.Enabled = not f.seSpinEdit.Enabled')
        self.btnSpinEditToggleEnabled.OnClick = OnToggleSpinEditEnabledClick
        def OnToggleSpinEditVisibleClick(sender):
            self.InternalRunScript('f.seSpinEdit.Visible = not f.seSpinEdit.Visible')
        self.btnSpinEditToggleVisible.OnClick = OnToggleSpinEditVisibleClick
        def OnSetSpinEditAlignClick(sender):
            self.InternalRunScript('f.seSpinEdit.Align = "alLeft"')
        self.btnSpinEditSetAlign.OnClick = OnSetSpinEditAlignClick
        def OnSetSpinEditMargins(sender):
            self.InternalRunScript('f.seSpinEdit.AlignWithMargins = True\r\nf.seSpinEdit.Margins.Left = 100\r\nf.seSpinEdit.Margins.Top = 10\r\nf.seSpinEdit.Margins.Right = 100\r\nf.seSpinEdit.Margins.Bottom = 10')
        self.btnSpinEditSetMargins.OnClick = OnSetSpinEditMargins
# Activity Indicator
        def OnSetActivityIndicatorIndicatorSizeClick(sender):
            self.InternalRunScript('f.aiActivityIndicator.IndicatorSize = "aisXLarge"')
        self.btnActivityIndicatorSetIndicatorSize.OnClick = OnSetActivityIndicatorIndicatorSizeClick
        def OnSetActivityIndicatorBoundsClick(sender):
            self.InternalRunScript('f.aiActivityIndicator.SetBounds(77, 51, 64, 64)')
        self.btnActivityIndicatorSetBounds.OnClick = OnSetActivityIndicatorBoundsClick
        def OnSetActivityIndicatorAlignClick(sender):
            self.InternalRunScript('f.aiActivityIndicator.Align = "alLeft"')
        self.btnActivityIndicatorSetAlign.OnClick = OnSetActivityIndicatorAlignClick
        def OnSetActivityIndicatorMargins(sender):
            self.InternalRunScript('f.aiActivityIndicator.AlignWithMargins = True\r\nf.aiActivityIndicator.Margins.Left = 100\r\nf.aiActivityIndicator.Margins.Top = 10\r\nf.aiActivityIndicator.Margins.Right = 100\r\nf.aiActivityIndicator.Margins.Bottom = 10')
        self.btnActivityIndicatorSetMargins.OnClick = OnSetActivityIndicatorMargins
# Toggle Switch
        def OnSetToggleSwitchAlignmentClick(sender):
            self.InternalRunScript('f.tgToggleSwitch.Alignment = "taLeftJustify"')
        self.btnToggleSwitchSetAlignment.OnClick = OnSetToggleSwitchAlignmentClick
        def OnSetToggleSwitchColorClick(sender):
            self.InternalRunScript('f.tgToggleSwitch.Color = clBlue')
        self.btnToggleSwitchSetColor.OnClick = OnSetToggleSwitchColorClick
        def OnSetToggleSwitchBoundsClick(sender):
            self.InternalRunScript('f.tgToggleSwitch.SetBounds(109, 64, 136, 40)')
        self.btnToggleSwitchSetBounds.OnClick = OnSetToggleSwitchBoundsClick
        def OnToggleToggleSwitchEnabledClick(sender):
            self.InternalRunScript('f.tgToggleSwitch.Enabled = not f.tgToggleSwitch.Enabled')
        self.btnToggleSwitchToggleEnabled.OnClick = OnToggleToggleSwitchEnabledClick
        def OnToggleToggleSwitchVisibleClick(sender):
            self.InternalRunScript('f.tgToggleSwitch.Visible = not f.tgToggleSwitch.Visible')
        self.btnToggleSwitchToggleVisible.OnClick = OnToggleToggleSwitchVisibleClick
        def OnSetToggleSwitchAlignClick(sender):
            self.InternalRunScript('f.tgToggleSwitch.Align = "alLeft"')
        self.btnToggleSwitchSetAlign.OnClick = OnSetToggleSwitchAlignClick
        def OnSetToggleSwitchMargins(sender):
            self.InternalRunScript('f.tgToggleSwitch.AlignWithMargins = True\r\nf.tgToggleSwitch.Margins.Left = 100\r\nf.tgToggleSwitch.Margins.Top = 10\r\nf.tgToggleSwitch.Margins.Right = 100\r\nf.tgToggleSwitch.Margins.Bottom = 10')
        self.btnToggleSwitchSetMargins.OnClick = OnSetToggleSwitchMargins
# Number Box
        def OnSetNumberBoxBorderStyleClick(sender):
            self.InternalRunScript('f.nbNumberBox.BorderStyle = "bsSingle"')
        self.btnNumberBoxSetBorderStyle.OnClick = OnSetNumberBoxBorderStyleClick
        def OnSetNumberBoxBiDiModeClick(sender):
            self.InternalRunScript('f.nbNumberBox.BiDiMode = "bdRightToLeft"')
        self.btnNumberBoxSetBiDiMode.OnClick = OnSetNumberBoxBiDiModeClick
        def OnSetNumberBoxColorClick(sender):
            self.InternalRunScript('f.nbNumberBox.Color = clMenuHighlight')
        self.btnNumberBoxSetColor.OnClick = OnSetNumberBoxColorClick
        def OnSetNumberBoxDisplayFormatClick(sender):
            self.InternalRunScript('f.nbNumberBox.DisplayFormat = "100"')
        self.btnNumberBoxSetDisplayFormat.OnClick = OnSetNumberBoxDisplayFormatClick
        def OnSetNumberBoxBoundsClick(sender):
            self.InternalRunScript('f.nbNumberBox.SetBounds(134, 70, 194, 38)')
        self.btnNumberBoxSetBounds.OnClick = OnSetNumberBoxBoundsClick
        def OnToggleNumberBoxEnabledClick(sender):
            self.InternalRunScript('f.nbNumberBox.Enabled = not f.nbNumberBox.Enabled')
        self.btnNumberBoxToggleEnabled.OnClick = OnToggleNumberBoxEnabledClick
        def OnToggleNumberBoxVisibleClick(sender):
            self.InternalRunScript('f.nbNumberBox.Visible = not f.nbNumberBox.Visible')
        self.btnNumberBoxToggleVisible.OnClick = OnToggleNumberBoxVisibleClick
        def OnSetNumberBoxAlignClick(sender):
            self.InternalRunScript('f.nbNumberBox.Align = "alLeft"')
        self.btnNumberBoxSetAlign.OnClick = OnSetNumberBoxAlignClick
        def OnSetNumberBoxMargins(sender):
            self.InternalRunScript('f.nbNumberBox.AlignWithMargins = True\r\nf.nbNumberBox.Margins.Left = 100\r\nf.nbNumberBox.Margins.Top = 10\r\nf.nbNumberBox.Margins.Right = 100\r\nf.nbNumberBox.Margins.Bottom = 10')
        self.btnNumberBoxSetMargins.OnClick = OnSetNumberBoxMargins
# Media Player
        def OnSetMediaPlayerAutoEnableClick(sender):
            self.InternalRunScript('f.mpMediaPlayer.AutoEnable = False')
        self.btnMediaPlayerSetAutoEnable.OnClick = OnSetMediaPlayerAutoEnableClick
        def OnSetMediaPlayerFileNameClick(sender):
            self.InternalRunScript('f.mpMediaPlayer.FileName = r"C:\\CANoe.avi"')
        self.btnMediaPlayerSetFileName.OnClick = OnSetMediaPlayerFileNameClick
        def OnSetMediaPlayerBoundsClick(sender):
            self.InternalRunScript('f.mpMediaPlayer.SetBounds(198, 90, 506, 48)')
        self.btnMediaPlayerSetBounds.OnClick = OnSetMediaPlayerBoundsClick
        def OnToggleMediaPlayerEnabledClick(sender):
            self.InternalRunScript('f.mpMediaPlayer.Enabled = not f.mpMediaPlayer.Enabled')
        self.btnMediaPlayerToggleEnabled.OnClick = OnToggleMediaPlayerEnabledClick
        def OnToggleMediaPlayerVisibleClick(sender):
            self.InternalRunScript('f.mpMediaPlayer.Visible = not f.mpMediaPlayer.Visible')
        self.btnMediaPlayerToggleVisible.OnClick = OnToggleMediaPlayerVisibleClick
        def OnSetMediaPlayerAlignClick(sender):
            self.InternalRunScript('f.mpMediaPlayer.Align = "alClient"')
        self.btnMediaPlayerSetAlign.OnClick = OnSetMediaPlayerAlignClick
        def OnSetMediaPlayerMargins(sender):
            self.InternalRunScript('f.mpMediaPlayer.AlignWithMargins = True\r\nf.mpMediaPlayer.Margins.Left = 100\r\nf.mpMediaPlayer.Margins.Top = 10\r\nf.mpMediaPlayer.Margins.Right = 100\r\nf.mpMediaPlayer.Margins.Bottom = 10')
        self.btnMediaPlayerSetMargins.OnClick = OnSetMediaPlayerMargins
# Image Button
        def OnSetImageButtonBevelInnerClick(sender):
            self.InternalRunScript('f.ibImageButton.BevelInner = "bvLowered"')
        self.btnImageButtonSetBevelInner.OnClick = OnSetImageButtonBevelInnerClick
        def OnSetImageButtonBevelKindClick(sender):
            self.InternalRunScript('f.ibImageButton.BevelKind = "dkDock"')
        self.btnImageButtonSetBevelKind.OnClick = OnSetImageButtonBevelKindClick
        def OnSetImageButtonBevelOuterClick(sender):
            self.InternalRunScript('f.ibImageButton.BevelOuter = "bvRaised"')
        self.btnImageButtonSetBevelOuter.OnClick = OnSetImageButtonBevelOuterClick
        def OnSetImageButtonImageStretchClick(sender):
            self.InternalRunScript('f.ibImageButton.ImageStretch = True')
        self.btnImageButtonSetImageStretch.OnClick = OnSetImageButtonImageStretchClick
        def OnSetImageButtonShowCaptionClick(sender):
            self.InternalRunScript('f.ibImageButton.ShowCaption = True')
        self.btnImageButtonSetShowCaption.OnClick = OnSetImageButtonShowCaptionClick
        def OnSetImageButtonColorClick(sender):
            self.InternalRunScript('f.ibImageButton.Color = clMenuHighlight')
        self.btnImageButtonSetColor.OnClick = OnSetImageButtonColorClick
        def OnSetImageButtonParentBackgroundClick(sender):
            self.InternalRunScript('f.ibImageButton.ParentBackground = False')
        self.btnImageButtonSetParentBackground.OnClick = OnSetImageButtonParentBackgroundClick
        def OnSetImageButtonBoundsClick(sender):
            self.InternalRunScript('f.ibImageButton.SetBounds(198, 90, 506, 48)')
        self.btnImageButtonSetBounds.OnClick = OnSetImageButtonBoundsClick
        def OnToggleImageButtonEnabledClick(sender):
            self.InternalRunScript('f.ibImageButton.Enabled = not f.ibImageButton.Enabled')
        self.btnImageButtonToggleEnabled.OnClick = OnToggleImageButtonEnabledClick
        def OnToggleImageButtonVisibleClick(sender):
            self.InternalRunScript('f.ibImageButton.Visible = not f.ibImageButton.Visible')
        self.btnImageButtonToggleVisible.OnClick = OnToggleImageButtonVisibleClick
        def OnSetImageButtonAlignClick(sender):
            self.InternalRunScript('f.ibImageButton.Align = "alClient"')
        self.btnImageButtonSetAlign.OnClick = OnSetImageButtonAlignClick
        def OnSetImageButtonMargins(sender):
            self.InternalRunScript('f.ibImageButton.AlignWithMargins = True\r\nf.ibImageButton.Margins.Left = 100\r\nf.ibImageButton.Margins.Top = 10\r\nf.ibImageButton.Margins.Right = 100\r\nf.ibImageButton.Margins.Bottom = 10')
        self.btnImageButtonSetMargins.OnClick = OnSetImageButtonMargins

# popup menu
        self.btnPopup.Images = app.get_system_imagelist_16px()
        self.btnPopup.ImageIndex = 123
        def on_menu_item1_click(sender):
            ShowMessage('menu 1 on click')
        def on_menu_item2_click(sender):
            ShowMessage('menu 2 on click')
        self.pop1 = PopupMenu(self)
        self.pop1.Images = app.get_system_imagelist_16px()
        itm1 = MenuItem(self.pop1)
        itm1.Caption = 'menu item 1'
        itm1.ImageIndex = 111
        itm1.OnClick = on_menu_item1_click
        self.pop1.Items.Add(itm1)
        itm1 = MenuItem(self.pop1)
        itm1.Caption = 'menu item 2'
        itm1.ImageIndex = 222
        itm1.OnClick = on_menu_item2_click
        self.pop1.Items.Add(itm1)
        self.btnPopup.PopupMenu = self.pop1
        def on_btnpop_click(sender):
            p = Point(5, 5)
            p = self.btnPopup.ClientToScreen(p)
            self.pop1.Popup(p.X, p.Y)
        self.btnPopup.OnClick = on_btnpop_click

        # TreeView
        self.trv.Images = app.get_system_imagelist_16px()
        self.trv.CheckBoxes = True
        self.node_top = self.trv.Items.AddChild(None, 'top node')
        self.node_sub1 = self.trv.Items.AddChild(self.node_top, 'sub node 1')
        self.node_sub2 = self.trv.Items.AddChild(self.node_top, 'sub node 2')
        self.node_top.ImageIndex = 100
        self.node_sub1.ImageIndex = 300
        self.node_sub2.ImageIndex = -1
        self.node_top.Checked = True        
        self.node_sub2.StateIndex = 1
        self.node_top.SelectedIndex = self.node_top.ImageIndex
        self.node_sub1.SelectedIndex = self.node_sub1.ImageIndex
        self.node_sub2.SelectedIndex = self.node_sub2.ImageIndex
        self.trv.FullExpand()
        self.node_sub1.CheckState = "ncsNone"
        # node_sub1.CheckedState = 0 # ncsNone, ncsUnchecked, ncsChecked, ncsPartial, ncsDimmed, ncsExclusion
        def on_treeview_align_click(Sender):
            self.InternalRunScript('f.trv.Align = "alLeft"')
        self.btnTreeViewAlign.OnClick = on_treeview_align_click
        def on_treeview_bounds_click(Sender):
            self.InternalRunScript('f.trv.Align = "alNone"\r\nf.trv.SetBounds(100, 100, 200, 200)')            
        self.btnTreeViewBounds.OnClick = on_treeview_bounds_click
        def on_treeview_checkbox_click(Sender):
            if self.node_sub1.CheckState == "ncsNone":
                self.InternalRunScript('f.node_sub1.CheckState = "ncsUnchecked"')
            else:
                self.InternalRunScript('f.node_sub1.CheckState = "ncsNone"')
        self.btnTreeViewCheckbox.OnClick = on_treeview_checkbox_click
        def on_treeview_checked_click(Sender):
            self.InternalRunScript('f.node_sub2.Checked = not f.node_sub2.Checked')
        self.btnTreeViewChecked.OnClick = on_treeview_checked_click
        def on_treeview_enabled_click(Sender):
            self.InternalRunScript('f.trv.Enabled = not f.trv.Enabled')
        self.btnTreeViewEnabled.OnClick = on_treeview_enabled_click
        def on_treeview_imageindex_click(Sender):
            self.InternalRunScript('f.node_sub1.ImageIndex = 400 - f.node_sub1.ImageIndex')
        self.btnTreeViewImageIndex.OnClick = on_treeview_imageindex_click
        def on_treeview_margins_click(Sender):
            self.InternalRunScript('f.trv.AlignWithMargins = not f.trv.AlignWithMargins')
        self.btnTreeViewMargins.OnClick = on_treeview_margins_click
        def on_treeview_visible_click(Sender):
            self.InternalRunScript('f.trv.Visible = not f.trv.Visible')
        self.btnTreeViewVisible.OnClick = on_treeview_visible_click
        def on_treeview_color_click(Sender):
            if self.trv.Color == clYellow:
                self.InternalRunScript('f.trv.Color = clBtnFace')
            else:
                self.InternalRunScript('f.trv.Color = clYellow')
        self.btnTreeViewColor.OnClick = on_treeview_color_click
        def on_treeview_check_changing(sender, Node: TreeNode, NewCheckState: int, OldCheckState: int, AllowChange: bool):
            print('tree view check state changing: ' + Node.Text)
            AllowChange = Node.Text == 'top node'
            return AllowChange
        self.trv.OnCheckStateChanging = on_treeview_check_changing

        # output info
        self.MM.Text = 'Screen.PrimaryMonitor.PixelsPerInch = ' + str(Screen.PrimaryMonitor.PixelsPerInch) + '\r\nScreen.PixelsPerInch = ' + str(Screen.PixelsPerInch) + '\r\nScreen.DefaultPixelsPerInch = ' + str(Screen.DefaultPixelsPerInch)

        # dynamically create a form
        def on_create_form_click(sender):
            frm = ConfigDialog.ConfigDialogForm(self)
            frm.Hide()
            frm.ShowModal()
            frm = None
        self.btnCreateForm.OnClick = on_create_form_click

        # list controls
        def on_list_controls_click(sender):
            n = self.grpFormProperties.ControlCount
            for i in range(n):
                self.log_hint("Control " + str(i + 1) + ': ' + rtl.get_control_by_index(self.grpFormProperties, i).ClassName)
        self.btnListControls.OnClick = on_list_controls_click

        # on system var change callback        
        def on_reg_sys_change_click(sender):
            if None == self.OnSystemVarChangeEvent:
                self.OnSystemVarChangeEvent = self.OnSystemVarChangeEventHandler            
                app.create_system_var('var_created_by_toolbox', 0, '111', 'auto created system var for demo')
                self.MM.Lines.Add('On system var change callback registered and a demo system var is created')
                self.RegisterOnSystemVarChangeEvent('var_created_by_toolbox')
            else:
                self.MM.Lines.Add('On system var change callback is already registered')
            
        self.btnRegOnSysVarChange.OnClick = on_reg_sys_change_click
        def on_trigger_sys_change_click(sender):
            if (None == self.OnSystemVarChangeEvent):
                ShowMessage('Please first register on system var change callback on right panel')
            else:
                app.set_system_var_generic('var_created_by_toolbox', str(random.randint(1, 999)))
        self.btnTriggerSysVarChange.OnClick = on_trigger_sys_change_click

        # custom image list
        self.btnImageList.Images = self.CreateImageList(16, app.get_current_toolbox_path('Toolbox_Guide') + r'/Images')
        self.btnImageList.ImageIndex = 0
        def on_btn_imagelist_click(sender):
            self.btnImageList.ImageIndex = 1 - self.btnImageList.ImageIndex        
        self.btnImageList.OnClick = on_btn_imagelist_click

        # treelist custom properties
        self.TSTreelist1.OptionsView.CheckGroups = True
        propRight = self.TSTreelist1.CreateEditProperties('TcxLabelProperties')
        propRight.Alignment.Horz = 'taRightJustify'
        # Treelist image column
        self.TSTreelist1Column1.Properties.Images = app.get_system_imagelist_16px()
        itm = self.TSTreelist1Column1.Properties.Items.Add()
        itm.Description = 'red'
        itm.ImageIndex = 172
        itm.Value = 'red'
        itm = self.TSTreelist1Column1.Properties.Items.Add()
        itm.Description = 'blue'
        itm.ImageIndex = 171
        itm.Value = 'blue'
        itm = self.TSTreelist1Column1.Properties.Items.Add()
        itm.Description = 'green'
        itm.ImageIndex = 173
        itm.Value = 'green'
        # Treelist
        def on_add_node_click(sender):
            node = self.TSTreelist1.Add()
            node.CheckGroupType = 'ncgCheckGroup'
            node.ImageIndex = self.TSTreelist1.Count
            node.SetValue(0, 'blue')
            node.SetValue(1, False)
            node.SetValue(2, 'this is a text')
            if node.Index % 2 == 0:
                self.TSTreelist1Column3.SetNodeProperties(node, propRight)                
                node.CheckState = 'cbsChecked'
            else:
                node.CheckState = 'cbsUnChecked'

        self.btnAddNode.OnClick = on_add_node_click
        def on_add_sub_node_click(sender):
            node = self.TSTreelist1.TopNode
            if node != None:
                node = node.AddChild()
                node.CheckState = 'cbsChecked'
                node.ImageIndex = self.TSTreelist1.Count
                node.SetValue(0, 'green')
                node.SetValue(1, True)
                node.SetValue(2, 'this is a sub node text')
                self.TSTreelist1.FocusedNode = node
        self.btnAddSubNodes.OnClick = on_add_sub_node_click
        def on_expand_all_click(sender):
            self.TSTreelist1.FullExpand()
        self.btnExpandAll.OnClick = on_expand_all_click
        def on_collapse_all_click(sender):
            self.TSTreelist1.FullCollapse()
        self.btnCollapseAll.OnClick = on_collapse_all_click
        def on_get_value_click(sender):
            node = self.TSTreelist1.TopNode
            if node != None:
                self.MM.Clear()
                self.MM.Lines.Add('first node value: ' + node.GetValue(0) + ', ' + node.GetValue(1) + ', ' + node.GetValue(2))
        self.btnGetValue.OnClick = on_get_value_click
        def on_set_value_click(sender):
            node = self.TSTreelist1.TopNode
            if node != None:
                node.ImageIndex = self.TSTreelist1.Count
                node.SetValue(0, 'red')
                node.SetValue(1, True)
                node.SetValue(2, 'value has been set')
        self.btnSetValue.OnClick = on_set_value_click
        def on_set_column_click(sender):
            self.TSTreelist1Column1.Caption.Text = 'Column 1 Text'
            self.TSTreelist1Column2.Caption.Text = 'Column 2 Text'
            self.TSTreelist1Column3.Caption.Text = 'Column 3 Text'
        self.btnSetColumn.OnClick = on_set_column_click
        def on_change_image_idx_click(sender):
            node = self.TSTreelist1.TopNode
            if node != None:
                node.ImageIndex = self.TSTreelist1.Count - node.ImageIndex
        self.btnChangeImageIdx.OnClick = on_change_image_idx_click
        # node check changing and changed events
        self.TSTreelist1.Root.CheckGroupType = 'ncgCheckGroup'
        def on_node_check_changing(ATreeList, ANode, AState, AAllow):
            v = ANode.GetValue(0)
            if v != None:
                # not during creation
                if ANode.Level == 0:
                    AAllow.Value = True
                else:
                    AAllow.Value = ANode.Index % 2 == 0 # you can control allow change here
                self.log_ok('node check changing: ' + v + ', state = ' + str(AState) + ', allowed = ' + str(AAllow))
        self.TSTreelist1.OnNodeCheckChanging = on_node_check_changing
        def on_node_check_changed(ATreeList, ANode, AState):
            v = ANode.GetValue(0)
            if v != None:
                # not during creation
                self.log_ok('node check changed: ' + v + ', state = ' + str(AState))
        self.TSTreelist1.OnNodeCheckChanged = on_node_check_changed

    def OnSystemVarChangeEventHandler(self, AVarname):
        log('AVarname changed', lvlOK)
        i, v = app.get_system_var_generic(AVarname)
        if 0 == i:
            s = f'var {AVarname} changed to: {v}'
            log(s, lvlOK)
            self.MM.Lines.Add(s)

    def OnScrollBarChangeEvent(self, sender):
        ShowMessage('Scroll bar position changed to: ' + str(self.sbScrollBar.Position))

    def OnRadioGroupClickEvent(self, sender):
        ShowMessage('Radio Group item index = ' + str(self.rgRadioGroup.ItemIndex))

    def OnStaticTextClickEvent(self, sender):
        ShowMessage('Static text is clicked')

    def OnListBoxChangeEvent(self, sender):
        if self.lstListBox.ItemIndex == -1:
            ShowMessage('List box index not set = -1')
        else:
            ShowMessage('List box index changed to: ' + str(self.lstListBox.ItemIndex) + ' = ' + self.lstListBox.Items[
                self.lstListBox.ItemIndex])

    def OnComboChangeEvent(self, sender):
        if self.cbCombo.ItemIndex == -1:
            ShowMessage('Combo box index not set = -1')
        else:
            ShowMessage('Combo box index changed to: ' + str(self.cbCombo.ItemIndex) + ' = ' + self.cbCombo.Items[
                self.cbCombo.ItemIndex])

    def OnMemoChangeEvent(self, sender):
        ShowMessage('Memo content changed to: ' + self.mmMemo.Text)

    def OnRadioButtonChangeEvent(self, sender):
        ShowMessage('Radio Buttons states: ' + str(self.rb1.Checked) + ' ' + str(self.rb2.Checked))

    def OnCheckboxClickEvent(self, sender):
        ShowMessage('Checked state: ' + str(self.chkCheckbox.Checked))

    def OnEditChangeEvent(self, sender):
        ShowMessage('Edit is changed to: ' + self.edtEdit.Text)

    def OnEditClickEvent(self, sender):
        ShowMessage('Edit is Clicked')

    def OnButtonClickEvent(self, sender):
        ShowMessage('Button is Clicked')

    def OnLabelClickEvent(self, sender):
        ShowMessage('Label is clicked')

    def InternalRunScript(self, AScript):
        self.MM.Text = AScript
        app.run_python_script(self.MM.Text)

    def OnConnectClick(self, Sender):
        if 0 == app.connect():
            app.make_toast('Connected!', 3)

    def OnDisconnectClick(self, sender):
        if 0 == app.disconnect():
            app.make_toast('Disconnected!', 3)

    def OnFormResizeEvent(self, Sender):
        self.log("Form size change event")

    def OnFormShowEvent(self, Sender):
        self.log("on show")

    def OnFormHideEvent(self, Sender):
        self.log("on hide")

    def btnHideClick(self, Sender):
        self.Hide()
        self.FShowHideCounter = 4
        app.make_toast("I am now hidden", 3)
        self.tim1.Enabled = True

    def OnShowTimer(self, sender):
        self.FShowHideCounter = self.FShowHideCounter - 1
        if self.FShowHideCounter > 0:
            app.make_toast(str(self.FShowHideCounter), 3)
        else:
            self.Show()
            app.make_toast("I am now shown again", 3)
            self.tim1.Enabled = False

    def UIRefreshEvent(self):
        if self.FNeedRefresh:
            self.FNeedRefresh = False
            self.log_ok("UI refresh event fired, Rx CAN frame count = " + str(self.FRecvCANCounter))

    def RawCANEvent(self, ACAN):
        self.FRecvCANCounter = self.FRecvCANCounter + 1
        self.FNeedRefresh = True
        self.log("Raw CAN: " + str(ACAN.id))

    def MeasurementPreStart(self):
        self.log_ok("On Measurement Pre Start event fired")

    def MeasurementStarted(self):
        self.log_ok("On Measurement Start event fired")

    def MeasurementPreStop(self):
        self.log_ok("On Measurement Pre Stop event fired")

    def MeasurementStopped(self):
        self.log_ok("On Measurement Stop event fired")


# Auto Generated Python Code, do not modify START [MAIN] ------------
if __name__ == "__main__":
    try:
        Toolbox_Guide_Copy().Show()
        Application.Run()
    except SystemExit:
        pass
# Auto Generated Python Code, do not modify END [MAIN] --------------
