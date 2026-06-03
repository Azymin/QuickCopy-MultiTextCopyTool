#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyperclip
import os
from pathlib import Path
import threading
from datetime import datetime
import platform
import ctypes


class Windows11Icons:
    """Windows 11 图标方案"""

    FILE_ICONS = {
        '.py': '🐍', '.js': '🟨', '.java': '☕', '.cpp': '⚙️', '.c': '🔧',
        '.h': '📋', '.cs': '🎯', '.php': '🐘', '.rb': '💎', '.go': '🔵',
        '.rs': '⚡', '.swift': '🕊️', '.kt': '📱', '.ts': '🔷', '.jsx': '⚛️',
        '.vue': '🟢', '.html': '🌐', '.css': '🎨', '.scss': '💅', '.json': '📦',
        '.xml': '📄', '.yaml': '⚙️', '.yml': '⚙️', '.toml': '🔧', '.ini': '⚙️',
        '.txt': '📝', '.md': '📘', '.rst': '📗', '.tex': '📐', '.pdf': '📕',
        '.doc': '📰', '.docx': '📰', '.xls': '📊', '.xlsx': '📊', '.ppt': '📽️',
        '.pptx': '📽️', '.rtf': '📃', '.jpg': '🖼️', '.jpeg': '🖼️', '.png': '🖼️',
        '.gif': '🎞️', '.bmp': '🖼️', '.svg': '🎨', '.ico': '🔷', '.webp': '🖼️',
        '.mp3': '🎵', '.wav': '🎵', '.flac': '🎶', '.aac': '🎵', '.mp4': '🎬',
        '.avi': '🎬', '.mkv': '🎬', '.mov': '🎬', '.zip': '📦', '.rar': '📦',
        '.7z': '📦', '.tar': '📦', '.gz': '📦', '.gitignore': '📋',
        '.dockerignore': '🐳', '.env': '🔐', '.exe': '⚙️', '.msi': '📦',
        '.bat': '📜', '.sh': '📜', '.ps1': '🔷', 'default': '📄'
    }

    FOLDER_ICONS = {
        'closed': '📁', 'open': '📂',
        'special': {
            'Desktop': '🖥️', 'Downloads': '⬇️', 'Documents': '📚',
            'Pictures': '🖼️', 'Music': '🎵', 'Videos': '🎬', 'Git': '📦',
            'node_modules': '📦', 'venv': '🐍', 'env': '🐍', '__pycache__': '⚡',
            '.git': '📋', '.vscode': '🔷', '.idea': '💡',
        }
    }

    # 🔧 大尺寸checkbox符号（使用更大的Unicode字符）
    CHECKBOX_UNCHECKED = '☐'  # 未选中
    CHECKBOX_CHECKED = '☑'  # 已选中
    CHECKBOX_PARTIAL = '◐'  # 部分选中

    @classmethod
    def get_file_icon(cls, file_path):
        """获取文件图标"""
        ext = os.path.splitext(file_path)[1].lower()
        basename = os.path.basename(file_path).lower()
        special_files = {'.gitignore': '📋', 'dockerfile': '🐳', 'makefile': '🔨',
                         'readme.md': '📖', 'license': '📜', 'requirements.txt': '📋',
                         'package.json': '📦'}
        if basename in special_files:
            return special_files[basename]
        return cls.FILE_ICONS.get(ext, cls.FILE_ICONS['default'])

    @classmethod
    def get_folder_icon(cls, folder_name, is_open=False):
        """获取文件夹图标"""
        if folder_name in cls.FOLDER_ICONS['special']:
            return cls.FOLDER_ICONS['special'][folder_name]
        return cls.FOLDER_ICONS['open'] if is_open else cls.FOLDER_ICONS['closed']


class Windows11Theme:
    """Windows 11 官方配色方案 - 大尺寸优化"""

    COLORS = {
        'bg_primary': '#f3f3f3', 'bg_secondary': '#ffffff', 'bg_tertiary': '#f9f9f9',
        'fg_primary': '#202020', 'fg_secondary': '#616161', 'fg_tertiary': '#9e9e9e',
        'accent': '#0067c0', 'accent_dark': '#004e8c', 'success': '#107c10',
        'error': '#e81123', 'border': '#e0e0e0', 'divider': '#f0f0f0',
        'hover': '#f5f5f5', 'selected': '#deecf9', 'glass': '#ffffff80',
    }

    FONTS = {
        # 🔧 增大所有字体尺寸
        'default': ('Segoe UI Variable', 13),  # 11 → 13
        'default_bold': ('Segoe UI Variable', 13, 'bold'),  # 11 → 13
        'title': ('Segoe UI Variable Display', 28, 'bold'),  # 24 → 28
        'subtitle': ('Segoe UI Variable Display', 18),  # 16 → 18
        'heading': ('Segoe UI Variable', 15, 'bold'),  # 13 → 15
        'body': ('Segoe UI Variable', 13),  # 11 → 13
        'small': ('Segoe UI Variable', 12),  # 10 → 12
        'code': ('Cascadia Code', 14),  # 12 → 14
        'icon': ('Segoe UI Emoji', 16),  # 14 → 16
        # 🔧 新增：Treeview专用大字体
        'tree_item': ('Segoe UI Variable', 14),  # Treeview项目字体
        'tree_folder': ('Segoe UI Variable', 14, 'bold'),  # Treeview文件夹字体
    }

    @classmethod
    def apply_theme(cls):
        """应用主题 - 增大行高和缩进"""
        style = ttk.Style()
        style.theme_use('clam')

        style.configure('Modern.Treeview',
                        background=cls.COLORS['bg_secondary'],
                        foreground=cls.COLORS['fg_primary'],
                        fieldbackground=cls.COLORS['bg_secondary'],
                        borderwidth=0,
                        relief='flat',
                        font=cls.FONTS['tree_item'],
                        rowheight=56,  # 🔧 48 → 56 增大行高，更容易点击
                        indent=30)  # 🔧 25 → 30 增大缩进，折叠箭头更明显
        style.map('Modern.Treeview',
                  background=[('selected', cls.COLORS['selected'])])

        style.configure('Modern.Treeview.Heading',
                        background=cls.COLORS['bg_tertiary'],
                        foreground=cls.COLORS['fg_primary'],
                        font=cls.FONTS['default_bold'],
                        borderwidth=1,
                        bordercolor=cls.COLORS['border'],
                        height=40)  # 🔧 35 → 40

        style.configure('Modern.Vertical.TScrollbar',
                        background=cls.COLORS['bg_tertiary'],
                        troughcolor=cls.COLORS['bg_primary'],
                        bordercolor=cls.COLORS['border'],
                        width=14)  # 🔧 12 → 14


