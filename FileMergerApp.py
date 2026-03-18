#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File Content Merger Pro Plus - Windows 11 官方风格版
Version: 3.5.0
Author: 为您服务的程序员
Description: 优化布局 - 确保所有按钮完整显示
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyperclip
import os
from pathlib import Path
import threading
from datetime import datetime
import platform
import ctypes
from ctypes import wintypes


class Windows11Icons:
    """Windows 11 40px大图标方案"""

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
        'closed': '📁', 'open': '📂', 'selected': '✅', 'partial': '◻️',
        'special': {
            'Desktop': '🖥️', 'Downloads': '⬇️', 'Documents': '📚',
            'Pictures': '🖼️', 'Music': '🎵', 'Videos': '🎬', 'Git': '📦',
            'node_modules': '📦', 'venv': '🐍', 'env': '🐍', '__pycache__': '⚡',
            '.git': '📋', '.vscode': '🔷', '.idea': '💡',
        }
    }

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
    def get_folder_icon(cls, folder_name, is_open=False, selected_state=None):
        """获取文件夹图标"""
        if selected_state == 'full':
            return '✅'
        elif selected_state == 'partial':
            return '◻️'
        if folder_name in cls.FOLDER_ICONS['special']:
            return cls.FOLDER_ICONS['special'][folder_name]
        return cls.FOLDER_ICONS['open'] if is_open else cls.FOLDER_ICONS['closed']


class Windows11Theme:
    """Windows 11 官方配色方案"""

    COLORS = {
        'bg_primary': '#f3f3f3', 'bg_secondary': '#ffffff', 'bg_tertiary': '#f9f9f9',
        'fg_primary': '#202020', 'fg_secondary': '#616161', 'fg_tertiary': '#9e9e9e',
        'accent': '#0067c0', 'accent_dark': '#004e8c', 'success': '#107c10',
        'error': '#e81123', 'border': '#e0e0e0', 'divider': '#f0f0f0',
        'hover': '#f5f5f5', 'selected': '#deecf9', 'glass': '#ffffff80',
    }

    FONTS = {
        'default': ('Segoe UI Variable', 11), 'default_bold': ('Segoe UI Variable', 11, 'bold'),
        'title': ('Segoe UI Variable Display', 24, 'bold'), 'subtitle': ('Segoe UI Variable Display', 16),
        'heading': ('Segoe UI Variable', 13, 'bold'), 'body': ('Segoe UI Variable', 11),
        'small': ('Segoe UI Variable', 10), 'code': ('Cascadia Code', 12),
        'icon': ('Segoe UI Emoji', 20),
    }

    @classmethod
    def apply_theme(cls):
        """应用主题"""
        style = ttk.Style()
        style.theme_use('clam')

        style.configure('Modern.Treeview',
                        background=cls.COLORS['bg_secondary'],
                        foreground=cls.COLORS['fg_primary'],
                        fieldbackground=cls.COLORS['bg_secondary'],
                        borderwidth=0,
                        relief='flat',
                        font=cls.FONTS['default'],
                        rowheight=60)
        style.map('Modern.Treeview',
                  background=[('selected', cls.COLORS['selected'])])

        style.configure('Modern.Treeview.Heading',
                        background=cls.COLORS['bg_tertiary'],
                        foreground=cls.COLORS['fg_primary'],
                        font=cls.FONTS['default_bold'],
                        borderwidth=1,
                        bordercolor=cls.COLORS['border'],
                        height=40)

        style.configure('Modern.Vertical.TScrollbar',
                        background=cls.COLORS['bg_tertiary'],
                        troughcolor=cls.COLORS['bg_primary'],
                        bordercolor=cls.COLORS['border'],
                        width=14)


