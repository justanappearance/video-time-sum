# Video Time Sum

A Python script to calculate the total duration of all video files in a given directory.

This project allows users to input a directory containing video files, and the script will compute the combined duration of all video files in the directory, outputting the total time in hours and minutes.

## Features

- **Calculate Total Duration**: Adds up the total length of all video files in a specified directory.
- **Supports Multiple Formats**: Works with common video file formats like `.mp4`, `.avi`, `.mov`, etc.
- **Readable Output**: Outputs the total time in hours and minutes.

## Installation

### Prerequisites

1. **Python 3.6+**: Ensure that Python is installed on your machine. You can check the version by running:

```python --version```

2. **Required Libraries**: This project uses the `moviepy` library to handle video files. Install the required dependencies by running:

```pip install -r requirements.txt```

If you don't have a `requirements.txt` file, you can install `moviepy` manually:

```pip install moviepy```

## Usage

1. Clone the repository to your local machine:

```git clone https://github.com/justanappearance/video-time-sum.git```

2. Navigate to the project directory:

```cd video-time-sum```

3. Run the script, providing the path to the directory containing your video files:

```python video_time_sum.py <path-to-video-directory>```

Example:

```python video_time_sum.py "C:/Users/Username/Videos"```

The script will output the total duration of all video files in the specified directory in hours and minutes.

## Example Output

```Total duration: 2 hours, 34 minutes, and 18 seconds.```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

**`MoviePy`**: Used for video processing. MoviePy documentation
