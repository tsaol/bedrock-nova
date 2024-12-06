# Bedrock Nova Examples

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) | [中文](README_zh.md)

A comprehensive collection of examples demonstrating the capabilities of Amazon Bedrock Nova models, including image understanding, image creation, video understanding, video creation, and text generation.

## Features

- 🖼️ **Image Processing**: 
  - Image understanding: analysis, Q&A, classification, and summarization
  - Image creation: generate images from text descriptions
- 🎥 **Video Processing**:
  - Video understanding: analysis, Q&A, and content summarization
  - Video creation: generate videos from text or images
- 📝 **Text Generation**: Both streaming and non-streaming text generation capabilities

## Prerequisites

- AWS Account with Bedrock access
- Python 3.7+
- Boto3
- AWS credentials configured

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bedrock-nova.git
cd bedrock-nova
```

2. Install dependencies:
```bash
pip install boto3
```

3. Configure AWS credentials:
```bash
aws configure
```

## Usage

### Image Understanding
```python
# Example of image analysis
from images.nova_image_understanding import analyze_image

response = analyze_image("path/to/image.jpg", "Describe this image.")
```

### Image Creation
```python
# Example of image generation
from images.nova_image_creation import create_image

response = create_image("A beautiful sunset over mountains")
```

### Video Understanding
```python
# Example of video analysis
from video.nova_video_understanding import analyze_video

response = analyze_video("path/to/video.mp4", "Summarize this video.")
```

### Video Creation
```python
# Example of video creation from images
from video.nova_video_creation_by_image import create_video_from_image

response = create_video_from_image("path/to/image.jpg", "Create a video with this image")
```

### Text Generation
```python
# Example of streaming text generation
from text.nova_text_generation_streaming import generate_text

response = generate_text("Write a story about...")
```

## Technical Specifications

### Image Understanding
- Total payload size limit: 25MB
- Supported aspect ratios: 1:1 to 1:9, 2:3, 2:4, and their transposes
- Minimum dimension: At least one side > 896px
- Maximum resolution: 8000x8000 pixels

#### Image-to-Token Conversion
| Image Resolution | Estimated Tokens |
|-----------------|------------------|
| 900 x 450       | ~800            |
| 900 x 900       | ~1300           |
| 1400 x 900      | ~1800           |
| 1800 x 900      | ~2400           |
| 1300 x 1300     | ~2600           |

### Video Understanding
- Single video per payload
- Base64 payload limit: 25MB
- S3 URI video size limit: 1GB
- Supported formats: MP4, MOV, MKV, WebM, FLV, MPEG, MPG, WMV, 3GP

#### Video Processing
- Resolution: All videos converted to 672x672 square
- Frame sampling:
  - ≤16 minutes: 1 FPS
  - >16 minutes: Reduced rate, fixed 960 frames
- Recommended durations:
  - Low motion: <1 hour
  - High motion: <16 minutes

#### Token Usage
| Video Duration | Frames Sampled | Sample Rate (FPS) | Token Count |
|---------------|----------------|-------------------|-------------|
| 10 sec        | 10            | 1                 | 2,880       |
| 30 sec        | 30            | 1                 | 8,640       |
| 16 min        | 960           | 1                 | 276,480     |
| 20 min        | 960           | 0.755             | 276,480     |
| 30 min        | 960           | 0.5               | 276,480     |
| 45 min        | 960           | 0.35556           | 276,480     |
| 1 hr          | 960           | 0.14              | 276,480     |
| 1.5 hr        | 960           | 0.096             | 276,480     |

## Project Structure

```
bedrock-nova/
├── images/
│   ├── nova_image_creation.py
│   ├── nova_image_understanding.py
│   └── test1.png
├── text/
│   ├── nova_text_generation.py
│   └── nova_text_generation_streaming.py
├── video/
│   ├── nova_video_creation.py
│   ├── nova_video_creation_by_image.py
│   ├── nova_video_understanding.py
│   └── animals.mp4
├── README.md
└── README_zh.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
