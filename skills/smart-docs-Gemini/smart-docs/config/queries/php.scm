; 定义
(function_definition name: (name) @definition.function)
(class_declaration name: (name) @definition.class)
(method_declaration name: (name) @definition.method)

; 继承
(base_clause (name) @reference.extends)
(class_interface_clause (name) @reference.extends)

; 调用
(function_call_expression function: (name) @reference.call)
(member_call_expression name: (name) @reference.call)
(scoped_call_expression name: (name) @reference.call)

; ... (原有内容) ...
(namespace_use_declaration) @reference.import