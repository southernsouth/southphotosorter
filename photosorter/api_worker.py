from google.cloud import vision
from env import credentials


def get_photo_data(photo_list):
    data = []

    for photo in photo_list:
        client = vision.ImageAnnotatorClient(credentials=credentials)
        image = vision.Image(content=photo)

        response = client.label_detection(image=image)
        labels = response.label_annotations

        data.append(labels)

    return data
