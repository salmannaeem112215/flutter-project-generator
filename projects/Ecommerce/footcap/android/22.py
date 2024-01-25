def convert_to_double_backslashes(input_path):
    return input_path.replace("\\", "\\\\")

# Example usage
input_path1 = r"C:\Users\PMLS\upload-keystore.jks"
input_path2 = r"C:\\Users\\PMLS\\upload-keystore.jks"

output_path1 = convert_to_double_backslashes(input_path1)
output_path2 = convert_to_double_backslashes(input_path2)

print(output_path1)
print(output_path2)
