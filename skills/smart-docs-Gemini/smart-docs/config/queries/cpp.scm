; 定义
(function_declarator declarator: (identifier) @definition.function)
(class_specifier name: (type_identifier) @definition.class)
(struct_specifier name: (type_identifier) @definition.struct)

; 继承
(base_class_clause (type_identifier) @reference.extends)

; 调用
(call_expression function: (identifier) @reference.call)
(call_expression function: (field_expression field: (field_identifier) @reference.call))