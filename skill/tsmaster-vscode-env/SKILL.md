---
name: tsmaster-vscode-env
description: 一键配置 TSMaster 的 VSCode C++ 编译环境。提供“傻瓜式”开箱即用体验。具备智能探测 TSMaster 安装路径、自动从安装包提取并本地化 TSMaster.h 头文件、生成稳健的批处理编译脚本、自动配置 Git 忽略名单及 Clean 任务的能力。当用户提到“配置 TSMaster 的 VSCode 环境”、“编译 mp/mp64 文件”或“用 C++ 写 TSMaster 小程序”时，请触发此 Skill。
---

# TSMaster VSCode 环境配置 Skill

此 Skill 用于自动化配置 VSCode C++ 开发环境，旨在为任何水平的用户提供最流畅的“一键式”配置体验。

## 执行流程

### 1. 确认配置模式
使用 `ask_user` 向用户提供两种选择（优先推荐默认配置）：
- **选项 1: 一键标准配置 (推荐)**
  - 行为：默认在当前工程目录下创建 `MP_Lib` 文件夹，产物名默认 `TSLib`，存放到 `dist` 目录。
- **选项 2: 自定义配置**
  - 行为：追问用户期望的“源码目录名”和“产物文件名”。

### 2. 智能环境探测 (静默执行)
在生成配置前，必须通过工具进行全自动探测：
- **A. 探测 TSMaster 根目录**：
  - 尝试按顺序检查以下路径：
    1. `C:\Program Files (x86)\TOSUN\TSMaster`
  - 如果都未找到，使用 `ask_user` 请求用户提供 TSMaster 安装路径。
- **B. 确认资源路径**：
  - 编译器：`<根路径>\Data\Compilers\llvm_mingw_x64\bin\g++.exe` 和 `x86` 版本。
  - 头文件模板：`<根路径>\Templates\MiniProgram`。

### 3. 工程化配置生成
在确认的目标目录（例如 `MP_Lib`）下执行以下操作：

#### **A. 本地化头文件 (重要)**
- 在目标目录下创建 `h` 文件夹。
- 从 TSMaster 安装目录的 `<根路径>\Templates\MiniProgram` 下拷贝所有 `.h` 文件（包括 `TSMaster.h`）到 `MP_Lib/h`。

#### **B. 固化配置模板代码**
必须严格按照以下内容生成文件，**强制使用 .bat 脚本进行编译以确保稳定性**：

**1. 生成 `build.bat` (编译脚本)**:
```batch
@echo off
setlocal
set PROJECT_NAME=产物名
set INC_PATH=-I"./h"
set GXX64="探测到的x64编译器绝对路径"
set GXX32="探测到的x86编译器绝对路径"

if "%1"=="clean" (
    echo Cleaning dist...
    if exist "dist" rd /s /q "dist"
    exit /b 0
)

if not exist "dist" mkdir "dist"

echo Compiling x64 (.mp64)...
%GXX64% -fms-extensions -shared -Wl,--kill-at %INC_PATH% *.cpp -o "dist/%PROJECT_NAME%.mp64"
if %errorlevel% neq 0 ( echo x64 Failed! && exit /b %errorlevel% )

echo Compiling x86 (.mp)...
%GXX32% -fms-extensions -shared -Wl,--kill-at %INC_PATH% *.cpp -o "dist/%PROJECT_NAME%.mp"
if %errorlevel% neq 0 ( echo x86 Failed! && exit /b %errorlevel% )

echo All builds successful!
echo Output Directory: %~dp0dist
for %%i in (dist\*) do echo %%~ti    %%~nxi
```

**2. 生成 `.vscode/tasks.json`**:
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Build All (Script)",
            "type": "shell",
            "command": "cmd",
            "args": ["/c", "build.bat"],
            "group": { "kind": "build", "isDefault": true },
            "problemMatcher": ["$gcc"],
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared",
                "showReuseMessage": false,
                "clear": true
            }
        },
        {
            "label": "Clean",
            "type": "shell",
            "command": "cmd",
            "args": ["/c", "build.bat clean"]
        }
    ]
}
```

**3. 生成 `.vscode/c_cpp_properties.json`**:
```json
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": ["${workspaceFolder}/**", "${workspaceFolder}/h"],
            "defines": ["_DEBUG", "UNICODE", "_UNICODE"],
            "compilerPath": "探测到的x64编译器绝对路径",
            "cStandard": "c17",
            "cppStandard": "c++17",
            "intelliSenseMode": "windows-gcc-x64"
        }
    ],
    "version": 4
}
```

**4. 生成/追加 `.gitignore`**:
在工程根目录下确保有以下内容：
```text
# TSMaster Build Artifacts
dist/
*.mp
*.mp64
```

### 4. 生成代码模版 (从 `templates/` 复制)
- `Common.h`
- `TSMaster_Entry.cpp`
- `test_suites.cpp`

## 使用说明
告知用户：
1. 按 `Ctrl + Shift + B` 一键全编译。
2. 产物在 `dist` 目录。
3. 如果需要清理旧文件，请手动删除 `dist` 目录或在脚本中扩展 clean 逻辑。
