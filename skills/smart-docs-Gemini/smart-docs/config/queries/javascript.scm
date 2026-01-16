; 定义
(function_declaration name: (identifier) @definition.function)
(class_declaration name: (identifier) @definition.class)
(method_definition name: (property_identifier) @definition.method)
(variable_declarator name: (identifier) @definition.function value: (arrow_function))

; 继承
(class_heritage (identifier) @reference.extends)

; 调用
(call_expression function: (identifier) @reference.call)
(call_expression function: (member_expression property: (property_identifier) @reference.call))
(import_statement source: (string) @reference.import)
(call_expression function: (identifier) @func (#eq? @func "require") arguments: (arguments (string) @reference.import))