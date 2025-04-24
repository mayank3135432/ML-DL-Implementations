import cv2

def get_frame_count(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Get the total number of frames
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Release the video capture object
    cap.release()
    
    return frame_count

# Example usage
video_path = 'SMAI_A1/input.mp4'
total_frames = get_frame_count(video_path)
print(f'Total number of frames: {total_frames}')
