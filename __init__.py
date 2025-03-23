from .node.Image_Tag import ImageTagSave, ImageTagLoad
from .node.Mask_Counter import MaskCounter
from .node.Add_TextToFiles import AddTextToFiles

NODE_CLASS_MAPPINGS = { 
    "WWL_ImageTagSave": ImageTagSave,
	"WWL_ImageTagLoad": ImageTagLoad,
    "WWL_MaskCounter": MaskCounter,
    "WWL_AddTextToFiles": AddTextToFiles,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']