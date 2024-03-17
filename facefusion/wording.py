from typing import Any, Dict, Optional

WORDING: Dict[str, Any] = {
    'python_not_supported': 'Python版本不支持，请升级至{version}或更高版本',
    'ffmpeg_not_installed': '未安装FFMpeg',
    'creating_temp': '创建临时资源',
    'extracting_frames': '提取帧，分辨率为{resolution}，帧率为{fps}帧/秒',
    'extracting_frames_succeed': '提取帧成功',
    'extracting_frames_failed': '提取帧失败',
    'analysing': '分析中',
    'processing': '处理中',
    'downloading': '下载中',
    'temp_frames_not_found': '未找到临时帧',
    'copying_image': '复制图像，分辨率为{resolution}',
    'copying_image_succeed': '复制图像成功',
    'copying_image_failed': '复制图像失败',
    'finalizing_image': '完成图像，分辨率为{resolution}',
    'finalizing_image_succeed': '完成图像成功',
    'finalizing_image_skipped': '跳过完成图像',
    'merging_video': '合并视频，分辨率为{resolution}，帧率为{fps}帧/秒',
    'merging_video_succeed': '合并视频成功',
    'merging_video_failed': '合并视频失败',
    'skipping_audio': '跳过音频',
    'restoring_audio_succeed': '恢复音频成功',
    'restoring_audio_skipped': '跳过恢复音频',
    'clearing_temp': '清除临时资源',
    'processing_stopped': '处理已停止',
    'processing_image_succeed': '图像处理成功，耗时{seconds}秒',
    'processing_image_failed': '图像处理失败',
    'processing_video_succeed': '视频处理成功，耗时{seconds}秒',
    'processing_video_failed': '视频处理失败',
    'model_download_not_done': '模型下载未完成',
    'model_file_not_present': '模型文件不存在',
    'select_image_source': '选择图像作为源路径',
    'select_audio_source': '选择音频作为源路径',
    'select_video_target': '选择视频作为目标路径',
    'select_image_or_video_target': '选择图像或视频作为目标路径',
    'select_file_or_directory_output': '选择文件或目录作为输出路径',
    'no_source_face_detected': '未检测到源脸部',
    'frame_processor_not_loaded': '无法加载帧处理器{frame_processor}',
    'frame_processor_not_implemented': '帧处理器{frame_processor}未正确实现',
    'ui_layout_not_loaded': '无法加载UI布局{ui_layout}',
    'ui_layout_not_implemented': 'UI布局{ui_layout}未正确实现',
    'stream_not_loaded': '无法加载流{stream_mode}',
    'point': '。',
    'comma': '，',
    'colon': '：',
    'question_mark': '？',
    'exclamation_mark': '！',
    'help': {
        # installer
        'install_dependency': '选择要安装的{dependency}变体',
        'skip_venv': '跳过虚拟环境检查',
        # general
        'source': '选择单个或多个源图像或音频',
        'target': '选择单个目标图像或视频',
        'output': '指定输出文件或目录',
        # misc
        'skip_download': '跳过自动下载和远程查找',
        'headless': '无界面运行程序',
        'log_level': '调整在终端中显示的消息严重程度',
        # execution
        'execution_providers': '使用不同的提供程序加速模型推理（选择项：{choices}，...）',
        'execution_thread_count': '指定处理时的并行线程数',
        'execution_queue_count': '指定每个线程处理的帧数',
        # memory
        'video_memory_strategy': '平衡快速帧处理和低显存使用率',
        'system_memory_limit': '限制处理时可用的内存',
        # face analyser
        'face_analyser_order': '指定人脸分析器检测人脸的顺序',
        'face_analyser_age': '根据年龄过滤检测到的人脸',
        'face_analyser_gender': '根据性别过滤检测到的人脸',
        'face_detector_model': '选择负责检测人脸的模型',
        'face_detector_size': '指定提供给人脸检测器的帧大小',
        'face_detector_score': '根据置信度分数过滤检测到的人脸',
        'face_landmarker_score': '根据置信度分数过滤检测到的关键点',
        # face selector
        'face_selector_mode': '使用基于参考的跟踪或简单匹配',
        'reference_face_position': '指定用于创建参考脸部的位置',
        'reference_face_distance': '指定参考脸部与目标脸部之间的相似度',
        'reference_frame_number': '指定用于创建参考脸部的帧',
        # face mask
        'face_mask_types': '混合和匹配不同类型的面部蒙版（选择项：{choices}）',
        'face_mask_blur': '指定应用于框蒙版的模糊程度',
        'face_mask_padding': '对框蒙版应用上、右、下、左的填充',
        'face_mask_regions': '选择用于区域蒙版的面部特征（选择项：{choices}）',
        # frame extraction
        'trim_frame_start': '指定目标视频的起始帧',
        'trim_frame_end': '指定目标视频的结束帧',
        'temp_frame_format': '指定临时资源的格式',
        'keep_temp': '在处理后保留临时资源',
        # output creation
        'output_image_quality': '指定图像质量，转化为压缩因子',
        'output_image_resolution': '根据目标图像指定图像输出分辨率',
        'output_video_encoder': '指定用于视频压缩的编码器',
        'output_video_preset': '平衡快速视频处理和视频文件大小',
        'output_video_quality': '指定视频质量，转化为压缩因子',
        'output_video_resolution': '根据目标视频指定视频输出分辨率',
        'output_video_fps': '根据目标视频指定视频输出帧率',
        'skip_audio': '跳过目标视频中的音频',
        # frame processors
        'frame_processors': '加载单个或多个帧处理器（选择项：{choices}，...）',
        'face_debugger_items': '加载单个或多个帧处理器（选择项：{choices}）',
        'face_enhancer_model': '选择负责增强面部的模型',
        'face_enhancer_blend': '将增强部分混合到上一个面部',
        'face_swapper_model': '选择负责交换面部的模型',
        'frame_enhancer_model': '选择负责增强帧的模型',
        'frame_enhancer_blend': '将增强部分混合到上一个帧',
        'lip_syncer_model': '选择负责同步嘴唇的模型',
        # uis
        'ui_layouts': '启动单个或多个UI布局（选择项：{choices}，...）'
    },
    'uis': {
        # general
        'start_button': '开始',
        'stop_button': '停止',
        'clear_button': '清除',
        # about
        'donate_button': '使用文档',
        # benchmark
        'benchmark_results_dataframe': '基准测试结果',
        # benchmark options
        'benchmark_runs_checkbox_group': '基准测试运行',
        'benchmark_cycles_slider': '基准测试循环次数',
        # common options
        'common_options_checkbox_group': '选项',
        # execution
        'execution_providers_checkbox_group': '执行提供程序',
        # execution queue count
        'execution_queue_count_slider': '执行队列计数',
        # execution thread count
        'execution_thread_count_slider': '执行线程计数',
        # face analyser
        'face_analyser_order_dropdown': '人脸分析器顺序',
        'face_analyser_age_dropdown': '人脸分析器年龄',
        'face_analyser_gender_dropdown': '人脸分析器性别',
        'face_detector_model_dropdown': '人脸检测器模型',
        'face_detector_size_dropdown': '人脸检测器大小',
        'face_detector_score_slider': '人脸检测器分数',
        'face_landmarker_score_slider': '人脸关键点分数',
        # face masker
        'face_mask_types_checkbox_group': '遮罩类型',
        'face_mask_blur_slider': '遮罩模糊度',
        'face_mask_padding_top_slider': '遮罩上填充',
        'face_mask_padding_right_slider': '遮罩右填充',
        'face_mask_padding_bottom_slider': '遮罩下填充',
        'face_mask_padding_left_slider': '遮罩左填充',
        'face_mask_region_checkbox_group': '遮罩区域',
        # face selector
        'face_selector_mode_dropdown': '人脸选择器模式',
        'reference_face_gallery': '参考脸部',
        'reference_face_distance_slider': '参考脸部距离',
        # frame processors
        'frame_processors_checkbox_group': '帧处理器',
        # frame processors options
        'face_debugger_items_checkbox_group': '面部调试项目',
        'face_enhancer_model_dropdown': '面部增强模型',
        'face_enhancer_blend_slider': '面部增强混合度',
        'face_swapper_model_dropdown': '面部交换模型',
        'frame_enhancer_model_dropdown': '帧增强模型',
        'frame_enhancer_blend_slider': '帧增强混合度',
        'lip_syncer_model_dropdown': '嘴唇同步模型',
        # memory
        'video_memory_strategy_dropdown': '视频内存策略',
        'system_memory_limit_slider': '系统内存限制',
        # output
        'output_image_or_video': '输出',
        # output options
        'output_path_textbox': '输出路径',
        'output_image_quality_slider': '输出图像质量',
        'output_image_resolution_dropdown': '输出图像分辨率',
        'output_video_encoder_dropdown': '输出视频编码器',
        'output_video_preset_dropdown': '输出视频预设',
        'output_video_quality_slider': '输出视频质量',
        'output_video_resolution_dropdown': '输出视频分辨率',
        'output_video_fps_slider': '输出视频帧率',
        # preview
        'preview_image': '预览',
        'preview_frame_slider': '预览帧',
        # source
        'source_file': '源',
        # target
        'target_file': '目标',
        # temp frame
        'temp_frame_format_dropdown': '临时帧格式',
        # trim frame
        'trim_frame_start_slider': '裁剪起始帧',
        'trim_frame_end_slider': '裁剪结束帧',
        # webcam
        'webcam_image': '网络摄像头',
        # webcam options
        'webcam_mode_radio': '网络摄像头模式',
        'webcam_resolution_dropdown': '网络摄像头分辨率',
        'webcam_fps_slider': '网络摄像头帧率'
    }
}


def get(key: str) -> Optional[str]:
    if '.' in key:
        section, name = key.split('.')
        if section in WORDING and name in WORDING[section]:
            return WORDING[section][name]
    if key in WORDING:
        return WORDING[key]
    return None
