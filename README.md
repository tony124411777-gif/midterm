# 🌙 月球表面隕石坑自動辨識系統 (Lunar Crater Detection)

## 📌 專案簡介
本專案為 **114-2 基礎程式設計(二) 期中專案**。
目標是利用 Python 整合 **YOLOv8** 電腦視覺模型，針對月球表面影像進行自動化隕石坑與地貌特徵辨識。專案中探討了通用 AI 模型在處理科學專業地貌影像時的表現與侷限性。

## 🛠️ 技術棧 (Tech Stack)
- **程式語言**: Python 3.11+
- **核心框架**: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- **影像處理**: OpenCV, PIL
- **開發環境**: VS Code / PowerShell

## 📂 檔案結構
- `test_yolo.py`: 核心執行程式碼（包含影像讀取、模型載入與辨識邏輯）。
- `moon_surface.jpg`: 用於測試的月球表面影像素材。
- `yolov8n.pt`: YOLOv8 官方預訓練模型權重檔（首次執行時自動生成）。
- `runs/`: 偵測結果存放目錄，包含標註後的圖片。

## 🚀 安裝與執行教學

### 1. 安裝必要環境
請確保已安裝 Python，並在終端機執行以下指令安裝核心套件：
```bash
pip install ultralytics opencv-python pillow
