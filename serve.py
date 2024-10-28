from concurrent import futures
import grpc
import picture_pb2
import picture_pb2_grpc
from PIL import Image
import torch
from torchvision import transforms
import io
from resnet_model import model

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)


# 图片预处理函数
def preprocess_image(image_bytes):
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image = preprocess(image)
    return image


class PictureConServiceServicer(picture_pb2_grpc.PictureConServiceServicer):
    def GetImageVector(self, request, context):
        image_bytes = request.image
        image_tensor = preprocess_image(image_bytes).unsqueeze(0).to(device)
        with torch.no_grad():
            feature_vector = model(image_tensor).squeeze(0).cpu().numpy().tolist()
        return picture_pb2.VectorResponse(vector=feature_vector)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    picture_pb2_grpc.add_PictureConServiceServicer_to_server(PictureConServiceServicer(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
