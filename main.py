import cv2

def extract_frame_colors(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_colors = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        colors = []

        # Iterating through each pixel in the frame
        for row in frame:
            for pixel in row:
                # Converting BGR to hexadecimal
                color_hex = "#{:02x}{:02x}{:02x}".format(pixel[2], pixel[1], pixel[0])
                colors.append(color_hex)

        frame_colors.append(colors)

    cap.release()
    return frame_colors

if __name__ == "__main__":
    video_path = "./videos/teste.mp4"  # Insira o caminho para o seu vídeo aqui
    colors_per_frame = extract_frame_colors(video_path)
    print(colors_per_frame)
