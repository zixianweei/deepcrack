import sys
import torch
from model.deepcrack import DeepCrack


def main() -> int:
    device = torch.device("cpu")
    model = DeepCrack()
    model.to(device)
    model.load_state_dict(torch.load("checkpoints/DeepCrack_CT260_FT1.pth", map_location=device))
    model.eval

    with torch.no_grad():
        image = torch.randn((1,3,512,512))
        trace = torch.jit.trace(model, example_inputs=image)
        torch.jit.save(trace, "deepcrack.pt")
    return 0


if __name__ == "__main__":
    sys.exit(main())