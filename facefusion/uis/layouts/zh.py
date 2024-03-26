import socket
import gradio

from facefusion.uis.components import about, frame_processors, frame_processors_options, execution, execution_thread_count, execution_queue_count, memory, temp_frame, output_options, common_options, source, target, output, preview, trim_frame, face_analyser, face_selector, face_masker


def pre_check() -> bool:
	return True


def pre_render() -> bool:
	return True


def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		with gradio.Row():
			with gradio.Column(scale = 2):
				with gradio.Blocks():
					about.render()
				with gradio.Blocks():
					frame_processors.render()
				with gradio.Blocks():
					frame_processors_options.render()
				with gradio.Blocks():
					execution.render()
					execution_thread_count.render()
					execution_queue_count.render()
				with gradio.Blocks():
					memory.render()
				with gradio.Blocks():
					temp_frame.render()
				with gradio.Blocks():
					output_options.render()
			with gradio.Column(scale = 2):
				with gradio.Blocks():
					source.render()
				with gradio.Blocks():
					target.render()
				with gradio.Blocks():
					output.render()
			with gradio.Column(scale = 3):
				with gradio.Blocks():
					preview.render()
				with gradio.Blocks():
					trim_frame.render()
				with gradio.Blocks():
					face_selector.render()
				with gradio.Blocks():
					face_masker.render()
				with gradio.Blocks():
					face_analyser.render()
				with gradio.Blocks():
					common_options.render()
                    
		with gradio.Blocks() as ui:
			gradio.Text(
				value="欢迎加入QQ群：837217096，仓库地址：https://github.com/Ccj0221/facefusion_Zh",
				label="了解更多",
			).style(container=False)
            
	return layout


def listen() -> None:
	frame_processors.listen()
	frame_processors_options.listen()
	execution.listen()
	execution_thread_count.listen()
	execution_queue_count.listen()
	memory.listen()
	temp_frame.listen()
	output_options.listen()
	source.listen()
	target.listen()
	output.listen()
	preview.listen()
	trim_frame.listen()
	face_selector.listen()
	face_masker.listen()
	face_analyser.listen()
	common_options.listen()

socket.disable_ipv6 = True

def run(ui: gradio.Blocks) -> None:
    ui.server_name = "127.0.0.1"  # 地址
    ui.server_port = 6006         # 端口
    ui.launch(server_name=ui.server_name, server_port=ui.server_port, share=True, show_api=True, quiet=False)
    ui.queue(concurrency_count=4).launch(show_api=False, quiet=True)

if __name__ == "__main__":
    ui = render()
    run(ui)

