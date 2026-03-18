#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File Content Merger Pro Plus - Windows 11 官方风格版
Version: 3.1.0
Author: 为您服务的程序员
Description: 完全按照Windows 11设计语言：蓝白灰配色，毛玻璃效果，圆角设计
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyperclip
import os
from pathlib import Path
import threading
from datetime import datetime
import platform


class Windows11Theme:
    """Windows 11 官方配色方案"""

    # Windows 11 官方配色
    COLORS = {
        # 背景色系
        'bg_primary': '#f3f3f3',  # 主背景色 - 浅灰
        'bg_secondary': '#ffffff',  # 次要背景色 - 纯白
        'bg_tertiary': '#f9f9f9',  # 第三背景色 - 暖白
        'bg_accent': '#f0f0f0',  # 强调背景色 - 浅灰

        # 前景色系
        'fg_primary': '#202020',  # 主要文字 - 深灰
        'fg_secondary': '#616161',  # 次要文字 - 中灰
        'fg_tertiary': '#9e9e9e',  # 第三文字 - 浅灰

        # Windows 11 主题蓝
        'accent': '#0067c0',  # 主题蓝 - 标准
        'accent_light': '#e6f0fa',  # 浅主题蓝 - 背景
        'accent_dark': '#004e8c',  # 深主题蓝 - 悬停
        'accent_transparent': '#0067c010',  # 透明主题蓝

        # 状态色
        'success': '#107c10',  # 成功绿
        'warning': '#ffb900',  # 警告黄
        'error': '#e81123',  # 错误红
        'info': '#0067c0',  # 信息蓝

        # 边框和分割线
        'border': '#e0e0e0',  # 边框色
        'divider': '#f0f0f0',  # 分割线

        # 交互状态
        'hover': '#f5f5f5',  # 悬停背景
        'selected': '#deecf9',  # 选中背景
        'disabled_bg': '#f5f5f5',  # 禁用背景
        'disabled_fg': '#bdbdbd',  # 禁用文字

        # 毛玻璃效果
        'glass': '#ffffff80',  # 毛玻璃白
        'glass_dark': '#00000010',  # 毛玻璃黑
    }

    # Windows 11 字体方案
    FONTS = {
        'default': ('Segoe UI Variable', 10),
        'default_bold': ('Segoe UI Variable', 10, 'bold'),
        'title': ('Segoe UI Variable Display', 20, 'bold'),
        'subtitle': ('Segoe UI Variable Display', 14),
        'heading': ('Segoe UI Variable', 12, 'bold'),
        'body': ('Segoe UI Variable', 10),
        'small': ('Segoe UI Variable', 9),
        'code': ('Cascadia Code', 10),
        'code_bold': ('Cascadia Code', 10, 'bold'),
    }

    @classmethod
    def apply_theme(cls):
        """应用Windows 11主题到ttk样式"""
        style = ttk.Style()
        style.theme_use('clam')

        # 基础样式
        style.configure('.',
                        background=cls.COLORS['bg_primary'],
                        foreground=cls.COLORS['fg_primary'],
                        font=cls.FONTS['default'],
                        relief='flat',
                        borderwidth=0
                        )

        # 标题样式
        style.configure('Title.TLabel',
                        font=cls.FONTS['title'],
                        foreground=cls.COLORS['fg_primary'],
                        background=cls.COLORS['bg_primary']
                        )

        # 副标题样式
        style.configure('Subtitle.TLabel',
                        font=cls.FONTS['subtitle'],
                        foreground=cls.COLORS['fg_secondary'],
                        background=cls.COLORS['bg_primary']
                        )

        # 卡片样式 - Windows 11 圆角卡片
        style.configure('Card.TFrame',
                        background=cls.COLORS['bg_secondary'],
                        relief='solid',
                        borderwidth=1,
                        bordercolor=cls.COLORS['border']
                        )

        # 毛玻璃效果卡片
        style.configure('Glass.TFrame',
                        background=cls.COLORS['glass']
                        )

        # 主要按钮 - Windows 11 主题蓝
        style.configure('Accent.TButton',
                        background=cls.COLORS['accent'],
                        foreground='white',
                        font=cls.FONTS['default_bold'],
                        borderwidth=0,
                        focuscolor='none',
                        relief='flat',
                        padding=(20, 10)
                        )
        style.map('Accent.TButton',
                  background=[('active', cls.COLORS['accent_dark']),
                              ('disabled', cls.COLORS['disabled_bg'])],
                  foreground=[('disabled', cls.COLORS['disabled_fg'])]
                  )

        # 次要按钮 - 白色背景，灰边框
        style.configure('Secondary.TButton',
                        background=cls.COLORS['bg_secondary'],
                        foreground=cls.COLORS['fg_primary'],
                        font=cls.FONTS['default'],
                        borderwidth=1,
                        bordercolor=cls.COLORS['border'],
                        focuscolor='none',
                        relief='flat',
                        padding=(15, 8)
                        )
        style.map('Secondary.TButton',
                  background=[('active', cls.COLORS['hover']),
                              ('disabled', cls.COLORS['disabled_bg'])],
                  bordercolor=[('active', cls.COLORS['accent'])]
                  )

        # 工具按钮 - 更小内边距
        style.configure('Tool.TButton',
                        background=cls.COLORS['bg_secondary'],
                        foreground=cls.COLORS['fg_primary'],
                        font=cls.FONTS['small'],
                        borderwidth=1,
                        bordercolor=cls.COLORS['border'],
                        focuscolor='none',
                        relief='flat',
                        padding=(10, 5)
                        )
        style.map('Tool.TButton',
                  background=[('active', cls.COLORS['hover'])]
                  )

        # 输入框 - Windows 11 风格
        style.configure('Modern.TEntry',
                        fieldbackground=cls.COLORS['bg_secondary'],
                        foreground=cls.COLORS['fg_primary'],
                        borderwidth=1,
                        bordercolor=cls.COLORS['border'],
                        relief='solid',
                        padding=(10, 8),
                        font=cls.FONTS['default']
                        )
        style.map('Modern.TEntry',
                  bordercolor=[('focus', cls.COLORS['accent'])]
                  )

        # 复选框
        style.configure('Modern.TCheckbutton',
                        background=cls.COLORS['bg_primary'],
                        foreground=cls.COLORS['fg_primary'],
                        font=cls.FONTS['default']
                        )

        # 标签框架
        style.configure('Modern.TLabelframe',
                        background=cls.COLORS['bg_primary'],
                        foreground=cls.COLORS['fg_primary'],
                        borderwidth=1,
                        bordercolor=cls.COLORS['border'],
                        relief='solid'
                        )
        style.configure('Modern.TLabelframe.Label',
                        background=cls.COLORS['bg_primary'],
                        foreground=cls.COLORS['accent'],
                        font=cls.FONTS['heading']
                        )

        # 树形视图
        style.configure('Modern.Treeview',
                        background=cls.COLORS['bg_secondary'],
                        foreground=cls.COLORS['fg_primary'],
                        fieldbackground=cls.COLORS['bg_secondary'],
                        borderwidth=0,
                        relief='flat',
                        font=cls.FONTS['default'],
                        rowheight=35
                        )
        style.map('Modern.Treeview',
                  background=[('selected', cls.COLORS['selected'])]
                  )
        style.configure('Modern.Treeview.Heading',
                        background=cls.COLORS['bg_tertiary'],
                        foreground=cls.COLORS['fg_primary'],
                        font=cls.FONTS['default_bold'],
                        borderwidth=1,
                        bordercolor=cls.COLORS['border']
                        )

        # 进度条
        style.configure('Modern.Horizontal.TProgressbar',
                        background=cls.COLORS['accent'],
                        troughcolor=cls.COLORS['bg_tertiary'],
                        borderwidth=0,
                        thickness=4
                        )

        # 滚动条 - Windows 11 细滚动条
        style.configure('Modern.Vertical.TScrollbar',
                        background=cls.COLORS['bg_tertiary'],
                        troughcolor=cls.COLORS['bg_primary'],
                        bordercolor=cls.COLORS['border'],
                        arrowcolor=cls.COLORS['fg_secondary'],
                        width=12
                        )
        style.map('Modern.Vertical.TScrollbar',
                  background=[('active', cls.COLORS['accent_light'])]
                  )

        # 分隔线
        style.configure('TSeparator',
                        background=cls.COLORS['divider']
                        )


