#!/usr/bin/env python3
"""Test YOLO inference with annotated image generation"""

import requests
import json
import base64
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
        'use_gpu': True,
        'custom_classes': 'person,bottle,car',
    }
    
    try:
        response = requests.post(url, files=files, data=data)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            
            # Check if annotated_image is present
            if result.get('annotated_image'):
                print(f"Annotated image received (length: {len(result['annotated_image'])})")
                
                # Save the annotated image
                image_data = base64.b64decode(result['annotated_image'])
                with open('annotated_output.jpg', 'wb') as img_file:
                    img_file.write(image_data)
                print("Annotated image saved as 'annotated_output.jpg'")
            else:
                print("No annotated image in response")
            
            print(f"Detections: {len(result['detections'])}")
            for detection in result['detections']:
                print(f"  - {detection['class_name']}: {detection['confidence']:.2f}")
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")
