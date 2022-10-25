md_file_path = './第六章.md'
op_file_path = './op.md'

def read_cache(departure):
    content = open(departure, 'r+')
    lines = content.readlines()
    content.close()
    return lines

if __name__ == '__main__':
    f2 = open(op_file_path, 'w+')
    parity_counter = 0
    dollar_counter = 0
    quote_modifier = 0
    quote_modifier_counter = 0
    # 替换$$
    lines_cache = read_cache(md_file_path)
    for line in lines_cache:
        # 替换引用中多余的">"符号
        if quote_modifier:
            if line.find('>') != -1:
                quote_modifier_counter += 1
                line = line.replace('>', ' ', 1)
        # 替换行内公式
        if line.find('$$') != -1:
            if parity_counter % 2 == 0:
                line_cache = line.replace('$$', '{{< math >}}', 1)
                quote_modifier = 1
            else:
                line_cache = line.replace('$$', '{{< /math >}}', 1)
                quote_modifier = 0
            parity_counter += 1
        # 替换行间公式
        elif line.find('$') != -1:
            line_cache = line
            # 遍历行内出现的多个公式
            while line_cache.find('$') != -1:
                if dollar_counter % 2 == 0:
                    line_cache = line_cache.replace('$', '{{< math "inline" >}}', 1)
                else:
                    line_cache = line_cache.replace('$', '{{< /math >}}', 1)
                dollar_counter += 1
        # 无替换情况
        else:
            line_cache = line
        # 写入
        f2.writelines(line_cache)
    # 输出总结
    print("process completed!\n")
    print("$$ replaced:", parity_counter)
    print("$ replaced:", dollar_counter)
    print("> modified:", quote_modifier_counter)
    f2.close()
