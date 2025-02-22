import os

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    if not lines:
        return  # 如果文件为空，直接返回
    
    first_line = lines[0].lstrip('#').lstrip()
    
    if not first_line.startswith('**'):
        first_line = '**' + first_line.rstrip() + '**\n'
    
    lines[0] = first_line
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def main():
    for file_name in os.listdir('.'):
        if file_name.endswith('.txt'):
            process_file(file_name)
            print(f"Processed: {file_name}")

if __name__ == "__main__":
    main()
