# RNGdle Hunting

自动抓取 [rngdle.com](https://rngdle.com) 随机数的脚本。

## 功能

- 自动点击生成随机数，利用网站特性刷新后直接查看结果并复制到剪贴板
- 输出每次抓取的结果，并计数
- 遇到 MYTHIC 或 ANOMALY 等级时自动暂停，保留浏览器窗口方便查看
- 浏览器自动最小化，减少干扰

## 环境要求

- Python 3.7+
- Selenium和Pyperclip库
- Chrome 
- ChromeDriver

## 安装与使用

1. 克隆仓库
   ```bash
   git clone https://github.com/lujunyu-China/rngdle-hunting.git
   cd rngdle-hunting
