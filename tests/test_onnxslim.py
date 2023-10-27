import subprocess

import pytest

from utils import download_onnx_from_url


class TestOnnxModel:
    @pytest.mark.parametrize(
        "name",
        (
            "swin_tiny",
            "glm_block_0",
            "mobilenet_v2",
            "resnet18",
            "tf_efficientnetv2_s",
            "UNetModel-fp16",
            "dinov2",
            "unet",
        ),
    )
    def test_onnx_model(self, request, name):
        filename = download_onnx_from_url(
            f"http://120.224.26.32:15030/aifarm/onnx/{name}.onnx"
        )
        command = f"onnxslim {filename} {name}_slim.onnx"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stderr.strip()
        # Assert the expected return code
        print(output)
        assert result.returncode == 0


if __name__ == "__main__":
    pytest.main(
        [
            "-p",
            "no:warnings",
            "-v",
            "tests/test_onnxslim.py",
        ]
    )
