import PyPDF2
from googletrans import Translator
import fpdf


def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            return text
    except Exception as e:
        return str(e)


def textstore(pdf_path1):
    if __name__ == "__main__":
        # Replace with the path to your PDF file
        extracted_text = extract_text_from_pdf(pdf_path1)

        if extracted_text:
            return extracted_text
        else:
            print("Error extracting text from the PDF.")


def translate(text1):
    # Define your text
    text_to_translate = text1

    # Set the language code here for the language you want to convert your pdf in
    target_language = 'hi'  # hindi

    # Initialize the translator
    translator = Translator()

    # Translate the text and store the result
    translated_text = translator.translate(text_to_translate, dest=target_language).text

    # Print the translated text
    return translated_text


def main():
    pdf_path = "Y:/My projects for Github/Translate pdf/PDF to Convert/COI.pdf"
    trans = translate(textstore(pdf_path))  # Assuming these functions are correctly defined
    data = trans
    print(trans)

    def save_string_to_file(output_string, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(output_string)

    # Example usage
    output_string = trans
    file_path = "Y:/My projects for Github/Translate and output/output.txt"

    save_string_to_file(output_string, file_path)




if __name__ == "__main__":
    main()


