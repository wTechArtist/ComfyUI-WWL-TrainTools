import cv2
import numpy as np
import torch

class MaskCounter:
    """
    A node that counts the number of separate masks in an input mask image
    
    Inputs: Mask image
    Outputs: Number of separate mask regions
    """
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "mask": ("MASK",),
            },
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("count",)
    FUNCTION = "count_masks"
    CATEGORY = "WWL/Mask"

    def count_masks(self, mask):
        """
        Count number of separate mask regions in the input mask
        
        Args:
            mask: Input mask image tensor
            
        Returns:
            Number of separate mask regions
        """
        try:
            # 确保输入是tensor
            if not isinstance(mask, torch.Tensor):
                raise ValueError("Input mask must be a tensor")
                
            # 转换为numpy数组
            mask_np = mask.cpu().numpy()
            
            # 确保数组不为空
            if mask_np.size == 0:
                return (0,)
                
            # 处理维度
            if len(mask_np.shape) == 3:
                mask_np = mask_np[0]  # 取第一个通道
            
            # 确保是2D数组
            if len(mask_np.shape) != 2:
                raise ValueError(f"Mask must be 2D array, got shape {mask_np.shape}")
                
            # 转换为8位无符号整数
            binary = np.uint8(mask_np > 0.5) * 255
            
            # 确保二值化成功
            if not np.any(binary) and not np.all(binary):
                return (0,)  # 如果图像全黑或全白，返回0
                
            # 使用connectedComponentsWithStats，这个函数更稳定
            num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
                binary, 
                connectivity=8,
                ltype=cv2.CV_32S
            )
            
            # 减去背景计数
            mask_count = num_labels - 1 if num_labels > 0 else 0
            
            return (mask_count,)
            
        except Exception as e:
            print(f"Error in mask counting: {str(e)}")
            return (0,)  # 发生错误时返回0
