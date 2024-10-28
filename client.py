import grpc
import picture_pb2
import picture_pb2_grpc
#  测试代码

def run():
    # 创建一个与服务器的通道
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = picture_pb2_grpc.PictureConServiceStub(channel)

        # 读取图像文件并发送请求
        with open('./image/val_30.JPEG', 'rb') as f:
            image_data = f.read()

        request = picture_pb2.ImageRequest(image=image_data)
        response = stub.GetImageVector(request)

        print("Received vector: ", response.vector)


if __name__ == '__main__':
    run()