class Windows11FileMerger:
    """Windows 11 风格文件合并工具 - 优化布局版"""

    def __init__(self, root):
        self.root = root
        self.root.title("文件合并工具 - Windows 11 40px大图标版")
        self.root.geometry("1600x900")  # 恢复为标准大小

        # 设置窗口背景
        self.root.configure(bg=Windows11Theme.COLORS['bg_primary'])

        # 应用主题
        Windows11Theme.apply_theme()

        # 当前根路径
        self.current_path = None

        # 存储所有文件的勾选状态
        self.file_vars = {}
        self.tree_nodes = {}
        self.node_paths = {}

        # 按选择顺序存储已选文件
        self.selected_files_order = []

        # 创建UI
        self.create_widgets()

        # 绑定事件
        self.bind_events()

        # 显示欢迎消息
        self.show_welcome()

    def show_welcome(self):
        """显示欢迎消息"""
        self.status_var.set("✨ 欢迎使用 Windows 11 文件合并工具 (40px大图标版)")

    def create_widgets(self):
        """创建Windows 11风格界面 - 优化布局"""

        # ========== 主容器 ==========
        main_container = tk.Frame(self.root, bg=Windows11Theme.COLORS['bg_primary'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)

        # ========== 顶部标题区域 ==========
        header_frame = tk.Frame(main_container, bg=Windows11Theme.COLORS['bg_primary'])
        header_frame.pack(fill=tk.X, pady=(0, 15))

        # 左侧标题
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
            text="V1.0.0",
            font=Windows11Theme.FONTS['subtitle'],
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_primary']
        )
        subtitle_label.pack(anchor=tk.W, pady=(2, 0))

        # 右侧统计卡片
        stats_card = tk.Frame(
            header_frame,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        stats_card.pack(side=tk.RIGHT)

        stats_inner = tk.Frame(stats_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=15, pady=8)
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
            font=('Segoe UI Variable Display', 24, 'bold'),
            fg=Windows11Theme.COLORS['accent'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        stats_number.pack()

        # ========== 主要内容区域（两列布局）==========
        content_frame = tk.Frame(main_container, bg=Windows11Theme.COLORS['bg_primary'])
        content_frame.pack(fill=tk.BOTH, expand=True)

        # 左侧面板 (65%宽度)
        left_container = tk.Frame(content_frame, bg=Windows11Theme.COLORS['bg_primary'])
        left_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # 右侧面板 (35%宽度)
        right_container = tk.Frame(content_frame, bg=Windows11Theme.COLORS['bg_primary'], width=500)
        right_container.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        right_container.pack_propagate(False)

        # 创建左右面板
        self.create_left_panel(left_container)
        self.create_right_panel(right_container)

        # ========== 底部状态栏 ==========
        status_frame = tk.Frame(
            main_container,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0,
            height=35
        )
        status_frame.pack(fill=tk.X, pady=(10, 0))
        status_frame.pack_propagate(False)

        status_inner = tk.Frame(status_frame, bg=Windows11Theme.COLORS['bg_secondary'], padx=10, pady=6)
        status_inner.pack(fill=tk.BOTH, expand=True)

        self.status_var = tk.StringVar(value="就绪")
        status_icon = tk.Label(
            status_inner,
            text="●",
            font=('Segoe UI', 10),
            fg=Windows11Theme.COLORS['success'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        status_icon.pack(side=tk.LEFT, padx=(0, 5))

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
            style='Modern.Horizontal.TProgressbar',
            mode='indeterminate',
            length=150
        )
        self.progress_bar.pack(side=tk.RIGHT)
        self.progress_bar.pack_forget()

    def create_left_panel(self, parent):
        """创建左侧面板 - 优化布局确保按钮可见"""

        # ========== 路径选择卡片 ==========
        path_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        path_card.pack(fill=tk.X, pady=(0, 8))

        path_content = tk.Frame(path_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=15, pady=12)
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
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8), ipady=6)

        self.browse_btn = tk.Button(
            path_row,
            text="📂 浏览",
            command=self.browse_folder,
            font=Windows11Theme.FONTS['body'],
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            relief='solid',
            bd=1,
            padx=15,
            pady=4,
            cursor='hand2'
        )
        self.browse_btn.pack(side=tk.LEFT, padx=(0, 5))

        self.load_btn = tk.Button(
            path_row,
            text="🔄 加载",
            command=self.load_folder_tree,
            font=Windows11Theme.FONTS['default_bold'],
            bg=Windows11Theme.COLORS['accent'],
            fg='white',
            relief='flat',
            bd=0,
            padx=20,
            pady=4,
            cursor='hand2'
        )
        self.load_btn.pack(side=tk.LEFT)

        # ========== 工具栏卡片 ==========
        toolbar_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        toolbar_card.pack(fill=tk.X, pady=(0, 8))

        toolbar_content = tk.Frame(toolbar_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=15, pady=10)
        toolbar_content.pack(fill=tk.X)

        # 工具按钮行
        tools_row = tk.Frame(toolbar_content, bg=Windows11Theme.COLORS['bg_secondary'])
        tools_row.pack(fill=tk.X, pady=(0, 8))

        tools = [
            ("✅ 全选", self.select_all, Windows11Theme.COLORS['accent']),
            ("❌ 全不选", self.deselect_all, Windows11Theme.COLORS['fg_secondary']),
            ("🔄 反选", self.invert_selection, Windows11Theme.COLORS['fg_primary']),
            ("💻 代码", self.select_code_files, '#881798'),
            ("📝 文本", self.select_text_files, '#ff8c00'),
        ]

        for text, command, color in tools:
            btn = tk.Button(
                tools_row,
                text=text,
                command=command,
                font=Windows11Theme.FONTS['small'],
                bg='white',
                fg=color,
                relief='solid',
                bd=1,
                padx=10,
                pady=4,
                cursor='hand2'
            )
            btn.pack(side=tk.LEFT, padx=(0, 5))

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
        search_icon.pack(side=tk.LEFT, padx=(0, 8))

        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.filter_tree)
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

        # ========== 文件树卡片 ==========
        tree_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        tree_card.pack(fill=tk.BOTH, expand=True, pady=(0, 8))

        tree_card_inner = tk.Frame(tree_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=15, pady=12)
        tree_card_inner.pack(fill=tk.BOTH, expand=True)

        tree_title = tk.Label(
            tree_card_inner,
            text="📋 文件浏览器 (40px图标)",
            font=Windows11Theme.FONTS['heading'],
            fg=Windows11Theme.COLORS['fg_primary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        tree_title.pack(anchor=tk.W, pady=(0, 8))

        # Treeview容器
        tree_container = tk.Frame(tree_card_inner, bg='white', relief='solid', bd=1)
        tree_container.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            tree_container,
            columns=('size', 'type', 'modified'),
            show='tree headings',
            selectmode='none',
            style='Modern.Treeview'
        )

        self.tree.heading('#0', text='文件名', anchor=tk.W)
        self.tree.heading('size', text='大小', anchor=tk.W)
        self.tree.heading('type', text='类型', anchor=tk.W)
        self.tree.heading('modified', text='修改时间', anchor=tk.W)

        self.tree.column('#0', width=400, minwidth=300)
        self.tree.column('size', width=80, minwidth=70)
        self.tree.column('type', width=120, minwidth=100)
        self.tree.column('modified', width=130, minwidth=110)

        self.tree.tag_configure('folder', font=('Segoe UI Variable', 11, 'bold'))
        self.tree.tag_configure('file', font=('Segoe UI Variable', 11))

        v_scrollbar = ttk.Scrollbar(
            tree_container,
            orient=tk.VERTICAL,
            command=self.tree.yview,
            style='Modern.Vertical.TScrollbar'
        )
        h_scrollbar = ttk.Scrollbar(
            tree_container,
            orient=tk.HORIZONTAL,
            command=self.tree.xview,
            style='Modern.Vertical.TScrollbar'
        )
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        self.tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')

        tree_container.grid_rowconfigure(0, weight=1)
        tree_container.grid_columnconfigure(0, weight=1)

        self.tree.bind('<Button-1>', self.on_tree_click)
        self.tree.bind('<Double-Button-1>', self.on_tree_double_click)
        self.tree.bind('<space>', self.on_tree_space)

        # ========== 底部操作栏 ==========
        action_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        action_card.pack(fill=tk.X)

        action_content = tk.Frame(action_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=15, pady=10)
        action_content.pack(fill=tk.X)

        # 第一行：设置选项
        settings_row = tk.Frame(action_content, bg=Windows11Theme.COLORS['bg_secondary'])
        settings_row.pack(fill=tk.X, pady=(0, 8))

        sep_label = tk.Label(
            settings_row,
            text="📏 分隔行:",
            font=Windows11Theme.FONTS['small'],
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        sep_label.pack(side=tk.LEFT, padx=(0, 5))

        self.separator_var = tk.StringVar(value="3")
        self.separator_spinbox = tk.Spinbox(
            settings_row,
            from_=0,
            to=10,
            width=3,
            textvariable=self.separator_var,
            font=Windows11Theme.FONTS['small'],
            bg='white',
            relief='solid',
            bd=1
        )
        self.separator_spinbox.pack(side=tk.LEFT, padx=(0, 15))

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
        self.show_filename_check.pack(side=tk.LEFT, padx=(0, 15))

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

        # 第二行：主要操作按钮
        buttons_row = tk.Frame(action_content, bg=Windows11Theme.COLORS['bg_secondary'])
        buttons_row.pack(fill=tk.X)

        # 复制按钮
        self.copy_btn = tk.Button(
            buttons_row,
            text="📋 复制选中内容",
            command=self.copy_selected_content,
            font=Windows11Theme.FONTS['default_bold'],
            bg=Windows11Theme.COLORS['accent'],
            fg='white',
            relief='flat',
            bd=0,
            padx=20,
            pady=6,
            cursor='hand2'
        )
        self.copy_btn.pack(side=tk.LEFT, padx=(0, 8))

        # 预览按钮
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
            pady=5,
            cursor='hand2'
        )
        self.preview_btn.pack(side=tk.LEFT, padx=(0, 8))

        # 展开/折叠按钮
        self.expand_all_btn = tk.Button(
            buttons_row,
            text="🔽 展开",
            command=self.expand_all,
            font=Windows11Theme.FONTS['small'],
            bg='white',
            fg=Windows11Theme.COLORS['fg_secondary'],
            relief='solid',
            bd=1,
            padx=10,
            pady=4,
            cursor='hand2'
        )
        self.expand_all_btn.pack(side=tk.LEFT, padx=(0, 5))

        self.collapse_all_btn = tk.Button(
            buttons_row,
            text="🔼 折叠",
            command=self.collapse_all,
            font=Windows11Theme.FONTS['small'],
            bg='white',
            fg=Windows11Theme.COLORS['fg_secondary'],
            relief='solid',
            bd=1,
            padx=10,
            pady=4,
            cursor='hand2'
        )
        self.collapse_all_btn.pack(side=tk.LEFT)

    def create_right_panel(self, parent):
        """创建右侧面板 - 优化布局"""

        selected_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        selected_card.pack(fill=tk.BOTH, expand=True)

        selected_content = tk.Frame(selected_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=15, pady=12)
        selected_content.pack(fill=tk.BOTH, expand=True)

        # 标题行
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
            text="🗑️ 清空",
            command=self.clear_all_selections,
            font=Windows11Theme.FONTS['small'],
            bg='white',
            fg=Windows11Theme.COLORS['error'],
            relief='solid',
            bd=1,
            padx=10,
            pady=2,
            cursor='hand2'
        )
        self.clear_all_btn.pack(side=tk.RIGHT)

        # 顺序控制栏
        order_frame = tk.Frame(selected_content, bg=Windows11Theme.COLORS['bg_secondary'])
        order_frame.pack(fill=tk.X, pady=(0, 10))

        order_label = tk.Label(
            order_frame,
            text="🔄 顺序:",
            font=Windows11Theme.FONTS['small'],
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        order_label.pack(side=tk.LEFT, padx=(0, 8))

        order_buttons = [
            ("↑", self.move_selected_up),
            ("↓", self.move_selected_down),
            ("⏫", self.move_selected_to_top),
            ("⏬", self.move_selected_to_bottom),
        ]

        self.order_btns = []
        for text, command in order_buttons:
            btn = tk.Button(
                order_frame,
                text=text,
                command=command,
                font=('Segoe UI', 10),
                bg='white',
                fg=Windows11Theme.COLORS['accent'],
                relief='solid',
                bd=1,
                width=2,
                pady=2,
                cursor='hand2',
                state='disabled'
            )
            btn.pack(side=tk.LEFT, padx=(0, 5))
            self.order_btns.append(btn)

        # 列表容器
        list_container = tk.Frame(selected_content, bg='white', relief='solid', bd=1)
        list_container.pack(fill=tk.BOTH, expand=True)

        self.selected_listbox = tk.Listbox(
            list_container,
            selectmode=tk.EXTENDED,
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            font=Windows11Theme.FONTS['code'],
            relief='flat',
            bd=0,
            highlightthickness=0,
            selectbackground=Windows11Theme.COLORS['selected']
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

        # 底部工具栏
        list_bottom = tk.Frame(selected_content, bg=Windows11Theme.COLORS['bg_secondary'])
        list_bottom.pack(fill=tk.X, pady=(10, 0))

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
            text="❌ 移除",
            command=self.remove_selected_from_list,
            font=Windows11Theme.FONTS['small'],
            bg='white',
            fg=Windows11Theme.COLORS['error'],
            relief='solid',
            bd=1,
            padx=10,
            pady=2,
            cursor='hand2'
        )
        self.remove_selected_btn.pack(side=tk.LEFT, padx=(0, 5))

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
            pady=2,
            cursor='hand2'
        )
        self.copy_list_btn.pack(side=tk.LEFT)

        # 绑定列表事件
        self.selected_listbox.bind('<<ListboxSelect>>', self.on_list_select)
        self.selected_listbox.bind('<Double-Button-1>', self.on_list_double_click)
        self.selected_listbox.bind('<Delete>', self.on_list_delete)

    # 以下方法保持不变（从之前的完整代码复制）
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
            icon = Windows11Icons.get_folder_icon(os.path.basename(folder))
            root_text = f"{icon}  {os.path.basename(folder)}"
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
                    icon = Windows11Icons.get_folder_icon(item, is_open=False)
                    folder_node = self.tree.insert(
                        parent_node, 'end',
                        text=f"{icon}  {item}",
                        values=('', '文件夹', ''),
                        tags=('folder',)
                    )
                    self.tree_nodes[folder_node] = full_path
                    self.node_paths[full_path] = folder_node
                    if self.include_subdirs_var.get():
                        self._add_tree_items(folder_node, full_path)
                else:
                    size = self.get_file_size(full_path)
                    ext = os.path.splitext(item)[1].lower() or '无扩展名'
                    modified = self.get_file_modified_time(full_path)
                    icon = Windows11Icons.get_file_icon(full_path)
                    file_node = self.tree.insert(
                        parent_node, 'end',
                        text=f"{icon}  {item}",
                        values=(size, ext, modified),
                        tags=('file',)
                    )
                    self.tree_nodes[file_node] = full_path
                    self.node_paths[full_path] = file_node
                    self.file_vars[full_path] = tk.BooleanVar(value=False)
        except PermissionError:
            pass

    def on_tree_click(self, event):
        region = self.tree.identify_region(event.x, event.y)
        if region == "tree":
            item = self.tree.identify_row(event.y)
            if item:
                column = self.tree.identify_column(event.x)
                if column == '#0':
                    bbox = self.tree.bbox(item, column='#0')
                    if bbox and event.x < bbox[0] + 50:
                        self.toggle_item_selection(item)
                        return "break"
                    else:
                        self.toggle_folder(item)
                        return "break"
        return None

    def on_tree_double_click(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self.toggle_folder(item)
            return "break"

    def on_tree_space(self, event):
        item = self.tree.focus()
        if item:
            self.toggle_item_selection(item)
            return "break"

    def toggle_folder(self, item):
        tags = self.tree.item(item, 'tags')
        if 'folder' in tags:
            if self.tree.item(item, 'open'):
                self.tree.item(item, open=False)
            else:
                self.tree.item(item, open=True)
            self.update_folder_icon(item)

    def toggle_item_selection(self, item):
        path = self.tree_nodes.get(item)
        if not path:
            return
        tags = self.tree.item(item, 'tags')
        if 'folder' in tags:
            self.toggle_folder_selection(path, item)
        else:
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
                self.update_file_icon(item, new_state)
                self.update_parent_folders(item)
                self.update_selected_list()
        self.update_file_count()

    def toggle_folder_selection(self, folder_path, folder_node):
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
                self.update_file_icon(node, new_state)
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

    def update_file_icon(self, node, selected):
        path = self.tree_nodes.get(node)
        if path and os.path.isfile(path):
            if selected:
                self.tree.item(node, text=f"✅  {os.path.basename(path)}")
            else:
                icon = Windows11Icons.get_file_icon(path)
                self.tree.item(node, text=f"{icon}  {os.path.basename(path)}")

    def update_folder_icon(self, folder_node):
        folder_path = self.tree_nodes.get(folder_node)
        if not folder_path or not os.path.isdir(folder_path):
            return
        folder_name = os.path.basename(folder_path)
        is_open = self.tree.item(folder_node, 'open')
        files_in_folder = []
        for file_path, var in self.file_vars.items():
            if file_path.startswith(folder_path) and os.path.isfile(file_path):
                files_in_folder.append(var.get())
        if not files_in_folder:
            selected_state = None
        else:
            selected_count = sum(files_in_folder)
            if selected_count == 0:
                selected_state = None
            elif selected_count == len(files_in_folder):
                selected_state = 'full'
            else:
                selected_state = 'partial'
        icon = Windows11Icons.get_folder_icon(folder_name, is_open, selected_state)
        self.tree.item(folder_node, text=f"{icon}  {folder_name}")

    def update_parent_folders(self, item):
        parent = self.tree.parent(item)
        while parent:
            self.update_folder_icon(parent)
            parent = self.tree.parent(parent)

    def update_selected_list(self):
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

    def get_file_size(self, file_path):
        try:
            size = os.path.getsize(file_path)
            if size < 1024:
                return f"{size} B"
            elif size < 1024 * 1024:
                return f"{size / 1024:.1f} KB"
            else:
                return f"{size / (1024 * 1024):.1f} MB"
        except:
            return "未知"

    def get_file_modified_time(self, file_path):
        try:
            timestamp = os.path.getmtime(file_path)
            return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')
        except:
            return "未知"

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
            preview_window.title("内容预览 - Windows 11 40px大图标版")
            preview_window.geometry("1200x800")
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
                padx=15,
                pady=15
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
            bottom_frame.pack(fill=tk.X, pady=(10, 0))
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
                padx=25,
                pady=6,
                cursor='hand2'
            )
            close_btn.pack(side=tk.RIGHT)
        except Exception as e:
            messagebox.showerror("错误", f"预览失败：{str(e)}")


def main():
    """主函数"""
    root = tk.Tk()

    if platform.system() == 'Windows':
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass

    app = Windows11FileMerger(root)

    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    root.mainloop()


if __name__ == "__main__":
    main()