class Windows11FileMerger:
    """Windows 11 官方风格文件合并工具"""

    def __init__(self, root):
        self.root = root
        self.root.title("文件合并工具 - Windows 11")
        self.root.geometry("1500x900")

        # 设置窗口背景
        self.root.configure(bg=Windows11Theme.COLORS['bg_primary'])

        # 应用主题
        Windows11Theme.apply_theme()

        # 设置窗口图标（如果有）
        try:
            self.root.iconbitmap(default='icon.ico')
        except:
            pass

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
        self.status_var.set("✨ 欢迎使用 Windows 11 文件合并工具")

    def create_widgets(self):
        """创建Windows 11风格界面"""

        # ========== 主容器 ==========
        main_container = tk.Frame(self.root, bg=Windows11Theme.COLORS['bg_primary'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        # ========== 顶部标题区域 ==========
        header_frame = tk.Frame(main_container, bg=Windows11Theme.COLORS['bg_primary'])
        header_frame.pack(fill=tk.X, pady=(0, 25))

        # 左侧标题
        title_frame = tk.Frame(header_frame, bg=Windows11Theme.COLORS['bg_primary'])
        title_frame.pack(side=tk.LEFT)

        # 主标题
        title_label = tk.Label(
            title_frame,
            text="文件内容合并工具",
            font=('Segoe UI Variable Display', 24, 'bold'),
            fg=Windows11Theme.COLORS['fg_primary'],
            bg=Windows11Theme.COLORS['bg_primary']
        )
        title_label.pack(anchor=tk.W)

        # 副标题
        subtitle_label = tk.Label(
            title_frame,
            text="批量选择文件，一键合并内容 - Windows 11 专属设计",
            font=('Segoe UI Variable', 12),
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
        stats_card.pack(side=tk.RIGHT, padx=10, pady=5)

        # 统计内容
        stats_inner = tk.Frame(stats_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=20, pady=10)
        stats_inner.pack()

        stats_label = tk.Label(
            stats_inner,
            text="已选择文件",
            font=('Segoe UI Variable', 10),
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        stats_label.pack()

        self.stats_var = tk.StringVar(value="0")
        stats_number = tk.Label(
            stats_inner,
            textvariable=self.stats_var,
            font=('Segoe UI Variable Display', 28, 'bold'),
            fg=Windows11Theme.COLORS['accent'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        stats_number.pack()

        # ========== 主要内容区域（两列布局）==========
        content_frame = tk.Frame(main_container, bg=Windows11Theme.COLORS['bg_primary'])
        content_frame.pack(fill=tk.BOTH, expand=True)

        # 左侧面板容器
        left_container = tk.Frame(content_frame, bg=Windows11Theme.COLORS['bg_primary'], width=950)
        left_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        left_container.pack_propagate(False)

        # 右侧面板容器
        right_container = tk.Frame(content_frame, bg=Windows11Theme.COLORS['bg_primary'], width=450)
        right_container.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(15, 0))
        right_container.pack_propagate(False)

        # 创建左右面板内容
        self.create_left_panel(left_container)
        self.create_right_panel(right_container)

        # ========== 底部状态栏 ==========
        status_frame = tk.Frame(
            main_container,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0,
            height=40
        )
        status_frame.pack(fill=tk.X, pady=(20, 0))
        status_frame.pack_propagate(False)

        status_inner = tk.Frame(status_frame, bg=Windows11Theme.COLORS['bg_secondary'], padx=15, pady=8)
        status_inner.pack(fill=tk.BOTH, expand=True)

        # 状态图标和文字
        self.status_var = tk.StringVar(value="就绪")
        status_icon = tk.Label(
            status_inner,
            text="●",
            font=('Segoe UI', 10),
            fg=Windows11Theme.COLORS['success'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        status_icon.pack(side=tk.LEFT, padx=(0, 8))

        status_label = tk.Label(
            status_inner,
            textvariable=self.status_var,
            font=('Segoe UI Variable', 10),
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        status_label.pack(side=tk.LEFT)

        # 进度条（隐藏）
        self.progress_bar = ttk.Progressbar(
            status_inner,
            style='Modern.Horizontal.TProgressbar',
            mode='indeterminate',
            length=150
        )
        self.progress_bar.pack(side=tk.RIGHT)
        self.progress_bar.pack_forget()

    def create_left_panel(self, parent):
        """创建左侧面板 - Windows 11 风格"""

        # ========== 路径选择卡片 ==========
        path_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        path_card.pack(fill=tk.X, pady=(0, 15))

        path_content = tk.Frame(path_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=20, pady=20)
        path_content.pack(fill=tk.X)

        # 卡片标题
        path_title = tk.Label(
            path_content,
            text="📁 文件夹路径",
            font=('Segoe UI Variable', 12, 'bold'),
            fg=Windows11Theme.COLORS['fg_primary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        path_title.pack(anchor=tk.W, pady=(0, 12))

        # 路径输入行
        path_row = tk.Frame(path_content, bg=Windows11Theme.COLORS['bg_secondary'])
        path_row.pack(fill=tk.X)

        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(
            path_row,
            textvariable=self.path_var,
            font=('Segoe UI Variable', 10),
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            relief='solid',
            bd=1,
            highlightthickness=1,
            highlightcolor=Windows11Theme.COLORS['border'],
            highlightbackground=Windows11Theme.COLORS['border']
        )
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=8)

        # 浏览按钮
        self.browse_btn = tk.Button(
            path_row,
            text="浏览",
            command=self.browse_folder,
            font=('Segoe UI Variable', 10),
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            relief='solid',
            bd=1,
            padx=20,
            pady=6,
            cursor='hand2'
        )
        self.browse_btn.pack(side=tk.LEFT, padx=(0, 5))

        # 加载按钮
        self.load_btn = tk.Button(
            path_row,
            text="加载",
            command=self.load_folder_tree,
            font=('Segoe UI Variable', 10, 'bold'),
            bg=Windows11Theme.COLORS['accent'],
            fg='white',
            relief='flat',
            bd=0,
            padx=25,
            pady=6,
            cursor='hand2'
        )
        self.load_btn.pack(side=tk.LEFT)

        # 绑定悬停效果
        self.browse_btn.bind('<Enter>', lambda e: self.browse_btn.config(bg=Windows11Theme.COLORS['hover']))
        self.browse_btn.bind('<Leave>', lambda e: self.browse_btn.config(bg='white'))
        self.load_btn.bind('<Enter>', lambda e: self.load_btn.config(bg=Windows11Theme.COLORS['accent_dark']))
        self.load_btn.bind('<Leave>', lambda e: self.load_btn.config(bg=Windows11Theme.COLORS['accent']))

        # ========== 工具栏卡片 ==========
        toolbar_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        toolbar_card.pack(fill=tk.X, pady=(0, 15))

        toolbar_content = tk.Frame(toolbar_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=20, pady=20)
        toolbar_content.pack(fill=tk.X)

        # 工具按钮行
        tools_row = tk.Frame(toolbar_content, bg=Windows11Theme.COLORS['bg_secondary'])
        tools_row.pack(fill=tk.X, pady=(0, 15))

        tools = [
            ("全选", self.select_all, Windows11Theme.COLORS['accent']),
            ("全不选", self.deselect_all, Windows11Theme.COLORS['fg_secondary']),
            ("反选", self.invert_selection, Windows11Theme.COLORS['fg_primary']),
            ("代码文件", self.select_code_files, '#881798'),
            ("文本文件", self.select_text_files, '#ff8c00'),
        ]

        for text, command, color in tools:
            btn = tk.Button(
                tools_row,
                text=text,
                command=command,
                font=('Segoe UI Variable', 10),
                bg='white',
                fg=color,
                relief='solid',
                bd=1,
                padx=15,
                pady=5,
                cursor='hand2'
            )
            btn.pack(side=tk.LEFT, padx=(0, 8))
            btn.bind('<Enter>', lambda e, b=btn: b.config(bg=Windows11Theme.COLORS['hover']))
            btn.bind('<Leave>', lambda e, b=btn: b.config(bg='white'))

        # 搜索行
        search_row = tk.Frame(toolbar_content, bg=Windows11Theme.COLORS['bg_secondary'])
        search_row.pack(fill=tk.X)

        search_icon = tk.Label(
            search_row,
            text="🔍",
            font=('Segoe UI', 14),
            bg=Windows11Theme.COLORS['bg_secondary'],
            fg=Windows11Theme.COLORS['fg_tertiary']
        )
        search_icon.pack(side=tk.LEFT, padx=(0, 8))

        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.filter_tree)
        self.search_entry = tk.Entry(
            search_row,
            textvariable=self.search_var,
            font=('Segoe UI Variable', 10),
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            relief='solid',
            bd=1,
            highlightthickness=1,
            highlightcolor=Windows11Theme.COLORS['border'],
            highlightbackground=Windows11Theme.COLORS['border']
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
        tree_card.pack(fill=tk.BOTH, expand=True)

        tree_content = tk.Frame(tree_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=20, pady=20)
        tree_content.pack(fill=tk.BOTH, expand=True)

        # 树标题
        tree_title = tk.Label(
            tree_content,
            text="📋 文件浏览器",
            font=('Segoe UI Variable', 12, 'bold'),
            fg=Windows11Theme.COLORS['fg_primary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        tree_title.pack(anchor=tk.W, pady=(0, 12))

        # Treeview容器
        tree_container = tk.Frame(tree_content, bg='white', relief='solid', bd=1)
        tree_container.pack(fill=tk.BOTH, expand=True)

        # 创建Treeview
        self.tree = ttk.Treeview(
            tree_container,
            columns=('size', 'type', 'modified'),
            show='tree headings',
            selectmode='none',
            style='Modern.Treeview'
        )

        # 定义列
        self.tree.heading('#0', text='文件名', anchor=tk.W)
        self.tree.heading('size', text='大小', anchor=tk.W)
        self.tree.heading('type', text='类型', anchor=tk.W)
        self.tree.heading('modified', text='修改时间', anchor=tk.W)

        # 设置列宽
        self.tree.column('#0', width=450, minwidth=350)
        self.tree.column('size', width=100, minwidth=80)
        self.tree.column('type', width=150, minwidth=120)
        self.tree.column('modified', width=150, minwidth=130)

        # 滚动条
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

        # 布局
        self.tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')

        tree_container.grid_rowconfigure(0, weight=1)
        tree_container.grid_columnconfigure(0, weight=1)

        # 绑定点击事件
        self.tree.bind('<Button-1>', self.on_tree_click)
        self.tree.bind('<Double-Button-1>', self.on_tree_double_click)
        self.tree.bind('<space>', self.on_tree_space)

        # ========== 底部设置卡片 ==========
        settings_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        settings_card.pack(fill=tk.X, pady=(15, 0))

        settings_content = tk.Frame(settings_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=20, pady=15)
        settings_content.pack(fill=tk.X)

        # 设置行
        settings_row = tk.Frame(settings_content, bg=Windows11Theme.COLORS['bg_secondary'])
        settings_row.pack(fill=tk.X, pady=(0, 12))

        # 分隔行数
        sep_label = tk.Label(
            settings_row,
            text="文件间分隔行数:",
            font=('Segoe UI Variable', 10),
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        sep_label.pack(side=tk.LEFT, padx=(0, 8))

        self.separator_var = tk.StringVar(value="3")
        self.separator_spinbox = tk.Spinbox(
            settings_row,
            from_=0,
            to=10,
            width=5,
            textvariable=self.separator_var,
            font=('Segoe UI Variable', 10),
            bg='white',
            relief='solid',
            bd=1
        )
        self.separator_spinbox.pack(side=tk.LEFT, padx=(0, 20))

        # 显示文件名
        self.show_filename_var = tk.BooleanVar(value=True)
        self.show_filename_check = tk.Checkbutton(
            settings_row,
            text="显示文件名",
            variable=self.show_filename_var,
            font=('Segoe UI Variable', 10),
            bg=Windows11Theme.COLORS['bg_secondary'],
            fg=Windows11Theme.COLORS['fg_primary'],
            activebackground=Windows11Theme.COLORS['bg_secondary'],
            selectcolor='white',
            relief='flat',
            bd=0
        )
        self.show_filename_check.pack(side=tk.LEFT, padx=(0, 20))

        # 包含子目录
        self.include_subdirs_var = tk.BooleanVar(value=True)
        self.include_subdirs_check = tk.Checkbutton(
            settings_row,
            text="包含子目录",
            variable=self.include_subdirs_var,
            command=self.toggle_subdirs,
            font=('Segoe UI Variable', 10),
            bg=Windows11Theme.COLORS['bg_secondary'],
            fg=Windows11Theme.COLORS['fg_primary'],
            activebackground=Windows11Theme.COLORS['bg_secondary'],
            selectcolor='white',
            relief='flat',
            bd=0
        )
        self.include_subdirs_check.pack(side=tk.LEFT)

        # 操作按钮行
        action_row = tk.Frame(settings_content, bg=Windows11Theme.COLORS['bg_secondary'])
        action_row.pack(fill=tk.X)

        # 复制按钮
        self.copy_btn = tk.Button(
            action_row,
            text="📋 复制选中内容",
            command=self.copy_selected_content,
            font=('Segoe UI Variable', 11, 'bold'),
            bg=Windows11Theme.COLORS['accent'],
            fg='white',
            relief='flat',
            bd=0,
            padx=25,
            pady=10,
            cursor='hand2'
        )
        self.copy_btn.pack(side=tk.LEFT, padx=(0, 10))
        self.copy_btn.bind('<Enter>', lambda e: self.copy_btn.config(bg=Windows11Theme.COLORS['accent_dark']))
        self.copy_btn.bind('<Leave>', lambda e: self.copy_btn.config(bg=Windows11Theme.COLORS['accent']))

        # 预览按钮
        self.preview_btn = tk.Button(
            action_row,
            text="👁️ 预览",
            command=self.preview_selected_content,
            font=('Segoe UI Variable', 11),
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            relief='solid',
            bd=1,
            padx=25,
            pady=9,
            cursor='hand2'
        )
        self.preview_btn.pack(side=tk.LEFT, padx=(0, 10))
        self.preview_btn.bind('<Enter>', lambda e: self.preview_btn.config(bg=Windows11Theme.COLORS['hover']))
        self.preview_btn.bind('<Leave>', lambda e: self.preview_btn.config(bg='white'))

        # 全部展开/折叠按钮
        self.expand_all_btn = tk.Button(
            action_row,
            text="🔽 全部展开",
            command=self.expand_all,
            font=('Segoe UI Variable', 10),
            bg='white',
            fg=Windows11Theme.COLORS['fg_secondary'],
            relief='solid',
            bd=1,
            padx=12,
            pady=6,
            cursor='hand2'
        )
        self.expand_all_btn.pack(side=tk.LEFT, padx=(0, 5))

        self.collapse_all_btn = tk.Button(
            action_row,
            text="🔼 全部折叠",
            command=self.collapse_all,
            font=('Segoe UI Variable', 10),
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
        """创建右侧面板 - Windows 11 风格"""

        # ========== 已选文件卡片 ==========
        selected_card = tk.Frame(
            parent,
            bg=Windows11Theme.COLORS['bg_secondary'],
            highlightbackground=Windows11Theme.COLORS['border'],
            highlightthickness=1,
            bd=0
        )
        selected_card.pack(fill=tk.BOTH, expand=True)

        selected_content = tk.Frame(selected_card, bg=Windows11Theme.COLORS['bg_secondary'], padx=20, pady=20)
        selected_content.pack(fill=tk.BOTH, expand=True)

        # 标题行
        title_row = tk.Frame(selected_content, bg=Windows11Theme.COLORS['bg_secondary'])
        title_row.pack(fill=tk.X, pady=(0, 15))

        title_label = tk.Label(
            title_row,
            text="📋 已选文件列表",
            font=('Segoe UI Variable', 14, 'bold'),
            fg=Windows11Theme.COLORS['fg_primary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        title_label.pack(side=tk.LEFT)

        # 清空按钮
        self.clear_all_btn = tk.Button(
            title_row,
            text="清空所有",
            command=self.clear_all_selections,
            font=('Segoe UI Variable', 10),
            bg='white',
            fg=Windows11Theme.COLORS['error'],
            relief='solid',
            bd=1,
            padx=12,
            pady=2,
            cursor='hand2'
        )
        self.clear_all_btn.pack(side=tk.RIGHT)
        self.clear_all_btn.bind('<Enter>', lambda e: self.clear_all_btn.config(bg=Windows11Theme.COLORS['hover']))
        self.clear_all_btn.bind('<Leave>', lambda e: self.clear_all_btn.config(bg='white'))

        # 顺序控制栏
        order_frame = tk.Frame(selected_content, bg=Windows11Theme.COLORS['bg_secondary'])
        order_frame.pack(fill=tk.X, pady=(0, 15))

        order_label = tk.Label(
            order_frame,
            text="调整顺序:",
            font=('Segoe UI Variable', 10),
            fg=Windows11Theme.COLORS['fg_secondary'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        order_label.pack(side=tk.LEFT, padx=(0, 10))

        # 顺序按钮
        order_buttons = [
            ("↑ 上移", self.move_selected_up),
            ("↓ 下移", self.move_selected_down),
            ("⏫ 置顶", self.move_selected_to_top),
            ("⏬ 置底", self.move_selected_to_bottom),
        ]

        self.order_btns = []
        for text, command in order_buttons:
            btn = tk.Button(
                order_frame,
                text=text,
                command=command,
                font=('Segoe UI Variable', 9),
                bg='white',
                fg=Windows11Theme.COLORS['accent'],
                relief='solid',
                bd=1,
                padx=8,
                pady=2,
                cursor='hand2',
                state='disabled'
            )
            btn.pack(side=tk.LEFT, padx=(0, 5))
            self.order_btns.append(btn)

            btn.bind('<Enter>',
                     lambda e, b=btn: b.config(bg=Windows11Theme.COLORS['hover']) if b['state'] != 'disabled' else None)
            btn.bind('<Leave>', lambda e, b=btn: b.config(bg='white') if b['state'] != 'disabled' else None)

        # 列表容器
        list_container = tk.Frame(selected_content, bg='white', relief='solid', bd=1)
        list_container.pack(fill=tk.BOTH, expand=True)

        # 列表box
        self.selected_listbox = tk.Listbox(
            list_container,
            selectmode=tk.EXTENDED,
            bg='white',
            fg=Windows11Theme.COLORS['fg_primary'],
            font=('Cascadia Code', 10),
            relief='flat',
            bd=0,
            highlightthickness=0,
            selectbackground=Windows11Theme.COLORS['selected'],
            selectforeground=Windows11Theme.COLORS['fg_primary']
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

        # 列表底部工具栏
        list_bottom = tk.Frame(selected_content, bg=Windows11Theme.COLORS['bg_secondary'])
        list_bottom.pack(fill=tk.X, pady=(15, 0))

        # 计数标签
        self.selected_count_label = tk.Label(
            list_bottom,
            text="0 个文件",
            font=('Segoe UI Variable', 11, 'bold'),
            fg=Windows11Theme.COLORS['success'],
            bg=Windows11Theme.COLORS['bg_secondary']
        )
        self.selected_count_label.pack(side=tk.LEFT)

        # 操作按钮
        btn_frame = tk.Frame(list_bottom, bg=Windows11Theme.COLORS['bg_secondary'])
        btn_frame.pack(side=tk.RIGHT)

        self.remove_selected_btn = tk.Button(
            btn_frame,
            text="移除选中",
            command=self.remove_selected_from_list,
            font=('Segoe UI Variable', 10),
            bg='white',
            fg=Windows11Theme.COLORS['error'],
            relief='solid',
            bd=1,
            padx=12,
            pady=4,
            cursor='hand2'
        )
        self.remove_selected_btn.pack(side=tk.LEFT, padx=(0, 8))

        self.copy_list_btn = tk.Button(
            btn_frame,
            text="复制列表",
            command=self.copy_file_list,
            font=('Segoe UI Variable', 10),
            bg='white',
            fg=Windows11Theme.COLORS['accent'],
            relief='solid',
            bd=1,
            padx=12,
            pady=4,
            cursor='hand2'
        )
        self.copy_list_btn.pack(side=tk.LEFT)

        # 绑定悬停效果
        for btn in [self.remove_selected_btn, self.copy_list_btn]:
            btn.bind('<Enter>', lambda e, b=btn: b.config(bg=Windows11Theme.COLORS['hover']))
            btn.bind('<Leave>', lambda e, b=btn: b.config(bg='white'))

        # 绑定列表事件
        self.selected_listbox.bind('<<ListboxSelect>>', self.on_list_select)
        self.selected_listbox.bind('<Double-Button-1>', self.on_list_double_click)
        self.selected_listbox.bind('<Delete>', self.on_list_delete)

    def bind_events(self):
        """绑定事件"""
        self.path_entry.bind('<Return>', lambda e: self.load_folder_tree())

    def browse_folder(self):
        """浏览文件夹"""
        folder = filedialog.askdirectory(title="选择文件夹")
        if folder:
            self.path_var.set(folder)
            self.load_folder_tree()

    def load_folder_tree(self):
        """加载文件夹树"""
        folder = self.path_var.get()
        if not folder or not os.path.exists(folder):
            messagebox.showerror("错误", "请选择有效的文件夹路径")
            return

        self.current_path = folder

        # 清空现有数据
        self.clear_tree()

        # 显示进度条
        self.progress_bar.pack(side=tk.RIGHT)
        self.progress_bar.start(10)

        # 更新状态
        self.status_var.set("正在加载文件列表...")
        self.root.update()

        # 在后台线程加载
        threading.Thread(target=self._load_tree_data, args=(folder,), daemon=True).start()

    def _load_tree_data(self, folder):
        """后台加载树数据"""
        try:
            # 添加根节点
            root_text = f"📂 {os.path.basename(folder)}"
            root_node = self.tree.insert('', 'end', text=root_text, open=True, tags=('folder',))
            self.tree_nodes[root_node] = folder
            self.node_paths[folder] = root_node

            # 递归添加文件和文件夹
            self._add_tree_items(root_node, folder)

            # 自动展开第一级
            self.tree.item(root_node, open=True)

            file_count = len(self.file_vars)

            # 更新UI
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
        """递归添加树项目"""
        try:
            items = sorted(os.listdir(path))

            for item in items:
                # 跳过隐藏文件和系统文件
                if item.startswith('.') or item.startswith('~'):
                    continue

                full_path = os.path.join(path, item)

                if os.path.isdir(full_path):
                    # 添加文件夹节点
                    folder_node = self.tree.insert(
                        parent_node, 'end',
                        text=f"📁 {item}",
                        values=('', '文件夹', ''),
                        tags=('folder',)
                    )
                    self.tree_nodes[folder_node] = full_path
                    self.node_paths[full_path] = folder_node

                    # 递归添加子文件夹内容
                    if self.include_subdirs_var.get():
                        self._add_tree_items(folder_node, full_path)

                else:
                    # 获取文件信息
                    size = self.get_file_size(full_path)
                    ext = os.path.splitext(item)[1].lower() or '无扩展名'
                    modified = self.get_file_modified_time(full_path)

                    # 添加文件节点
                    file_node = self.tree.insert(
                        parent_node, 'end',
                        text=f"📄 {item}",
                        values=(size, ext, modified),
                        tags=('file',)
                    )
                    self.tree_nodes[file_node] = full_path
                    self.node_paths[full_path] = file_node

                    # 创建勾选变量
                    self.file_vars[full_path] = tk.BooleanVar(value=False)

        except PermissionError:
            pass  # 跳过无权限访问的文件夹

    def on_tree_click(self, event):
        """处理树点击事件"""
        region = self.tree.identify_region(event.x, event.y)
        if region == "tree":
            item = self.tree.identify_row(event.y)
            if item:
                # 获取点击位置是否在图标区域
                x, y = event.x, event.y
                bbox = self.tree.bbox(item, column='#0')

                if bbox and x < bbox[0] + 25:  # 点击在图标区域
                    self.toggle_item_selection(item)
                else:
                    # 点击在其他区域，展开/折叠
                    self.toggle_folder(item)
                return "break"

    def on_tree_double_click(self, event):
        """处理双击事件"""
        item = self.tree.identify_row(event.y)
        if item:
            self.toggle_folder(item)
            return "break"

    def on_tree_space(self, event):
        """处理空格键"""
        item = self.tree.focus()
        if item:
            self.toggle_item_selection(item)
            return "break"

    def toggle_folder(self, item):
        """展开/折叠文件夹"""
        tags = self.tree.item(item, 'tags')
        if 'folder' in tags:
            if self.tree.item(item, 'open'):
                self.tree.item(item, open=False)
            else:
                self.tree.item(item, open=True)

    def toggle_item_selection(self, item):
        """切换项目的选择状态"""
        path = self.tree_nodes.get(item)
        if not path:
            return

        tags = self.tree.item(item, 'tags')

        if 'folder' in tags:
            # 文件夹：切换所有子文件的选择状态
            self.toggle_folder_selection(path, item)
        else:
            # 文件：切换单个文件状态
            if path in self.file_vars:
                current = self.file_vars[path].get()
                new_state = not current
                self.file_vars[path].set(new_state)
                self.update_file_icon(item, new_state)

                # 更新选择顺序列表
                if new_state:
                    if path not in self.selected_files_order:
                        self.selected_files_order.append(path)
                        self.status_var.set(f"已添加: {os.path.basename(path)}")
                else:
                    if path in self.selected_files_order:
                        self.selected_files_order.remove(path)
                        self.status_var.set(f"已移除: {os.path.basename(path)}")

                # 更新已选文件列表显示
                self.update_selected_list()

        self.update_file_count()
        self.update_parent_folders(item)

    def toggle_folder_selection(self, folder_path, folder_node):
        """切换文件夹内所有文件的选择状态"""
        # 获取文件夹内所有文件
        files_in_folder = []
        for file_path in self.file_vars:
            if file_path.startswith(folder_path) and os.path.isfile(file_path):
                files_in_folder.append(file_path)

        if not files_in_folder:
            return

        # 判断当前状态
        selected_count = sum(1 for f in files_in_folder if self.file_vars[f].get())

        # 切换状态：全选 -> 全不选 -> 全选
        new_state = selected_count < len(files_in_folder)

        # 应用新状态
        for file_path in files_in_folder:
            self.file_vars[file_path].set(new_state)

        # 更新文件夹内所有文件的图标
        self.update_folder_files_icon(folder_path, new_state)

        # 更新选择顺序列表
        if new_state:
            for file_path in files_in_folder:
                if file_path not in self.selected_files_order:
                    self.selected_files_order.append(file_path)
        else:
            for file_path in files_in_folder:
                if file_path in self.selected_files_order:
                    self.selected_files_order.remove(file_path)

        # 更新已选文件列表
        self.update_selected_list()

    def update_folder_files_icon(self, folder_path, state):
        """更新文件夹内所有文件的图标"""
        for file_path, node in self.node_paths.items():
            if file_path.startswith(folder_path) and os.path.isfile(file_path):
                if node in self.tree_nodes:
                    self.update_file_icon(node, state)

    def update_file_icon(self, node, selected):
        """更新文件图标"""
        path = self.tree_nodes.get(node)
        if path and os.path.isfile(path):
            text = self.tree.item(node, 'text')
            # 移除现有图标
            if text.startswith('✅ '):
                text = text[2:]
            elif text.startswith('📄 '):
                text = text[2:]

            # 添加新图标
            if selected:
                self.tree.item(node, text=f"✅ {text}")
            else:
                self.tree.item(node, text=f"📄 {text}")

    def update_parent_folders(self, item):
        """更新所有父文件夹的状态"""
        parent = self.tree.parent(item)
        while parent:
            self.update_folder_icon(parent)
            parent = self.tree.parent(parent)

    def update_folder_icon(self, folder_node):
        """更新文件夹图标"""
        folder_path = self.tree_nodes.get(folder_node)
        if not folder_path or not os.path.isdir(folder_path):
            return

        # 获取文件夹内所有文件的选择状态
        files_in_folder = []
        for file_path, var in self.file_vars.items():
            if file_path.startswith(folder_path) and os.path.isfile(file_path):
                files_in_folder.append(var.get())

        if not files_in_folder:
            # 空文件夹或没有文件
            icon = "📁"
        else:
            selected_count = sum(files_in_folder)
            if selected_count == 0:
                icon = "📁"
            elif selected_count == len(files_in_folder):
                icon = "✅"
            else:
                icon = "◻️"

        # 更新文件夹图标
        text = self.tree.item(folder_node, 'text')
        if text.startswith('✅ '):
            text = text[2:]
        elif text.startswith('📁 '):
            text = text[2:]
        elif text.startswith('◻️ '):
            text = text[2:]

        self.tree.item(folder_node, text=f"{icon} {text}")

    def update_selected_list(self):
        """更新已选文件列表"""
        self.selected_listbox.delete(0, tk.END)

        for index, file_path in enumerate(self.selected_files_order, 1):
            if os.path.isfile(file_path):
                if self.current_path:
                    rel_path = os.path.relpath(file_path, self.current_path)
                else:
                    rel_path = os.path.basename(file_path)

                display_text = f"{index:3d}.  {rel_path}"
                self.selected_listbox.insert(tk.END, display_text)

                # 设置序号颜色
                self.selected_listbox.itemconfig(tk.END, fg=Windows11Theme.COLORS['fg_primary'])

        count = len(self.selected_files_order)
        self.selected_count_label.config(text=f"{count} 个文件")
        self.stats_var.set(str(count))

        # 更新顺序按钮状态
        self.update_order_buttons()

    def update_order_buttons(self):
        """更新顺序按钮状态"""
        selection = self.selected_listbox.curselection()
        has_selection = len(selection) > 0
        has_multiple = len(self.selected_files_order) > 1

        state = 'normal' if has_selection and has_multiple else 'disabled'
        for btn in self.order_btns:
            btn.config(state=state)

    def on_list_select(self, event):
        """列表选择事件"""
        self.update_order_buttons()

    def move_selected_up(self):
        """上移选中的文件"""
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
            self.status_var.set(f"已上移文件 #{index + 1}")

    def move_selected_down(self):
        """下移选中的文件"""
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
            self.status_var.set(f"已下移文件 #{index + 1}")

    def move_selected_to_top(self):
        """置顶选中的文件"""
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
            self.status_var.set("已置顶文件")

    def move_selected_to_bottom(self):
        """置底选中的文件"""
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
            self.status_var.set("已置底文件")

    def on_list_double_click(self, event):
        """双击已选列表项"""
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
        """删除键 - 移除选中的列表项"""
        self.remove_selected_from_list()

    def remove_selected_from_list(self):
        """从列表中移除选中的文件"""
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
        self.status_var.set(f"已移除 {len(files_to_remove)} 个文件")

    def copy_file_list(self):
        """复制文件列表到剪贴板"""
        if not self.selected_files_order:
            messagebox.showwarning("警告", "没有选中的文件")
            return

        list_lines = ["📋 已选文件列表:", ""]

        for index, file_path in enumerate(self.selected_files_order, 1):
            if self.current_path:
                rel_path = os.path.relpath(file_path, self.current_path)
            else:
                rel_path = os.path.basename(file_path)
            list_lines.append(f"{index:3d}. {rel_path}")

        list_text = "\n".join(list_lines)

        try:
            pyperclip.copy(list_text)
            self.status_var.set("✅ 已复制文件列表到剪贴板")
        except Exception as e:
            messagebox.showerror("错误", f"复制失败：{str(e)}")

    def get_selected_files(self):
        """获取所有选中的文件"""
        return [f for f in self.selected_files_order if os.path.isfile(f)]

    def update_file_count(self):
        """更新文件计数"""
        count = len(self.selected_files_order)
        self.stats_var.set(str(count))

    def get_file_size(self, file_path):
        """获取文件大小"""
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
        """获取文件修改时间"""
        try:
            timestamp = os.path.getmtime(file_path)
            return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')
        except:
            return "未知"

    def select_all(self):
        """全选所有文件"""
        self.progress_bar.pack(side=tk.RIGHT)
        self.progress_bar.start(10)

        def task():
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

            self.root.after(0, self.update_selected_list)
            self.root.after(0, self.update_file_count)
            self.root.after(0, lambda: self.status_var.set("已全选所有文件"))
            self.root.after(0, lambda: self.progress_bar.stop())
            self.root.after(0, lambda: self.progress_bar.pack_forget())

        threading.Thread(target=task, daemon=True).start()

    def _update_all_folders_recursive(self, node):
        """递归更新所有文件夹图标"""
        self.update_folder_icon(node)
        for child in self.tree.get_children(node):
            self._update_all_folders_recursive(child)

    def deselect_all(self):
        """全不选"""
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
        """反选"""
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
        """只选代码文件"""
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
        """只选文本文件"""
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
        """清空所有勾选"""
        if messagebox.askyesno("确认", "确定要清空所有文件勾选吗？"):
            self.deselect_all()

    def toggle_subdirs(self):
        """切换是否包含子目录"""
        if self.current_path:
            self.load_folder_tree()

    def expand_all(self):
        """全部展开"""

        def expand_recursive(node):
            self.tree.item(node, open=True)
            for child in self.tree.get_children(node):
                expand_recursive(child)

        for node in self.tree.get_children(''):
            expand_recursive(node)
        self.status_var.set("已全部展开")

    def collapse_all(self):
        """全部折叠"""

        def collapse_recursive(node):
            self.tree.item(node, open=False)
            for child in self.tree.get_children(node):
                collapse_recursive(child)

        for node in self.tree.get_children(''):
            collapse_recursive(node)
        self.status_var.set("已全部折叠")

    def filter_tree(self, *args):
        """过滤树显示"""
        search_text = self.search_var.get().lower()

        if not search_text:
            for node in self.tree.get_children(''):
                self.tree.item(node, open=True)
                self._show_all_recursive(node)
        else:
            for node in self.tree.get_children(''):
                self._filter_recursive(node, search_text)

    def _show_all_recursive(self, node):
        """递归显示所有"""
        self.tree.item(node, open=True)
        for child in self.tree.get_children(node):
            self._show_all_recursive(child)

    def _filter_recursive(self, node, search_text):
        """递归过滤"""
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
        """显示所有父节点"""
        parent = self.tree.parent(node)
        while parent:
            self.tree.item(parent, open=True)
            parent = self.tree.parent(parent)

    def clear_tree(self):
        """清空树"""
        self.tree.delete(*self.tree.get_children())
        self.file_vars.clear()
        self.tree_nodes.clear()
        self.node_paths.clear()
        self.selected_files_order.clear()

        self.selected_listbox.delete(0, tk.END)
        self.selected_count_label.config(text="0 个文件")

    def merge_selected_files(self):
        """合并选中的文件内容"""
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
                    merged_content.append(f"=== [{i + 1}] {rel_path} ===")

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
        """尝试多种编码读取文件"""
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
        """复制选中文件的内容"""
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
        """预览选中的内容"""
        selected_files = self.get_selected_files()
        if not selected_files:
            messagebox.showwarning("警告", "请至少选择一个文件")
            return

        try:
            merged_content = self.merge_selected_files()

            # 创建预览窗口
            preview_window = tk.Toplevel(self.root)
            preview_window.title("内容预览 - Windows 11")
            preview_window.geometry("1100x700")
            preview_window.configure(bg=Windows11Theme.COLORS['bg_primary'])

            # 主容器
            main_frame = tk.Frame(preview_window, bg=Windows11Theme.COLORS['bg_primary'])
            main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)

            # 标题
            title_label = tk.Label(
                main_frame,
                text="📄 内容预览",
                font=('Segoe UI Variable Display', 18, 'bold'),
                fg=Windows11Theme.COLORS['fg_primary'],
                bg=Windows11Theme.COLORS['bg_primary']
            )
            title_label.pack(anchor=tk.W, pady=(0, 15))

            # 文本容器
            text_container = tk.Frame(main_frame, bg='white', relief='solid', bd=1)
            text_container.pack(fill=tk.BOTH, expand=True)

            text_widget = tk.Text(
                text_container,
                wrap=tk.WORD,
                font=('Cascadia Code', 11),
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

            # 底部按钮栏
            bottom_frame = tk.Frame(main_frame, bg=Windows11Theme.COLORS['bg_primary'])
            bottom_frame.pack(fill=tk.X, pady=(15, 0))

            count_label = tk.Label(
                bottom_frame,
                text=f"共 {len(selected_files)} 个文件",
                font=('Segoe UI Variable', 11),
                fg=Windows11Theme.COLORS['success'],
                bg=Windows11Theme.COLORS['bg_primary']
            )
            count_label.pack(side=tk.LEFT)

            close_btn = tk.Button(
                bottom_frame,
                text="关闭",
                command=preview_window.destroy,
                font=('Segoe UI Variable', 11),
                bg=Windows11Theme.COLORS['accent'],
                fg='white',
                relief='flat',
                bd=0,
                padx=30,
                pady=8,
                cursor='hand2'
            )
            close_btn.pack(side=tk.RIGHT)
            close_btn.bind('<Enter>', lambda e: close_btn.config(bg=Windows11Theme.COLORS['accent_dark']))
            close_btn.bind('<Leave>', lambda e: close_btn.config(bg=Windows11Theme.COLORS['accent']))

        except Exception as e:
            messagebox.showerror("错误", f"预览失败：{str(e)}")



def main():
    """主函数"""
    root = tk.Tk()

    # 设置DPI感知
    if platform.system() == 'Windows':
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass

    app = Windows11FileMerger(root)

    # 居中显示
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    root.mainloop()


if __name__ == "__main__":
    main()