class QuickCopy:
    """多文本快速复制工具 - 大尺寸优化完美版"""

    def __init__(self, root):
        self.root = root
        self.root.title("多文本快速复制工具")
        self.root.geometry("1400x900")  # 🔧 1300x800 → 1400x900
        self.root.minsize(1100, 750)  # 🔧 1000x700 → 1100x750

        self.root.configure(bg=Windows11Theme.COLORS['bg_primary'])
        Windows11Theme.apply_theme()

        self.current_path = None
        self.file_vars = {}
        self.tree_nodes = {}
        self.node_paths = {}
        self.selected_files_order = []
        self._click_processed = False

        self.create_widgets()
        self.bind_events()
        self.show_welcome()

    def show_welcome(self):
        self.status_var.set("✨ 欢迎使用 多文本快速复制工具 - 大尺寸优化版")

    def create_widgets(self):
        main_container = tk.Frame(self.root, bg=Windows11Theme.COLORS['bg_primary'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)  # 🔧 增大边距

        main_container.grid_rowconfigure(0, weight=0)
        main_container.grid_rowconfigure(1, weight=1)
        main_container.grid_rowconfigure(2, weight=0)
        main_container.grid_columnconfigure(0, weight=1)

        header_frame = tk.Frame(main_container, bg=Windows11Theme.COLORS['bg_primary'])
        header_frame.grid(row=0, column=0, sticky='ew', pady=(0, 15))

        title_frame = tk.Frame(header_frame, bg=Windows11Theme.COLORS['bg_primary'])
        title_frame.pack(side=tk.LEFT)

        title_label = tk.Label(
            title_frame,
            text="📁 多文本快速复制工具",
            font=Windows11Theme.FONTS['title'],
            fg=Windows11Theme.COLORS['fg_primary'],
            bg=Windows11Theme.COLORS['bg_primary']
        )
        title_label.pack(anchor=tk.W)

        subtitle_label = tk.Label(
            title_frame,
            text="V1.0.1",
            font=Windows11Theme.FONTS['subtitle'],
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_primary']
        )
        subtitle_label.pack(anchor=tk.W, pady=(4, 0))

        stats_card = tk.Frame(
            header_frame,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        stats_card.pack(side=tk.RIGHT)

        stats_inner = tk.Frame(stats_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=16, pady=8)
        stats_inner.pack()

        stats_label = tk.Label(
            stats_inner,
            text="📊 已选择",
            font=Windows11Theme.FONTS['small'],
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        stats_label.pack()

        self.stats_var = tk.StringVar(value="0")
        stats_number = tk.Label(
            stats_inner,
            textvariable=self.stats_var,
            font=('Segoe UI Variable Display', 24, 'bold'),  # 🔧 20 → 24
            fg=Windows11Theme.COLORS['accent'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        stats_number.pack()

        content_frame = tk.Frame(main_container, bg=Windows11Theme.COLORS['bg_primary'])
        content_frame.grid(row=1, column=0, sticky='nsew')
        content_frame.grid_columnconfigure(0, weight=3)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)

        left_container = tk.Frame(content_frame, bg=Windows11Theme.COLORS['bg_primary'])
        left_container.grid(row=0, column=0, sticky='nsew', padx=(0, 12))
        left_container.grid_rowconfigure(3, weight=1)
        left_container.grid_columnconfigure(0, weight=1)

        right_container = tk.Frame(content_frame, bg=Windows11Theme.COLORS['bg_primary'])
        right_container.grid(row=0, column=1, sticky='nsew')
        right_container.grid_rowconfigure(2, weight=1)
        right_container.grid_columnconfigure(0, weight=1)

        self.create_left_panel(left_container)
        self.create_right_panel(right_container)

        status_frame = tk.Frame(
            main_container,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0,
            height=36  # 🔧 32 → 36
        )
        status_frame.grid(row=2, column=0, sticky='ew', pady=(12, 0))
        status_frame.pack_propagate(False)

        status_inner = tk.Frame(status_frame, bg=Windows11Theme.COLORS['bg_secondary'], padx=12, pady=6)
        status_inner.pack(fill=tk.BOTH, expand=True)

        self.status_var = tk.StringVar(value="就绪")
        status_icon = tk.Label(
            status_inner,
            text="●",
            font=('Segoe UI', 10),  # 🔧 9 → 10
            fg=Windows11Theme.COLORS['success'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        status_icon.pack(side=tk.LEFT, padx=(0, 6))

        status_label = tk.Label(
            status_inner,
            textvariable=self.status_var,
            font=Windows11Theme.FONTS['small'],
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        status_label.pack(side=tk.LEFT)

        self.progress_bar = ttk.Progressbar(
            status_inner,
            mode='indeterminate',
            length=140
        )
        self.progress_bar.pack(side=tk.RIGHT)
        self.progress_bar.pack_forget()

    def create_left_panel(self, parent):
        parent.grid_rowconfigure(0, weight=0)
        parent.grid_rowconfigure(1, weight=0)
        parent.grid_rowconfigure(2, weight=1)
        parent.grid_rowconfigure(3, weight=0)
        parent.grid_columnconfigure(0, weight=1)

        # 路径选择卡片
        path_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        path_card.grid(row=0, column=0, sticky='ew', pady=(0, 10))

        path_content = tk.Frame(path_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=14, pady=12)
        path_content.pack(fill=tk.X)

        path_title = tk.Label(
            path_content,
            text="📁 文件夹路径",
            font=Windows11Theme.FONTS['heading'],
            fg=Windows11Theme.COLORS['fg_primary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        path_title.pack(anchor=tk.W, pady=(0, 8))

        path_row = tk.Frame(path_content, bg=Windows11Theme.COLORS['bg_secondary'])
        path_row.pack(fill=tk.X)

        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(
            path_row,
            textvariable=self.path_var,
            font=Windows11Theme.FONTS['body'],
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            relief='solid',
            bd=1
        )
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=6)  # 🔧 增大内边距

        self.browse_btn = tk.Button(
            path_row,
            text="📂 浏览",
            command=self.browse_folder,
            font=Windows11Theme.FONTS['body'],
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            relief='solid',
            bd=1,
            padx=16,  # 🔧 12 → 16
            pady=5,  # 🔧 3 → 5
            cursor='hand2'
        )
        self.browse_btn.pack(side=tk.LEFT, padx=(0, 6))

        self.load_btn = tk.Button(
            path_row,
            text="🔄 加载",
            command=self.load_folder_tree,
            font=Windows11Theme.FONTS['default_bold'],
            bg=Windows11Theme.COLORS['accent'],
            fg='white',
            relief='flat',
            bd=0,
            padx=20,  # 🔧 16 → 20
            pady=5,  # 🔧 3 → 5
            cursor='hand2'
        )
        self.load_btn.pack(side=tk.LEFT)

        # 工具栏卡片
        toolbar_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        toolbar_card.grid(row=1, column=0, sticky='ew', pady=(0, 10))

        toolbar_content = tk.Frame(toolbar_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=14, pady=10)
        toolbar_content.pack(fill=tk.X)

        tools_row = tk.Frame(toolbar_content, bg=Windows11Theme.COLORS['bg_secondary'])
        tools_row.pack(fill=tk.X, pady=(0, 8))

        tools = [
            ("✅ 全选", self.select_all),
            ("❌ 全不选", self.deselect_all),
            ("🔄 反选", self.invert_selection),
            ("💻 代码文件", self.select_code_files),
            ("📝 文本文件", self.select_text_files),
        ]

        for text, command in tools:
            btn = tk.Button(
                tools_row,
                text=text,
                command=command,
                font=Windows11Theme.FONTS['small'],
                bg='white',
                fg=Windows11Theme.COLORS['fg_primary'],
                relief='solid',
                bd=1,
                padx=10,  # 🔧 8 → 10
                pady=3,  # 🔧 2 → 3
                cursor='hand2'
            )
            btn.pack(side=tk.LEFT, padx=(0, 6))

        # 搜索行
        search_row = tk.Frame(toolbar_content, bg=Windows11Theme.COLORS['bg_secondary'])
        search_row.pack(fill=tk.X)

        search_icon = tk.Label(
            search_row,
            text="🔍",
            font=Windows11Theme.FONTS['icon'],
            bg=Windows11Theme.COLORS['bg_secondary'],
            fg=Windows11Theme.COLORS['fg_tertiary']
        )
        search_icon.pack(side=tk.LEFT, padx=(0, 10))

        self.search_var = tk.StringVar()
        self.search_var.trace_add('write', self.filter_tree)
        self.search_entry = tk.Entry(
            search_row,
            textvariable=self.search_var,
            font=Windows11Theme.FONTS['body'],
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            relief='solid',
            bd=1
        )
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6)

        # 文件树卡片
        tree_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        tree_card.grid(row=2, column=0, sticky='nsew', pady=(0, 10))

        tree_card_inner = tk.Frame(tree_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=14, pady=12)
        tree_card_inner.pack(fill=tk.BOTH, expand=True)

        tree_title = tk.Label(
            tree_card_inner,
            text="📋 文件浏览器 (点击 ☐/☑ 勾选 | 双击文件夹 展开/折叠 | 单击 ▶ 展开/折叠)",
            font=Windows11Theme.FONTS['heading'],
            fg=Windows11Theme.COLORS['fg_primary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        tree_title.pack(anchor=tk.W, pady=(0, 10))

        tree_container = tk.Frame(tree_card_inner, bg='white', relief='solid', bd=1)
        tree_container.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            tree_container,
            columns=(),
            show='tree',
            selectmode='none',
            style='Modern.Treeview'
        )

        # 🔧 使用更大的字体标签
        self.tree.tag_configure('folder', font=Windows11Theme.FONTS['tree_folder'])
        self.tree.tag_configure('file', font=Windows11Theme.FONTS['tree_item'])

        v_scrollbar = ttk.Scrollbar(
            tree_container,
            orient=tk.VERTICAL,
            command=self.tree.yview,
            style='Modern.Vertical.TScrollbar'
        )
        self.tree.configure(yscrollcommand=v_scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 事件绑定
        self.tree.bind('<Button-1>', self.on_tree_click)
        self.tree.bind('<Double-Button-1>', self.on_tree_double_click)
        self.tree.bind('<space>', self.on_tree_space)
        self.tree.bind('<Control-Button-1>', self.on_tree_ctrl_click)
        self.tree.bind('<Shift-Button-1>', self.on_tree_shift_click)

        # 底部操作栏
        action_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        action_card.grid(row=3, column=0, sticky='ew')

        action_content = tk.Frame(action_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=14, pady=10)
        action_content.pack(fill=tk.X)

        settings_row = tk.Frame(action_content, bg=Windows11Theme.COLORS['bg_secondary'])
        settings_row.pack(fill=tk.X, pady=(0, 8))

        sep_label = tk.Label(
            settings_row,
            text="📏 分隔行数:",
            font=Windows11Theme.FONTS['small'],
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        sep_label.pack(side=tk.LEFT, padx=(0, 6))

        self.separator_var = tk.StringVar(value="3")
        self.separator_spinbox = tk.Spinbox(
            settings_row,
            from_=0,
            to=10,
            width=5,  # 🔧 4 → 5
            textvariable=self.separator_var,
            font=Windows11Theme.FONTS['body'],
            bg='white',
            relief='solid',
            bd=1
        )
        self.separator_spinbox.pack(side=tk.LEFT, padx=(0, 20))

        self.show_filename_var = tk.BooleanVar(value=True)
        self.show_filename_check = tk.Checkbutton(
            settings_row,
            text="📄 显示文件名",
            variable=self.show_filename_var,
            font=Windows11Theme.FONTS['small'],
            bg=Windows11Theme.COLORS['bg_secondary'],
            fg=Windows11Theme.COLORS['fg_primary'],
            activebackground=Windows11Theme.COLORS['bg_secondary'],
            selectcolor='white',
            relief='flat',
            bd=0
        )
        self.show_filename_check.pack(side=tk.LEFT, padx=(0, 20))

        self.include_subdirs_var = tk.BooleanVar(value=True)
        self.include_subdirs_check = tk.Checkbutton(
            settings_row,
            text="📁 包含子目录",
            variable=self.include_subdirs_var,
            command=self.toggle_subdirs,
            font=Windows11Theme.FONTS['small'],
            bg=Windows11Theme.COLORS['bg_secondary'],
            fg=Windows11Theme.COLORS['fg_primary'],
            activebackground=Windows11Theme.COLORS['bg_secondary'],
            selectcolor='white',
            relief='flat',
            bd=0
        )
        self.include_subdirs_check.pack(side=tk.LEFT)

        buttons_row = tk.Frame(action_content, bg=Windows11Theme.COLORS['bg_secondary'])
        buttons_row.pack(fill=tk.X)

        self.copy_btn = tk.Button(
            buttons_row,
            text="📋 复制选中内容",
            command=self.copy_selected_content,
            font=Windows11Theme.FONTS['default_bold'],
            bg=Windows11Theme.COLORS['accent'],
            fg='white',
            relief='flat',
            bd=0,
            padx=20,  # 🔧 16 → 20
            pady=7,  # 🔧 5 → 7
            cursor='hand2'
        )
        self.copy_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.preview_btn = tk.Button(
            buttons_row,
            text="👁️ 预览",
            command=self.preview_selected_content,
            font=Windows11Theme.FONTS['body'],
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            relief='solid',
            bd=1,
            padx=20,
            pady=6,
            cursor='hand2'
        )
        self.preview_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.expand_all_btn = tk.Button(
            buttons_row,
            text="🔽 展开所有",
            command=self.expand_all,
            font=Windows11Theme.FONTS['small'],
            bg='white',
            fg=Windows11Theme.COLORS['fg_secondary'],
            relief='solid',
            bd=1,
            padx=12,
            pady=6,
            cursor='hand2'
        )
        self.expand_all_btn.pack(side=tk.LEFT, padx=(0, 6))

        self.collapse_all_btn = tk.Button(
            buttons_row,
            text="🔼 折叠所有",
            command=self.collapse_all,
            font=Windows11Theme.FONTS['small'],
            bg='white',
            fg=Windows11Theme.COLORS['fg_secondary'],
            relief='solid',
            bd=1,
            padx=12,
            pady=6,
            cursor='hand2'
        )
        self.collapse_all_btn.pack(side=tk.LEFT)

    def create_right_panel(self, parent):
        parent.grid_rowconfigure(0, weight=0)
        parent.grid_rowconfigure(1, weight=0)
        parent.grid_rowconfigure(2, weight=1)
        parent.grid_rowconfigure(3, weight=0)
        parent.grid_columnconfigure(0, weight=1)

        selected_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        selected_card.grid(row=0, column=0, sticky='nsew', rowspan=4)

        selected_content = tk.Frame(selected_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=14, pady=12)
        selected_content.pack(fill=tk.BOTH, expand=True)

        title_row = tk.Frame(selected_content, bg=Windows11Theme.COLORS['bg_secondary'])
        title_row.pack(fill=tk.X, pady=(0, 10))

        title_label = tk.Label(
            title_row,
            text="📋 已选文件列表",
            font=Windows11Theme.FONTS['heading'],
            fg=Windows11Theme.COLORS['fg_primary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        title_label.pack(side=tk.LEFT)

        self.clear_all_btn = tk.Button(
            title_row,
            text="🗑️ 清空所有",
            command=self.clear_all_selections,
            font=Windows11Theme.FONTS['small'],
            bg='white',
            fg=Windows11Theme.COLORS['error'],
            relief='solid',
            bd=1,
            padx=10,
            pady=3,
            cursor='hand2'
        )
        self.clear_all_btn.pack(side=tk.RIGHT)

        order_frame = tk.Frame(selected_content, bg=Windows11Theme.COLORS['bg_secondary'])
        order_frame.pack(fill=tk.X, pady=(0, 10))

        order_label = tk.Label(
            order_frame,
            text="🔄 顺序:",
            font=Windows11Theme.FONTS['small'],
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        order_label.pack(side=tk.LEFT, padx=(0, 10))

        order_buttons = [
            ("▲ 上移", self.move_selected_up),
            ("▼ 下移", self.move_selected_down),
            ("⤒ 置顶", self.move_selected_to_top),
            ("⤓ 置底", self.move_selected_to_bottom),
        ]

        self.order_btns = []
        for text, command in order_buttons:
            btn = tk.Button(
                order_frame,
                text=text,
                command=command,
                font=Windows11Theme.FONTS['small'],
                bg='white',
                fg=Windows11Theme.COLORS['accent'],
                relief='solid',
                bd=1,
                padx=10,
                pady=3,
                cursor='hand2',
                state='disabled'
            )
            btn.pack(side=tk.LEFT, padx=(0, 6))
            self.order_btns.append(btn)

        list_container = tk.Frame(selected_content, bg='white', relief='solid', bd=1)
        list_container.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        self.selected_listbox = tk.Listbox(
            list_container,
            selectmode=tk.EXTENDED,
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            font=Windows11Theme.FONTS['code'],
            relief='flat',
            bd=0,
            highlightthickness=0,
            selectbackground=Windows11Theme.COLORS['selected'],
            height=10  # 🔧 设置初始可见行数
        )

        scrollbar = ttk.Scrollbar(
            list_container,
            orient=tk.VERTICAL,
            command=self.selected_listbox.yview,
            style='Modern.Vertical.TScrollbar'
        )
        self.selected_listbox.configure(yscrollcommand=scrollbar.set)

        self.selected_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        list_bottom = tk.Frame(selected_content, bg=Windows11Theme.COLORS['bg_secondary'])
        list_bottom.pack(fill=tk.X)

        self.selected_count_label = tk.Label(
            list_bottom,
            text="0 个文件",
            font=Windows11Theme.FONTS['default_bold'],
            fg=Windows11Theme.COLORS['success'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        self.selected_count_label.pack(side=tk.LEFT)

        btn_frame = tk.Frame(list_bottom, bg=Windows11Theme.COLORS['bg_secondary'])
        btn_frame.pack(side=tk.RIGHT)

        self.remove_selected_btn = tk.Button(
            btn_frame,
            text="❌ 移除选中",
            command=self.remove_selected_from_list,
            font=Windows11Theme.FONTS['small'],
            bg='white',
            fg=Windows11Theme.COLORS['error'],
            relief='solid',
            bd=1,
            padx=10,
            pady=3,
            cursor='hand2'
        )
        self.remove_selected_btn.pack(side=tk.LEFT, padx=(0, 6))

        self.copy_list_btn = tk.Button(
            btn_frame,
            text="📋 复制列表",
            command=self.copy_file_list,
            font=Windows11Theme.FONTS['small'],
            bg='white',
            fg=Windows11Theme.COLORS['accent'],
            relief='solid',
            bd=1,
            padx=10,
            pady=3,
            cursor='hand2'
        )
        self.copy_list_btn.pack(side=tk.LEFT)

        self.selected_listbox.bind('<<ListboxSelect>>', self.on_list_select)
        self.selected_listbox.bind('<Double-Button-1>', self.on_list_double_click)
        self.selected_listbox.bind('<Delete>', self.on_list_delete)

    def bind_events(self):
        self.path_entry.bind('<Return>', lambda e: self.load_folder_tree())

    def browse_folder(self):
        folder = filedialog.askdirectory(title="选择文件夹")
        if folder:
            self.path_var.set(folder)
            self.load_folder_tree()

    def load_folder_tree(self):
        folder = self.path_var.get()
        if not folder or not os.path.exists(folder):
            messagebox.showerror("错误", "请选择有效的文件夹路径")
            return

        self.current_path = folder
        self.clear_tree()
        self.progress_bar.pack(side=tk.RIGHT)
        self.progress_bar.start(10)
        self.status_var.set("正在加载文件列表...")
        self.root.update()
        threading.Thread(target=self._load_tree_data, args=(folder,), daemon=True).start()

    def _load_tree_data(self, folder):
        try:
            folder_icon = Windows11Icons.get_folder_icon(os.path.basename(folder))
            # 🔧 使用统一的大尺寸格式：checkbox + 两个空格 + 图标 + 两个空格 + 名称
            root_text = f"☐    {folder_icon}    {os.path.basename(folder)}"  # 🔧 增加间距
            root_node = self.tree.insert('', 'end', text=root_text, open=True, tags=('folder',))
            self.tree_nodes[root_node] = folder
            self.node_paths[folder] = root_node
            self._add_tree_items(root_node, folder)
            self.tree.item(root_node, open=True)
            file_count = len(self.file_vars)
            self.root.after(0, lambda: self.status_var.set(f"加载完成 - 共 {file_count} 个文件"))
            self.root.after(0, lambda: self.progress_bar.stop())
            self.root.after(0, lambda: self.progress_bar.pack_forget())
            self.root.after(0, self.update_file_count)
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("错误", f"加载失败：{str(e)}"))
            self.root.after(0, lambda: self.status_var.set("加载失败"))
            self.root.after(0, lambda: self.progress_bar.stop())
            self.root.after(0, lambda: self.progress_bar.pack_forget())

    def _add_tree_items(self, parent_node, path):
        try:
            items = sorted(os.listdir(path))
            for item in items:
                if item.startswith('.') or item.startswith('~'):
                    continue
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    folder_icon = Windows11Icons.get_folder_icon(item, is_open=False)
                    # 🔧 文件夹：增加间距让checkbox更容易点击
                    folder_node = self.tree.insert(
                        parent_node, 'end',
                        text=f"☐    {folder_icon}    {item}",
                        tags=('folder',)
                    )
                    self.tree_nodes[folder_node] = full_path
                    self.node_paths[full_path] = folder_node
                    if self.include_subdirs_var.get():
                        self._add_tree_items(folder_node, full_path)
                else:
                    icon = Windows11Icons.get_file_icon(full_path)
                    # 🔧 文件：增加间距让checkbox更容易点击
                    file_node = self.tree.insert(
                        parent_node, 'end',
                        text=f"☐    {icon}    {item}",
                        tags=('file',)
                    )
                    self.tree_nodes[file_node] = full_path
                    self.node_paths[full_path] = file_node
                    self.file_vars[full_path] = tk.BooleanVar(value=False)
        except PermissionError:
            pass

    def get_indent_level(self, item):
        """获取节点的缩进级别"""
        level = 0
        parent = self.tree.parent(item)
        while parent:
            level += 1
            parent = self.tree.parent(parent)
        return level

    def is_click_on_toggle(self, event, item):
        """判断是否点击在展开/折叠箭头上 - 增大检测区域"""
        bbox = self.tree.bbox(item, column='#0')
        if not bbox:
            return False

        level = self.get_indent_level(item)
        # 🔧 展开箭头检测区域增大：缩进后的前28px（30-2=28）
        indent_width = level * 30  # 与style中的indent=30对应
        toggle_region_start = indent_width
        toggle_region_end = indent_width + 28  # 🔧 20 → 28 增大箭头点击区域

        click_x = event.x - bbox[0]

        tags = self.tree.item(item, 'tags')
        if 'folder' not in (tags or ()):
            return False

        return toggle_region_start <= click_x <= toggle_region_end

    def on_tree_click(self, event):
        """单击事件：勾选/取消勾选（除展开箭头外）"""
        item = self.tree.identify_row(event.y)
        if not item:
            return

        if hasattr(self, '_click_processed') and self._click_processed:
            self._click_processed = False
            return

        # 如果点击展开箭头 → 展开/折叠
        if self.is_click_on_toggle(event, item):
            self.toggle_expand(item)
            return "break"
        else:
            # 点击其他区域 → 勾选/取消勾选
            self.toggle_item_selection(item)
            return "break"

    def on_tree_double_click(self, event):
        """双击事件：展开/折叠文件夹"""
        item = self.tree.identify_row(event.y)
        if not item:
            return

        self._click_processed = True

        tags = self.tree.item(item, 'tags')
        if 'folder' in (tags or ()):
            self.toggle_expand(item)
            return "break"
        elif 'file' in (tags or ()):
            self.toggle_item_selection(item)
            return "break"

    def on_tree_ctrl_click(self, event):
        """Ctrl+单击"""
        item = self.tree.identify_row(event.y)
        if item:
            self.toggle_item_selection(item)
            return "break"

    def on_tree_shift_click(self, event):
        """Shift+单击"""
        item = self.tree.identify_row(event.y)
        if item:
            self.toggle_item_selection(item)
            return "break"

    def toggle_expand(self, item):
        """展开/折叠文件夹"""
        tags = self.tree.item(item, 'tags')
        if 'folder' not in (tags or ()):
            return

        if self.tree.item(item, 'open'):
            self.tree.item(item, open=False)
        else:
            self.tree.item(item, open=True)

        self.update_folder_icon(item)
        self.status_var.set(f"{'折叠' if not self.tree.item(item, 'open') else '展开'}文件夹")

    def on_tree_space(self, event):
        """空格键：勾选/取消勾选"""
        item = self.tree.focus()
        if item:
            self.toggle_item_selection(item)
            return "break"

    def toggle_item_selection(self, item):
        """勾选/取消勾选项目"""
        path = self.tree_nodes.get(item)
        if not path:
            return

        tags = self.tree.item(item, 'tags')

        if 'folder' in (tags or ()):
            self.toggle_folder_selection(path, item)
        elif 'file' in (tags or ()):
            if path in self.file_vars:
                current = self.file_vars[path].get()
                new_state = not current
                self.file_vars[path].set(new_state)

                if new_state:
                    if path not in self.selected_files_order:
                        self.selected_files_order.append(path)
                else:
                    if path in self.selected_files_order:
                        self.selected_files_order.remove(path)

                self.update_item_icon(item, new_state)
                self.update_parent_folders(item)
                self.update_selected_list()

                self.status_var.set(f"{'☑ 已勾选' if new_state else '☐ 已取消'} {os.path.basename(path)}")

        self.update_file_count()

    def toggle_folder_selection(self, folder_path, folder_node):
        """勾选/取消勾选整个文件夹"""
        files_in_folder = []
        for file_path in self.file_vars:
            if file_path.startswith(folder_path) and os.path.isfile(file_path):
                files_in_folder.append(file_path)

        if not files_in_folder:
            return

        selected_count = sum(1 for f in files_in_folder if self.file_vars[f].get())
        new_state = selected_count < len(files_in_folder)

        for file_path in files_in_folder:
            self.file_vars[file_path].set(new_state)

        for file_path in files_in_folder:
            node = self.node_paths.get(file_path)
            if node:
                self.update_item_icon(node, new_state)

        if new_state:
            for file_path in files_in_folder:
                if file_path not in self.selected_files_order:
                    self.selected_files_order.append(file_path)
        else:
            for file_path in files_in_folder:
                if file_path in self.selected_files_order:
                    self.selected_files_order.remove(file_path)

        self.update_folder_icon(folder_node)
        self.update_selected_list()

        self.status_var.set(f"{'☑ 已勾选' if new_state else '☐ 已取消'} 文件夹 {os.path.basename(folder_path)}")

    def update_item_icon(self, node, selected):
        """统一更新项目图标 - 大间距版本"""
        path = self.tree_nodes.get(node)
        if not path:
            return

        if os.path.isfile(path):
            icon = Windows11Icons.get_file_icon(path)
        else:
            icon = Windows11Icons.get_folder_icon(os.path.basename(path), self.tree.item(node, 'open'))

        checkbox = Windows11Icons.CHECKBOX_CHECKED if selected else Windows11Icons.CHECKBOX_UNCHECKED
        # 🔧 使用4个空格增加间距，让checkbox区域更大更容易点击
        self.tree.item(node, text=f"{checkbox}    {icon}    {os.path.basename(path)}")

    def update_file_icon(self, node, selected):
        """更新文件图标（保持向后兼容）"""
        self.update_item_icon(node, selected)

    def update_folder_icon(self, folder_node):
        """更新文件夹图标，包含部分选择状态 - 大间距版本"""
        folder_path = self.tree_nodes.get(folder_node)
        if not folder_path or not os.path.isdir(folder_path):
            return

        folder_name = os.path.basename(folder_path)
        is_open = self.tree.item(folder_node, 'open')
        folder_icon = Windows11Icons.get_folder_icon(folder_name, is_open)

        # 计算勾选状态
        files_in_folder = []
        for file_path, var in self.file_vars.items():
            if file_path.startswith(folder_path) and os.path.isfile(file_path):
                files_in_folder.append(var.get())

        if not files_in_folder:
            checkbox = Windows11Icons.CHECKBOX_UNCHECKED
        else:
            selected_count = sum(files_in_folder)
            if selected_count == 0:
                checkbox = Windows11Icons.CHECKBOX_UNCHECKED
            elif selected_count == len(files_in_folder):
                checkbox = Windows11Icons.CHECKBOX_CHECKED
            else:
                checkbox = Windows11Icons.CHECKBOX_PARTIAL

        # 🔧 使用4个空格增加间距
        self.tree.item(folder_node, text=f"{checkbox}    {folder_icon}    {folder_name}")

    def update_parent_folders(self, item):
        """更新父文件夹图标"""
        parent = self.tree.parent(item)
        while parent:
            self.update_folder_icon(parent)
            parent = self.tree.parent(parent)

    def update_selected_list(self):
        """更新右侧已选列表"""
        self.selected_listbox.delete(0, tk.END)
        for index, file_path in enumerate(self.selected_files_order, 1):
            if os.path.isfile(file_path):
                if self.current_path:
                    rel_path = os.path.relpath(file_path, self.current_path)
                else:
                    rel_path = os.path.basename(file_path)
                icon = Windows11Icons.get_file_icon(file_path)
                display_text = f"{index:3d}. {icon}  {rel_path}"
                self.selected_listbox.insert(tk.END, display_text)

        count = len(self.selected_files_order)
        self.selected_count_label.config(text=f"{count} 个文件")
        self.stats_var.set(str(count))
        self.update_order_buttons()

    def update_order_buttons(self):
        selection = self.selected_listbox.curselection()
        has_selection = len(selection) > 0
        has_multiple = len(self.selected_files_order) > 1
        state = 'normal' if has_selection and has_multiple else 'disabled'
        for btn in self.order_btns:
            btn.config(state=state)

    def on_list_select(self, event):
        self.update_order_buttons()

    def move_selected_up(self):
        selection = self.selected_listbox.curselection()
        if not selection or len(selection) != 1:
            return
        index = selection[0]
        if index > 0:
            self.selected_files_order[index], self.selected_files_order[index - 1] = \
                self.selected_files_order[index - 1], self.selected_files_order[index]
            self.update_selected_list()
            self.selected_listbox.selection_set(index - 1)
            self.selected_listbox.see(index - 1)

    def move_selected_down(self):
        selection = self.selected_listbox.curselection()
        if not selection or len(selection) != 1:
            return
        index = selection[0]
        if index < len(self.selected_files_order) - 1:
            self.selected_files_order[index], self.selected_files_order[index + 1] = \
                self.selected_files_order[index + 1], self.selected_files_order[index]
            self.update_selected_list()
            self.selected_listbox.selection_set(index + 1)
            self.selected_listbox.see(index + 1)

    def move_selected_to_top(self):
        selection = self.selected_listbox.curselection()
        if not selection or len(selection) != 1:
            return
        index = selection[0]
        if index > 0:
            file_path = self.selected_files_order.pop(index)
            self.selected_files_order.insert(0, file_path)
            self.update_selected_list()
            self.selected_listbox.selection_set(0)
            self.selected_listbox.see(0)

    def move_selected_to_bottom(self):
        selection = self.selected_listbox.curselection()
        if not selection or len(selection) != 1:
            return
        index = selection[0]
        if index < len(self.selected_files_order) - 1:
            file_path = self.selected_files_order.pop(index)
            self.selected_files_order.append(file_path)
            self.update_selected_list()
            last_index = len(self.selected_files_order) - 1
            self.selected_listbox.selection_set(last_index)
            self.selected_listbox.see(last_index)

    def on_list_double_click(self, event):
        selection = self.selected_listbox.curselection()
        if selection:
            index = selection[0]
            if index < len(self.selected_files_order):
                file_path = self.selected_files_order[index]
                self.file_vars[file_path].set(False)
                node = self.node_paths.get(file_path)
                if node:
                    self.update_file_icon(node, False)
                    self.update_parent_folders(node)
                self.selected_files_order.pop(index)
                self.update_selected_list()
                self.update_file_count()

    def on_list_delete(self, event):
        self.remove_selected_from_list()

    def remove_selected_from_list(self):
        selection = self.selected_listbox.curselection()
        if not selection:
            return
        files_to_remove = []
        for index in reversed(selection):
            if index < len(self.selected_files_order):
                files_to_remove.append(self.selected_files_order[index])
        for file_path in files_to_remove:
            self.file_vars[file_path].set(False)
            node = self.node_paths.get(file_path)
            if node:
                self.update_file_icon(node, False)
                self.update_parent_folders(node)
            if file_path in self.selected_files_order:
                self.selected_files_order.remove(file_path)
        self.update_selected_list()
        self.update_file_count()

    def copy_file_list(self):
        if not self.selected_files_order:
            messagebox.showwarning("警告", "没有选中的文件")
            return
        list_lines = ["📋 已选文件列表:", ""]
        for index, file_path in enumerate(self.selected_files_order, 1):
            if self.current_path:
                rel_path = os.path.relpath(file_path, self.current_path)
            else:
                rel_path = os.path.basename(file_path)
            icon = Windows11Icons.get_file_icon(file_path)
            list_lines.append(f"{index:3d}. {icon} {rel_path}")
        list_text = "\n".join(list_lines)
        try:
            pyperclip.copy(list_text)
            self.status_var.set("✅ 已复制文件列表到剪贴板")
        except Exception as e:
            messagebox.showerror("错误", f"复制失败：{str(e)}")

    def get_selected_files(self):
        return [f for f in self.selected_files_order if os.path.isfile(f)]

    def update_file_count(self):
        count = len(self.selected_files_order)
        self.stats_var.set(str(count))

    def select_all(self):
        for var in self.file_vars.values():
            var.set(True)
        for path, node in self.node_paths.items():
            if os.path.isfile(path):
                self.update_file_icon(node, True)
        for node in self.tree.get_children(''):
            self.update_folder_icon(node)
            self._update_all_folders_recursive(node)
        self.selected_files_order = []
        for file_path in sorted(self.file_vars.keys()):
            if os.path.isfile(file_path):
                self.selected_files_order.append(file_path)
        self.update_selected_list()
        self.update_file_count()
        self.status_var.set("已全选所有文件")

    def _update_all_folders_recursive(self, node):
        self.update_folder_icon(node)
        for child in self.tree.get_children(node):
            self._update_all_folders_recursive(child)

    def deselect_all(self):
        for var in self.file_vars.values():
            var.set(False)
        for path, node in self.node_paths.items():
            if os.path.isfile(path):
                self.update_file_icon(node, False)
        for node in self.tree.get_children(''):
            self.update_folder_icon(node)
            for child in self.tree.get_children(node):
                self.update_folder_icon(child)
        self.selected_files_order.clear()
        self.update_selected_list()
        self.update_file_count()
        self.status_var.set("已取消所有选择")

    def invert_selection(self):
        for var in self.file_vars.values():
            var.set(not var.get())
        for path, node in self.node_paths.items():
            if os.path.isfile(path):
                self.update_file_icon(node, self.file_vars[path].get())
        for node in self.tree.get_children(''):
            self.update_folder_icon(node)
            for child in self.tree.get_children(node):
                self.update_folder_icon(child)
        self.selected_files_order = []
        for file_path, var in self.file_vars.items():
            if var.get() and os.path.isfile(file_path):
                self.selected_files_order.append(file_path)
        self.update_selected_list()
        self.update_file_count()
        self.status_var.set("已反选")

    def select_code_files(self):
        code_exts = {'.py', '.js', '.java', '.cpp', '.c', '.h', '.cs', '.php',
                     '.rb', '.go', '.rs', '.swift', '.kt', '.ts', '.jsx', '.vue'}
        for var in self.file_vars.values():
            var.set(False)
        self.selected_files_order = []
        for file_path, var in self.file_vars.items():
            ext = os.path.splitext(file_path)[1].lower()
            if ext in code_exts:
                var.set(True)
                self.selected_files_order.append(file_path)
        for path, node in self.node_paths.items():
            if os.path.isfile(path):
                self.update_file_icon(node, self.file_vars[path].get())
        for node in self.tree.get_children(''):
            self.update_folder_icon(node)
            for child in self.tree.get_children(node):
                self.update_folder_icon(child)
        self.update_selected_list()
        self.update_file_count()
        self.status_var.set(f"已选择 {len(self.selected_files_order)} 个代码文件")

    def select_text_files(self):
        text_exts = {'.txt', '.md', '.rst', '.tex', '.json', '.xml', '.yaml',
                     '.yml', '.ini', '.cfg', '.conf', '.log', '.csv'}
        for var in self.file_vars.values():
            var.set(False)
        self.selected_files_order = []
        for file_path, var in self.file_vars.items():
            ext = os.path.splitext(file_path)[1].lower()
            if ext in text_exts:
                var.set(True)
                self.selected_files_order.append(file_path)
        for path, node in self.node_paths.items():
            if os.path.isfile(path):
                self.update_file_icon(node, self.file_vars[path].get())
        for node in self.tree.get_children(''):
            self.update_folder_icon(node)
            for child in self.tree.get_children(node):
                self.update_folder_icon(child)
        self.update_selected_list()
        self.update_file_count()
        self.status_var.set(f"已选择 {len(self.selected_files_order)} 个文本文件")

    def clear_all_selections(self):
        if messagebox.askyesno("确认", "确定要清空所有文件勾选吗？"):
            self.deselect_all()

    def toggle_subdirs(self):
        if self.current_path:
            self.load_folder_tree()

    def expand_all(self):
        def expand_recursive(node):
            self.tree.item(node, open=True)
            self.update_folder_icon(node)
            for child in self.tree.get_children(node):
                expand_recursive(child)

        for node in self.tree.get_children(''):
            expand_recursive(node)
        self.status_var.set("已全部展开")

    def collapse_all(self):
        def collapse_recursive(node):
            self.tree.item(node, open=False)
            self.update_folder_icon(node)
            for child in self.tree.get_children(node):
                collapse_recursive(child)

        for node in self.tree.get_children(''):
            collapse_recursive(node)
        self.status_var.set("已全部折叠")

    def filter_tree(self, *args):
        search_text = self.search_var.get().lower()
        if not search_text:
            for node in self.tree.get_children(''):
                self.tree.item(node, open=True)
                self._show_all_recursive(node)
        else:
            for node in self.tree.get_children(''):
                self._filter_recursive(node, search_text)

    def _show_all_recursive(self, node):
        self.tree.item(node, open=True)
        for child in self.tree.get_children(node):
            self._show_all_recursive(child)

    def _filter_recursive(self, node, search_text):
        text = self.tree.item(node, 'text').lower()
        if search_text in text:
            self.tree.item(node, open=True)
            self._show_parents(node)
            return True
        has_match = False
        for child in self.tree.get_children(node):
            if self._filter_recursive(child, search_text):
                has_match = True
        if has_match:
            self.tree.item(node, open=True)
        else:
            self.tree.item(node, open=False)
        return has_match

    def _show_parents(self, node):
        parent = self.tree.parent(node)
        while parent:
            self.tree.item(parent, open=True)
            parent = self.tree.parent(parent)

    def clear_tree(self):
        self.tree.delete(*self.tree.get_children())
        self.file_vars.clear()
        self.tree_nodes.clear()
        self.node_paths.clear()
        self.selected_files_order.clear()
        self.selected_listbox.delete(0, tk.END)
        self.selected_count_label.config(text="0 个文件")

    def merge_selected_files(self):
        selected_files = self.get_selected_files()
        if not selected_files:
            return ""
        merged_content = []
        separator_lines = int(self.separator_var.get())
        separator = "\n" * separator_lines
        for i, file_path in enumerate(selected_files):
            try:
                content = self.read_file_with_encoding(file_path)
                if self.show_filename_var.get():
                    if self.current_path:
                        rel_path = os.path.relpath(file_path, self.current_path)
                    else:
                        rel_path = os.path.basename(file_path)
                    icon = Windows11Icons.get_file_icon(file_path)
                    merged_content.append(f"=== {icon} [{i + 1}] {rel_path} ===")
                merged_content.append(content.rstrip())
                if i < len(selected_files) - 1:
                    merged_content.append(separator)
            except Exception as e:
                error_msg = f"读取失败: {str(e)}"
                merged_content.append(f"!!! [{i + 1}] {os.path.basename(file_path)} - {error_msg} !!!")
                if i < len(selected_files) - 1:
                    merged_content.append(separator)
        return "\n".join(merged_content)

    def read_file_with_encoding(self, file_path):
        encodings = ['utf-8', 'gbk', 'gb2312', 'utf-16', 'latin-1']
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
            except Exception as e:
                raise e
        with open(file_path, 'rb') as f:
            content = f.read()
            return content.decode('utf-8', errors='ignore')

    def copy_selected_content(self):
        selected_files = self.get_selected_files()
        if not selected_files:
            messagebox.showwarning("警告", "请至少选择一个文件")
            return

        def copy_task():
            try:
                self.root.after(0, lambda: self.copy_btn.config(state='disabled'))
                self.root.after(0, lambda: self.status_var.set("正在合并内容..."))
                self.root.after(0, lambda: self.progress_bar.pack(side=tk.RIGHT))
                self.root.after(0, lambda: self.progress_bar.start(10))
                merged_content = self.merge_selected_files()
                pyperclip.copy(merged_content)
                count = len(selected_files)
                self.root.after(0, lambda: self.status_var.set(f"✅ 已复制 {count} 个文件的内容"))
                self.root.after(0, lambda: messagebox.showinfo("成功", f"已复制 {count} 个文件的内容到剪贴板"))
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("错误", f"复制失败：{str(e)}"))
            finally:
                self.root.after(0, lambda: self.copy_btn.config(state='normal'))
                self.root.after(0, lambda: self.progress_bar.stop())
                self.root.after(0, lambda: self.progress_bar.pack_forget())

        threading.Thread(target=copy_task, daemon=True).start()

    def preview_selected_content(self):
        selected_files = self.get_selected_files()
        if not selected_files:
            messagebox.showwarning("警告", "请至少选择一个文件")
            return
        try:
            merged_content = self.merge_selected_files()
            preview_window = tk.Toplevel(self.root)
            preview_window.title("内容预览")
            preview_window.geometry("1100x750")  # 🔧 1000x700 → 1100x750
            preview_window.minsize(850, 550)  # 🔧 800x500 → 850x550
            preview_window.configure(bg=Windows11Theme.COLORS['bg_primary'])
            main_frame = tk.Frame(preview_window, bg=Windows11Theme.COLORS['bg_primary'])
            main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
            title_label = tk.Label(
                main_frame,
                text="📄 内容预览",
                font=Windows11Theme.FONTS['title'],
                fg=Windows11Theme.COLORS['fg_primary'],
                bg=Windows11Theme.COLORS['bg_primary']
            )
            title_label.pack(anchor=tk.W, pady=(0, 15))
            text_container = tk.Frame(main_frame, bg='white', relief='solid', bd=1)
            text_container.pack(fill=tk.BOTH, expand=True)
            text_widget = tk.Text(
                text_container,
                wrap=tk.WORD,
                font=Windows11Theme.FONTS['code'],
                bg='white',
                fg=Windows11Theme.COLORS['fg_primary'],
                relief='flat',
                bd=0,
                padx=16,
                pady=16
            )
            scrollbar = ttk.Scrollbar(
                text_container,
                orient=tk.VERTICAL,
                command=text_widget.yview,
                style='Modern.Vertical.TScrollbar'
            )
            text_widget.configure(yscrollcommand=scrollbar.set)
            text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            text_widget.insert('1.0', merged_content)
            text_widget.config(state=tk.DISABLED)
            bottom_frame = tk.Frame(main_frame, bg=Windows11Theme.COLORS['bg_primary'])
            bottom_frame.pack(fill=tk.X, pady=(12, 0))
            count_label = tk.Label(
                bottom_frame,
                text=f"📊 共 {len(selected_files)} 个文件",
                font=Windows11Theme.FONTS['body'],
                fg=Windows11Theme.COLORS['success'],
                bg=Windows11Theme.COLORS['bg_primary']
            )
            count_label.pack(side=tk.LEFT)
            close_btn = tk.Button(
                bottom_frame,
                text="关闭",
                command=preview_window.destroy,
                font=Windows11Theme.FONTS['body'],
                bg=Windows11Theme.COLORS['accent'],
                fg='white',
                relief='flat',
                bd=0,
                padx=24,
                pady=7,
                cursor='hand2'
            )
            close_btn.pack(side=tk.RIGHT)
        except Exception as e:
            messagebox.showerror("错误", f"预览失败：{str(e)}")


def main():
    root = tk.Tk()

    if platform.system() == 'Windows':
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass

    app = QuickCopy(root)

    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    root.mainloop()


if __name__ == "__main__":
    main()