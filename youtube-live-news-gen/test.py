from apitemplateio_lib import APITemplateIO

api_key = "4d40MjEzODM6MTg0OTg6RTgxUTdXZHJSaTdwcXZVTg="

def test_pdf():
    template_id = "db177b23b6740f9a"
    data = {
        "name": "hello world"
    }
    save_to = "/home/dev/result.pdf"

    apitemplate = APITemplateIO(api_key)
    apitemplate.create_pdf(template_id, data, save_to)

def test_image():
    template_id = "db177b23b6740f9a"
    data = {
        "overrides": [
            {
                "name" : "text_quote",
                "text" : "1 hello world, this is the test message to tese the length of the text and image generation of the so and so. 2 hello world, this is the test message to tese the length of the text and image generation of the so and so. 3 hello world, this is the test message to tese the length of the text and image generation of the so and so. 4 hello world, this is the test message to tese the length of the text and image generation of the so and so. 5 hello world, this is the test message to tese the length of the text and image generation of the so and so. 6 hello world, this is the test message to tese the length of the text and image generation of the so and so.",
            }
        ]
    }
    save_to_jpeg = "F:/certifications/IIITH-AIML/research/imagen/banner/result.jpeg"
    save_to_png = "F:/certifications/IIITH-AIML/research\imagen/banner/result.png"

    apitemplate = APITemplateIO(api_key)
    apitemplate.create_image(template_id, data, save_to_png)

def test_account_information():
    apitemplate = APITemplateIO(api_key)
    print(apitemplate.get_account_information())

def test_list_templates():
    apitemplate = APITemplateIO(api_key)
    templates = apitemplate.list_templates()
    for t in templates:
        print(t)

if __name__ == "__main__":
    #test_pdf()
    test_image()
    #test_account_information()
    #test_list_templates()

