import pytesseract
import cv2
import spacy

def extract_names_from_image(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)

    # Perform OCR on the image to extract text
    extracted_text = pytesseract.image_to_string(image)

    # Load a pre-trained NLP model
    nlp = spacy.load("en_core_web_sm")

    # Process the extracted text and find named entities
    doc = nlp(extracted_text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

    return names

if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"  # Replace with your image path
    names = extract_names_from_image(image_path)
    print("Extracted Names:", names)