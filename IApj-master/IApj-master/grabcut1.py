import cv2

# Read the images
cam = cv2.VideoCapture(0)
def show_webcam(mirror=False):
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)

        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
		          break  # esc to quit

    cv2.destroyAllWindows()


show_webcam(mirror=True)

foreground = cv2.imread("descarga.png")
foreground = cv2.resize(foreground, (1040,585))
background = cv2.imread("ocean.png")
background = cv2.resize(background, (1040,585))
alpha = cv2.imread("puppets_alpha.png")

# Convert uint8 to float
foreground = foreground.astype(float)
background = background.astype(float)

# Normalize the alpha mask to keep intensity between 0 and 1
alpha = alpha.astype(float)/255

# Multiply the foreground with the alpha matte
foreground = cv2.multiply(alpha, foreground)

# Multiply the background with ( 1 - alpha )
background = cv2.multiply(1.0 - alpha, background)

# Add the masked foreground and background.
outImage = cv2.add(foreground, background)

# Display image
cv2.imshow("outImg", outImage/255)
cv2.waitKey(0)
