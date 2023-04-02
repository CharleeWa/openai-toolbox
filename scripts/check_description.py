import re

def line_length_without_links(line):
    md_link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    line_without_links = md_link_pattern.sub(r'\1', line)
    return len(line_without_links.rstrip())

def check_line_length(file_path, max_length=80, skip_lines=15):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if index < skip_lines:
                continue
            if line_length_without_links(line) > max_length:
                print(f"校验不通过: 第 {index + 1} 行超过 {max_length} 字符")
                return False
    return True

if __name__ == "__main__":
    file_path = "README.md"
    if check_line_length(file_path):
        print("校验通过")
    else:
        print("部分行校验未通过，请检查并修复")
