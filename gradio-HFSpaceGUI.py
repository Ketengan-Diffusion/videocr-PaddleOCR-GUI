import gradio as gr
from videocr import save_subtitles_to_file

def video_ocr(input_video, output_file, language_code, use_gpu, start_time, end_time, confidence_threshold, similarity_threshold, frames_to_skip, crop_x, crop_y, crop_width, crop_height):
    save_subtitles_to_file(input_video, output_file, lang=language_code,
                           time_start=start_time, time_end=end_time,
                           conf_threshold=confidence_threshold, sim_threshold=similarity_threshold,
                           use_gpu=use_gpu,
                           frames_to_skip=frames_to_skip,
                           crop_x=crop_x, crop_y=crop_y, crop_width=crop_width, crop_height=crop_height)
    return output_file

iface = gr.Interface(
    fn=video_ocr,
    inputs=[
        gr.Video(label="Input Video"),
        gr.Textbox(label="Output File Name", value="subtitle.srt"),
        gr.Textbox(label="Language Code", value="ch"),
        gr.Checkbox(label="Use GPU", value=True),
        gr.Textbox(label="Start Time (HH:MM:SS)", value="00:00:00"),
        gr.Textbox(label="End Time (HH:MM:SS)", value=""),
        gr.Slider(label="Confidence Threshold", minimum=0, maximum=100, step=1, value=75),
        gr.Slider(label="Similarity Threshold", minimum=0, maximum=100, step=1, value=80),
        gr.Slider(label="Frames to Skip", minimum=0, maximum=10, step=1, value=0),
        gr.Number(label="Crop X", value=0),
        gr.Number(label="Crop Y", value=0),
        gr.Number(label="Crop Width", value=0),
        gr.Number(label="Crop Height", value=0),
    ],
    outputs=gr.File(label="Output SRT File"),
    title="VideoOCR with PaddleOCR",
    description="Extract hardcoded subtitles from videos using PaddleOCR on GPU.",
)

iface.launch(share=True)
