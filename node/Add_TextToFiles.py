import os
import glob

class AddTextToFiles:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Text": ("STRING", {"default": ""}),
                "Path": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Result",)
    FUNCTION = "add_text_to_files"
    CATEGORY = "WWL/Text"
    OUTPUT_NODE = True

    def add_text_to_files(self, Text, Path):
        result_message = ""
        try:
            # 确保路径存在
            if not os.path.exists(Path):
                result_message += f"警告: 路径 '{Path}' 不存在!\n"
                return (result_message,)
            
            # 遍历文件夹中所有的.txt文件
            files = glob.glob(os.path.join(Path, "*.txt"))
            
            if not files:
                result_message += f"警告: 文件夹中没有找到.txt文件!\n"
            else:
                count = 0
                processed_files = []
                
                for file_path in files:
                    try:
                        # 读取文件内容
                        with open(file_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                        
                        # 写入修改后的内容
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(Text + content)
                        
                        count += 1
                        processed_files.append(os.path.basename(file_path))
                    except Exception as e:
                        result_message += f"处理文件 {os.path.basename(file_path)} 时出错: {e}\n"
                
                result_message += f"完成! 共处理了 {count} 个文件。\n"
                if processed_files:
                    result_message += "已处理的文件:\n" + "\n".join(processed_files)
        except Exception as e:
            result_message += f"发生错误: {e}\n"
        
        return (result_message,)
