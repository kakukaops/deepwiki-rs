import sys
import json
import os
from tree_sitter_languages import get_language, get_parser

EXT_TO_LANG = {
    ".py": "python", ".java": "java", ".go": "go", ".rs": "rust",
    ".c": "c", ".h": "c", ".cpp": "cpp", ".hpp": "cpp", ".cc": "cpp",
    ".js": "javascript", ".jsx": "javascript",
    ".ts": "typescript", ".tsx": "tsx", ".php": "php"
}

def load_query(lang_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    query_path = os.path.join(base_dir, "..", "config", "queries", f"{lang_name}.scm")
    if not os.path.exists(query_path): return None
    with open(query_path, "r", encoding="utf-8") as f: return f.read()

def calculate_complexity(node):
    """
    计算圈复杂度 (Cyclomatic Complexity)
    规则: 1 (基础) + 分支节点数 (if, for, while, case, etc.)
    """
    complexity = 1
    # 这是一个简化的分支节点列表，涵盖大多数语言的控制流关键字
    branch_types = {
        "if_statement", "for_statement", "while_statement", "case_statement",
        "catch_clause", "conditional_expression", # ternary operator
        "binary_expression", "boolean_operator"   # &&, || (需进一步判断，简化起见暂不深度检查)
    }
    
    cursor = node.walk()
    visited_children = False
    while True:
        if visited_children:
            if cursor.node.type in branch_types:
                # 对于 binary_expression，只有逻辑运算 (&&, ||) 才增加复杂度
                # 这里为了性能做简化处理，仅对明确的控制流语句 +1
                if "statement" in cursor.node.type or "clause" in cursor.node.type:
                    complexity += 1
            
            if cursor.goto_next_sibling():
                visited_children = False
            elif cursor.goto_parent():
                visited_children = True
            else:
                break
        else:
            if cursor.goto_first_child():
                visited_children = False
            else:
                visited_children = True
    return complexity

def analyze_file(file_path):
    ext = os.path.splitext(file_path)[1]
    lang_name = EXT_TO_LANG.get(ext)
    if not lang_name: return {"error": f"Unsupported extension: {ext}"}

    try:
        language = get_language(lang_name)
        parser = get_parser(lang_name)
        with open(file_path, "r", encoding="utf-8") as f: code = f.read()
        tree = parser.parse(bytes(code, "utf8"))
        
        scm = load_query(lang_name)
        if not scm: return {"error": f"Missing query for {lang_name}"}
        
        query = language.query(scm)
        captures = query.captures(tree.root_node)
    except Exception as e:
        return {"error": str(e)}

    containers = []
    calls = []
    extends = []
    imports = []

    for node, tag in captures:
        text = node.text.decode("utf8", errors="ignore")
        start_line = node.start_point[0] + 1
        end_line = node.end_point[0] + 1
        
        if tag.startswith("definition"):
            kind = tag.split(".")[1]
            
            # 计算复杂度 (仅对函数/方法)
            comp = 0
            if kind in ["function", "method"]:
                comp = calculate_complexity(node)

            containers.append({
                "kind": kind,
                "name": text,
                "start_line": start_line,
                "end_line": end_line,
                "complexity": comp,  # ✅ 新增复杂度字段
                "calls": set(),
                "extends": []
            })
        elif tag.startswith("reference.call"):
            calls.append({"name": text, "line": start_line})
        elif tag.startswith("reference.extends"):
            extends.append({"name": text, "line": start_line})
        elif tag.startswith("reference.import"):
            imports.append(text)

    # 归属继承
    for relation in extends:
        for cont in containers:
            if cont["kind"] == "class":
                if cont["start_line"] <= relation["line"] <= cont["end_line"]:
                    cont["extends"].append(relation["name"])
                    break

    # 归属调用
    for call in calls:
        target = None
        min_len = float("inf")
        for cont in containers:
            if cont["kind"] in ["function", "method"]:
                if cont["start_line"] <= call["line"] <= cont["end_line"]:
                    length = cont["end_line"] - cont["start_line"]
                    if length < min_len:
                        min_len = length
                        target = cont
        if target:
            target["calls"].add(call["name"])

    # 格式化输出
    classes = []
    functions = []
    
    for cont in containers:
        call_list = list(cont["calls"])
        if len(call_list) > 50:
            call_list = call_list[:50] + ["...truncated..."]
        cont["calls"] = call_list
        
        if cont["kind"] in ["class", "struct", "interface"]:
            classes.append(cont)
        else:
            functions.append(cont)

    return json.dumps({
        "file": file_path,
        "language": lang_name,
        "loc": len(code.splitlines()),
        "imports": imports[:100],
        "structure": {
            "classes": classes,
            "functions": functions
        }
    }, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(1)
    print(analyze_file(sys.argv[1]))