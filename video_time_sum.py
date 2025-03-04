import os
import moviepy.editor as mp


def get_total_video_duration(directory):
    total_duration = 0  # Store total duration in seconds

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file (not a directory) and has a video extension
        if os.path.isfile(file_path) and filename.lower().endswith(
            (".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv")
        ):
            try:
                video = mp.VideoFileClip(file_path)  # Load video file
                total_duration += video.duration  # Add duration in seconds
                video.close()  # Close the file to free resources
                print(f"Processed: {filename} ({video.duration:.2f} seconds)")
            except Exception as e:
                print(f"Skipping {filename}: {e}")

    return total_duration


def convert_seconds_to_hms(seconds):
    hours = int(seconds // 3600)  # Get the number of hours
    minutes = int((seconds % 3600) // 60)  # Get the number of minutes
    remaining_seconds = int(seconds % 60)  # Get the remaining seconds
    return hours, minutes, remaining_seconds


if __name__ == "__main__":
    directory = input(
        "Enter the directory path: "
    ).strip()  # Get directory input from user
    if os.path.isdir(directory):
        total_time_seconds = get_total_video_duration(directory)
        hours, minutes, seconds = convert_seconds_to_hms(total_time_seconds)
        print(
            f"\nTotal video duration: {hours} hours, {minutes} minutes, {seconds} seconds"
        )
    else:
        print("Invalid directory. Please check the path and try again.")
