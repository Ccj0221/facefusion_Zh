FaceFusion
==========

> FaceFusion的中文界面版本.

[![Build Status](https://img.shields.io/github/actions/workflow/status/facefusion/facefusion/ci.yml.svg?branch=master)](https://github.com/facefusion/facefusion/actions?query=workflow:ci)
![License](https://img.shields.io/badge/license-MIT-green)


Preview
-------

![Preview](https://raw.githubusercontent.com/facefusion/facefusion/master/.github/preview.png?sanitize=true)
![image](https://github.com/Ccj0221/facefusion_Zh/assets/129196783/7494de9e-5b3d-4552-9418-77b1ceb4962b)


Installation
------------

Be aware, the installation needs technical skills and is not for beginners. Please do not open platform and installation related issues on GitHub. We have a very helpful [Discord](https://join.facefusion.io) community that will guide you to complete the installation.

Get started with the [installation](https://docs.facefusion.io/installation) guide.


用法
-----

启动参数:

```
python run.py [options]

选项：
  -h, --help                                                                                                             显示此帮助信息并退出
  -s SOURCE_PATHS, --source SOURCE_PATHS                                                                                 选择单个或多个源图像或音频
  -t TARGET_PATH, --target TARGET_PATH                                                                                   选择单个目标图像或视频
  -o OUTPUT_PATH, --output OUTPUT_PATH                                                                                   指定输出文件或目录
  -v, --version                                                                                                          显示程序的版本号并退出

其他：
  --skip-download                                                                                                        省略自动下载和远程查找
  --headless                                                                                                             在没有用户界面的情况下运行程序
  --log-level {error,warn,info,debug}                                                                                    调整终端显示的消息严重程度

执行：
  --execution-providers EXECUTION_PROVIDERS [EXECUTION_PROVIDERS ...]                                                    使用不同提供程序加速模型推理（选择：cpu，...）
  --execution-thread-count [1-128]                                                                                       指定处理时的并行线程数量
  --execution-queue-count [1-32]                                                                                         指定每个线程处理的帧数

内存：
  --video-memory-strategy {strict,moderate,tolerant}                                                                     平衡快速帧处理和低VRAM使用
  --system-memory-limit [0-128]                                                                                          限制可用于处理的可用RAM

人脸分析：
  --face-analyser-order {left-right,right-left,top-bottom,bottom-top,small-large,large-small,best-worst,worst-best}      指定人脸分析器检测人脸的顺序。
  --face-analyser-age {child,teen,adult,senior}                                                                          根据年龄过滤检测到的人脸
  --face-analyser-gender {female,male}                                                                                   根据性别过滤检测到的人脸
  --face-detector-model {many,retinaface,scrfd,yoloface,yunet}                                                           选择负责检测人脸的模型
  --face-detector-size FACE_DETECTOR_SIZE                                                                                指定提供给人脸检测器的帧的大小
  --face-detector-score [0.0-1.0]                                                                                        根据置信度分数过滤检测到的人脸
  --face-landmarker-score [0.0-1.0]                                                                                      根据置信度分数过滤检测到的标志点

人脸选择器：
  --face-selector-mode {many,one,reference}                                                                              使用基于参考的跟踪或简单匹配
  --reference-face-position REFERENCE_FACE_POSITION                                                                      指定用于创建参考人脸的位置
  --reference-face-distance [0.0-1.5]                                                                                    指定参考人脸与目标人脸之间的期望相似度
  --reference-frame-number REFERENCE_FRAME_NUMBER                                                                        指定用于创建参考人脸的帧

人脸遮罩：
  --face-mask-types FACE_MASK_TYPES [FACE_MASK_TYPES ...]                                                                混合和匹配不同的人脸遮罩类型（选择：box，occlusion，region）
  --face-mask-blur [0.0-1.0]                                                                                             指定应用于框遮罩的模糊程度
  --face-mask-padding FACE_MASK_PADDING [FACE_MASK_PADDING ...]                                                          将上，右，下和左边距应用于框遮罩
  --face-mask-regions FACE_MASK_REGIONS [FACE_MASK_REGIONS ...]                                                          选择用于区域遮罩的面部特征（选择：skin，left-eyebrow，right-eyebrow，left-eye，right-eye，eye-glasses，nose，mouth，upper-lip，lower-lip）

帧提取：
  --trim-frame-start TRIM_FRAME_START                                                                                    指定目标视频的起始帧
  --trim-frame-end TRIM_FRAME_END                                                                                        指定目标视频的结束帧
  --temp-frame-format {bmp,jpg,png}                                                                                      指定临时资源的格式
  --keep-temp                                                                                                            在处理后保留临时资源

输出创建：
  --output-image-quality [0-100]                                                                                         指定图像质量，转换为压缩因子
  --output-image-resolution OUTPUT_IMAGE_RESOLUTION                                                                      根据目标图像指定图像输出分辨率
  --output-video-encoder {libx264,libx265,libvpx-vp9,h264_nvenc,hevc_nvenc,h264_amf,hevc_amf}                            指定用于视频压缩的编码器
  --output-video-preset {ultrafast,superfast,veryfast,faster,fast,medium,slow,slower,veryslow}                           平衡快速视频处理和视频文件大小
  --output-video-quality [0-100]                                                                                         指定视频质量，转换为压缩因子
  --output-video-resolution OUTPUT_VIDEO_RESOLUTION                                                                      根据目标视频指定视频输出分辨率
  --output-video-fps OUTPUT_VIDEO_FPS                                                                                    根据目标视频指定视频输出帧率
  --skip-audio                                                                                                           省略目标视频中的音频

帧处理器：
  --frame-processors FRAME_PROCESSORS [FRAME_PROCESSORS ...]                                                             加载单个或多个帧处理器。 （选择：face_debugger，face_enhancer，face_swapper，frame_enhancer，lip_syncer，...）
  --face-debugger-items FACE_DEBUGGER_ITEMS [FACE_DEBUGGER_ITEMS ...]                                                    加载单个或多个帧处理器（选择：bounding-box，face-landmark-5，face-landmark-5/68，face-landmark-68，face-mask，face-detector-score，face-landmarker-score，age，gender）
  --face-enhancer-model {codeformer,gfpgan_1.2,gfpgan_1.3,gfpgan_1.4,gpen_bfr_256,gpen_bfr_512,restoreformer_plus_plus}  选择负责增强人脸的模型
  --face-enhancer-blend [0-100]                                                                                          将增强混合到先前的人脸中
  --face-swapper-model {blendswap_256,inswapper_128,inswapper_128_fp16,simswap_256,simswap_512_unofficial,uniface_256}   选择负责交换人脸的模型
  --frame-enhancer-model {lsdir_x4,nomos8k_sc_x4,real_esrgan_x4,real_esrgan_x4_fp16,span_kendata_x4}                     选择负责增强帧的模型
  --frame-enhancer-blend [0-100]                                                                                         将增强混合到先前的帧中
  --lip-syncer-model {wav2lip_gan}                                                                                       选择负责同步嘴唇的模型

用户界面：
  --ui-layouts UI_LAYOUTS [UI_LAYOUTS ...]                                                                               启动单个或多个UI布局（选择：benchmark，default，webcam，...）

```


Documentation
-------------

Read the [documentation](https://docs.facefusion.io) for a deep dive.
