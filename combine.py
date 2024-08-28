import moviepy

from moviepy.editor import *

from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip
from pydub import AudioSegment


# # function to list all of the the jpeg files in the img folder in sorted number
# def list_images():
#     files = os.listdir("img/cropped")
#     files = [file for file in files if file.endswith(".jpeg")]
#     files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))
#     return files

# imgs = list_images()
# remove_paths = []
# video_clips = []
# for i in range(len(imgs)):
#     img_path = "img/cropped/" + imgs[i]
#     audio_path = "audio/output" + str(i) + ".mp3"

#     # Load the audio file
#     audio_clip = AudioFileClip(audio_path)

#     # Load an image and set the duration to the audio clip's duration
#     image_clip = ImageClip(img_path).set_duration(audio_clip.duration)

#     # Set the audio of the image clip to be the audio clip
#     video_clip = image_clip.set_audio(audio_clip)

#     output_path = "output" + str(i) + ".mp4"
#     remove_paths.append(output_path)
#     # Export the video
#     video_clip.write_videofile(output_path, fps=24)  # You can adjust fps to desired frame rate

#     video_clips.append( VideoFileClip(output_path))

# final_video = concatenate_videoclips(video_clips)

# # Check if the duration of the final video is over 60 seconds
# if final_video.duration > 60:
#     # Calculate the speed factor to adjust the duration to 60 seconds
#     speed_factor = final_video.duration / 60

#     # Speed up the video by the calculated factor
#     final_video = final_video.fx(vfx.speedx, speed_factor)

# final_video.write_videofile("final_output.mp4")



# def clean():
#     for path in remove_paths:
#         os.remove(path)

# clean()


from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip, concatenate_videoclips, vfx
import os

# function to list all of the JPEG files in the 'img/cropped' folder and sort them by number
def list_images():
    files = os.listdir("img/cropped")
    files = [file for file in files if file.endswith(".jpeg")]
    files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))
    return files

# Fetch the list of image paths
imgs = list_images()
remove_paths = []
video_clips = []
fade_duration = 0.5  # Duration for fade in and fade out in seconds

for i in range(len(imgs)):
    img_path = "img/cropped/" + imgs[i]
    audio_path = "audio/output" + str(i) + "_speedup.wav"

    # Load the audio file
    audio_clip = AudioFileClip(audio_path)

    audio = AudioSegment.from_file(audio_path)
    duration = audio.duration_seconds + 0.01

    # Load an image and set the duration to the audio clip's duration
    image_clip = ImageClip(img_path).set_duration(duration)

    # Apply fade in and fade out effects
    image_clip = image_clip.fadein(fade_duration).fadeout(fade_duration)
    print("Image duration:", audio_clip.duration)
    # Set the audio of the image clip to be the audio clip
    video_clip = image_clip.set_audio(audio_clip)

    output_path = "output" + str(i) + ".mp4"
    remove_paths.append(output_path)
    # Export the video
    video_clip.write_videofile(output_path, fps=24)  # Adjust fps to desired frame rate

    video_clips.append(VideoFileClip(output_path))

# Concatenate all video clips into one final video
final_video = concatenate_videoclips(video_clips)

# Export the final concatenated video
final_video.write_videofile("final_output.mp4")

# remove all the .mp4 files in the curent folder except the final output
for i in range(len(imgs)):
    if i != len(imgs)-1:
        os.remove("output" + str(i) + ".mp4")


# # Function to clean up intermediate files
# def clean():
#     for path in remove_paths:
#         os.remove(path)

# clean()  # Call the clean function to remove intermediate files
