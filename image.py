import cv2

# Load the color image
color_img = cv2.imread(r'D:\insta profile.jpeg')

# Check if the image was loaded successfully
if color_img is None:
    print("Error: Unable to read the image.")
else:
    # Convert the color image to grayscale
    bw_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    # Display the original and black and white images
    cv2.imshow('Original Image', color_img)
    cv2.imshow('Black and White Image', bw_img)

    # Save the black and white image
    cv2.imwrite(r'D:\insta profile.jpeg', bw_img)

    # Wait for a key event and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()