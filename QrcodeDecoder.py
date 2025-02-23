from pyzbar.pyzbar import decode
from PIL import Image
import json

class QrcodeDecoder:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.decoded_objects = decode(self.image)

    def parse_decoded_object(self, obj):
        return {
            "datos": obj.data.decode("utf-8"),
            "tipo": obj.type,
            "rect": {
                "izquierda": obj.rect.left,
                "arriba": obj.rect.top,
                "ancho": obj.rect.width,
                "alto": obj.rect.height
            },
            "polígono": [(p.x, p.y) for p in obj.polygon],
            "orientación": "ARRIBA",  # pyzbar no devuelve orientación
            "calidad": 77  # Este valor es ficticio, pyzbar no da calidad
        }

    def get_decoded_results(self):
        return [self.parse_decoded_object(obj) for obj in self.decoded_objects]
    
    def get_label_data(self, label):
        for obj in self.get_decoded_results():
            if obj["datos"] == label:
                return obj
        return None
    
    def get_all_labels(self):
        return [obj["datos"] for obj in self.get_decoded_results()]

    def print_results(self):
        print(json.dumps(self.get_decoded_results(), indent=4, ensure_ascii=False))

# Uso
#decoder = QrcodeDecoder('Escaneo.jpg')
#decoder.print_results()


# Obtener solo los valores de "datos"
#all_labels = decoder.get_all_labels()
#print("Todos los datos extraídos:", all_labels)