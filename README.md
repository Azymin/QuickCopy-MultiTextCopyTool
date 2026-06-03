```markdown
# QuickCopy - 多文本快速复制工具

作者：**[Azymin](https://github.com/Azymin)**

一键复制多个文件内容，快速复制到粘贴板。（一个个复制代码给AI太累了）

## 功能特点

- 📁 **选择文件夹** - 加载文件夹内的所有文件
- ✅ **批量勾选** - 支持文件夹批量勾选
- 📋 **一键复制** - 合并内容直接复制到剪贴板
- 🔍 **快速搜索** - 实时过滤查找文件
- 📝 **智能筛选** - 一键筛选代码文件或文本文件
- 🔄 **顺序调整** - 自由调整文件合并顺序

## 下载使用

### 方式一：直接运行（推荐）

1. 前往 [Releases](https://github.com/Azymin/QuickCopy-MultiTextCopyTool/releases) 下载最新的 `QuickCopy.exe`
2. 双击运行即可，无需安装 Python

### 方式二：源码运行

```bash
pip install pyperclip
python FileMergerApp.py
```

## 使用场景

- 向AI提问时批量发送代码文件
- 代码审查时收集多个文件
- 文档整理时合并文本内容

## 打包说明

如需自行打包为 exe：

```bash
pip install pyinstaller pyperclip
pyinstaller --onefile --windowed --hidden-import=pyperclip --name "QuickCopy" FileMergerApp.py
```

## 依赖

### 直接运行（exe版本）
- 无需任何依赖，Windows 10/11 直接运行

### 源码运行
- Python 3.6+
- tkinter（Python自带）
- pyperclip

## 许可证

MIT


---

# QuickCopy - MultiTextCopyTool

Author: **[Azymin](https://github.com/Azymin)**

One-click copy multiple file contents to clipboard. (Tired of copying code files one by one for AI?)

## Features

- 📁 **Select Folder** - Load all files in the selected folder
- ✅ **Batch Select** - Select all files in a folder at once
- 📋 **One-Click Copy** - Copy merged content directly to clipboard
- 🔍 **Quick Search** - Real-time file filtering
- 📝 **Smart Filter** - One-click filter code files or text files
- 🔄 **Order Adjustment** - Freely adjust file merge order

## Download & Usage

### Method 1: Direct Run (Recommended)

1. Download the latest `QuickCopy.exe` from [Releases](https://github.com/Azymin/QuickCopy-MultiTextCopyTool/releases)
2. Double-click to run, no Python installation required

### Method 2: Run from Source

```bash
pip install pyperclip
python FileMergerApp.py
```

## Use Cases

- Batch send code files when asking AI questions
- Collect multiple files for code review
- Merge text content for document organization

## Build Instructions

To package as exe yourself:

```bash
pip install pyinstaller pyperclip
pyinstaller --onefile --windowed --hidden-import=pyperclip --name "QuickCopy" FileMergerApp.py
```

## Dependencies

### Direct Run (exe version)
- No dependencies required, runs directly on Windows 10/11

### Run from Source
- Python 3.6+
- tkinter (built-in)
- pyperclip

## License

MIT
```
