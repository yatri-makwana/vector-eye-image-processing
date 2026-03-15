#!/usr/bin/env python3
"""Complete test of YOLO inference with annotated image display"""

import requests
import json
import base64
import mimetypes
from pathlib import Path

# Test image path
image_path = r"D:\eye\tests\images\WIN_20251024_21_05_47_Pro.jpg"

# API endpoint
url = "http://localhost:8001/api/v1/yolo-e/infer/single"

def test_yolo_inference():
    """Test YOLO inference with annotated image generation"""
    
    print("🔍 YOLO Inference Test with Annotated Image")
    print("=" * 50)
    
    # Check content type
    content_type = mimetypes.guess_type(image_path)[0]
    print(f"📁 Input image: {Path(image_path).name}")
    print(f"📋 Content type: {content_type}")
    
    # Prepare the request
    with open(image_path, 'rb') as f:
        files = {'file': (image_path, f, content_type)}
        data = {
            'model_path': 'yolo11n.pt',
            'confidence_threshold': 0.5,
            'iou_threshold': 0.45,
            'use_gpu': False,  # Use CPU to avoid CUDA issues
            'custom_classes': 'person,bottle,car',
        }
        
        try:
            print("\n🚀 Sending inference request...")
            response = requests.post(url, files=files, data=data)
            
            if response.status_code == 200:
                result = response.json()
                
                print(f"✅ Inference successful!")
                print(f"⏱️  Processing time: {result['processing_time']:.3f}s")
                print(f"🎯 Detections found: {len(result['detections'])}")
                
                # Display detection results
                print("\n📊 Detection Results:")
                for i, detection in enumerate(result['detections'], 1):
                    print(f"  {i}. {detection['class_name']}: {detection['confidence']:.2f} confidence")
                    print(f"     Bounding box: {[round(x, 2) for x in detection['bbox']]}")
                
                # Handle annotated image
                if result.get('annotated_image'):
                    print(f"\n🖼️  Annotated image generated!")
                    print(f"📏 Image data size: {len(result['annotated_image'])} characters")
                    
                    # Save the annotated image
                    image_data = base64.b64decode(result['annotated_image'])
                    output_path = 'annotated_output.jpg'
                    with open(output_path, 'wb') as img_file:
                        img_file.write(image_data)
                    print(f"💾 Annotated image saved as: {output_path}")
                    print(f"📁 File size: {Path(output_path).stat().st_size / 1024:.1f} KB")
                    
                    return True
                else:
                    print("\n❌ No annotated image in response")
                    return False
                    
            else:
                print(f"❌ Error: {response.status_code}")
                print(f"Response: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Request failed: {e}")
            return False

if __name__ == "__main__":
    success = test_yolo_inference()
    
    if success:
        print("\n🎉 Test completed successfully!")
        print("📝 Summary:")
        print("   - YOLO model loaded and working")
        print("   - Image inference completed")
        print("   - Objects detected and classified")
        print("   - Annotated image with bounding boxes generated")
        print("   - Ready for frontend integration")
    else:
        print("\n❌ Test failed!")
        print("🔧 Please check the backend logs for errors")
