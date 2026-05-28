# FaceFusion 中文使用说明（Windows）

这份说明给普通用户使用：你只需要双击一个文件即可启动。

## 你需要先准备

1. Windows 10 或 Windows 11
2. 已安装 Python 3.10+（安装时勾选 **Add Python to PATH**）
3. 网络正常（首次启动会自动安装依赖）

## 一键启动（最简单）

1. 打开本项目文件夹。
2. **双击 `start.bat`**。
3. 程序会自动做以下事情：
   - 检查 Python 版本
   - 自动安装 `requirements.txt` 依赖
   - 自动启动 FaceFusion 主程序
   - 自动打开浏览器到：`http://127.0.0.1:7860`

## 如果启动失败怎么办

- 请查看项目目录里的 `error.log`。
- 把 `error.log` 内容发给技术人员即可定位问题。

## 常见问题

### 双击后提示找不到 python
说明 Python 没有加入系统 PATH。请重新安装 Python，并勾选 **Add Python to PATH**。

### 浏览器没有自动打开
你可以手动打开浏览器，输入：`http://127.0.0.1:7860`

---

## 最后结论

你应该双击启动的文件是：**`start.bat`**。
