#!/usr/bin/env python3
"""Test YOLO inference with the backend API"""

import requests
import json
import mimetypes

# Test image path
image_path = r"D:\eye\tests\images\WIN_20251024_21_05_47_Pro.jpg"

# API endpoint
url = "http://localhost:8001/api/v1/yolo-e/infer/single"

# Check content type
content_type = mimetypes.guess_type(image_path)[0]
print(f"Content type: {content_type}")

# Prepare the request
with open(image_path, 'rb') as f:
    files = {'file': (image_path, f, content_type)}
    data = {
        'model_path': 'yolo11n.pt',
        'confidence_threshold': 0.5,
        'iou_threshold': 0.45,
        'use_gpu': True,  # Test with GPU requested but not available
        'custom_classes': 'person,bottle,car',  # Test custom classes with YOLO11 (should show warning)
    }
    
    try:
        response = requests.post(url, files=files, data=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
