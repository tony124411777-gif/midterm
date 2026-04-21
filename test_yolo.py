from ultralytics import YOLO
import os

def main():
    # 1. 檢查照片是否存在
    img_path = 'moon_surface.jpg'
    if not os.path.exists(img_path):
        print(f"錯誤：請確保資料夾內有 {img_path} 檔案")
        return

    # 2. 載入通用預訓練模型 (COCO 資料集訓練)
    print("正在載入 YOLOv8 官方通用模型...")
    model = YOLO('yolov8n.pt') 

    # 3. 執行偵測 (設定較低的門檻值嘗試捕捉特徵)
    print("正在分析月球影像...")
    results = model.predict(source=img_path, save=True, conf=0.15)

    # 4. 輸出結果分析
    for result in results:
        count = len(result.boxes)
        print("\n" + "="*30)
        print(f"辨識結果報告：")
        print(f"偵測到的物件數量：{count}")
        
        if count == 0:
            print("【分析】未偵測到物件：這反映了通用模型在專業地貌辨識上的侷限性。")
        else:
            print("【分析】偵測到部分特徵：模型嘗試將月球特徵對應至已知的 80 種地球類別。")
        print(f"結果圖路徑：{result.save_dir}")
        print("="*30)

if __name__ == "__main__":
    main()